import enum
import inspect
from typing import List, Dict, Tuple
from basyx.aas.model import *


def upper_first(obj: str):
    if not obj:
        return obj
    return f"{obj[0].upper()}{obj[1:]}"


def lower_first(obj: str):
    if not obj:
        return obj
    return f"{obj[0].lower()}{obj[1:]}"


def get_mapped_attr_name(obj, arg: str):
    if hasattr(obj, arg):
        return arg
    elif hasattr(obj, arg.strip("_")):
        return arg.strip("_")
    else:
        raise KeyError(f"Attr for the following arg is unknown: {arg}")


def get_mapped_attr(obj, arg: str):
    try:
        attr_name = get_mapped_attr_name(obj, arg)
        return getattr(obj, attr_name)
    except KeyError as e:
        if arg == "items" and isinstance(obj, NamespaceSet):
            items = tuple([i for i in obj])
            return items
        elif arg == "target_type" and isinstance(obj, AASReference):
            return obj.type
        else:
            raise e


def repr_obj(obj):
    if obj is None:
        return "None"
    elif type(obj) is str:
        return f"'{obj}'"
    elif type(obj) in (bool, int, float):
        return str(obj)
    elif isinstance(obj, type):
        return obj.__name__  # .split('.')[-1],
    elif isinstance(obj, enum.Enum):
        return str(obj)
    elif isinstance(obj, List):
        return f"[{', '.join([repr_obj(i) for i in obj])}]"
    elif isinstance(obj, (tuple, NamespaceSet)):
        return f"({', '.join([repr_obj(i) for i in obj])})"
    else:
        kwargs = get_kwargs_from(obj)
        kwargs = stringify_kwargs(kwargs)
        kwargs_repr = ", ".join([f"{arg}={kwargs[arg]}" for arg in kwargs])
        typ = repr_obj(type(obj))
        res = f"{typ}({kwargs_repr})"
        return res


def get_kwargs_from(obj, exceptions: Tuple[str] = ("parent",)):
    args: List[str] = inspect.getfullargspec(type(obj).__init__).args
    args.remove("self")

    kwargs = dict()
    for arg in args:
        if arg in exceptions:
            continue
        kwargs[arg] = get_mapped_attr(obj, arg)
    return kwargs


def stringify_kwargs(kwargs: Dict):
    for arg in kwargs:
        kwargs[arg] = repr_obj(kwargs[arg])
    return kwargs
