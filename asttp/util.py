import enum
import keyword
import typing
from basyx.aas.model import *
from basyx.aas.model.submodel import _SE


class NamingGenerator:
    @classmethod
    def create_specific_referable_cls_name(cls, obj: Referable) -> str:
        cls_name = StringHandler.upper_first(obj.id_short)
        cls_name = StringHandler.remove_iteration_ending(cls_name)
        return cls_name

    @classmethod
    def create_arg_name_for_referable(cls, obj: Referable) -> str:
        arg_name = StringHandler.lower_first(obj.id_short)
        arg_name = StringHandler.remove_iteration_ending(arg_name)
        # check if arg_name is one of python reserved keywords or is already used in the class as an attribute
        if arg_name in keyword.kwlist or hasattr(obj, arg_name):
            return f"{arg_name}_"
        return arg_name


class ReferableHandler:
    @classmethod
    def is_optional(cls, obj: Qualifiable):
        for q in obj.qualifier:
            if q.type in ("Cardinality", "Multiplicity", "SMT/Multiplicity", "SMT/Cardinality"):
                if q.value in ("ZeroToOne", "ZeroToMany"):
                    return True
                elif q.value in ("One", "OneToMany"):
                    return False
        return None

    @classmethod
    def is_iterable(cls, obj: Qualifiable):
        for q in obj.qualifier:
            if q.type in ("Cardinality", "Multiplicity", "SMT/Multiplicity", "SMT/Cardinality"):
                if q.value in ("ZeroToMany", "OneToMany"):
                    return True
                elif q.value in ("ZeroToOne", "One"):
                    return False
        return None


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
    def remove_parent_modules_in_typehint(cls, typehint: str):
        pattern = r"(\w+(\.\w+)+)"
        matches = re.findall(pattern, typehint)
        for match in matches:
            last_word = match[0].split(".")[-1]
            typehint = typehint.replace(match[0], last_word)
        return typehint

    @classmethod
    def reprify(cls, val):
        typehint_reprs = {
            DataTypeDefXsd: "DataTypeDefXsd",
            ValueDataType: "ValueDataType",
            LangStringSet: "LangStringSet",
            Optional[DataTypeDefXsd]: "Optional[DataTypeDefXsd]",
            Optional[ValueDataType]: "Optional[ValueDataType]",
            Optional[LangStringSet]: "Optional[LangStringSet]",
            _SE: "SubmodelElement",
            Type[_SE]: "SubmodelElement",
        }
        for typehint in typehint_reprs:
            if val == typehint:
                return typehint_reprs[typehint]

        if val is None:
            return "None"
        elif isinstance(val, typing._GenericAlias):
            return cls.remove_parent_modules_in_typehint(repr(val))
        elif type(val) is str:
            if "'" in val:
                val = val.replace("'", r"\'")
            return f"'{val}'"
        elif type(val) in (bool, int, float):
            return str(val)
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
            return val.__name__  # .split('.')[-1],
        elif isinstance(val, enum.Enum):
            return str(val)
        elif isinstance(val, List):
            return f"[{', '.join([cls.reprify(i) for i in val])}]"
        elif isinstance(val, (tuple, NamespaceSet, ConstrainedList)):
            res = f"({', '.join([cls.reprify(i) for i in val])})"
            if len(val) == 1:
                res = f"{res[:-1]},)"
            return res
        else:
            kwargs = get_kwargs_for_init(val)
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

def get_typehints_for_args(obj, args):
    args_typehints = {}
    typehints = inspect.getfullargspec(type(obj).__init__).annotations
    for arg in args:
        if arg in typehints:
            args_typehints[arg] = typehints[arg]
    return args_typehints


def is_mutable(obj):
    mutable_types = (list, dict, set, bytearray, memoryview, Referable)

    if isinstance(obj, mutable_types):
        return True
    return False