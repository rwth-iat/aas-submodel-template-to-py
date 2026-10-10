"""Regression tests for the kind of submodels built with generated classes.

Generated classes copied the kind of the template, so their instances were
serialized as templates (kind=Template), see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/37

Instances have kind=Instance. Template qualifiers (e.g. SMT/Cardinality, FormTitle for
editors) are only allowed in templates (AASd-119 for submodels, AASd-129 for submodel
elements), so they aren't taken over, also not in template objects used as defaults
(e.g. Operation variables).
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/kind-test"


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="KindTest",
        kind=model.ModellingKind.TEMPLATE,
        qualifier=[
            model.Qualifier("FormTitle", str, value="Kind test form", kind=model.QualifierKind.TEMPLATE_QUALIFIER),
            model.Qualifier("Usage", str, value="Example", kind=model.QualifierKind.CONCEPT_QUALIFIER),
        ],
        submodel_element=[
            model.Property("Name", str, qualifier=[
                model.Qualifier("SMT/Cardinality", str, value="One", kind=model.QualifierKind.TEMPLATE_QUALIFIER),
                model.Qualifier("Unit", str, value="kg", kind=model.QualifierKind.VALUE_QUALIFIER),
            ]),
            model.Operation("Compute", input_variable=[
                model.Property("Input", float, qualifier=[model.Qualifier(
                    "SMT/Cardinality", str, value="One", kind=model.QualifierKind.TEMPLATE_QUALIFIER)]),
            ]),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "kind_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("kind_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_submodel(module, **kwargs):
    return module.KindTest(id_=SUBMODEL_ID, name="x", compute=module.KindTest.Compute(), **kwargs)


def test_instance_has_kind_instance(generated_module):
    assert build_submodel(generated_module).kind is model.ModellingKind.INSTANCE


def test_template_qualifiers_of_the_submodel_are_not_taken_over(generated_module):
    submodel = build_submodel(generated_module)

    assert [(q.type, q.kind) for q in submodel.qualifier] == [("Usage", model.QualifierKind.CONCEPT_QUALIFIER)]


def test_template_qualifiers_of_elements_are_not_taken_over(generated_module):
    submodel = build_submodel(generated_module)

    assert [(q.type, q.kind) for q in submodel.get_referable("Name").qualifier] == \
        [("Unit", model.QualifierKind.VALUE_QUALIFIER)]


def test_template_qualifiers_of_default_elements_are_not_taken_over(generated_module):
    [input_variable] = build_submodel(generated_module).get_referable("Compute").input_variable

    assert list(input_variable.qualifier) == []


def test_kind_template_can_be_passed(generated_module):
    submodel = build_submodel(generated_module, kind=model.ModellingKind.TEMPLATE)

    assert submodel.kind is model.ModellingKind.TEMPLATE
