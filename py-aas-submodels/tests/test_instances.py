"""Build instances of generated submodel classes, serialize them with BaSyx and check the result.

- aas-core3.1, an AAS SDK independent of BaSyx, reads the JSON and XML strictly and verifies
  the constraints of AAS metamodel V3.1.
- BaSyx reads its own output back without loss.
- The JSON of a Digital Nameplate holds the given values and the semantic IDs and structure of
  its template (IDTA 02006-3-0-1).
- An instance of every generated submodel class, built from sample values for its required
  arguments, passes these checks.
"""
import collections.abc
import importlib
import inspect
import io
import json
import pathlib
import typing

import aas_core3_1.jsonization as aas_jsonization
import aas_core3_1.verification as aas_verification
import aas_core3_1.xmlization as aas_xmlization
import pytest
from basyx.aas import model
from basyx.aas.adapter.json import read_aas_json_file, write_aas_json_file
from basyx.aas.adapter.xml import read_aas_xml_file, write_aas_xml_file
from basyx.aas.model import datatypes

import py_aas_submodels
from py_aas_submodels.digital_nameplate_3_0_1 import Nameplate

# BaSyx <= 2.2.0 serializes Entities without specific asset IDs as an empty list, which
# metamodel V3.1 doesn't allow (https://github.com/eclipse-basyx/basyx-python-sdk/issues/636)
BASYX_EMPTY_SPECIFIC_ASSET_IDS = "Specific asset IDs must be either not set or have at least one item."


def to_json(store: model.AbstractObjectStore) -> str:
    output = io.StringIO()
    write_aas_json_file(output, store)
    return output.getvalue()


def to_xml(store: model.AbstractObjectStore) -> bytes:
    output = io.BytesIO()
    write_aas_xml_file(output, store)
    return output.getvalue()


def verification_errors(environment) -> list:
    return [f"{error.path}: {error.cause}" for error in aas_verification.verify(environment)
            if error.cause != BASYX_EMPTY_SPECIFIC_ASSET_IDS]


def serialization_errors(submodel: model.Submodel) -> list:
    """Serialize `submodel` to JSON and XML with BaSyx, and return the errors aas-core3.1 finds in them.
    Raise if aas-core3.1 can't read them, or if BaSyx can't read them back without loss"""
    store = model.DictIdentifiableStore([submodel])

    json_text = to_json(store)
    errors = verification_errors(aas_jsonization.environment_from_jsonable(json.loads(json_text)))
    assert json.loads(to_json(read_aas_json_file(io.StringIO(json_text), failsafe=False))) == json.loads(json_text)

    xml = to_xml(store)
    errors += verification_errors(aas_xmlization.environment_from_str(xml.decode("utf-8")))
    assert to_xml(read_aas_xml_file(io.BytesIO(xml), failsafe=False)) == xml
    return errors


def to_jsonable(submodel: model.Submodel) -> dict:
    return json.loads(to_json(model.DictIdentifiableStore([submodel])))["submodels"][0]


def semantic_id(element: dict) -> str:
    return element["semanticId"]["keys"][0]["value"]


def by_id_short(elements: list) -> dict:
    return {element["idShort"]: element for element in elements}


@pytest.fixture
def nameplate():
    marking = Nameplate.Markings.Markings_item
    return Nameplate(
        id_="https://example.com/ids/sm/nameplate-001",
        uRIOfTheProduct="https://www.domain-abc.com/Model-Nr-1234",
        manufacturerName=model.MultiLanguageTextType({"de": "Muster AG", "en": "Muster Ltd."}),
        manufacturerProductDesignation=model.MultiLanguageTextType({"en": "ABC-123"}),
        addressInformation=Nameplate.AddressInformation(),
        orderCodeOfManufacturer="ABC-123-XYZ",
        serialNumber=Nameplate.SerialNumber("12345678"),
        yearOfConstruction="2022",
        dateOfManufacture=datatypes.Date(2022, 3, 1),
        companyLogo=Nameplate.CompanyLogo(value="/aasx/logo.png"),
        markings=[
            marking(markingName="CE", markingFile=marking.MarkingFile(value="/aasx/ce.png"),
                    issueDate=datatypes.Date(2022, 1, 15)),
            marking(markingName="UKCA", markingFile=marking.MarkingFile(value="/aasx/ukca.png")),
        ],
    )


def test_nameplate_is_valid_aas(nameplate):
    assert serialization_errors(nameplate) == []


def test_nameplate_json_holds_values_and_template_metadata(nameplate):
    submodel = to_jsonable(nameplate)
    elements = by_id_short(submodel["submodelElements"])

    assert (submodel["id"], submodel["idShort"]) == ("https://example.com/ids/sm/nameplate-001", "Nameplate")
    assert semantic_id(submodel) == "https://admin-shell.io/idta/nameplate/3/0/Nameplate"
    assert submodel["administration"]["templateId"] == "https://admin-shell.io/idta-02006-3-0"
    # Only the passed elements, in the order of the template
    assert list(elements) == [
        "URIOfTheProduct", "ManufacturerName", "ManufacturerProductDesignation", "AddressInformation",
        "OrderCodeOfManufacturer", "SerialNumber", "YearOfConstruction", "DateOfManufacture", "CompanyLogo",
        "Markings"]

    expected = {
        # idShort: (modelType, semanticId, valueType, value)
        "URIOfTheProduct": ("Property", "0112/2///61987#ABN590#002", "xs:anyURI",
                            "https://www.domain-abc.com/Model-Nr-1234"),
        "OrderCodeOfManufacturer": ("Property", "0112/2///61987#ABA950#008", "xs:string", "ABC-123-XYZ"),
        "SerialNumber": ("Property", "0112/2///61987#ABA951#009", "xs:string", "12345678"),
        "YearOfConstruction": ("Property", "0112/2///61987#ABP000#002", "xs:string", "2022"),
        "DateOfManufacture": ("Property", "0112/2///61987#ABB757#007", "xs:date", "2022-03-01"),
    }
    for id_short, (model_type, semantic, value_type, value) in expected.items():
        element = elements[id_short]
        assert (element["modelType"], semantic_id(element), element["valueType"], element["value"]) == \
            (model_type, semantic, value_type, value), id_short

    manufacturer_name = elements["ManufacturerName"]
    assert (manufacturer_name["modelType"], semantic_id(manufacturer_name)) == \
        ("MultiLanguageProperty", "0112/2///61987#ABA565#009")
    assert sorted(manufacturer_name["value"], key=lambda text: text["language"]) == [
        {"language": "de", "text": "Muster AG"}, {"language": "en", "text": "Muster Ltd."}]

    logo = elements["CompanyLogo"]
    assert (logo["modelType"], semantic_id(logo), logo["contentType"], logo["value"]) == \
        ("File", "0112/2///61987#ABP463#001", "image/png", "/aasx/logo.png")

    address = elements["AddressInformation"]
    assert (address["modelType"], semantic_id(address)) == \
        ("SubmodelElementCollection", "https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation")


def test_nameplate_json_holds_list_items(nameplate):
    markings = to_jsonable(nameplate)["submodelElements"][-1]

    assert (markings["idShort"], markings["modelType"], semantic_id(markings)) == \
        ("Markings", "SubmodelElementList", "0112/2///61360_7#AAS006#001")
    assert markings["typeValueListElement"] == "SubmodelElementCollection"
    # Items of lists have no idShort by default (optional since metamodel V3.1)
    assert [("idShort" in item, item["modelType"], semantic_id(item)) for item in markings["value"]] == \
        [(False, "SubmodelElementCollection", "0112/2///61360_7#AAS009#001")] * 2

    first, second = (by_id_short(item["value"]) for item in markings["value"])
    assert (first["MarkingName"]["value"], second["MarkingName"]["value"]) == ("CE", "UKCA")
    assert (first["IssueDate"]["valueType"], first["IssueDate"]["value"]) == ("xs:date", "2022-01-15")
    assert "IssueDate" not in second
    assert (first["MarkingFile"]["contentType"], first["MarkingFile"]["value"]) == ("image/png", "/aasx/ce.png")
    assert semantic_id(first["MarkingName"]) == "0112/2///61987#ABA231#009"


@pytest.mark.xfail(strict=True, reason="Issue #37: instances of generated submodel classes have kind Template")
def test_nameplate_is_an_instance(nameplate):
    assert to_jsonable(nameplate).get("kind", "Instance") == "Instance"


# Instances of all generated submodel classes

SAMPLE_LEXICALS = ("1", "true", "2024-01-01", "2024-01-01T00:00:00Z", "P1D", "12:00:00Z", "x")


def sample_value(value_type: type):
    """A value of an XSD type, parsed from the first sample lexical representation it accepts"""
    for lexical in SAMPLE_LEXICALS:
        try:
            return datatypes.from_xsd(lexical, value_type)
        except ValueError:
            pass
    raise ValueError(f"No sample value for {value_type}")


def build_instance(cls: type):
    """Instance of a generated class with sample values for all its required arguments.
    Raw values are preferred over instances of generated classes, so that both are built"""
    typehints = typing.get_type_hints(cls.__init__)
    kwargs = {name: sample_argument(cls, name, typehints[name])
              for name, parameter in inspect.signature(cls.__init__).parameters.items()
              if name != "self" and parameter.default is inspect.Parameter.empty}
    if issubclass(cls, model.Entity) and \
            inspect.signature(cls.__init__).parameters["entity_type"].default is model.EntityType.SELF_MANAGED_ENTITY:
        kwargs["global_asset_id"] = "https://example.com/ids/asset"  # AASd-014
    return cls(**kwargs)


def sample_argument(cls: type, name: str, typehint):
    origin, args = typing.get_origin(typehint), typing.get_args(typehint)
    if name == "id_":
        return f"https://example.com/ids/sm/{cls.__name__}"
    elif origin is typing.Union:
        return sample_argument(cls, name, args[0])
    elif origin is collections.abc.Iterable:
        return [sample_argument(cls, name, args[0])]
    elif origin is tuple:
        return tuple(sample_argument(cls, name, arg) for arg in args)
    elif isinstance(typehint, type) and typehint.__module__ == cls.__module__:
        return build_instance(typehint)
    elif typehint is model.LangStringSet:
        return model.MultiLanguageTextType({"en": "x"})
    elif typehint is model.Reference:
        return model.ExternalReference((model.Key(model.KeyTypes.GLOBAL_REFERENCE, "https://example.com/ids/x"),))
    elif name == "content_type":
        return "application/pdf"
    elif isinstance(typehint, type):
        return sample_value(typehint)
    raise TypeError(f"No sample argument {cls.__qualname__}.{name}: {typehint}")


def generated_submodel_classes():
    for path in sorted(pathlib.Path(py_aas_submodels.__file__).parent.glob("*.py")):
        if path.stem != "__init__":
            module = importlib.import_module(f"py_aas_submodels.{path.stem}")
            for obj in vars(module).values():
                if isinstance(obj, type) and issubclass(obj, model.Submodel) and obj.__module__ == module.__name__:
                    yield pytest.param(obj, id=f"{path.stem}.{obj.__name__}")


@pytest.mark.parametrize("submodel_cls", list(generated_submodel_classes()))
def test_instance_of_generated_submodel_class_is_valid_aas(submodel_cls):
    # The first instance must not keep elements the second one needs
    build_instance(submodel_cls)
    try:
        submodel = build_instance(submodel_cls)
    except ValueError as e:
        if "already a parent" in str(e):
            pytest.xfail("Issue #38: generated classes share default submodel elements between instances")
        raise

    errors = serialization_errors(submodel)
    if errors and all("AASd-014" in error for error in errors):
        pytest.xfail("Issue #39: instances get the statements of the template's Entities")
    assert errors == []
