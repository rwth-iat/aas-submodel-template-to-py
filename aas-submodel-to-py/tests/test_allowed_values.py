"""Regression tests for the allowed values of generated Property classes.

Templates restrict the values of Properties (SMT/AllowedValue, SMT/AllowedRange, FormChoices,
enumeration), but generated classes accepted any value, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/44

Generated Property classes have the class attributes ALLOWED_VALUES, ALLOWED_PATTERN and
ALLOWED_RANGE, and raise a ValueError for other values. As the templates use these qualifiers
inconsistently, constraints that can't be interpreted are ignored with a warning.
"""
import importlib.util
import warnings

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/allowed-test"
TEMPLATE, CONCEPT = model.QualifierKind.TEMPLATE_QUALIFIER, model.QualifierKind.CONCEPT_QUALIFIER


def prop(id_short, value_type, *qualifiers, default=None):
    specs = [("SMT/Cardinality", "ZeroToOne", TEMPLATE), *qualifiers]
    if default is not None:
        specs.append(("SMT/DefaultValue", default, TEMPLATE))
    return model.Property(id_short, value_type, qualifier=[
        model.Qualifier(type_, str, value=value, kind=kind) for type_, value, kind in specs])


ELEMENTS = [
    prop("SafetyMeasure", str, ("SMT/AllowedValue", "True;False", TEMPLATE), ("FormChoices", "True;False", CONCEPT),
         default="False"),
    prop("CountryCode", str, ("SMT/AllowedValue", "[A-Z]{2}", TEMPLATE)),
    prop("Quality", str, ("SMT/AllowedValue", "good | bad | uncertain", TEMPLATE)),
    prop("Recipient", str, ("SMT/AllowedValue1", "Purchaser", TEMPLATE), ("SMT/AllowedValue2", "Consignee", TEMPLATE)),
    prop("Enabled", datatypes.Boolean, ("FormChoices", "True; False", CONCEPT)),
    prop("ControlType", str, ("FormChoices", "Path controlled; Point controlled, Track controlled", CONCEPT)),
    prop("SILLevel", str, ("enumeration", "SIL 0, SIL 1, SIL 2", CONCEPT)),
    prop("Diagnosis", str, ("enumeration", "TBD according to APOS H1", CONCEPT)),
    prop("Percentage", datatypes.Int, ("SMT/AllowedRange", "[0,100]", TEMPLATE)),
    prop("Identifier", datatypes.Long, ("SMT/AllowedRange", "[0x00000000 , 0x1f]", TEMPLATE)),
    prop("Duration", datatypes.Float, ("SMT/AllowedRange", "ZeroToInf", TEMPLATE)),
    prop("VoltageLevel", str, ("SMT/AllowedRange", "ZeroToInf", TEMPLATE)),
]


@pytest.fixture(scope="module")
def generation(tmp_path_factory):
    submodel = model.Submodel(id_=SUBMODEL_ID, id_short="AllowedTest", submodel_element=ELEMENTS)
    output_file = tmp_path_factory.mktemp("generated") / "allowed_test.py"
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("allowed_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, [str(warning.message) for warning in caught]


@pytest.fixture(scope="module")
def cls(generation):
    return generation[0].AllowedTest


@pytest.mark.parametrize("element, allowed, not_allowed", [
    ("SafetyMeasure", "True", "maybe"),
    ("CountryCode", "DE", "Deutschland"),
    ("Quality", "uncertain", "ugly"),
    ("Recipient", "Consignee", "Seller"),
    ("ControlType", "Track controlled", "Free controlled"),
    ("SILLevel", "SIL 1", "SIL 5"),
    ("Percentage", 100, 101),
    ("Identifier", 0x1f, 0x20),
    ("Duration", 1.5, -1.0),
])
def test_allowed_values(cls, element, allowed, not_allowed):
    element_cls = getattr(cls, element)

    assert element_cls(allowed).value == allowed
    with pytest.raises(ValueError, match=f"not an allowed value of {element}"):
        element_cls(not_allowed)


def test_allowed_values_are_class_attributes(cls):
    assert cls.SafetyMeasure.ALLOWED_VALUES == ("True", "False")
    assert cls.CountryCode.ALLOWED_PATTERN == "[A-Z]{2}"
    assert cls.Percentage.ALLOWED_RANGE == (0, 100)
    assert cls.Duration.ALLOWED_RANGE == (0, None)


def test_boolean_choices_are_converted(cls):
    assert cls.Enabled.ALLOWED_VALUES == (True, False)
    assert cls.Enabled(False).value is False


def test_default_value_is_allowed(cls):
    assert cls.SafetyMeasure().value == "False"


def test_raw_values_in_enclosing_class_are_checked(cls):
    with pytest.raises(ValueError, match="not an allowed value of SafetyMeasure"):
        cls(id_=SUBMODEL_ID, safetyMeasure="maybe")


def test_constraints_that_cant_be_interpreted_are_ignored(generation, cls):
    # A single value of an enumeration is a note, ranges only apply to numbers
    assert cls.Diagnosis("anything").value == "anything"
    assert cls.VoltageLevel("anything").value == "anything"
    messages = generation[1]
    assert any("Diagnosis" in message and "TBD according to APOS H1" in message for message in messages)
    assert any("VoltageLevel" in message and "ZeroToInf" in message for message in messages)
