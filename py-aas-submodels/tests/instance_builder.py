"""Build instances of generated classes with sample values, as used by the tests"""
import collections.abc
import inspect
import typing

from basyx.aas import model
from basyx.aas.model import datatypes

SAMPLE_LEXICALS = ("1", "true", "2024", "2024-01-01", "2024-01-01T00:00:00Z", "P1D", "12:00:00Z", "x")


def sample_value(value_type: type):
    """A value of an XSD type, parsed from the first sample lexical representation it accepts"""
    for lexical in SAMPLE_LEXICALS:
        try:
            return datatypes.from_xsd(lexical, value_type)
        except ValueError:
            pass
    raise ValueError(f"No sample value for {value_type}")


def build_instance(cls: type, full: bool = False):
    """Instance of a generated class with sample values for all its required arguments, and if `full`,
    also for all optional arguments taking submodel elements (with one element if they take several).
    Raw values are preferred over instances of generated classes, so that both are built"""
    typehints = typing.get_type_hints(cls.__init__)
    kwargs = {}
    for name, parameter in inspect.signature(cls.__init__).parameters.items():
        if name == "self":
            continue
        if parameter.default is inspect.Parameter.empty or (full and takes_generated_class(cls, typehints[name])):
            kwargs[name] = sample_argument(cls, name, typehints[name], full)
    if issubclass(cls, model.Entity) and \
            inspect.signature(cls.__init__).parameters["entity_type"].default is model.EntityType.SELF_MANAGED_ENTITY:
        kwargs["global_asset_id"] = "https://example.com/ids/asset"  # AASd-014
    return cls(**kwargs)


def takes_generated_class(cls: type, typehint) -> bool:
    """Return if `typehint` refers to a class generated in the module of `cls`"""
    if isinstance(typehint, type):
        return typehint.__module__ == cls.__module__
    return any(takes_generated_class(cls, arg) for arg in typing.get_args(typehint))


def sample_argument(cls: type, name: str, typehint, full: bool = False):
    origin, args = typing.get_origin(typehint), typing.get_args(typehint)
    if name == "id_":
        return f"https://example.com/ids/sm/{cls.__name__}"
    elif origin is typing.Union:
        # Raw values come first; lists of items without class (e.g. Iterable[aas.SubmodelElement]) can't be sampled
        for arg in args[:-1]:
            try:
                return sample_argument(cls, name, arg, full)
            except ValueError:
                pass
        return sample_argument(cls, name, args[-1], full)
    elif origin is collections.abc.Iterable:
        return [sample_argument(cls, name, args[0], full)]
    elif origin is tuple:
        return tuple(sample_argument(cls, name, arg, full) for arg in args)
    elif isinstance(typehint, type) and typehint.__module__ == cls.__module__:
        return build_instance(typehint, full)
    elif typehint is model.LangStringSet:
        return model.MultiLanguageTextType({"en": "x"})
    elif typehint is model.Reference:
        return model.ExternalReference((model.Key(model.KeyTypes.GLOBAL_REFERENCE, "https://example.com/ids/x"),))
    elif name == "content_type":
        return "application/pdf"
    elif isinstance(typehint, type):
        return sample_value(typehint)
    raise TypeError(f"No sample argument {cls.__qualname__}.{name}: {typehint}")
