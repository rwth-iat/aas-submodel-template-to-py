"""Regression tests for building Range elements from raw values.

Arguments taking Range elements also accept raw ``(min, max)`` pairs. The
generated code used to split the typehint ``Union[Tuple[str, str], ...]`` at
every comma, producing invalid code, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/17
"""
import importlib.util
import json

import pytest
from basyx.aas import model
from basyx.aas.adapter.json import AASToJsonEncoder
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/range-test"


def cardinality(value):
    return [model.Qualifier("SMT/Cardinality", str, value=value)]


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="RangeTest",
        submodel_element=[
            model.Range("ArbitraryRange", str, qualifier=cardinality("ZeroToMany")),
            model.Range("MeasuringRange", datatypes.Float, qualifier=cardinality("One")),
            model.Range("TimeStamp", datatypes.DateTime, qualifier=cardinality("ZeroToOne")),
            model.Property("Keyword", str, qualifier=cardinality("ZeroToMany")),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "range_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("range_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def elements_by_id_short(submodel):
    return {se.id_short: se for se in submodel.submodel_element}


def test_ranges_built_from_raw_pairs(generated_module):
    submodel = generated_module.RangeTest(
        id_=SUBMODEL_ID,
        arbitraryRange=[("a", "b"), ("c", "d")],
        measuringRange=(datatypes.Float(0.5), datatypes.Float(1.5)),
        timeStamp=(datatypes.DateTime(2024, 1, 1), datatypes.DateTime(2024, 12, 31)),
    )
    elements = elements_by_id_short(submodel)

    assert isinstance(elements["ArbitraryRange0"], generated_module.RangeTest.ArbitraryRange)
    assert (elements["ArbitraryRange0"].min, elements["ArbitraryRange0"].max) == ("a", "b")
    assert (elements["ArbitraryRange1"].min, elements["ArbitraryRange1"].max) == ("c", "d")
    assert (elements["MeasuringRange"].min, elements["MeasuringRange"].max) == (0.5, 1.5)
    assert elements["TimeStamp"].max == datatypes.DateTime(2024, 12, 31)


def test_existing_range_objects_are_kept(generated_module):
    cls = generated_module.RangeTest
    existing_range = cls.ArbitraryRange(min="x", max="y")
    measuring_range = cls.MeasuringRange(min=datatypes.Float(0), max=datatypes.Float(1))

    submodel = cls(
        id_=SUBMODEL_ID,
        arbitraryRange=[existing_range, ("a", "b")],
        measuringRange=measuring_range,
    )
    elements = elements_by_id_short(submodel)

    assert elements["ArbitraryRange0"] is existing_range
    assert (elements["ArbitraryRange1"].min, elements["ArbitraryRange1"].max) == ("a", "b")
    assert elements["MeasuringRange"] is measuring_range


def test_properties_built_from_raw_values(generated_module):
    submodel = generated_module.RangeTest(
        id_=SUBMODEL_ID,
        measuringRange=(datatypes.Float(0), datatypes.Float(1)),
        keyword=["foo", "bar"],
    )
    elements = elements_by_id_short(submodel)

    assert (elements["Keyword0"].value, elements["Keyword1"].value) == ("foo", "bar")


def test_range_serialization_keeps_bounds_and_xsd_type(generated_module):
    submodel = generated_module.RangeTest(
        id_=SUBMODEL_ID,
        measuringRange=(datatypes.Float(0.5), datatypes.Float(1.5)),
        timeStamp=(datatypes.DateTime(2024, 1, 1), datatypes.DateTime(2024, 12, 31)),
    )
    elements = elements_by_id_short(submodel)

    measuring_range = json.loads(json.dumps(elements["MeasuringRange"], cls=AASToJsonEncoder))
    assert (measuring_range["valueType"], measuring_range["min"], measuring_range["max"]) == \
        ("xs:float", "0.5", "1.5")
    time_stamp = json.loads(json.dumps(elements["TimeStamp"], cls=AASToJsonEncoder))
    assert (time_stamp["valueType"], time_stamp["min"], time_stamp["max"]) == \
        ("xs:dateTime", "2024-01-01T00:00:00", "2024-12-31T00:00:00")
