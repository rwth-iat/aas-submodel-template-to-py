"""Regression tests for building submodel elements from falsy raw values.

Arguments taking submodel elements also accept raw values. Falsy raw values
(``0``, ``0.0``, ``False``, ``""``) used to be passed on unconverted, raising
``TypeError: Unknown type of value in submodel_element_args``, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/22
"""
import importlib.util

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/falsy-test"


def cardinality(value):
    return [model.Qualifier("SMT/Cardinality", str, value=value)]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="FalsyTest",
        submodel_element=[
            model.Property("Count", datatypes.Int, qualifier=cardinality("One")),
            model.Property("Ratio", datatypes.Double, qualifier=cardinality("One")),
            model.Property("Enabled", datatypes.Boolean, qualifier=cardinality("One")),
            model.Property("Comment", datatypes.String, qualifier=cardinality("One")),
            model.Property("OptionalCount", datatypes.Int, qualifier=cardinality("ZeroToOne")),
            model.Property("Levels", datatypes.Int, qualifier=cardinality("ZeroToMany")),
            model.SubmodelElementCollection(
                "Settings",
                value=[model.Property("Retries", datatypes.Int, qualifier=cardinality("One"))],
                qualifier=cardinality("One"),
            ),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "falsy_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("falsy_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def elements_by_id_short(element):
    children = element.submodel_element if isinstance(element, model.Submodel) else element.value
    return {se.id_short: se for se in children}


def build_submodel(module, **kwargs):
    cls = module.FalsyTest
    args = dict(
        id_=SUBMODEL_ID,
        count=1,
        ratio=1.5,
        enabled=True,
        comment="text",
        settings=cls.Settings(retries=1),
    )
    args.update(kwargs)
    return cls(**args)


@pytest.mark.parametrize("arg, id_short, raw_value", [
    ("count", "Count", 0),
    ("ratio", "Ratio", 0.0),
    ("enabled", "Enabled", False),
    ("comment", "Comment", ""),
    ("optionalCount", "OptionalCount", 0),
])
def test_property_built_from_falsy_raw_value(generated_module, arg, id_short, raw_value):
    submodel = build_submodel(generated_module, **{arg: raw_value})
    element = elements_by_id_short(submodel)[id_short]

    assert isinstance(element, getattr(generated_module.FalsyTest, id_short))
    assert element.value == raw_value
    assert type(element.value) is type(element.value_type(raw_value))


def test_falsy_raw_values_in_list(generated_module):
    submodel = build_submodel(generated_module, levels=[0, 1])
    elements = elements_by_id_short(submodel)

    assert (elements["Levels0"].value, elements["Levels1"].value) == (0, 1)


def test_falsy_raw_value_in_collection(generated_module):
    settings = generated_module.FalsyTest.Settings(retries=0)

    assert elements_by_id_short(settings)["Retries"].value == 0


def test_all_falsy_raw_values_at_once(generated_module):
    cls = generated_module.FalsyTest
    submodel = cls(id_=SUBMODEL_ID, count=0, ratio=0.0, enabled=False, comment="",
                   optionalCount=0, levels=[0], settings=cls.Settings(retries=0))
    elements = elements_by_id_short(submodel)

    assert [elements[i].value for i in ("Count", "Ratio", "Enabled", "Comment", "OptionalCount", "Levels0")] == \
        [0, 0.0, False, "", 0, 0]
