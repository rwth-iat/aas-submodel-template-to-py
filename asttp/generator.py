import os.path
import pathlib
from typing import Union, Iterable, Any

import black
from basyx.aas.adapter.aasx import AASXReader, DictSupplementaryFileContainer
from basyx.aas.adapter.json import read_aas_json_file
from basyx.aas.adapter.xml import read_aas_xml_file
from basyx.aas.model import Property, Referable, Qualifiable, Submodel, \
    SubmodelElement, SubmodelElementCollection, DictObjectStore, MultiLanguageProperty, \
    ReferenceElement, ModelingKind, AbstractObjectStore, SubmodelElementList, Range

from jinja2 import Environment, FileSystemLoader

from asttp import util
from asttp.util import StringHandler, ReferableHandler, NamingGenerator, \
    get_typehints_for_args

CODE_TEMPLATES = os.path.join(os.path.dirname(__file__), 'code_templates')


class SubmodelCodegen:
    def __init__(self, templates_dir=CODE_TEMPLATES):
        # Set the directory containing the Jinja templates
        self.env = Environment(loader=FileSystemLoader(templates_dir))

    def generate_from(self, input_file: Union[str, pathlib.Path],
                      output_file: Union[str, pathlib.Path] = "output.py"):
        input_str = str(input_file).lower()
        if input_str.endswith(".aasx"):
            obj_store = DictObjectStore()
            file_store = DictSupplementaryFileContainer()
            AASXReader(input_file).read_into(obj_store, file_store)
        elif input_str.endswith(".json"):
            with open(input_file, "r", encoding='utf-8-sig') as f:
                obj_store = read_aas_json_file(f)
        elif input_str.endswith(".xml"):
            with open(input_file, 'rb') as xml_file:
                obj_store = read_aas_xml_file(xml_file)

        self.generate_from_obj_store(obj_store, output_file)

    def generate_from_obj_store(self, obj_store: AbstractObjectStore,
                                output_file: Union[str, pathlib.Path] = "output.py"):
        result = f"\n{self.generate_imports()}"

        for obj in obj_store:
            if isinstance(obj, Submodel):
                result = f"{result}\n\n{self.gen_cls_for_submodel(obj)}"

        try:
            # Format the rendered class using Black
            result = black.format_str(result, mode=black.Mode())
        except Exception as e:
            print(e)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

    def generate_imports(self) -> str:
        template = self.env.get_template("imports.pyi")
        imports = template.render()
        return imports

    def get_se_typehint(self, se, add_raw_val_type=True):
        typehint = NamingGenerator.create_specific_referable_cls_name(se)

        if add_raw_val_type:
            if isinstance(se, Property):
                typehint = f"Union[{StringHandler.reprify(se.value_type)}, {typehint}]"
            elif isinstance(se, Range):
                typehint = f"Union[Tuple[{StringHandler.reprify(se.value_type)}, " \
                           f"{StringHandler.reprify(se.value_type)}], {typehint}]"
            elif isinstance(se, MultiLanguageProperty):
                typehint = f"Union[LangStringSet, {typehint}]"
            elif isinstance(se, ReferenceElement):
                typehint = f"Union[Reference, {typehint}]"
            elif isinstance(se, SubmodelElementList) \
                    and se.type_value_list_element is Property \
                    and se.value_type_list_element is not None:
                typehint = f"Union[Iterable[{StringHandler.reprify(se.value_type_list_element)}], {typehint}]"

        if ReferableHandler.is_iterable(se):
            typehint = f"Iterable[{typehint}]"
        if ReferableHandler.is_optional(se):
            typehint = f"Optional[{typehint}]"
        return typehint

    def gen_cls_for_submodel(self, submodel: Submodel,
                             template: str = 'submodel_class.pyi') -> str:
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(
            submodel, exclude_from_args=["submodel_element"])

        se_as_args = [NamingGenerator.create_arg_name_for_referable(i) for i in submodel]
        for se, arg in zip(submodel, se_as_args):
            render_kwargs["typehints"][arg] = self.get_se_typehint(se)
        render_kwargs["kwargs"].pop("id_")
        render_kwargs["args"].append("id_")

        embedded_se_classes = "\n\n".join(
            [self.gen_cls_for_se(se) for se in submodel])

        # Render the template with the given variables
        render_kwargs.update(before_init_content=embedded_se_classes,
                             args_for_submodel_elements=se_as_args)
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
        elif isinstance(se, (SubmodelElementCollection, SubmodelElementList)):
            return self.gen_cls_for_se_collection_or_list(se)
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
                                        remove_numeric_ending_from_id_short = True) -> dict:
        exceptions = ["parent"]
        if exclude_from_args is not None:
            exceptions.extend(exclude_from_args)
        referable_kwargs = util.get_kwargs_for_init(referable, exceptions=exceptions)

        # set default value of kind to INSTANCE,
        # as initialized objects of generated classes will be mostly instances
        if "kind" in referable_kwargs and referable_kwargs["kind"] is ModelingKind.TEMPLATE:
            referable_kwargs["kind"] = ModelingKind.INSTANCE

        if remove_numeric_ending_from_id_short and hasattr(referable, "id_short"):
            referable_kwargs["id_short"] = util.StringHandler.remove_iteration_ending(referable_kwargs["id_short"])

        # Find and save args with mutable defaults to kwargs_with_mutable_defaults
        # Set defaults of these args to None
        # These args will be handled appropriately in the template
        handle_as_arg_with_mutable_default = ["qualifier"]
        kwargs_with_mutable_defaults = {}
        for arg, default in referable_kwargs.items():
            if util.is_mutable(default) or arg in handle_as_arg_with_mutable_default:
                kwargs_with_mutable_defaults[arg] = default
                referable_kwargs[arg] = None

        typehints = get_typehints_for_args(referable, referable_kwargs.keys())

        args = [i for i in include_in_args] if include_in_args else []

        return {
            "cls_name": NamingGenerator.create_specific_referable_cls_name(referable),
            "parent_cls_name": StringHandler.reprify(type(referable)),
            "args": args,
            "kwargs": StringHandler.reprify_kwarg_values(referable_kwargs),
            "kwargs_mutable_defaults": StringHandler.reprify_kwarg_values(
                kwargs_with_mutable_defaults),
            "typehints": StringHandler.reprify_kwarg_values(typehints)
        }

    def gen_cls_for_se_collection_or_list(self,
                                  se_collection: SubmodelElementCollection,
                                  template: str = 'se_col_class.pyi') -> str:
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(se_collection,
                                                             exclude_from_args=["value"])
        # generate arg names for included items of collection
        collection_items = [NamingGenerator.create_arg_name_for_referable(i) for i in
                            se_collection]
        # provide args of included items with typehints
        for se, arg in zip(se_collection, collection_items):
            render_kwargs["typehints"][arg] = self.get_se_typehint(se)

        if isinstance(se_collection, SubmodelElementList) and collection_items:
            collection_items = [collection_items[0]]
            for se in se_collection:
                embedded_se_classes = self.gen_cls_for_se(se)
                break
        else:
            embedded_se_classes = "\n\n".join(
                [self.gen_cls_for_se(se) for se in se_collection])

        render_kwargs.update(before_init_content=embedded_se_classes,
                             args_for_submodel_elements=collection_items)
        return self.render_cls_with_template(template, **render_kwargs)

    def _default_referable_render_kwargs_with_value_in_args(self, se: SubmodelElement):
        return self.default_referable_render_kwargs(se,
                                                    exclude_from_args=["value"],
                                                    include_in_args=["value"])

    def gen_cls_for_property(self, se: Property,
                             template: str = 'base_class.pyi') -> str:
        render_kwargs = self._default_referable_render_kwargs_with_value_in_args(se)
        render_kwargs["typehints"]["value"] = StringHandler.reprify(se.value_type)
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_multilang_property(self, se: MultiLanguageProperty,
                             template: str = 'base_class.pyi') -> str:
        render_kwargs = self._default_referable_render_kwargs_with_value_in_args(se)
        render_kwargs["typehints"]["value"] = "LangStringSet"
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_reference_element(self, se: ReferenceElement,
                             template: str = 'base_class.pyi') -> str:
        render_kwargs = self._default_referable_render_kwargs_with_value_in_args(se)
        render_kwargs["typehints"]["value"] = "Reference"
        return self.render_cls_with_template(template, **render_kwargs)

    def gen_cls_for_range(self, se: Range,
                             template: str = 'base_class.pyi') -> str:
        render_kwargs = self.default_referable_render_kwargs(
            se, exclude_from_args=["min", "max"], include_in_args=["min", "max"])
        render_kwargs["typehints"]["min"] = StringHandler.reprify(se.value_type)
        render_kwargs["typehints"]["max"] = StringHandler.reprify(se.value_type)
        return self.render_cls_with_template(template, **render_kwargs)
