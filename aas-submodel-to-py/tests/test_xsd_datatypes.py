"""Regression tests for code generation of XSD datatypes.

Some XSD types are aliases in ``basyx.aas.model.datatypes`` (e.g.
``Duration = relativedelta``). Generated modules must refer to them by their
alias and restore their values losslessly, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/16
"""
import importlib.util
import json

import pytest
from basyx.aas import model
from basyx.aas.adapter.json import AASToJsonEncoder
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen
from aas_submodel_to_py.util import StringHandler

SUBMODEL_ID = "https://example.com/ids/sm/xsd-test"
TIMESPAN_MIN = datatypes.DateTime(2024, 1, 1, 0, 0, tzinfo=datatypes.datetime.timezone.utc)
TIMESPAN_MAX = datatypes.DateTime(2024, 12, 31, 23, 59, 59, tzinfo=datatypes.datetime.timezone.utc)
INTERVAL = datatypes.Duration(hours=1, minutes=30)
START_TIME = datatypes.Time(12, 30)
LAST_UPDATE = datatypes.DateTime(2024, 6, 1, 12, 0, tzinfo=datatypes.datetime.timezone.utc)
MIN_INTERVAL = datatypes.Duration(minutes=5)


@pytest.fixture(scope="module")
def generated_file(tmp_path_factory):
    observed = model.ModelReference(
        (model.Key(model.KeyTypes.SUBMODEL, SUBMODEL_ID),), model.Submodel)
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="XsdTest",
        submodel_element=[
            model.Property(id_short="PlannedProcessTime", value_type=datatypes.Duration),
            model.Property(id_short="Timestamp", value_type=datatypes.DateTime),
            model.Property(id_short="StartTime", value_type=datatypes.Time),
            # Operation variables are rendered as default values including their values
            model.Operation(
                id_short="DeriveSegment",
                input_variable=[
                    model.Range(id_short="Timespan", value_type=datatypes.DateTime,
                                min=TIMESPAN_MIN, max=TIMESPAN_MAX),
                    model.Property(id_short="Interval", value_type=datatypes.Duration, value=INTERVAL),
                    model.Property(id_short="Start", value_type=datatypes.Time, value=START_TIME),
                    model.Property(id_short="Count", value_type=datatypes.PositiveInteger,
                                   value=datatypes.PositiveInteger(5)),
                ],
            ),
            # Typehints of last_update/min_interval are Optional[DateTime]/Optional[Duration]
            model.BasicEventElement(
                id_short="ParameterChanged",
                observed=observed,
                direction=model.Direction.OUTPUT,
                state=model.StateOfEvent.ON,
                last_update=LAST_UPDATE,
                min_interval=MIN_INTERVAL,
            ),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "xsd_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictObjectStore([submodel]), output_file)
    return output_file


@pytest.fixture(scope="module")
def generated_module(generated_file):
    spec = importlib.util.spec_from_file_location("xsd_test", generated_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_generated_code_does_not_use_underlying_class_names(generated_file):
    source = generated_file.read_text(encoding="utf-8")

    assert "relativedelta" not in source
    assert "= datetime," not in source
    assert "= time," not in source


@pytest.mark.parametrize("cls_name, value, xsd_type, xsd_value", [
    ("PlannedProcessTime", datatypes.Duration(hours=2), "xs:duration", "PT2H"),
    ("Timestamp", datatypes.DateTime(2024, 5, 1, 8, 0), "xs:dateTime", "2024-05-01T08:00:00"),
    ("StartTime", datatypes.Time(8, 15), "xs:time", "08:15:00"),
])
def test_property_keeps_xsd_type(generated_module, cls_name, value, xsd_type, xsd_value):
    prop = getattr(generated_module.XsdTest, cls_name)(value=value)

    assert prop.value == value
    serialized = json.loads(json.dumps(prop, cls=AASToJsonEncoder))
    assert serialized["valueType"] == xsd_type
    assert serialized["value"] == xsd_value


def test_operation_variables_keep_values(generated_module):
    operation = generated_module.XsdTest.DeriveSegment()
    variables = {var.id_short: var for var in operation.input_variable}

    assert variables["Timespan"].value_type is datatypes.DateTime
    assert variables["Timespan"].min == TIMESPAN_MIN
    assert variables["Timespan"].max == TIMESPAN_MAX
    assert variables["Interval"].value_type is datatypes.Duration
    assert variables["Interval"].value == INTERVAL
    assert variables["Start"].value == START_TIME
    assert variables["Count"].value == 5
    assert type(variables["Count"].value) is datatypes.PositiveInteger


def test_event_element_keeps_values(generated_module):
    event = generated_module.XsdTest.ParameterChanged()

    assert event.last_update == LAST_UPDATE
    assert event.min_interval == MIN_INTERVAL


@pytest.mark.parametrize("typehint, expected", [
    ("typing.Optional[dateutil.relativedelta.relativedelta]", "Optional[Duration]"),
    ("typing.Optional[datetime.datetime]", "Optional[DateTime]"),
    ("typing.Union[datetime.time, basyx.aas.model.datatypes.Date]", "Union[Time, Date]"),
    ("typing.Optional[datetime.timezone]", "Optional[timezone]"),
])
def test_typehint_uses_xsd_type_aliases(typehint, expected):
    assert StringHandler.remove_parent_modules_in_typehint(typehint) == expected
