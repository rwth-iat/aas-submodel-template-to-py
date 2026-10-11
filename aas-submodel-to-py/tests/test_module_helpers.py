"""Regression tests for the helpers, which generated modules define once instead of in every class.

Every class with submodel elements contained the loop collecting them, and every list class a copy
of BaSyx's _check_constraints, which accepts generated item classes. They are defined once per module
as collect_submodel_elements() and GeneratedSubmodelElementList, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/50
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/helper-test"


def cardinality(value):
    return [model.Qualifier("SMT/Cardinality", str, value=value)]


@pytest.fixture(scope="module")
def generated(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="HelperTest",
        submodel_element=[
            # Named like the helpers: must neither replace them nor be replaced
            model.SubmodelElementCollection("GeneratedSubmodelElementList", value=[model.Property("Note", str)]),
            model.Property("collect_submodel_elements", str),
            model.SubmodelElementList("Values", model.Property, value_type_list_element=str,
                                      value=[model.Property(None, str)]),
            model.Property("Keyword__00__", str, qualifier=cardinality("ZeroToMany")),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "helper_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("helper_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, output_file.read_text()


def test_helpers_are_defined_once_per_module(generated):
    source = generated[1]

    assert source.count("class GeneratedSubmodelElementList(aas.SubmodelElementList):") == 1
    assert source.count("def collect_submodel_elements(") == 1
    assert source.count("def _check_constraints(") == 1
    assert "for se_arg in" not in source


def test_list_classes_inherit_the_constraint_check(generated):
    module = generated[0]
    values = module.HelperTest.Values

    assert values.__bases__ == (module.GeneratedSubmodelElementList,)
    assert "_check_constraints" not in vars(values)
    assert isinstance(values(["a"]), model.SubmodelElementList)


def test_list_classes_accept_generated_items(generated):
    values = generated[0].HelperTest.Values

    assert [item.value for item in values(["a", values.Values_item("b")])] == ["a", "b"]


def test_list_classes_check_the_value_type(generated):
    values = generated[0].HelperTest.Values

    with pytest.raises(model.AASConstraintViolation, match="AASd-109"):
        values([model.Property(None, int, 1)])


def test_list_classes_reject_other_types(generated):
    values = generated[0].HelperTest.Values

    with pytest.raises(model.AASConstraintViolation, match="AASd-108"):
        values([model.MultiLanguageProperty(None)])


def test_collect_submodel_elements(generated):
    collect = generated[0].collect_submodel_elements
    single, first, second = model.Property("Single", str), model.Property("Keyword", str), \
        model.Property("Keyword", str)

    assert [e.id_short for e in collect(single, None, [first, second])] == ["Single", "Keyword00", "Keyword01"]


def test_collect_submodel_elements_without_numbering(generated):
    collect = generated[0].collect_submodel_elements
    items = [model.Property(None, str), model.Property("Named", str)]

    assert [e.id_short for e in collect(items, number_repeated=False)] == [None, "Named"]


def test_collect_submodel_elements_rejects_other_types(generated):
    with pytest.raises(TypeError, match="int"):
        generated[0].collect_submodel_elements(42)


def test_helper_names_are_reserved(generated):
    module = generated[0]
    cls = module.HelperTest
    instance = cls(id_=SUBMODEL_ID, generatedSubmodelElementList=cls.GeneratedSubmodelElementList_(note="n"),
                   collect_submodel_elements_="c", values=["v"], keyword=["k1", "k2"])

    assert module.GeneratedSubmodelElementList.__bases__ == (model.SubmodelElementList,)
    assert instance.get_referable("collect_submodel_elements").value == "c"
    assert [e.id_short for e in instance.submodel_element] == [
        "GeneratedSubmodelElementList", "collect_submodel_elements", "Values", "Keyword00", "Keyword01"]
