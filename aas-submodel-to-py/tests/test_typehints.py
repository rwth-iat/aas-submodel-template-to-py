"""Regression tests for typehints rendered into generated modules.

Since Python 3.14, Optional[X] and Union[X, Y] are no longer typing._GenericAlias
instances and are represented as "X | None". They were rendered as "Union()",
so modules generated on Python 3.14 failed on import with Python <= 3.13, and
their annotations couldn't be evaluated, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/24

Typehints must be rendered the same way on every Python version.
"""
import importlib.util
import inspect
import typing
from typing import ForwardRef, Iterable, Optional, Set, Union

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen
from aas_submodel_to_py.util import StringHandler

SUBMODEL_ID = "https://example.com/ids/sm/typehint-test"
# Forward reference as used by BaSyx (e.g. in ModelReference typehints)
AAS_FORWARD_REF = ForwardRef("aas.AssetAdministrationShell")


@pytest.mark.parametrize("typehint, expected", [
    (Optional[str], "Optional[str]"),
    (Union[str, int], "Union[str, int]"),
    (Optional[model.Reference], "Optional[aas.Reference]"),
    (Optional[datatypes.DateTime], "Optional[xsd.DateTime]"),
    (Iterable[model.Qualifier], "Iterable[aas.Qualifier]"),
    (Optional[Set[model.Reference]], "Optional[Set[aas.Reference]]"),
    (model.ModelReference[Union[model.Submodel, model.Entity]], "aas.ModelReference[Union[aas.Submodel, aas.Entity]]"),
    (Optional[model.ModelReference[AAS_FORWARD_REF]],
     "Optional[aas.ModelReference[ForwardRef('aas.AssetAdministrationShell')]]"),
])
def test_reprify_typehint(typehint, expected):
    assert StringHandler.reprify(typehint) == expected


def basyx_init_annotations():
    for name in sorted(dir(model)):
        cls = getattr(model, name)
        if isinstance(cls, type) and issubclass(cls, model.Referable):
            for arg, typehint in inspect.getfullargspec(cls.__init__).annotations.items():
                if arg != "return":
                    yield f"{name}.{arg}", typehint


@pytest.mark.parametrize("arg, typehint", list(basyx_init_annotations()))
def test_basyx_annotations_are_rendered_as_evaluable_code(arg, typehint):
    rendered = StringHandler.reprify(typehint)
    if "~" in rendered:
        pytest.skip(f"TypeVar in {rendered}, not used in generated arguments")

    namespace = {"aas": model, "xsd": datatypes, **{name: getattr(typing, name) for name in typing.__all__}}
    eval(rendered, namespace)
    assert "|" not in rendered and "Union()" not in rendered


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="TypehintTest",
        submodel_element=[
            model.Property("Name", str),
            model.MultiLanguageProperty("Title"),
            model.Range("Limits", datatypes.Double),
            model.File("Manual", content_type="application/pdf"),
            model.ReferenceElement("Link"),
            model.SubmodelElementCollection("Address", value=[model.Property("City", str)]),
            model.SubmodelElementList("Phases", model.Property, value_type_list_element=str,
                                      value=[model.Property(None, str)]),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "typehint_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("typehint_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generated_classes(cls):
    yield cls
    for obj in vars(cls).values():
        if isinstance(obj, type) and obj.__module__ == cls.__module__:
            yield from generated_classes(obj)


def test_annotations_of_generated_classes_can_be_evaluated(generated_module):
    for cls in generated_classes(generated_module.TypehintTest):
        typing.get_type_hints(cls.__init__)
