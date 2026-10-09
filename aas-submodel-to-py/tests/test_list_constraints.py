"""Regression tests for the constraints checked by generated SubmodelElementList classes.

Generated list classes relax AASd-108 to accept the generated item classes
(subclasses of type_value_list_element). Their check of AASd-109 (value type of
items) never fired, so properties of any value type were accepted, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/34
"""
import importlib.util

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/list-constraints-test"


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="ListConstraintsTest",
        submodel_element=[
            model.SubmodelElementList(
                "Phases", model.Property, value_type_list_element=str, value=[model.Property(None, str)]),
            model.SubmodelElementList(
                "Limits", model.Range, value_type_list_element=datatypes.Double,
                value=[model.Range(None, datatypes.Double)]),
            model.SubmodelElementList(
                "Groups", model.SubmodelElementCollection, value=[model.SubmodelElementCollection(None)]),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "list_constraints_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("list_constraints_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_property_of_other_value_type_violates_aasd_109(generated_module):
    with pytest.raises(model.AASConstraintViolation) as excinfo:
        generated_module.ListConstraintsTest.Phases([model.Property(None, int, 1)])

    assert excinfo.value.constraint_id == 109


def test_property_of_other_value_type_added_later_violates_aasd_109(generated_module):
    phases = generated_module.ListConstraintsTest.Phases(["A1"])

    with pytest.raises(model.AASConstraintViolation) as excinfo:
        phases.value.add(model.Property(None, int, 1))

    assert excinfo.value.constraint_id == 109
    assert [item.value for item in phases.value] == ["A1"]


def test_range_of_other_value_type_violates_aasd_109(generated_module):
    with pytest.raises(model.AASConstraintViolation) as excinfo:
        generated_module.ListConstraintsTest.Limits([model.Range(None, datatypes.Int, 0, 1)])

    assert excinfo.value.constraint_id == 109


def test_items_of_the_value_type_are_accepted(generated_module):
    phases_cls = generated_module.ListConstraintsTest.Phases
    limits_cls = generated_module.ListConstraintsTest.Limits

    phases = phases_cls([phases_cls.Phases_item("A1"), model.Property(None, str, "B2"), "C3"])
    limits = limits_cls([(0.0, 1.0), model.Range(None, datatypes.Double, 2.0, 3.0)])

    assert [item.value for item in phases.value] == ["A1", "B2", "C3"]
    assert [(item.min, item.max) for item in limits.value] == [(0.0, 1.0), (2.0, 3.0)]


def test_subclasses_of_type_value_list_element_are_accepted(generated_module):
    # AASd-108 is relaxed for the generated item classes
    groups_cls = generated_module.ListConstraintsTest.Groups
    item = groups_cls.Groups_item()

    assert list(groups_cls([item]).value) == [item]


def test_element_of_other_type_violates_aasd_108(generated_module):
    with pytest.raises(model.AASConstraintViolation) as excinfo:
        generated_module.ListConstraintsTest.Groups([model.Property(None, str, "x")])

    assert excinfo.value.constraint_id == 108
