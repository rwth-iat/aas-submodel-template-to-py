"""Regression tests for the compact rendering of references to global identifiers.

Semantic IDs and other external references with a single GlobalReference key were rendered as full
constructor calls, which Black spreads over several lines. They are rendered as calls of the helper
global_ref(), which each generated module defines, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/48
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/global-ref-test"


def global_reference(*values, referred_semantic_id=None):
    return model.ExternalReference(tuple(model.Key(model.KeyTypes.GLOBAL_REFERENCE, v) for v in values),
                                   referred_semantic_id=referred_semantic_id)


NAME_ID = global_reference("https://example.com/ids/cd/Name")
UNIT_ID = global_reference("https://example.com/ids/cd/Unit")
SUPPLEMENTAL_ID = global_reference("0173-1#02-AAO677#004")
TWO_KEYS = global_reference("https://example.com/ids/a", "https://example.com/ids/b")
REFERRED = global_reference("https://example.com/ids/c", referred_semantic_id=NAME_ID)
MODEL_REFERENCE = model.ModelReference((model.Key(model.KeyTypes.CONCEPT_DESCRIPTION, "https://example.com/ids/cd/1"),),
                                       model.ConceptDescription)


@pytest.fixture(scope="module")
def generated(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="GlobalRefTest",
        semantic_id=global_reference("https://example.com/ids/sm/GlobalRefTest"),
        submodel_element=[
            model.Property("Name", str, semantic_id=NAME_ID, supplemental_semantic_id=[SUPPLEMENTAL_ID],
                           qualifier=[model.Qualifier("unit", str, value="kg", semantic_id=UNIT_ID)]),
            model.Property("TwoKeys", str, semantic_id=TWO_KEYS),
            model.Property("Referred", str, semantic_id=REFERRED),
            model.Property("Concept", str, semantic_id=MODEL_REFERENCE),
            model.Property("global_ref", str),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "global_ref_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("global_ref_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, output_file.read_text()


def test_global_references_are_rendered_compactly(generated):
    source = generated[1]

    assert 'semantic_id: Optional[aas.Reference] = global_ref(r"https://example.com/ids/cd/Name"),' in source
    assert 'global_ref(r"0173-1#02-AAO677#004")' in source
    assert 'global_ref(r"https://example.com/ids/cd/Unit")' in source
    assert source.count("def global_ref(") == 1


def test_global_references_are_equal_to_the_template(generated):
    cls = generated[0].GlobalRefTest
    name = cls.Name("x")

    assert (name.semantic_id, list(name.supplemental_semantic_id)) == (NAME_ID, [SUPPLEMENTAL_ID])
    assert type(name.semantic_id) is model.ExternalReference
    assert name.get_qualifier_by_type("unit").semantic_id == UNIT_ID


@pytest.mark.parametrize("element, reference", [
    ("TwoKeys", TWO_KEYS),
    ("Referred", REFERRED),
    ("Concept", MODEL_REFERENCE),
])
def test_other_references_are_rendered_in_full(generated, element, reference):
    assert getattr(generated[0].GlobalRefTest, element)("x").semantic_id == reference


def test_global_ref_is_a_reserved_argument_name(generated):
    cls = generated[0].GlobalRefTest

    assert cls(id_=SUBMODEL_ID, name="n", twoKeys="t", referred="r", concept="c", global_ref_="g") \
        .get_referable("global_ref").value == "g"
