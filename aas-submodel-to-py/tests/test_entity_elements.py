"""Regression tests for generated Entity classes.

The statements of Entities (their submodel elements) used to be generated as a default
value holding the template's statements, so they couldn't be passed, and every instance
got the template's statements, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/39

Entities are generated like collections: one nested class and one argument per statement.
"""
import importlib.util

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/entity-test"


def cardinality(value):
    return [model.Qualifier("SMT/Cardinality", str, value=value, kind=model.QualifierKind.TEMPLATE_QUALIFIER)]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="EntityTest",
        submodel_element=[
            model.Entity(
                "Machine", model.EntityType.SELF_MANAGED_ENTITY, global_asset_id="https://example.com/ids/asset",
                qualifier=cardinality("One"),
                statement=[
                    model.Property("SerialNumber", str, qualifier=cardinality("One")),
                    model.Property("Weight", datatypes.Double, qualifier=cardinality("ZeroToOne")),
                    model.Entity("Part", model.EntityType.CO_MANAGED_ENTITY, qualifier=cardinality("ZeroToMany"),
                                 statement=[model.Property("PartNumber", str, qualifier=cardinality("One"))]),
                ]),
            model.Entity(
                "Buyer", model.EntityType.CO_MANAGED_ENTITY, qualifier=cardinality("ZeroToOne"),
                statement=[model.Property("BuyerReferenceID", str, qualifier=cardinality("One"))]),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "entity_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("entity_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def statements(entity) -> dict:
    return {statement.id_short: statement for statement in entity.statement}


def test_statements_are_built_from_raw_values(generated_module):
    machine_cls = generated_module.EntityTest.Machine

    machine = machine_cls(serialNumber="SN-1", weight=1.5)

    assert {id_short: s.value for id_short, s in statements(machine).items()} == {"SerialNumber": "SN-1", "Weight": 1.5}
    assert isinstance(statements(machine)["SerialNumber"], machine_cls.SerialNumber)


def test_template_statements_are_not_taken_over(generated_module):
    machine = generated_module.EntityTest.Machine(serialNumber="SN-1")

    assert list(statements(machine)) == ["SerialNumber"]


def test_required_statements_must_be_passed(generated_module):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'serialNumber'"):
        generated_module.EntityTest.Machine()


def test_nested_entities_take_several_statements(generated_module):
    machine_cls = generated_module.EntityTest.Machine

    machine = machine_cls(serialNumber="SN-1", part=[machine_cls.Part(partNumber="P-1"), machine_cls.Part(partNumber="P-2")])

    parts = [s for s in machine.statement if isinstance(s, machine_cls.Part)]
    assert [statements(part)["PartNumber"].value for part in parts] == ["P-1", "P-2"]
    assert all(part.entity_type is model.EntityType.CO_MANAGED_ENTITY for part in parts)


def test_entity_attributes_can_be_passed(generated_module):
    machine = generated_module.EntityTest.Machine(serialNumber="SN-1", global_asset_id="https://example.com/ids/asset-2")

    assert (machine.entity_type, machine.global_asset_id) == \
        (model.EntityType.SELF_MANAGED_ENTITY, "https://example.com/ids/asset-2")


def test_entities_in_submodel(generated_module):
    cls = generated_module.EntityTest

    submodel = cls(id_=SUBMODEL_ID, machine=cls.Machine(serialNumber="SN-1"), buyer=cls.Buyer(buyerReferenceID="B-1"))

    assert statements(submodel.get_referable("Buyer"))["BuyerReferenceID"].value == "B-1"
    assert submodel.get_referable("Machine").global_asset_id == "https://example.com/ids/asset"
