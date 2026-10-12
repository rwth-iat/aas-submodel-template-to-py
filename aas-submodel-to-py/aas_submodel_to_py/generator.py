import decimal
import os.path
import pathlib
import re
import warnings
from typing import Union, Iterable, Any, Optional

import black
from basyx.aas.adapter.aasx import AASXReader, DictSupplementaryFileContainer
from basyx.aas.adapter.json import read_aas_json_file
from basyx.aas.adapter.xml import read_aas_xml_file
from basyx.aas.model import datatypes
from basyx.aas.model import Property, Referable, Submodel, \
    SubmodelElement, SubmodelElementCollection, DictIdentifiableStore, MultiLanguageProperty, \
    ReferenceElement, AbstractObjectStore, SubmodelElementList, Range, File, ModellingKind, Qualifiable, Entity, \
    Qualifier

from jinja2 import Environment, FileSystemLoader

from aas_submodel_to_py import util
from aas_submodel_to_py.util import StringHandler, ReferableHandler, NamingGenerator, \
    get_typehints_for_args, MODEL_ALIAS, TYPING_IMPORTS

CODE_TEMPLATES = os.path.join(os.path.dirname(__file__), 'code_templates')


class NoSubmodelError(ValueError):
    """Raised if the input contains no submodel to generate classes for"""


class SubmodelCodegen:
    def __init__(self, templates_dir=CODE_TEMPLATES, line_length: int = 120):
        # Set the directory containing the Jinja templates
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        # Line length of the generated code: longer than Black's default (88), as deeply nested
        # classes would otherwise be wrapped into many lines, each repeating the indentation
        self.line_length = line_length
        self.imported_modules = set()
        self.metadata_classes = {}

    def generate_from(self, input_file: Union[str, pathlib.Path],
                      output_file: Union[str, pathlib.Path] = "output.py"):
        input_str = str(input_file).lower()
        if input_str.endswith(".aasx"):
            obj_store = DictIdentifiableStore()
            file_store = DictSupplementaryFileContainer()
            AASXReader(input_file).read_into(obj_store, file_store)
        elif input_str.endswith(".json"):
            with open(input_file, "r", encoding='utf-8-sig') as f:
                obj_store = read_aas_json_file(f)
        elif input_str.endswith(".xml"):
            with open(input_file, 'rb') as xml_file:
                obj_store = read_aas_xml_file(xml_file)
        else:
            raise ValueError(f"Unsupported file format: {input_file}. "
                             "Supported formats are .aasx, .json, and .xml.")

        if not any(isinstance(obj, Submodel) for obj in obj_store):
            hint = ""
            if input_str.endswith((".aasx", ".xml")):
                # The BaSyx Python SDK logs an error and reads such files as empty
                hint = (" AASX and XML files of AAS metamodel 3.0 are not supported, as the BaSyx Python SDK "
                        "only reads XML of metamodel 3.1. Use the JSON version of the template or its "
                        "_forAASMetamodelV3.1 variant instead.")
            raise NoSubmodelError(f"No submodel found in {input_file}.{hint}")

        self.generate_from_obj_store(obj_store, output_file)

    def generate_from_obj_store(self, obj_store: AbstractObjectStore,
                                output_file: Union[str, pathlib.Path] = "output.py"):
        submodels = [obj for obj in obj_store if isinstance(obj, Submodel)]
        if not submodels:
            raise NoSubmodelError("No submodel found in the object store.")

        # Modules imported by the generated classes, besides the standard imports,
        # and TypedDicts typing the metadata of their BaSyx classes (see add_metadata_cls)
        self.imported_modules = set()
        self.metadata_classes = {}
        classes = "\n\n".join(self.gen_cls_for_submodel(submodel) for submodel in submodels)
        result = (f"\n{self.generate_imports(self.imported_modules)}\n\n{self.generate_helpers()}\n\n"
                  f"{self.generate_metadata_classes()}\n\n{classes}")

        try:
            # Format the rendered class using Black
            result = black.format_str(result, mode=black.Mode(line_length=self.line_length))
        except Exception as e:
            print(e)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

    def generate_imports(self, modules: Iterable[str] = ()) -> str:
        template = self.env.get_template("imports.pyi")
        imports = template.render(typing_imports=TYPING_IMPORTS, modules=sorted(modules))
        return imports

    def generate_helpers(self) -> str:
        return self.env.get_template("helpers.pyi").render()

    def generate_metadata_classes(self) -> str:
        return self.env.get_template("metadata.pyi").render(metadata_classes=dict(sorted(self.metadata_classes.items())))

    def add_metadata_cls(self, referable: Referable) -> str:
        """Return the name of the TypedDict typing the metadata of the BaSyx class of `referable`
        (e.g. PropertyMetadata), which is defined once in the generated module"""
        basyx_cls = type(referable)
        name = util.metadata_cls_name(basyx_cls)
        if name not in self.metadata_classes:
            args = util.metadata_args(basyx_cls)
            typehints = StringHandler.reprify_kwarg_values(get_typehints_for_args(referable, args))
            self.metadata_classes[name] = (StringHandler.reprify(basyx_cls),
                                           {arg: typehints.get(arg, "Any") for arg in args})
        return name

    def get_raw_value_typehint(self, se: SubmodelElement) -> Optional[str]:
        """Return the typehint of a raw value the specific class of `se` can be built from,
        or None if it can only be passed as a submodel element"""
        if isinstance(se, Property):
            return StringHandler.reprify(se.value_type)
        elif isinstance(se, Range):
            return f"Tuple[{StringHandler.reprify(se.value_type)}, {StringHandler.reprify(se.value_type)}]"
        elif isinstance(se, MultiLanguageProperty):
            return f"{MODEL_ALIAS}.MultiLanguageTextType"
        elif isinstance(se, ReferenceElement):
            return f"{MODEL_ALIAS}.Reference"
        elif isinstance(se, SubmodelElementList):
            # Lists can be built from their items, which can be raw values as well
            return f"Iterable[{self.get_list_item_typehint(se, qualified=True)}]"
        return None

    def get_list_item_typehint(self, se_list: SubmodelElementList, qualified: bool = False) -> str:
        """Return the typehint of an item of `se_list`, qualified with the name of the
        list class (as needed outside of it), if `qualified`"""
        list_item = next(iter(se_list), None)
        if list_item is None:
            # Without an item in the template, items are only typed by type_value_list_element
            typehint = util.qualified_name(se_list.type_value_list_element)
            if se_list.type_value_list_element is Property and se_list.value_type_list_element is not None:
                typehint = f"Union[{StringHandler.reprify(se_list.value_type_list_element)}, {typehint}]"
            return typehint

        typehint = NamingGenerator.create_specific_referable_cls_name(list_item)
        if qualified:
            typehint = f"{NamingGenerator.create_specific_referable_cls_name(se_list)}.{typehint}"
        raw_value_typehint = self.get_raw_value_typehint(list_item)
        if raw_value_typehint is not None:
            typehint = f"Union[{raw_value_typehint}, {typehint}]"
        return typehint

    def get_list_item_raw_value_builder(self, se_list: SubmodelElementList, raw_value: str) -> Optional[str]:
        """Return code building an item of `se_list` in its list class from the raw value in the
        variable `raw_value`, or None if items can not be built from raw values"""
        list_item = next(iter(se_list), None)
        if list_item is not None:
            return self.get_raw_value_builder(list_item, raw_value)
        if se_list.type_value_list_element is Property and se_list.value_type_list_element is not None:
            # The value type is metadata, which may be passed
            value_type = StringHandler.reprify(se_list.value_type_list_element)
            return f'{MODEL_ALIAS}.Property(None, {util.METADATA_ARG}.get("value_type_list_element", {value_type}), {raw_value})'

        return None

    def get_raw_value_builder(self, se: SubmodelElement, raw_value: str) -> Optional[str]:
        """Return code building the specific class of `se` from the raw value in the
        variable `raw_value`, or None if it can not be built from a raw value"""
        if self.get_raw_value_typehint(se) is None:
            return None
        cls_name = NamingGenerator.create_specific_referable_cls_name(se)
        if isinstance(se, Range):
            # A raw range is a (min, max) pair
            return f"self.{cls_name}(min={raw_value}[0], max={raw_value}[1])"
        return f"self.{cls_name}({raw_value})"

    def get_se_typehint(self, se, add_raw_val_type=True):
        typehint = NamingGenerator.create_specific_referable_cls_name(se)

        raw_value_typehint = self.get_raw_value_typehint(se)
        if add_raw_val_type and raw_value_typehint is not None:
            typehint = f"Union[{raw_value_typehint}, {typehint}]"

        if ReferableHandler.takes_several(se):
            typehint = f"Iterable[{typehint}]"
        if ReferableHandler.is_optional(se):
            typehint = f"Optional[{typehint}]"
        return typehint

    def add_se_arg_render_kwargs(self, render_kwargs: dict, se: SubmodelElement, arg: str):
        """Add typehint and raw value builder of the init argument `arg` taking `se`"""
        render_kwargs["typehints"][arg] = self.get_se_typehint(se)

        iterable = ReferableHandler.takes_several(se)
        if iterable or isinstance(se, SubmodelElementList):
            # Lists can be built from several items, so a str is rejected here already,
            # naming the argument it was passed to
            render_kwargs.setdefault("args_taking_several", []).append(arg)
        builder = self.get_raw_value_builder(se, raw_value="i" if iterable else arg)
        if builder is not None:
            render_kwargs.setdefault("raw_value_builders", {})[arg] = {
                "iterable": iterable, "code": builder}

    def gen_cls_for_submodel(self, submodel: Submodel,
                             template: str = 'submodel_class.pyi') -> str:
        # Define the variables for the template
        # Generated classes build instances of the template
        render_kwargs = self.default_referable_render_kwargs(
            submodel, exclude_from_args=["submodel_element"], defaults={"kind": ModellingKind.INSTANCE})

        se_as_args = [NamingGenerator.create_arg_name_for_referable(i) for i in submodel]
        for se, arg in zip(submodel, se_as_args):
            self.add_se_arg_render_kwargs(render_kwargs, se, arg)
        render_kwargs["kwargs"].pop("id_")
        render_kwargs["args"].append("id_")

        embedded_se_classes = "\n\n".join(
            [self.gen_cls_for_se(se) for se in submodel])

        # Render the template with the given variables
        render_kwargs.update(before_init_content=embedded_se_classes,
                             args_for_submodel_elements=se_as_args,
                             either_or_groups=self.get_either_or_groups(submodel, se_as_args))
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_se(self, se: SubmodelElement,
                       template: str = 'base_class.pyi') -> str:
        if isinstance(se, Property):
            return self.gen_cls_for_property(se)
        elif isinstance(se, MultiLanguageProperty):
            return self.gen_cls_for_multilang_property(se)
        elif isinstance(se, ReferenceElement):
            return self.gen_cls_for_reference_element(se)
        elif isinstance(se, Range):
            return self.gen_cls_for_range(se)
        elif isinstance(se, SubmodelElementCollection):
            return self.gen_cls_for_se_collection(se)
        elif isinstance(se, Entity):
            return self.gen_cls_for_entity(se)
        elif isinstance(se, SubmodelElementList):
            return self.gen_cls_for_se_list(se)
        elif isinstance(se, File):
            return self.gen_cls_for_file(se)
        else:
            return self.render_cls_with_template(
                template, **self.default_referable_render_kwargs(se))

    def render_cls_with_template(self, template: str, *args: Any, **kwargs: Any):
        template = self.env.get_template(template)
        rendered_class = template.render(*args, **kwargs)
        return rendered_class

    def default_referable_render_kwargs(self, referable: Referable,
                                        exclude_from_args: Iterable[str] = None,
                                        include_in_args: Iterable[str] = None,
                                        remove_numeric_ending_from_id_short = True,
                                        defaults: Optional[dict] = None) -> dict:
        """Return the variables for rendering the class of `referable`. Its values (see util.VALUE_ARGS) are
        init arguments: those in `include_in_args` without default, the others with the template's value
        as default. Its metadata are keyword arguments, typed by a TypedDict (see add_metadata_cls), whose
        template's values (its attributes, except for those given in `defaults`) template_defaults() returns,
        if they differ from the defaults of BaSyx"""
        exceptions = ["parent"]
        if exclude_from_args is not None:
            exceptions.extend(exclude_from_args)
        referable_kwargs = util.get_kwargs_for_init(referable, exceptions=exceptions)

        if remove_numeric_ending_from_id_short and hasattr(referable, "id_short"):
            referable_kwargs["id_short"] = NamingGenerator.create_id_short_stem(referable)
        if isinstance(referable.parent, SubmodelElementList):
            # IdShorts of list items are optional since metamodel V3.1 (AASd-120 was removed),
            # but must be unique: a default idShort would be the same for all items
            referable_kwargs["id_short"] = None
        if isinstance(referable, Qualifiable):
            referable_kwargs["qualifier"] = util.instance_qualifiers(referable)
        referable_kwargs.update(defaults or {})

        basyx_cls = type(referable)
        args = [i for i in include_in_args] if include_in_args else []
        kwargs = {arg: referable_kwargs.pop(arg) for arg in util.VALUE_ARGS.get(basyx_cls, ()) if arg in referable_kwargs}
        template_defaults = {arg: value for arg, value in referable_kwargs.items()
                             if not util.is_init_default(basyx_cls, arg, value)}
        typehints = get_typehints_for_args(referable, [*args, *kwargs])

        return {
            "cls_name": NamingGenerator.create_specific_referable_cls_name(referable),
            "parent_cls_name": StringHandler.reprify(basyx_cls),
            "args": args,
            "kwargs": StringHandler.reprify_kwarg_values(kwargs),
            "typehints": StringHandler.reprify_kwarg_values(typehints),
            "metadata_cls": self.add_metadata_cls(referable),
            "template_defaults": StringHandler.reprify_kwarg_values(template_defaults),
        }


    def gen_cls_for_se_list(self, se_list: SubmodelElementList, template: str = 'se_list_class.pyi') -> str:
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(se_list, exclude_from_args=["value"])

        list_item = next(iter(se_list), None)
        list_items_arg = f"{render_kwargs['cls_name']}_items".lower()

        # The items argument always takes several items, whose cardinality qualifier
        # (if any) tells if the list may be empty
        typehint = f"Iterable[{self.get_list_item_typehint(se_list)}]"
        if list_item is None or ReferableHandler.is_optional(list_item):
            typehint = f"Optional[{typehint}]"
        render_kwargs["typehints"][list_items_arg] = typehint
        builder = self.get_list_item_raw_value_builder(se_list, raw_value="i")
        if builder is not None:
            render_kwargs["raw_value_builders"] = {list_items_arg: {"iterable": True, "code": builder}}

        if list_item is not None:
            render_kwargs["before_init_content"] = self.gen_cls_for_se(list_item)
        # Don't append an index to idShorts of items: they are None by default, explicit ones are kept
        render_kwargs.update(args_for_submodel_elements=[list_items_arg], args_taking_several=[list_items_arg],
                             index_id_shorts=False, parent_cls_name=util.LIST_BASE_CLS)
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_se_collection(self,
                                  se_collection: SubmodelElementCollection,
                                  template: str = 'se_col_class.pyi') -> str:
        return self.gen_cls_with_se_args(se_collection, se_collection.value, "value", template)

    def gen_cls_for_entity(self, entity: Entity, template: str = 'entity_class.pyi') -> str:
        # The statements of an entity are its submodel elements, like the value of a collection
        return self.gen_cls_with_se_args(entity, entity.statement, "statement", template)

    def gen_cls_with_se_args(self, referable: Referable, submodel_elements: Iterable[SubmodelElement],
                             elements_attr: str, template: str) -> str:
        """Render the class of a collection or entity, which takes its `submodel_elements` (in the
        attribute `elements_attr`) as arguments and has a nested class for each of them"""
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(referable, exclude_from_args=[elements_attr])

        # generate arg names for the submodel elements
        se_args = [NamingGenerator.create_arg_name_for_referable(i) for i in submodel_elements]
        # provide args of the submodel elements with typehints
        for se, arg in zip(submodel_elements, se_args):
            self.add_se_arg_render_kwargs(render_kwargs, se, arg)

        embedded_se_classes = "\n\n".join([self.gen_cls_for_se(se) for se in submodel_elements])

        render_kwargs.update(before_init_content=embedded_se_classes, args_for_submodel_elements=se_args,
                             either_or_groups=self.get_either_or_groups(submodel_elements, se_args))
        return self.render_cls_with_template(template, **render_kwargs)

    def _default_referable_render_kwargs_with_value_in_args(self, se: SubmodelElement):
        return self.default_referable_render_kwargs(se,
                                                    exclude_from_args=["value"],
                                                    include_in_args=["value"])

    def gen_cls_for_property(self, se: Property,
                             template: str = 'property_class.pyi') -> str:
        default_value = self.get_default_value(se)
        if default_value is None:
            render_kwargs = self._default_referable_render_kwargs_with_value_in_args(se)
        else:
            # The value defaults to the default value of the template, as first keyword argument
            render_kwargs = self.default_referable_render_kwargs(se, exclude_from_args=["value"])
            render_kwargs["kwargs"] = {"value": StringHandler.reprify(default_value), **render_kwargs["kwargs"]}
        render_kwargs["typehints"]["value"] = StringHandler.reprify(se.value_type)
        constraints = self.get_value_constraints(se)
        if "ALLOWED_PATTERN" in constraints:
            getattr(self, "imported_modules", set()).add("re")
        render_kwargs["value_constraints"] = {name: StringHandler.reprify(value) for name, value in constraints.items()}
        return self.render_cls_with_template(template, **render_kwargs)

    @classmethod
    def get_value_constraints(cls, se: Property) -> dict:
        """Return the class attributes restricting the value of `se`, given by its qualifiers:
        - ALLOWED_VALUES: tuple of values, from SMT/AllowedValue with a list of values (separated by ";" or "|"),
          SMT/AllowedValue1, 2, ..., FormChoices (separated by ";" or ","), and enumeration (separated by ",")
        - ALLOWED_PATTERN: regular expression from SMT/AllowedValue without separator
        - ALLOWED_RANGE: (minimum, maximum or None) from SMT/AllowedRange ("[0,100]", "ZeroToInf") of numbers
        Templates use these qualifiers inconsistently: constraints that can't be interpreted are ignored with a warning"""
        constraints = {}
        value_lists = []
        indexed_values = []

        def ignore(qualifier, reason):
            warnings.warn(f"Ignoring {qualifier.type} {qualifier.value!r} of {se!r}: {reason}")

        for qualifier in se.qualifier:
            type_ = qualifier.type.strip().lower()
            value = qualifier.value
            if not isinstance(value, str) or not value.strip():
                continue
            if type_ == "smt/allowedvalue":
                if ";" in value or "|" in value:
                    value_lists.append((qualifier, re.split(r"[;|]", value)))
                else:
                    try:
                        re.compile(value)
                        constraints["ALLOWED_PATTERN"] = value
                    except re.error as e:
                        ignore(qualifier, f"no regular expression ({e})")
            elif re.fullmatch(r"smt/allowedvalue\d+", type_):
                indexed_values.append(value)
            elif type_ in ("formchoices", "enumeration"):
                values = re.split(r"[;,]" if type_ == "formchoices" else ",", value)
                if len([v for v in values if v.strip()]) < 2:
                    ignore(qualifier, "a single value isn't a list of allowed values")
                else:
                    value_lists.append((qualifier, values))
            elif type_ == "smt/allowedrange":
                try:
                    constraints["ALLOWED_RANGE"] = cls.parse_range(value, se.value_type)
                except ValueError as e:
                    ignore(qualifier, str(e))
        if indexed_values:
            value_lists.append((Qualifier("SMT/AllowedValue<n>", str, value=";".join(indexed_values)), indexed_values))

        allowed = None
        for qualifier, values in value_lists:
            try:
                typed = [cls.to_value_type(v.strip(), se.value_type) for v in values if v.strip()]
            except ValueError as e:
                ignore(qualifier, str(e))
                continue
            typed = list(dict.fromkeys(typed))
            # All lists restrict the value
            allowed = typed if allowed is None else [v for v in allowed if v in typed]
        if allowed:
            constraints["ALLOWED_VALUES"] = tuple(allowed)
        elif allowed is not None:
            warnings.warn(f"Ignoring the allowed values of {se!r}: its lists of allowed values have no value in common")
        return constraints

    @staticmethod
    def to_value_type(lexical: str, value_type: type):
        """Convert an allowed value to `value_type`; booleans are given as True/False as well"""
        if value_type is datatypes.Boolean:
            if lexical.lower() in ("true", "false", "1", "0"):
                return lexical.lower() in ("true", "1")
            raise ValueError(f"{lexical!r} is no boolean")
        try:
            return datatypes.from_xsd(lexical, value_type)
        except ValueError as e:
            raise ValueError(f"{lexical!r} is no value of {value_type.__name__}") from e

    @staticmethod
    def parse_range(value: str, value_type: type) -> tuple:
        """Return (minimum, maximum or None) of an allowed range, e.g. "[0,100]", "[0x00 , 0x1f]", "ZeroToInf" """
        if value_type is datatypes.Boolean or not issubclass(value_type, (int, float, decimal.Decimal)):
            raise ValueError(f"ranges only apply to numbers, not to {value_type.__name__}")
        if value.strip().lower() == "zerotoinf":
            return value_type(0), None
        match = re.fullmatch(r"\s*\[\s*([^,\s]+)\s*,\s*([^\]\s]+)\s*\]\s*", value)
        if not match:
            raise ValueError("no range like [minimum,maximum]")
        bounds = []
        for bound in match.groups():
            try:
                bounds.append(value_type(int(bound, 0)) if re.fullmatch(r"[+-]?(0[xX][0-9a-fA-F]+|\d+)", bound)
                              else datatypes.from_xsd(bound, value_type))
            except ValueError as e:
                raise ValueError(f"{bound!r} is no value of {value_type.__name__}") from e
        return tuple(bounds)

    @staticmethod
    def get_either_or_groups(submodel_elements: Iterable[SubmodelElement], se_args: Iterable[str]) -> list:
        """Return the arguments of each group of `submodel_elements` with the same SMT/EitherOr value, of
        which only one may be given, and the code of the error message. A value of a single element isn't
        a group (e.g. a list of values in Safety Instrumented Functions)"""
        groups = {}
        for se, arg in zip(submodel_elements, se_args):
            for qualifier in se.qualifier:
                if qualifier.type.strip().lower() == "smt/eitheror" and qualifier.value:
                    groups.setdefault(qualifier.value, []).append(arg)
        return [(args, StringHandler.reprify(f"Only one of {', '.join(args)} may be given (SMT/EitherOr {group!r})"))
                for group, args in groups.items() if len(args) > 1]

    # Qualifiers giving the default value of a Property, by priority
    DEFAULT_VALUE_QUALIFIERS = ("smt/defaultvalue", "defaultvalue", "smt/initialvalue")

    @classmethod
    def get_default_value(cls, se: Property):
        """Return the default value of `se` given by its qualifiers SMT/DefaultValue, DefaultValue or
        SMT/InitialValue, converted to its value type, or None if it has none"""
        qualifiers = {q.type.strip().lower(): q for q in se.qualifier}
        for qualifier_type in cls.DEFAULT_VALUE_QUALIFIERS:
            qualifier = qualifiers.get(qualifier_type)
            if qualifier is None or qualifier.value is None:
                continue
            lexical = qualifier.value if isinstance(qualifier.value, str) else datatypes.xsd_repr(qualifier.value)
            try:
                return datatypes.from_xsd(lexical, se.value_type)
            except ValueError:
                warnings.warn(f"Ignoring {qualifier.type} {lexical!r} of {se!r}, as it isn't a value of its value "
                              f"type {se.value_type.__name__}")
        return None

    def gen_cls_for_multilang_property(self, se: MultiLanguageProperty,
                             template: str = 'base_class.pyi') -> str:
        render_kwargs = self._default_referable_render_kwargs_with_value_in_args(se)
        render_kwargs["typehints"]["value"] = f"{MODEL_ALIAS}.MultiLanguageTextType"
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_reference_element(self, se: ReferenceElement,
                             template: str = 'base_class.pyi') -> str:
        render_kwargs = self._default_referable_render_kwargs_with_value_in_args(se)
        render_kwargs["typehints"]["value"] = f"{MODEL_ALIAS}.Reference"
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_range(self, se: Range,
                             template: str = 'base_class.pyi') -> str:
        render_kwargs = self.default_referable_render_kwargs(
            se, exclude_from_args=["min", "max"], include_in_args=["min", "max"])
        render_kwargs["typehints"]["min"] = StringHandler.reprify(se.value_type)
        render_kwargs["typehints"]["max"] = StringHandler.reprify(se.value_type)
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_file(self, se: File,
                         template: str = 'base_class.pyi') -> str:
        if se.content_type == "{arbitrary}":
            render_kwargs = self.default_referable_render_kwargs(
                se, exclude_from_args=["value", "content_type"],
                include_in_args=["value", "content_type"])
            render_kwargs["typehints"]["value"] = "str"
            render_kwargs["typehints"]["content_type"] = "str"
        else:
            render_kwargs = self._default_referable_render_kwargs_with_value_in_args(se)
            render_kwargs["typehints"]["value"] = "str"
        return self.render_cls_with_template(template, **render_kwargs)
