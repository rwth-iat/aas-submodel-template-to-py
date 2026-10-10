"""Regression tests for lists with the cardinality ZeroToMany/OneToMany.

A list is always generated as a single list keeping its idShort: the
cardinality of the list itself only decides if it is optional, as the number
of items is given by the list. Such lists used to be generated as several
lists with indexed idShorts, so that ["EN 15804", "ISO 14067"] was split into
two lists of characters, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/36

Strings passed to arguments taking several items raise a TypeError instead of
being split into characters.
"""
import importlib.util
import typing
from typing import Iterable, Optional, Union

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/list-cardinality-test"


def cardinality(value):
    return [model.Qualifier("SMT/Cardinality", str, value=value)]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="ListCardinalityTest",
        submodel_element=[
            # Cardinality on the list instead of its item (e.g. Carbon Footprint PcfCalculationMethods)
            model.SubmodelElementList(
                "Methods", model.Property, value_type_list_element=str,
                value=[model.Property(None, str, qualifier=cardinality("One"))],
                qualifier=cardinality("OneToMany")),
            model.SubmodelElementList(
                "Images", model.Property, value_type_list_element=str,
                value=[model.Property(None, str)], qualifier=cardinality("ZeroToMany")),
            # Placeholder without an item (e.g. Technical Data ArbitrarySML)
            model.SubmodelElementList(
                "ArbitrarySML", model.SubmodelElement, qualifier=cardinality("ZeroToMany")),
            model.Property("Keyword", str, qualifier=cardinality("ZeroToMany")),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "list_cardinality_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("list_cardinality_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_submodel(module, **kwargs):
    return module.ListCardinalityTest(id_=SUBMODEL_ID, **{"methods": ["EN 15804"], **kwargs})


def lists_by_id_short(submodel):
    return {se.id_short: se for se in submodel.submodel_element if isinstance(se, model.SubmodelElementList)}


def test_list_with_cardinality_one_to_many_is_one_list(generated_module):
    submodel = build_submodel(generated_module, methods=["EN 15804", "ISO 14067"])

    lists = lists_by_id_short(submodel)
    assert list(lists) == ["Methods"]
    assert [item.value for item in lists["Methods"].value] == ["EN 15804", "ISO 14067"]


def test_list_with_cardinality_one_to_many_is_required(generated_module):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'methods'"):
        generated_module.ListCardinalityTest(id_=SUBMODEL_ID)


def test_list_with_cardinality_zero_to_many_is_one_optional_list(generated_module):
    assert "Images" not in lists_by_id_short(build_submodel(generated_module))

    submodel = build_submodel(generated_module, images=["a.png", "b.png"])

    images = lists_by_id_short(submodel)["Images"]
    assert [item.value for item in images.value] == ["a.png", "b.png"]


def test_list_without_item_with_cardinality_zero_to_many_is_one_list(generated_module):
    items = [model.Property(None, str, value="x"), model.MultiLanguageProperty(None)]

    submodel = build_submodel(generated_module, arbitrarySML=items)

    assert list(lists_by_id_short(submodel)["ArbitrarySML"].value) == items


def test_typehints_of_lists_with_cardinality_to_many(generated_module):
    cls = generated_module.ListCardinalityTest
    typehints = typing.get_type_hints(cls.__init__)

    assert typehints["methods"] == Union[Iterable[Union[str, cls.Methods.Methods_item]], cls.Methods]
    assert typehints["images"] == Optional[Union[Iterable[Union[str, cls.Images.Images_item]], cls.Images]]


@pytest.mark.parametrize("arg, value", [
    ("methods", "EN 15804"),
    ("images", "a.png"),
    ("keyword", "foo"),
])
def test_str_passed_for_several_items_raises_type_error(generated_module, arg, value):
    # The error names the argument the str was passed to
    with pytest.raises(TypeError, match=f"^{arg} takes several elements, got a str$"):
        build_submodel(generated_module, **{arg: value})


def test_str_passed_to_list_class_raises_type_error(generated_module):
    with pytest.raises(TypeError, match="got a str"):
        generated_module.ListCardinalityTest.Methods("EN 15804")


def test_several_elements_of_cardinality_zero_to_many_get_indexed_id_shorts(generated_module):
    # Unchanged for elements other than lists
    submodel = build_submodel(generated_module, keyword=["foo", "bar"])

    assert submodel.get_referable("Keyword0").value == "foo"
    assert submodel.get_referable("Keyword1").value == "bar"
