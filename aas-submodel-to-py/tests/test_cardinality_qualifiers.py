"""Regression tests for cardinality qualifiers spelled in non-standard ways.

Published templates spell cardinality qualifiers in several ways (e.g. the
value "ZerotoOne" or "ZeroToOne " and the type "SMT/SMT/Cardinality"). These
were ignored, so optional or multiple elements became required single
arguments, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/35
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py.util import ReferableHandler
from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/cardinality-test"


def qualified_property(id_short, type_, value):
    return model.Property(id_short, str, qualifier=[model.Qualifier(type_, str, value=value)])


@pytest.mark.parametrize("type_, value, optional, iterable", [
    ("SMT/Cardinality", "One", False, False),
    ("SMT/Cardinality", "ZeroToOne", True, False),
    ("SMT/Cardinality", "ZeroToMany", True, True),
    ("SMT/Cardinality", "OneToMany", False, True),
    ("Cardinality", "ZeroToOne", True, False),
    ("Multiplicity", "ZeroToMany", True, True),
    ("SMT/Multiplicity", "OneToMany", False, True),
    # Non-standard spellings in published templates
    ("Cardinality", "ZerotoOne", True, False),
    ("Cardinality", "ZerotoMany", True, True),
    ("SMT/Cardinality", "ZeroToOne ", True, False),
    ("SMT/Cardinality", "TwoToMany", False, True),
    ("SMT/SMT/Cardinality", "ZeroToMany", True, True),
    ("SMT/SMT/Cardinality", "One", False, False),
])
def test_cardinality(type_, value, optional, iterable):
    prop = qualified_property("Prop", type_, value)

    assert bool(ReferableHandler.is_optional(prop)) is optional
    assert bool(ReferableHandler.is_iterable(prop)) is iterable


def test_no_cardinality():
    prop = model.Property("Prop", str, qualifier=[model.Qualifier("SMT/RequiredLang", str, value="en")])

    assert ReferableHandler.is_optional(prop) is None
    assert ReferableHandler.is_iterable(prop) is None


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="CardinalityTest",
        submodel_element=[
            qualified_property("Mandatory", "SMT/Cardinality", "One"),
            qualified_property("OptionalA", "Cardinality", "ZerotoOne"),
            qualified_property("OptionalB", "SMT/Cardinality", "ZeroToOne "),
            qualified_property("Several", "Cardinality", "ZerotoMany"),
            qualified_property("AtLeastTwo", "SMT/Cardinality", "TwoToMany"),
            qualified_property("Interface", "SMT/SMT/Cardinality", "ZeroToMany"),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "cardinality_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("cardinality_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_generated_arguments_follow_non_standard_cardinalities(generated_module):
    # OptionalA, OptionalB, Several and Interface can be omitted
    submodel = generated_module.CardinalityTest(
        id_=SUBMODEL_ID, mandatory="m", atLeastTwo=["a", "b"], several=["x", "y"], interface=["i"])

    values = {se.id_short: se.value for se in submodel.submodel_element}
    assert values == {"Mandatory": "m", "AtLeastTwo0": "a", "AtLeastTwo1": "b",
                      "Several0": "x", "Several1": "y", "Interface0": "i"}


def test_element_with_cardinality_two_to_many_is_required(generated_module):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'atLeastTwo'"):
        generated_module.CardinalityTest(id_=SUBMODEL_ID, mandatory="m")
