"""Regression tests for qualifiers that only describe templates.

Generated classes didn't take over qualifiers of kind TemplateQualifier (#37), but many templates
mark template-only qualifiers as ConceptQualifier, ValueQualifier or without kind (e.g. Multiplicity,
FormInfo, ExampleValue), so they were copied into every instance, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/42

Qualifiers of the SMT specification (SMT/...), their older names and hints for template editors
aren't taken over, whatever their kind. Template-specific annotations (e.g. unit) are kept.
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/qualifier-test"
CONCEPT, VALUE = model.QualifierKind.CONCEPT_QUALIFIER, model.QualifierKind.VALUE_QUALIFIER

TEMPLATE_ONLY = [
    ("Multiplicity", "ZeroToOne", CONCEPT),
    ("Cardinality", "ZeroToOne", CONCEPT),
    ("SMT/Cardinality", "ZeroToOne", CONCEPT),
    ("SMT/SMT/Cardinality", "ZeroToOne", CONCEPT),
    ("FormInfo", "Info for the editor", CONCEPT),
    ("FormChoices", "a;b", CONCEPT),
    ("PresetIdShort", "Name", CONCEPT),
    ("AllowedIdShort", "Name[\\d{2}]", CONCEPT),
    ("EditDescription", "True", CONCEPT),
    ("ExampleValue", "Example", CONCEPT),
    ("SMT/ExampleValue", "Example", VALUE),
    ("SMT/ExampleValue/ECLASS", "Example", VALUE),
    ("DefaultValue", "Default", CONCEPT),
    ("SMT/AllowedValue", "a|b", VALUE),
]
ANNOTATIONS = [
    ("unit", "kg", CONCEPT),
    ("Constraint", "Only applicable for number-based values", CONCEPT),
    ("Note", "A note", VALUE),
]


def qualifiers(specs):
    return [model.Qualifier(type_, str, value=value, kind=kind) for type_, value, kind in specs]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="QualifierTest",
        qualifier=qualifiers([("FormTitle", "Form", CONCEPT), ("Naming", "Naming", CONCEPT)]),
        submodel_element=[
            # Several qualifiers of the same family would make the cardinality ambiguous, so it's
            # given once, as ZeroToOne, by the first of them
            model.Property("Name", str, qualifier=qualifiers(TEMPLATE_ONLY + ANNOTATIONS)),
            model.Operation("Compute", input_variable=[
                model.Property("Input", str, qualifier=qualifiers([("Multiplicity", "One", CONCEPT),
                                                                   ("unit", "s", CONCEPT)])),
            ]),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "qualifier_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("qualifier_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def types(element) -> list:
    return [q.type for q in element.qualifier]


def test_template_only_qualifiers_of_elements_are_not_taken_over(generated_module):
    assert types(generated_module.QualifierTest.Name("x")) == ["unit", "Constraint", "Note"]


def test_template_only_qualifiers_of_submodels_are_not_taken_over(generated_module):
    cls = generated_module.QualifierTest

    assert types(cls(id_=SUBMODEL_ID, compute=cls.Compute())) == ["Naming"]


def test_template_only_qualifiers_of_default_elements_are_not_taken_over(generated_module):
    [input_variable] = generated_module.QualifierTest.Compute().input_variable

    assert types(input_variable) == ["unit"]
