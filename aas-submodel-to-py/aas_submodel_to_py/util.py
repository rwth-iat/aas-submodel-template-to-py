import builtins
import datetime
import decimal
import enum
import keyword
import pydoc
import types
import typing
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
TYPING_IMPORTS = ("Any", "ForwardRef", "Iterable", "Optional", "Tuple", "Union")
# Names generated code uses unqualified, which generated classes must not shadow
RESERVED_CLS_NAMES = frozenset(TYPING_IMPORTS) | frozenset(dir(builtins)) | frozenset(keyword.kwlist)
# Init arguments must not shadow the module aliases used in the init body
RESERVED_ARG_NAMES = frozenset((MODEL_ALIAS, DATATYPES_ALIAS)) | frozenset(keyword.kwlist)

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
        """Return the idShort without its iteration ending (e.g. "Document01" -> "Document"),
        unless siblings would get the same name (e.g. "AddressLine1", "AddressLine2")"""
        id_short = obj.id_short
        if id_short is None:
            return None
        stem = StringHandler.remove_iteration_ending(id_short)
        if stem != id_short and any(
                cls._name_key(StringHandler.remove_iteration_ending(sibling.id_short)) == cls._name_key(stem)
                for sibling in cls._siblings(obj)):
            return id_short
        return stem

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
        # check if arg_name is reserved or is already used in the class as an attribute
        if arg_name in RESERVED_ARG_NAMES or hasattr(obj, arg_name):
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
            Type[_SE]: f"{MODEL_ALIAS}.SubmodelElement",
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

def instance_qualifiers(obj: Qualifiable) -> tuple:
    """Return the qualifiers of the template element `obj` that its instances take over: template
    qualifiers (e.g. SMT/Cardinality) are only allowed in templates (AASd-119, AASd-129)"""
    return tuple(q for q in obj.qualifier if q.kind is not QualifierKind.TEMPLATE_QUALIFIER)


def get_typehints_for_args(obj, args):
    args_typehints = {}
    typehints = inspect.getfullargspec(type(obj).__init__).annotations
    for arg in args:
        if arg in typehints:
            args_typehints[arg] = typehints[arg]
    return args_typehints


# Values that can't be changed, so that instances can share them as default values
# (BaSyx References and Keys are immutable)
IMMUTABLE_TYPES = (type(None), bool, int, float, str, bytes, decimal.Decimal, datetime.date, datetime.time,
                   enum.Enum, type, Reference, Key)


def is_mutable(obj) -> bool:
    """Return if `obj` can be changed or holds objects that can (e.g. a tuple of submodel elements),
    so that it must be created for each instance instead of being shared as a default value"""
    if isinstance(obj, TUPLE_TYPES):
        return any(is_mutable(item) for item in obj)
    return not isinstance(obj, IMMUTABLE_TYPES)