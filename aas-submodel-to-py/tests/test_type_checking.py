"""Regression tests for type checking generated modules with mypy.

Generated modules didn't pass mypy, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/54:
- values of XSD types (e.g. of ALLOWED_RANGE) were rendered as xsd.from_xsd(...), which is typed as the
  union of all XSD types
- items of lists without template item were built with the optional value type of the metadata
- references to fragments were rendered with the referred type type(None), as BaSyx reads them from JSON;
  they refer to their file or blob (Referable is abstract)
- forward references in typehints (e.g. of BasicEventElement.observed) were rendered as ForwardRef("...")
  instead of a string
"""
import datetime
import importlib.util
import inspect

import pytest
from basyx.aas import model
from basyx.aas.model import datatypes

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/type-checking-test"
FRAGMENT = model.ModelReference((model.Key(model.KeyTypes.SUBMODEL, "https://example.com/ids/sm/documents"),
                                 model.Key(model.KeyTypes.FILE, "Manual"),
                                 model.Key(model.KeyTypes.FRAGMENT_REFERENCE, "page=1")), type(None))


def qualifiers(type_, value):
    return [model.Qualifier("SMT/Cardinality", str, value="ZeroToOne"), model.Qualifier(type_, str, value=value)]


@pytest.fixture(scope="module")
def generated(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="TypeCheckingTest",
        submodel_element=[
            model.Property("Ratio", datatypes.Float, qualifier=qualifiers("SMT/AllowedRange", "[0.0,1.0]")),
            model.Property("Count", datatypes.PositiveInteger, qualifier=qualifiers("SMT/AllowedRange", "[1,10]")),
            model.Property("Price", datatypes.Decimal, qualifier=qualifiers("SMT/DefaultValue", "1.50")),
            model.Property("Homepage", datatypes.AnyURI,
                           qualifier=qualifiers("SMT/DefaultValue", "https://example.com")),
            model.Property("Start", datatypes.DateTime,
                           qualifier=qualifiers("SMT/DefaultValue", "2020-01-01T00:00:00Z")),
            model.SubmodelElementList("Values", model.Property, value_type_list_element=datatypes.Int),
            model.RelationshipElement("Page", first=FRAGMENT, second=FRAGMENT),
            model.BasicEventElement("Changed", observed=model.ModelReference(
                (model.Key(model.KeyTypes.SUBMODEL, SUBMODEL_ID),), model.Submodel),
                                    direction=model.Direction.OUTPUT, state=model.StateOfEvent.ON),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "type_checking_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("type_checking_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, output_file


def test_generated_module_passes_mypy(generated, tmp_path):
    mypy = pytest.importorskip("mypy.api")

    stdout, stderr, status = mypy.run([str(generated[1]), "--python-version", "3.11", "--follow-imports=silent",
                                       "--ignore-missing-imports", "--cache-dir", str(tmp_path / "mypy")])

    assert status == 0, stdout + stderr


def test_xsd_values_are_rendered_with_their_type(generated):
    cls = generated[0].TypeCheckingTest

    assert cls.Ratio.ALLOWED_RANGE == (datatypes.Float(0.0), datatypes.Float(1.0))
    assert cls.Count.ALLOWED_RANGE == (datatypes.PositiveInteger(1), datatypes.PositiveInteger(10))
    defaults = {name: inspect.signature(getattr(cls, name).__init__).parameters["value"].default
                for name in ("Price", "Homepage", "Start")}
    assert defaults == {"Price": datatypes.Decimal("1.50"), "Homepage": datatypes.AnyURI("https://example.com"),
                        "Start": datetime.datetime(2020, 1, 1, tzinfo=datetime.timezone.utc)}
    values = [*cls.Ratio.ALLOWED_RANGE, *cls.Count.ALLOWED_RANGE, *defaults.values()]
    assert [type(value) for value in values] == [datatypes.Float, datatypes.Float, datatypes.PositiveInteger,
                                                 datatypes.PositiveInteger, datatypes.Decimal, datatypes.AnyURI,
                                                 datatypes.DateTime]


def test_items_of_lists_without_template_item_are_built_with_the_value_type(generated):
    values = generated[0].TypeCheckingTest.Values([1, 2])

    assert [(item.value_type, item.value) for item in values] == [(datatypes.Int, 1), (datatypes.Int, 2)]


def test_references_to_fragments_refer_to_their_file(generated):
    first = generated[0].TypeCheckingTest.Page().first

    assert (first.key, first.type) == (FRAGMENT.key, model.File)
