"""Regression tests for idShorts ending in digits.

Trailing digits were removed from the idShort of every element without colliding siblings,
so instances of elements occurring once got idShorts not in the template (e.g.
bacv_isISO8601 -> bacv_isISO, Tank_1 -> Tank), see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/41

Only elements that may occur several times lose their iteration ending, as their instances
get an index instead. Other elements only lose the placeholders {00} and __00__.
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/digits-test"


def cardinality(value):
    return [model.Qualifier("SMT/Cardinality", str, value=value, kind=model.QualifierKind.TEMPLATE_QUALIFIER)]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="DigitsTest",
        submodel_element=[
            model.Property("bacv_isISO8601", bool, qualifier=cardinality("ZeroToOne")),
            model.Property("Tank_1", str, qualifier=cardinality("One")),
            model.Property("Mode__00__", str, qualifier=cardinality("One")),
            model.Property("Keyword__00__", str, qualifier=cardinality("ZeroToMany")),
            model.Property("ApplicationUri01", str, qualifier=cardinality("ZeroToMany")),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "digits_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("digits_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_elements_occurring_once_keep_their_digits(generated_module):
    cls = generated_module.DigitsTest

    assert (cls.Bacv_isISO8601(True).id_short, cls.Tank_1("T").id_short) == ("bacv_isISO8601", "Tank_1")


def test_placeholders_are_removed(generated_module):
    assert generated_module.DigitsTest.Mode("Auto").id_short == "Mode"


def test_elements_occurring_several_times_get_an_index(generated_module):
    cls = generated_module.DigitsTest

    submodel = cls(id_=SUBMODEL_ID, tank_1="T", mode="Auto", bacv_isISO8601=True,
                   keyword=["a", "b"], applicationUri=["https://example.com/app"])

    assert sorted(se.id_short for se in submodel.submodel_element) == \
        ["ApplicationUri0", "Keyword0", "Keyword1", "Mode", "Tank_1", "bacv_isISO8601"]
