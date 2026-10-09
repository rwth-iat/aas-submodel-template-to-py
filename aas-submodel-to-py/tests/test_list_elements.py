"""Regression tests for generated SubmodelElementList classes.

List classes used to take a single item, couldn't be built from several raw
values, and gave all items the same invented default idShort, so that a second
item violated AASd-022, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/23

Since metamodel V3.1 (AASd-120 removed), idShorts of list items are optional;
generated list items default to None.
"""
import importlib.util
import json
import pathlib

import pytest
from basyx.aas import model
from basyx.aas.adapter.json import AASToJsonEncoder
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/list-test"


def cardinality(value):
    return [model.Qualifier("SMT/Cardinality", str, value=value)]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="ListTest",
        submodel_element=[
            # The usual case: cardinality on the list, none on its item
            model.SubmodelElementList(
                "Phases", model.Property, value_type_list_element=str,
                value=[model.Property(None, str)], qualifier=cardinality("ZeroToOne")),
            model.SubmodelElementList(
                "Tags", model.Property, value_type_list_element=str,
                value=[model.Property(None, str, qualifier=cardinality("ZeroToMany"))],
                qualifier=cardinality("ZeroToOne")),
            # The template gives the item an idShort (allowed since metamodel V3.1)
            model.SubmodelElementList(
                "Schemes", model.SubmodelElementCollection,
                value=[model.SubmodelElementCollection(
                    "definesSecurityScheme",
                    value=[model.Property("Name", str, qualifier=cardinality("One"))],
                    qualifier=cardinality("OneToMany"))],
                qualifier=cardinality("ZeroToOne")),
            model.SubmodelElementList(
                "Limits", model.Range, value_type_list_element=datatypes.Double,
                value=[model.Range(None, datatypes.Double)], qualifier=cardinality("ZeroToOne")),
            # Lists without an item in the template
            model.SubmodelElementList(
                "Values", model.Property, value_type_list_element=datatypes.Double,
                qualifier=cardinality("ZeroToOne")),
            model.SubmodelElementList(
                "Groups", model.SubmodelElementCollection, qualifier=cardinality("ZeroToOne")),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "list_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("list_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_submodel(module, **kwargs):
    return module.ListTest(id_=SUBMODEL_ID, **kwargs)


def item_values(se_list):
    return [item.value for item in se_list.value]


def serialized_items(se_list):
    return json.loads(json.dumps(se_list, cls=AASToJsonEncoder))["value"]


def test_list_item_default_id_short_is_none(generated_module):
    cls = generated_module.ListTest

    assert cls.Phases.Phases_item("A1").id_short is None
    assert cls.Schemes.Schemes_item(name="a").id_short is None


def test_list_items_typehint_is_iterable(generated_module):
    # Compare the source, as evaluating all annotations fails on Python 3.14 (issue #24)
    source = "".join(pathlib.Path(generated_module.__file__).read_text().split())

    assert "phases_items:Iterable[Union[str,Phases_item]]," in source
    assert "phases:Optional[Union[Iterable[Union[str,Phases.Phases_item]],Phases]]=None," in source


def test_list_built_from_several_items(generated_module):
    phases = generated_module.ListTest.Phases

    se_list = phases([phases.Phases_item("A1"), phases.Phases_item("B2")])

    assert item_values(se_list) == ["A1", "B2"]
    assert all(isinstance(item, phases.Phases_item) for item in se_list.value)
    assert all("idShort" not in item for item in serialized_items(se_list))


def test_list_built_from_several_raw_values(generated_module):
    phases = generated_module.ListTest.Phases

    se_list = phases(["A1", "B2"])

    assert item_values(se_list) == ["A1", "B2"]
    assert all(isinstance(item, phases.Phases_item) for item in se_list.value)


def test_list_built_from_items_and_raw_values(generated_module):
    phases = generated_module.ListTest.Phases
    item = phases.Phases_item("A1")

    se_list = phases([item, "B2"])

    assert se_list.value[0] is item
    assert item_values(se_list) == ["A1", "B2"]


def test_explicit_id_shorts_of_items_are_kept(generated_module):
    phases = generated_module.ListTest.Phases

    se_list = phases([phases.Phases_item("A1", id_short="first"), phases.Phases_item("B2", id_short="second")])

    assert [item.id_short for item in se_list.value] == ["first", "second"]


def test_enclosing_class_builds_list_from_raw_values(generated_module):
    submodel = build_submodel(generated_module, phases=["A1", "B2"], tags=["x", "y", "z"])

    phases = submodel.get_referable("Phases")
    assert isinstance(phases, generated_module.ListTest.Phases)
    assert item_values(phases) == ["A1", "B2"]
    assert item_values(submodel.get_referable("Tags")) == ["x", "y", "z"]


def test_optional_list_items_can_be_omitted(generated_module):
    assert item_values(generated_module.ListTest.Tags()) == []


def test_list_of_collections_with_template_id_short(generated_module):
    schemes = generated_module.ListTest.Schemes

    submodel = build_submodel(generated_module, schemes=[schemes.Schemes_item(name="a"), schemes.Schemes_item(name="b")])

    se_list = submodel.get_referable("Schemes")
    assert [item.get_referable("Name").value for item in se_list.value] == ["a", "b"]
    assert all("idShort" not in item for item in serialized_items(se_list))


def test_list_of_ranges_built_from_raw_pairs(generated_module):
    submodel = build_submodel(generated_module, limits=[(0.0, 1.0), (2.0, 3.0)])

    assert [(item.min, item.max) for item in submodel.get_referable("Limits").value] == [(0.0, 1.0), (2.0, 3.0)]


def test_list_without_template_item_built_from_raw_values(generated_module):
    submodel = build_submodel(generated_module, values=[0.5, 1.5])

    se_list = submodel.get_referable("Values")
    assert item_values(se_list) == [0.5, 1.5]
    assert all(type(item) is model.Property and item.value_type is datatypes.Double for item in se_list.value)


def test_list_without_template_item_built_from_items(generated_module):
    groups = [model.SubmodelElementCollection(None), model.SubmodelElementCollection(None)]

    submodel = build_submodel(generated_module, groups=groups)

    assert list(submodel.get_referable("Groups").value) == groups
