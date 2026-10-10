"""Regression tests for the idShorts of elements that may occur several times.

Their index was appended with a single digit (Keyword0, Keyword1, ...), but templates expect
two or more digits: the placeholders {00} and __00__, and AllowedIdShort qualifiers like
Policy[\\d]{2,3}, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/46
"""
import importlib.util
import re

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/repeated-test"


def several():
    return [model.Qualifier("SMT/Cardinality", str, value="ZeroToMany", kind=model.QualifierKind.TEMPLATE_QUALIFIER)]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="RepeatedTest",
        submodel_element=[
            model.Property("Keyword__00__", str, qualifier=several()),
            model.SubmodelElementCollection(
                "Policies", value=[model.Property("Policy", str, qualifier=several() + [
                    model.Qualifier("AllowedIdShort", str, value=r"Policy[\d]{2,3}")])]),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "repeated_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("repeated_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def id_shorts(element) -> list:
    children = element.submodel_element if isinstance(element, model.Submodel) else element.value
    return [child.id_short for child in children]


def test_repeated_elements_are_numbered_with_two_digits(generated_module):
    submodel = generated_module.RepeatedTest(id_=SUBMODEL_ID, keyword=["a", "b", "c"],
                                             policies=generated_module.RepeatedTest.Policies())

    assert id_shorts(submodel)[:3] == ["Keyword00", "Keyword01", "Keyword02"]


def test_index_matches_allowed_id_short(generated_module):
    policies = generated_module.RepeatedTest.Policies(policy=["keep 10 years"] * 12)

    assert id_shorts(policies)[-1] == "Policy11"
    assert all(re.fullmatch(r"Policy[\d]{2,3}", id_short) for id_short in id_shorts(policies))
