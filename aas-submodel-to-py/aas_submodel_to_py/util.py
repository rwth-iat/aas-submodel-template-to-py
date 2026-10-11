import builtins
import enum
import keyword
import pydoc
import types
import inspect
import typing
from typing import List
from basyx.aas import model as aas_model
from basyx.aas.model import *
from basyx.aas.model import datatypes as aas_datatypes
from basyx.aas.model.datatypes import XSD_TYPE_NAMES, Duration, DateTime, Time, xsd_repr
from basyx.aas.model.submodel import _SE

# Generated modules refer to basyx.aas.model and basyx.aas.model.datatypes through
# these module aliases (see code_templates/imports.pyi), so that generated classes
# named like BaSyx classes (e.g. an element "Key") don't shadow them
MODEL_ALIAS = "aas"
DATATYPES_ALIAS = "xsd"
# Names generated modules import from typing
TYPING_IMPORTS = ("Any", "ForwardRef", "Iterable", "Optional", "Tuple", "TypedDict", "Union", "Unpack")
# Helpers each generated module defines (see code_templates/helpers.pyi): creating references to global
# identifiers, collecting the submodel elements passed to inits and the base class of list classes
GLOBAL_REF_HELPER = "global_ref"
COLLECT_HELPER = "collect_submodel_elements"
LIST_BASE_CLS = "GeneratedSubmodelElementList"

# Init arguments of BaSyx classes, which generated classes take explicitly, as they are values of the element.
# The other ones (metadata, e.g. semantic_id) are keyword arguments, typed by a TypedDict (see metadata_cls_name)
VALUE_ARGS = {
    Submodel: ("id_",),
    Property: ("value",),
    MultiLanguageProperty: ("value",),
    Range: ("min", "max"),
    ReferenceElement: ("value",),
    File: ("value", "content_type"),
    Blob: ("value", "content_type"),
}
# Init arguments of BaSyx classes taking the submodel elements, which generated classes build from their arguments
ELEMENT_ARGS = {
    Submodel: "submodel_element",
    SubmodelElementCollection: "value",
    SubmodelElementList: "value",
    Entity: "statement",
}
# Name of the parameter of generated inits taking the metadata
METADATA_ARG = "kwargs"


def metadata_cls_name(basyx_cls: type) -> str:
    """Return the name of the TypedDict typing the metadata of `basyx_cls` (e.g. PropertyMetadata)"""
    return f"{basyx_cls.__name__}Metadata"


def metadata_args(basyx_cls: type) -> List[str]:
    """Return the init arguments of `basyx_cls`, which generated classes take as metadata"""
    excluded = {"self", "parent", *VALUE_ARGS.get(basyx_cls, ()), ELEMENT_ARGS.get(basyx_cls)}
    return [arg for arg in inspect.signature(basyx_cls.__init__).parameters if arg not in excluded]


def is_init_default(basyx_cls: type, arg: str, value) -> bool:
    """Return if `value` is the default of the init argument `arg` of `basyx_cls`, so that it needn't be passed"""
    default = inspect.signature(basyx_cls.__init__).parameters[arg].default
    if default is inspect.Parameter.empty:
        return False
    if isinstance(default, tuple):
        # Iterables (e.g. qualifier) default to an empty tuple
        return isinstance(value, (*TUPLE_TYPES, list)) and len(value) == 0
    return value is default or (type(value) is type(default) and value == default)


def is_value_arg_name(obj: Referable, arg_name: str) -> bool:
    """Return if `arg_name` is the name of a value or metadata argument of the generated class of `obj`"""
    basyx_cls = type(obj)
    return arg_name in VALUE_ARGS.get(basyx_cls, ()) or arg_name in metadata_args(basyx_cls)
# Names generated code uses unqualified, which generated classes must not shadow
RESERVED_CLS_NAMES = (frozenset(TYPING_IMPORTS) | frozenset(dir(builtins)) | frozenset(keyword.kwlist)
                      | frozenset((LIST_BASE_CLS,))
                      | frozenset(metadata_cls_name(cls) for cls in vars(aas_model).values()
                                  if isinstance(cls, type) and issubclass(cls, Referable)))
# Init arguments must not shadow the module aliases used in the init body (and the module re, used
# for checking allowed values, and the helpers), nor be named like the other parameters of inits
RESERVED_ARG_NAMES = (frozenset((MODEL_ALIAS, DATATYPES_ALIAS, "re", GLOBAL_REF_HELPER, COLLECT_HELPER,
                                 "self", METADATA_ARG))
                      | frozenset(keyword.kwlist))

# Collections rendered as tuples in generated code (see StringHandler.reprify)
TUPLE_TYPES = (tuple, NamespaceSet, ConstrainedList)

# XSD types defined as aliases in basyx.aas.model.datatypes: their class names
# (relativedelta, datetime, time) don't exist in basyx.aas.model.datatypes
XSD_TYPE_ALIASES = {
    Duration: "Duration",
    DateTime: "DateTime",
    Time: "Time",
}


def qualified_name(typ: type) -> str:
    """Return the name, under which `typ` is available in generated modules"""
    name = typ.__name__
    if typ is type(None):
        # NoneType isn't a builtin name, e.g. the referred type of ModelReferences to fragments
        return "type(None)"
    elif getattr(builtins, name, None) is typ:
        return name
    elif typ in XSD_TYPE_ALIASES:
        return f"{DATATYPES_ALIAS}.{XSD_TYPE_ALIASES[typ]}"
    elif getattr(aas_datatypes, name, None) is typ:
        return f"{DATATYPES_ALIAS}.{name}"
    elif getattr(aas_model, name, None) is typ:
        return f"{MODEL_ALIAS}.{name}"
    return name


class NamingGenerator:
    @classmethod
    def create_id_short_stem(cls, obj: Referable) -> Optional[str]:
        """Return the idShort without its iteration ending (e.g. "Document01" -> "Document") if the element
        may occur several times, as its instances get an index instead, else without placeholder (e.g.
        "Mode__00__" -> "Mode"), unless siblings would get the same name (e.g. "AddressLine1", "AddressLine2")"""
        id_short = obj.id_short
        if id_short is None:
            return None
        stem = cls._stem(obj)
        if stem != id_short and any(cls._name_key(cls._stem(sibling)) == cls._name_key(stem)
                                    for sibling in cls._siblings(obj)):
            return id_short
        return stem

    @staticmethod
    def _stem(obj: Referable) -> str:
        # Trailing digits of elements occurring once are part of their name (e.g. "ISO8601", issue #41)
        if isinstance(obj, Qualifiable) and ReferableHandler.takes_several(obj):
            return StringHandler.remove_iteration_ending(obj.id_short)
        return StringHandler.remove_placeholder(obj.id_short)

    @staticmethod
    def _name_key(name: str) -> str:
        # Class and argument names only differ in the case of the first letter
        return StringHandler.lower_first(name)

    @staticmethod
    def _siblings(obj: Referable) -> List[Referable]:
        parent = obj.parent
        if not isinstance(parent, UniqueIdShortNamespace):
            return []
        return [element for namespace_set in parent.namespace_element_sets for element in namespace_set
                if element is not obj and isinstance(element, Referable) and element.id_short is not None]

    @classmethod
    def create_specific_referable_cls_name(cls, obj: Referable) -> str:
        if isinstance(obj.parent, SubmodelElementList):
            # Items of lists are named after their list (e.g. "Phases_item"), as their idShort is optional
            return StringHandler.upper_first(f"{cls.create_specific_referable_cls_name(obj.parent)}_item".lower())
        cls_name = StringHandler.upper_first(cls.create_id_short_stem(obj))
        if cls_name in RESERVED_CLS_NAMES:
            return f"{cls_name}_"
        return cls_name

    @classmethod
    def create_arg_name_for_referable(cls, obj: Referable) -> str:
        arg_name = StringHandler.lower_first(cls.create_id_short_stem(obj))
        # check if arg_name is reserved, is already used in the class as an attribute
        # or is the name of another argument of the init taking it
        if arg_name in RESERVED_ARG_NAMES or hasattr(obj, arg_name) \
                or (obj.parent is not None and is_value_arg_name(obj.parent, arg_name)):
            return f"{arg_name}_"
        return arg_name


class ReferableHandler:
    @classmethod
    def get_cardinality(cls, obj: Qualifiable) -> Optional[str]:
        """Return the value of the cardinality qualifier of `obj` in lower case (e.g. "zerotomany"),
        or None if it has none. Templates spell these qualifiers in several ways, e.g. the type
        "SMT/Cardinality", "Multiplicity" or "SMT/SMT/Cardinality" and the value "ZerotoOne" or "ZeroToOne " """
        for q in obj.qualifier:
            if q.type.rsplit("/", 1)[-1].strip().lower() in ("cardinality", "multiplicity") \
                    and isinstance(q.value, str):
                return q.value.strip().lower()
        return None

    @classmethod
    def is_optional(cls, obj: Qualifiable) -> Optional[bool]:
        cardinality = cls.get_cardinality(obj)
        if cardinality is None:
            return None
        # ZeroToOne, ZeroToMany
        return cardinality.startswith("zero")

    @classmethod
    def is_iterable(cls, obj: Qualifiable) -> Optional[bool]:
        cardinality = cls.get_cardinality(obj)
        if cardinality is None:
            return None
        # ZeroToMany, OneToMany, TwoToMany
        return cardinality.endswith("tomany")

    @classmethod
    def takes_several(cls, obj: Qualifiable) -> bool:
        """Return if arguments taking `obj` take several elements like it. Lists never do: they
        already hold several items, so a cardinality ZeroToMany/OneToMany of a list is meant for
        its items and only tells if the list is optional"""
        return not isinstance(obj, SubmodelElementList) and bool(cls.is_iterable(obj))


class StringHandler:
    @classmethod
    def upper_first(cls, val: str):
        if not val:
            return val
        return f"{val[0].upper()}{val[1:]}"

    @classmethod
    def lower_first(cls, val: str):
        if not val:
            return val
        return f"{val[0].lower()}{val[1:]}"

    @classmethod
    def remove_placeholder(cls, val: str):
        # remove placeholders for numbers like {00} or __00__
        return re.sub(r'(\{\d+\}|__\d+__)$', '', val)

    @classmethod
    def remove_iteration_ending(cls, val: str):
        # remove iteration ending like {00}
        val = re.sub(r'\{\d+\}$', '', val)
        # remove one or more digits at the end
        val = re.sub(r'_?\d+$', '', val)
        # remove one or more digits at the end like something__00__
        val = re.sub(r'__\d+__$', '', val)
        return val

    @classmethod
    def qualify_names_in_typehint(cls, typehint: str):
        """Replace the fully qualified names in the repr of a typehint (e.g.
        "typing.Optional[basyx.aas.model.base.Reference]") by the names available in
        generated modules (e.g. "Optional[aas.Reference]")"""
        def name_in_generated_module(match):
            full_name = match.group(0)
            short_name = full_name.split(".")[-1]
            if full_name.startswith("typing."):
                return short_name
            # Forward references in BaSyx use its own module aliases, e.g. "aas.AssetAdministrationShell"
            obj = pydoc.locate(full_name) or getattr(aas_model, short_name, None)
            return qualified_name(obj) if isinstance(obj, type) else short_name

        return re.sub(r"\w+(\.\w+)+", name_in_generated_module, typehint)

    @classmethod
    def typehint_repr(cls, typehint) -> str:
        """Return the code of a typehint (e.g. "Optional[aas.Reference]"), built from its origin and
        arguments the same way on every Python version. Since Python 3.14, Optional[X] and Union[X, Y]
        are represented as "X | None", which can't be evaluated with forward references"""
        origin, args = typing.get_origin(typehint), typing.get_args(typehint)
        if origin is typing.Union or origin is types.UnionType:
            if len(args) == 2 and type(None) in args:
                return f"Optional[{cls.typehint_repr(next(arg for arg in args if arg is not type(None)))}]"
            return f"Union[{', '.join(cls.typehint_repr(arg) for arg in args)}]"
        elif origin is not None:
            # Generic alias, e.g. typing.Iterable[...] or basyx.aas.model.base.ModelReference[...]
            name = cls.qualify_names_in_typehint(repr(typehint).split("[", 1)[0])
            return f"{name}[{', '.join(cls.typehint_repr(arg) for arg in args)}]" if args else name
        elif isinstance(typehint, typing.ForwardRef):
            return cls.qualify_names_in_typehint(f"ForwardRef({typehint.__forward_arg__!r})")
        elif typehint is type(None):
            return "None"
        elif typehint is Ellipsis:
            return "..."
        elif isinstance(typehint, type):
            return qualified_name(typehint)
        # e.g. TypeVars
        return cls.qualify_names_in_typehint(repr(typehint))

    @classmethod
    def reprify(cls, val):
        typehint_reprs = {
            DataTypeDefXsd: f"{MODEL_ALIAS}.DataTypeDefXsd",
            ValueDataType: f"{MODEL_ALIAS}.ValueDataType",
            LangStringSet: f"{MODEL_ALIAS}.LangStringSet",
            Optional[DataTypeDefXsd]: f"Optional[{MODEL_ALIAS}.DataTypeDefXsd]",
            Optional[ValueDataType]: f"Optional[{MODEL_ALIAS}.ValueDataType]",
            Optional[LangStringSet]: f"Optional[{MODEL_ALIAS}.LangStringSet]",
            _SE: f"{MODEL_ALIAS}.SubmodelElement",
            Type[_SE]: f"type[{MODEL_ALIAS}.SubmodelElement]",
        }
        for typehint in typehint_reprs:
            if val == typehint:
                return typehint_reprs[typehint]

        if val is None:
            return "None"
        elif typing.get_origin(val) is not None:
            return cls.typehint_repr(val)
        elif type(val) is str:
            # Prefer raw string literals, which keep backslashes (e.g. in regex patterns)
            # readable. They can't contain the quote or line breaks, nor end with a backslash
            if any(char in val for char in "'\n\r\0") or val.endswith("\\"):
                return repr(val)
            return f"r'{val}'"
        elif type(val) in (bool, int, float):
            return str(val)
        elif type(val) in XSD_TYPE_NAMES:
            # Values of other XSD types (e.g. Duration, DateTime, Long) are restored from
            # their XSD lexical representation, as their constructors differ widely
            return f"{DATATYPES_ALIAS}.from_xsd({cls.reprify(xsd_repr(val))}, {cls.reprify(type(val))})"
        elif type(val) is dict:
            if val:
                items_repr = [f"{cls.reprify(key)}: {cls.reprify(value)}" for key, value in val.items()]
                res = ",".join(items_repr)
                return f"{{{res}}}"
            return "set()"
        elif type(val) is set:
            if val:
                res = ",".join([cls.reprify(i) for i in val])
                return f"{{{res}}}"
            return "set()"
        elif isinstance(val, type):
            return qualified_name(val)
        elif isinstance(val, enum.Enum):
            return f"{qualified_name(type(val))}.{val.name}"
        elif isinstance(val, List):
            return f"[{', '.join([cls.reprify(i) for i in val])}]"
        elif isinstance(val, TUPLE_TYPES):
            res = f"({', '.join([cls.reprify(i) for i in val])})"
            if len(val) == 1:
                res = f"{res[:-1]},)"
            return res
        elif is_global_reference(val):
            # Rendered compactly, as semantic IDs are such references
            return f"{GLOBAL_REF_HELPER}({cls.reprify(val.key[0].value)})"
        else:
            kwargs = get_kwargs_for_init(val)
            if isinstance(val, Qualifiable):
                kwargs["qualifier"] = instance_qualifiers(val)
            kwargs = cls.reprify_kwarg_values(kwargs)
            kwargs_repr = ", ".join([f"{arg}={kwargs[arg]}" for arg in kwargs])
            typ = cls.reprify(type(val))
            res = f"{typ}({kwargs_repr})"
            return res

    @classmethod
    def reprify_kwarg_values(cls, kwargs: Dict):
        for arg in kwargs:
            kwargs[arg] = cls.reprify(kwargs[arg])
        return kwargs


def get_mapped_attr_name_of_arg(obj, arg: str):
    if hasattr(obj, arg):
        return arg
    elif hasattr(obj, arg.strip("_")):
        return arg.strip("_")
    else:
        raise KeyError(f"Attr for the following arg is unknown: {arg}")


def get_mapped_attr_of_arg(obj, arg: str):
    try:
        attr_name = get_mapped_attr_name_of_arg(obj, arg)
        return getattr(obj, attr_name)
    except KeyError as e:
        if arg == "items" and isinstance(obj, NamespaceSet):
            items = tuple([i for i in obj])
            return items
        elif arg == "dict_" and isinstance(obj, LangStringSet):
            return obj._dict
        else:
            raise e


def get_kwargs_for_init(obj, exceptions: Tuple[str] = ("parent",)):
    args: List[str] = inspect.getfullargspec(type(obj).__init__).args
    args.remove("self")

    kwargs = dict()
    for arg in args:
        if arg in exceptions:
            continue
        kwargs[arg] = get_mapped_attr_of_arg(obj, arg)
    return kwargs

# Types of qualifiers that only describe templates, also if they aren't of kind TemplateQualifier:
# older names of qualifiers of the SMT specification and hints for template editors
TEMPLATE_QUALIFIER_TYPES = frozenset((
    "cardinality", "multiplicity", "examplevalue", "example", "defaultvalue",
    "allowedidshort", "editidshort", "presetidshort", "editdescription",
    "forminfo", "formtitle", "formchoices", "formurl", "formtag",
))


def is_template_qualifier(qualifier: Qualifier) -> bool:
    """Return if `qualifier` only describes the template: qualifiers of kind TemplateQualifier, qualifiers
    of the SMT specification (SMT/...) and their older names, and hints for template editors (Form...)"""
    type_ = qualifier.type.strip().lower()
    return qualifier.kind is QualifierKind.TEMPLATE_QUALIFIER or type_.startswith("smt/") \
        or type_ in TEMPLATE_QUALIFIER_TYPES


def is_global_reference(obj) -> bool:
    """Return if `obj` is an external reference to a global identifier, created by the helper global_ref() of
    generated modules: a single key of type GlobalReference, no referred semantic ID"""
    return type(obj) is ExternalReference and len(obj.key) == 1 \
        and obj.key[0].type is KeyTypes.GLOBAL_REFERENCE and obj.referred_semantic_id is None


def instance_qualifiers(obj: Qualifiable) -> tuple:
    """Return the qualifiers of the template element `obj` that its instances take over: template
    qualifiers (e.g. SMT/Cardinality) are only allowed in templates (AASd-119, AASd-129), and other
    qualifiers only describing the template (e.g. Multiplicity, FormInfo) don't belong to instances"""
    return tuple(q for q in obj.qualifier if not is_template_qualifier(q))


def get_typehints_for_args(obj, args):
    args_typehints = {}
    typehints = inspect.getfullargspec(type(obj).__init__).annotations
    for arg in args:
        if arg in typehints:
            args_typehints[arg] = typehints[arg]
    return args_typehints
