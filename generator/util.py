import enum
import inspect
import keyword
import typing
from typing import List, Dict, Tuple
from basyx.aas.model import *


class NamingGenerator:
    @classmethod
    def create_specific_referable_cls_name(cls, obj: Referable) -> str:
        cls_name = StringHandler.upper_first(obj.id_short)
        cls_name = StringHandler.remove_iteration_ending(cls_name)
        return cls_name

    @classmethod
    def create_arg_name_for_referable(cls, obj: Referable) -> str:
        res = StringHandler.lower_first(obj.id_short)
        res = StringHandler.remove_iteration_ending(res)
        # check if res is one of python reserved keywords
        if res in keyword.kwlist:
            return f"{res}_"
        return res


class ReferableHandler:
    @classmethod
    def is_optional(cls, obj: Qualifiable):
        for q in obj.qualifier:
            if q.type in ("Cardinality", "Multiplicity"):
                if q.value in ("ZeroToOne", "ZeroToMany"):
                    return True
                elif q.value in ("One", "OneToMany"):
                    return False
        return None

    @classmethod
    def is_iterable(cls, obj: Qualifiable):
        for q in obj.qualifier:
            if q.type in ("Cardinality", "Multiplicity"):
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
        return val

    @classmethod
    def reprify(cls, val):
        if val is None:
            return "None"
        elif type(val) is str:
            return f"'{val}'"
        elif type(val) in (bool, int, float):
            return str(val)
        elif isinstance(val, type):
            return val.__name__  # .split('.')[-1],
        elif isinstance(val, enum.Enum):
            return str(val)
        elif isinstance(val, List):
            return f"[{', '.join([cls.reprify(i) for i in val])}]"
        elif isinstance(val, (tuple, NamespaceSet)):
            return f"({', '.join([cls.reprify(i) for i in val])})"
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
        elif arg == "target_type" and isinstance(obj, AASReference):
            return obj.type
        else:
            raise e


def get_kwargs_and_typehints_from(obj, exceptions: Tuple[str] = ("parent",)):
    args: List[str] = inspect.getfullargspec(type(obj).__init__).args
    args.remove("self")

    kwargs = dict()
    for arg in args:
        if arg in exceptions:
            continue
        kwargs[arg] = get_mapped_attr_of_arg(obj, arg)
    return kwargs


def get_kwargs_for_init(obj, exceptions: Tuple[str] = ("parent",)):
    args: List[str] = inspect.getfullargspec(type(obj).__init__).args
    args.remove("self")

    kwargs = dict()
    for arg in args:
        if arg in exceptions:
            continue
        kwargs[arg] = get_mapped_attr_of_arg(obj, arg)
    return kwargs
