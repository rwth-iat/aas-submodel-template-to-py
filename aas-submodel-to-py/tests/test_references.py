"""Tests for rendering references in generated code.

BaSyx sets the referred type of model references ending in a fragment key to
NoneType, which used to be rendered as the undefined name `NoneType`, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/21
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen
from aas_submodel_to_py.util import StringHandler

SUBMODEL_ID = "https://example.com/ids/sm/reference-test"
FRAGMENT_REFERENCE = model.ModelReference(
    (
        model.Key(model.KeyTypes.SUBMODEL, SUBMODEL_ID),
        model.Key(model.KeyTypes.FILE, "AutomationMLData"),
        model.Key(model.KeyTypes.FRAGMENT_REFERENCE, "AML/6eb1965c-9a52-49ac-a19a-a4a32db75317.onOff"),
    ),
    type(None),
)
PROPERTY_REFERENCE = model.ModelReference(
    (
        model.Key(model.KeyTypes.SUBMODEL, SUBMODEL_ID),
        model.Key(model.KeyTypes.PROPERTY, "OnOff"),
    ),
    model.Property,
)


def test_none_type_rendered_as_expression():
    assert StringHandler.reprify(type(None)) == "type(None)"


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="ReferenceTest",
        submodel_element=[
            model.Property(id_short="OnOff", value_type=bool),
            model.RelationshipElement(
                id_short="Relation", first=FRAGMENT_REFERENCE, second=PROPERTY_REFERENCE),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "reference_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("reference_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_references_keep_keys_and_type(generated_module):
    relation = generated_module.ReferenceTest.Relation()

    assert relation.first == FRAGMENT_REFERENCE
    assert relation.first.type is type(None)
    assert relation.second == PROPERTY_REFERENCE
    assert relation.second.type is model.Property
