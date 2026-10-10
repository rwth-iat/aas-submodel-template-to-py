"""Tests for names in generated code.

Generated classes are named after idShorts. With star imports, a class for an
element named e.g. `Key` shadowed `basyx.aas.model.Key` in the enclosing class
body, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/20.
Generated code therefore refers to BaSyx through the module aliases `aas` and
`xsd`, and only the few names imported directly must not be used as class names.
"""
import decimal
import importlib.util

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen
from aas_submodel_to_py.util import NamingGenerator, StringHandler

SUBMODEL_ID = "https://example.com/ids/sm/class-name-test"


def semantic_id(name):
    return model.ExternalReference((model.Key(model.KeyTypes.GLOBAL_REFERENCE, f"https://example.com/{name}"),))


@pytest.mark.parametrize("val, expected", [
    (model.Property, "aas.Property"),
    (model.KeyTypes.GLOBAL_REFERENCE, "aas.KeyTypes.GLOBAL_REFERENCE"),
    (datatypes.Duration, "xsd.Duration"),
    (datatypes.Date, "xsd.Date"),
    (decimal.Decimal, "xsd.Decimal"),
    (str, "str"),
])
def test_basyx_names_are_qualified(val, expected):
    assert StringHandler.reprify(val) == expected


@pytest.mark.parametrize("id_short, cls_name", [
    # BaSyx names don't conflict, as generated code uses them qualified (aas.Key)
    ("Key", "Key"),
    ("Reference", "Reference"),
    ("Property", "Property"),
    ("Duration", "Duration"),
    ("Type", "Type"),
    ("Name", "Name"),
    ("Document01", "Document01"),
    # Names imported directly or builtins used in generated code
    ("Optional", "Optional_"),
    ("Union", "Union_"),
    ("TypeError", "TypeError_"),
    ("None", "None_"),
])
def test_class_name(id_short, cls_name):
    se = model.Property(id_short=id_short, value_type=str)

    assert NamingGenerator.create_specific_referable_cls_name(se) == cls_name


@pytest.mark.parametrize("id_short, arg_name", [
    ("Key", "key"),
    ("Aas", "aas_"),
    ("Xsd", "xsd_"),
])
def test_arg_name(id_short, arg_name):
    se = model.Property(id_short=id_short, value_type=str)

    assert NamingGenerator.create_arg_name_for_referable(se) == arg_name


@pytest.fixture(scope="module")
def generated_file(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="ClassNameTest",
        submodel_element=[
            # Mirrors ActualPersonnelWorkTime of the KPI template: the collection's own
            # semantic ID is rendered after the nested classes Key, Property, ...
            model.SubmodelElementCollection(
                id_short="Measurement",
                semantic_id=semantic_id("Measurement"),
                value=[
                    model.Property(id_short="Key", value_type=str, semantic_id=semantic_id("Key")),
                    model.Property(id_short="Property", value_type=int, semantic_id=semantic_id("Property")),
                    model.ReferenceElement(id_short="Reference", semantic_id=semantic_id("Reference")),
                    model.Property(id_short="Duration", value_type=str),
                    # Its value_type default is rendered after the class Duration
                    model.Property(id_short="Interval", value_type=datatypes.Duration),
                    model.Property(id_short="Optional", value_type=str),
                ],
            ),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "class_name_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)
    return output_file


@pytest.fixture(scope="module")
def generated_module(generated_file):
    spec = importlib.util.spec_from_file_location("class_name_test", generated_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_generated_code_has_no_star_imports(generated_file):
    assert "import *" not in generated_file.read_text(encoding="utf-8")


def test_elements_named_like_basyx_classes(generated_module):
    cls = generated_module.ClassNameTest.Measurement
    reference = model.ExternalReference((model.Key(model.KeyTypes.GLOBAL_REFERENCE, "https://example.com/x"),))

    measurement = cls(key="k1", property=42, reference=reference, duration="long",
                      interval=datatypes.Duration(hours=1), optional="maybe")
    elements = {se.id_short: se for se in measurement.value}

    assert measurement.semantic_id == semantic_id("Measurement")
    assert isinstance(elements["Key"], cls.Key)
    assert isinstance(elements["Key"], model.Property)
    assert elements["Key"].value == "k1"
    assert elements["Key"].semantic_id == semantic_id("Key")
    assert isinstance(elements["Property"], model.Property)
    assert elements["Property"].value == 42
    assert elements["Reference"].value == reference
    assert elements["Interval"].value_type is datatypes.Duration
    assert isinstance(elements["Optional"], cls.Optional_)
