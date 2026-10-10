"""Regression tests for default values of generated Property classes.

The qualifiers SMT/DefaultValue and SMT/InitialValue define the default or initial value of a
Property in the template. They were ignored, so the value was always a required argument, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/43

The value of a Property class defaults to its SMT/DefaultValue (or the older DefaultValue), else
to its SMT/InitialValue, converted to its value type. The argument of the element in the enclosing
class keeps its cardinality.
"""
import importlib.util

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/default-test"
TEMPLATE = model.QualifierKind.TEMPLATE_QUALIFIER


def qualifiers(*specs):
    return [model.Qualifier(type_, str, value=value, kind=kind) for type_, value, kind in specs]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="DefaultTest",
        submodel_element=[
            model.Property("Severity", str, qualifier=qualifiers(
                ("SMT/Cardinality", "One", TEMPLATE), ("SMT/DefaultValue", "low", TEMPLATE),
                ("SMT/InitialValue", "medium", TEMPLATE))),
            model.Property("Count", datatypes.Int, qualifier=qualifiers(
                ("SMT/Cardinality", "ZeroToOne", TEMPLATE), ("SMT/DefaultValue", "42", TEMPLATE))),
            model.Property("Enabled", datatypes.Boolean, qualifier=qualifiers(
                ("SMT/Cardinality", "ZeroToOne", TEMPLATE), ("SMT/InitialValue", "true", TEMPLATE))),
            model.Property("Priority", str, qualifier=qualifiers(
                ("Cardinality", "ZeroToOne", model.QualifierKind.CONCEPT_QUALIFIER),
                ("DefaultValue", "Medium", model.QualifierKind.CONCEPT_QUALIFIER))),
            model.Property("Name", str, qualifier=qualifiers(("SMT/Cardinality", "ZeroToOne", TEMPLATE))),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "default_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("default_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_default_value(generated_module):
    severity_cls = generated_module.DefaultTest.Severity

    # SMT/DefaultValue is preferred over SMT/InitialValue
    assert severity_cls().value == "low"
    assert severity_cls("high").value == "high"


def test_default_value_has_value_type(generated_module):
    count = generated_module.DefaultTest.Count()

    assert count.value == 42 and isinstance(count.value, int)


def test_initial_value_without_default_value(generated_module):
    assert generated_module.DefaultTest.Enabled().value is True


def test_older_qualifier_default_value(generated_module):
    assert generated_module.DefaultTest.Priority().value == "Medium"


def test_property_without_default_value_requires_value(generated_module):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'value'"):
        generated_module.DefaultTest.Name()


def test_mandatory_element_with_default_value_stays_required(generated_module):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'severity'"):
        generated_module.DefaultTest(id_=SUBMODEL_ID)

    submodel = generated_module.DefaultTest(id_=SUBMODEL_ID, severity=generated_module.DefaultTest.Severity())
    assert submodel.get_referable("Severity").value == "low"
