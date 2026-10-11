"""Regression tests for passing the metadata of generated classes as typed keyword arguments.

Every generated class repeated all init arguments of its BaSyx class (id_short, description, semantic_id, ...)
in its signature, in super().__init__() and, for values created per instance, in "if x is None" blocks: 77% of
the size of py-aas-submodels. Inits only name the submodel elements and values; metadata is passed as
**kwargs, typed by a TypedDict per BaSyx class (PEP 692), and template_defaults() returns the template's
values, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/51
"""
import importlib.util
import inspect
import typing

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/metadata-test"


def global_reference(value):
    return model.ExternalReference((model.Key(model.KeyTypes.GLOBAL_REFERENCE, value),))


NAME_ID = global_reference("https://example.com/ids/cd/Name")
OTHER_ID = global_reference("https://example.com/ids/cd/Other")
DESCRIPTION = {"en": "Name of the product"}


def optional():
    return [model.Qualifier("SMT/Cardinality", str, value="ZeroToOne")]


@pytest.fixture(scope="module")
def generated(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="MetadataTest",
        semantic_id=global_reference("https://example.com/ids/sm/MetadataTest"),
        administration=model.AdministrativeInformation(version="1", revision="0"),
        submodel_element=[
            model.Property("Name", str, semantic_id=NAME_ID, description=model.MultiLanguageTextType(DESCRIPTION),
                           qualifier=[model.Qualifier("unit", str, value="kg")]),
            model.Property("Mode", str, qualifier=optional() + [
                model.Qualifier("SMT/DefaultValue", str, value="auto")]),
            model.Range("Temperature", int, qualifier=optional()),
            model.File("Manual", "application/pdf", qualifier=optional()),
            model.File("Attachment", "{arbitrary}", qualifier=optional()),
            model.SubmodelElementCollection("Address", qualifier=optional(), value=[
                model.Property("Street", str, qualifier=optional())]),
            model.Entity("Part", model.EntityType.SELF_MANAGED_ENTITY, global_asset_id="https://example.com/a",
                         qualifier=optional()),
            # Named like the parameter of the metadata, a TypedDict and metadata of the submodel
            model.Property("Kwargs", str, qualifier=optional()),
            model.Property("PropertyMetadata", str, qualifier=optional()),
            model.Property("Administration", str, qualifier=optional()),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "metadata_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("metadata_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, output_file.read_text()


def parameters(cls) -> list:
    return [(name, p.kind) for name, p in inspect.signature(cls.__init__).parameters.items() if name != "self"]


KEYWORD = inspect.Parameter.POSITIONAL_OR_KEYWORD
VAR_KEYWORD = inspect.Parameter.VAR_KEYWORD


def test_inits_only_name_values_and_elements(generated):
    cls = generated[0].MetadataTest

    assert parameters(cls.Name) == [("value", KEYWORD), ("kwargs", VAR_KEYWORD)]
    assert parameters(cls.Temperature) == [("min", KEYWORD), ("max", KEYWORD), ("kwargs", VAR_KEYWORD)]
    assert parameters(cls.Address) == [("street", KEYWORD), ("kwargs", VAR_KEYWORD)]
    assert parameters(cls)[:2] == [("id_", KEYWORD), ("name", KEYWORD)]
    assert parameters(cls)[-1] == ("kwargs", VAR_KEYWORD)


def test_values_with_template_defaults_are_keyword_arguments(generated):
    cls = generated[0].MetadataTest

    assert inspect.signature(cls.Mode.__init__).parameters["value"].default == "auto"
    assert parameters(cls.Manual) == [("value", KEYWORD), ("content_type", KEYWORD), ("kwargs", VAR_KEYWORD)]
    assert inspect.signature(cls.Manual.__init__).parameters["content_type"].default == "application/pdf"
    assert inspect.signature(cls.Attachment.__init__).parameters["content_type"].default is inspect.Parameter.empty


def test_template_defaults_are_the_values_of_the_template(generated):
    defaults = generated[0].MetadataTest.Name.template_defaults()

    # Only values differing from the defaults of BaSyx
    assert set(defaults) == {"id_short", "value_type", "description", "semantic_id", "qualifier"}
    assert (defaults["id_short"], defaults["value_type"], defaults["semantic_id"]) == ("Name", str, NAME_ID)
    assert dict(defaults["description"]) == DESCRIPTION
    assert [q.type for q in defaults["qualifier"]] == ["unit"]


def test_template_defaults_are_created_for_each_call(generated):
    name = generated[0].MetadataTest.Name

    assert name.template_defaults()["description"] is not name.template_defaults()["description"]
    assert name("a").description is not name("b").description


def test_unpassed_metadata_has_the_template_values(generated):
    module = generated[0]
    instance = module.MetadataTest(id_=SUBMODEL_ID, name="n")

    assert (instance.id_short, instance.kind, instance.administration.version) == (
        "MetadataTest", model.ModellingKind.INSTANCE, "1")
    name = instance.get_referable("Name")
    assert (name.semantic_id, dict(name.description), name.category) == (NAME_ID, DESCRIPTION, None)


def test_passed_metadata_replaces_the_template_values(generated):
    cls = generated[0].MetadataTest
    name = cls.Name("n", semantic_id=OTHER_ID, category="PARAMETER", description=None)

    assert (name.semantic_id, name.category, name.description) == (OTHER_ID, "PARAMETER", None)
    assert cls(id_=SUBMODEL_ID, name="n", id_short="Other").id_short == "Other"


def test_unknown_metadata_is_rejected(generated):
    with pytest.raises(TypeError, match="semantic_idd"):
        generated[0].MetadataTest.Name("n", semantic_idd=OTHER_ID)


def test_metadata_is_typed_by_a_typed_dict_per_basyx_class(generated):
    module, source = generated

    assert source.count("class PropertyMetadata(TypedDict, total=False):") == 1
    assert set(module.PropertyMetadata.__annotations__) == set(inspect.signature(model.Property.__init__).parameters) \
        - {"self", "parent", "value"}
    assert set(module.SubmodelMetadata.__annotations__) == set(inspect.signature(model.Submodel.__init__).parameters) \
        - {"self", "parent", "id_", "submodel_element"}
    assert "content_type" not in module.FileMetadata.__annotations__
    assert "statement" not in module.EntityMetadata.__annotations__
    assert not hasattr(module, "BlobMetadata")


def test_metadata_typehints_can_be_resolved(generated):
    module = generated[0]
    hints = typing.get_type_hints(module.MetadataTest.Name.__init__)

    assert hints["kwargs"] == typing.Unpack[module.PropertyMetadata]
    assert typing.get_type_hints(module.MetadataTest.Name.template_defaults)["return"] is module.PropertyMetadata


def test_names_of_metadata_are_reserved(generated):
    cls = generated[0].MetadataTest
    instance = cls(id_=SUBMODEL_ID, name="n", kwargs_="k", propertyMetadata="p", administration_="a",
                   administration=model.AdministrativeInformation(version="2"))

    assert cls.PropertyMetadata_("p").id_short == "PropertyMetadata"
    assert [instance.get_referable(id_short).value for id_short in ("Kwargs", "PropertyMetadata", "Administration")] \
        == ["k", "p", "a"]
    assert instance.administration.version == "2"
