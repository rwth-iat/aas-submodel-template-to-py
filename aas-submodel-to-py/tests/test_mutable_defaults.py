"""Regression tests for default values of generated classes, which must not be shared between instances.

Defaults holding submodel elements of the template (Entity statements, Operation variables)
were created once and shared, so the second instance failed with "Object has already a parent".
Mutable defaults like descriptions were shared as well, so changing one instance changed all,
see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/38
"""
import importlib.util

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/defaults-test"
REFERENCE = model.ExternalReference((model.Key(model.KeyTypes.GLOBAL_REFERENCE, "https://example.com/ids/x"),))


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="DefaultsTest",
        description=model.MultiLanguageTextType({"en": "Submodel description"}),
        administration=model.AdministrativeInformation(version="1", revision="0",
                                                       template_id="https://example.com/ids/template"),
        submodel_element=[
            model.Property("Name", str, description=model.MultiLanguageTextType({"en": "Name description"})),
            model.Entity("Node", model.EntityType.CO_MANAGED_ENTITY,
                         statement=[model.Property("Weight", datatypes.Double)]),
            model.Operation("Compute", input_variable=[model.Property("Input", str)],
                            output_variable=[model.Property("Output", str)]),
            model.AnnotatedRelationshipElement("Relation", first=REFERENCE, second=REFERENCE,
                                               annotation=[model.Property("Note", str)]),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "defaults_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("defaults_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def shared(first, second) -> set:
    return {id(element) for element in first} & {id(element) for element in second}


def build_submodel(cls):
    return cls(id_=SUBMODEL_ID, name="x", node=cls.Node(weight=1.0), compute=cls.Compute(), relation=cls.Relation())


def test_entity_statements_are_not_shared(generated_module):
    # Statements are arguments (issue #39), so they can't be shared defaults any more
    node_cls = generated_module.DefaultsTest.Node
    first, second = node_cls(weight=1.0), node_cls(weight=2.0)

    assert [statement.value for statement in second.statement] == [2.0]
    assert not shared(first.statement, second.statement)


def test_operation_variables_are_not_shared(generated_module):
    compute_cls = generated_module.DefaultsTest.Compute
    first, second = compute_cls(), compute_cls()

    assert ([v.id_short for v in second.input_variable], [v.id_short for v in second.output_variable]) == \
        (["Input"], ["Output"])
    assert not shared(first.input_variable, second.input_variable)
    assert not shared(first.output_variable, second.output_variable)


def test_annotations_are_not_shared(generated_module):
    relation_cls = generated_module.DefaultsTest.Relation
    first, second = relation_cls(), relation_cls()

    assert [annotation.id_short for annotation in second.annotation] == ["Note"]
    assert not shared(first.annotation, second.annotation)


def test_descriptions_are_not_shared(generated_module):
    name_cls = generated_module.DefaultsTest.Name
    first, second = name_cls("a"), name_cls("b")

    first.description["en"] = "changed"

    assert dict(second.description) == {"en": "Name description"}
    assert dict(name_cls("c").description) == {"en": "Name description"}


def test_administration_and_description_of_submodels_are_not_shared(generated_module):
    cls = generated_module.DefaultsTest
    first, second = build_submodel(cls), build_submodel(cls)

    assert first.administration is not second.administration
    assert first.description is not second.description
    assert (second.administration.version, second.administration.template_id) == \
        ("1", "https://example.com/ids/template")


def test_passed_values_replace_defaults(generated_module):
    description = model.MultiLanguageTextType({"de": "Eigene Beschreibung"})

    assert dict(generated_module.DefaultsTest.Name("a", description=description).description) == \
        {"de": "Eigene Beschreibung"}
