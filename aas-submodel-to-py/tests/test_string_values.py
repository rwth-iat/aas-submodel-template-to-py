"""Tests for rendering string values in generated code.

Strings containing line breaks used to be rendered as single-line raw string
literals, so the generated module could not be parsed, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/18
"""
import ast
import importlib.util
import warnings

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen
from aas_submodel_to_py.util import StringHandler

STRINGS = [
    "",
    "simple text",
    "it's",
    'say "hello"',
    "it's \"quoted\"",
    "line1\nline2",
    "line1\r\nline2",
    "ends with backslash\\",
    "regex \\d+\\.\\d+",
    "it's in C:\\new\\table",
    "tab\tseparated",
    "Umlaute äöü and “typographic quotes”",
]


@pytest.mark.parametrize("value", STRINGS)
def test_string_literal_round_trip(value):
    literal = StringHandler.reprify(value)

    with warnings.catch_warnings():
        # Invalid escape sequences only cause a warning
        warnings.simplefilter("error")
        assert ast.literal_eval(literal) == value


@pytest.mark.parametrize("value", ["simple text", "regex \\d+\\.\\d+", 'say "hello"'])
def test_raw_string_literal_kept(value):
    assert StringHandler.reprify(value) == f"r'{value}'"


DESCRIPTION = {
    "en": "The currency used. Must be a three-letter\n                    ISO currency code. (Mandatory)",
    "de": "Die verwendete Währung, z.B. \"EUR\" oder 'USD'",
}
DISPLAY_NAME = {"en": "Path C:\\new\\"}
EXAMPLE_VALUE = "first line\nsecond line with C:\\temp\\"


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_="https://example.com/ids/sm/string-test",
        id_short="StringTest",
        submodel_element=[
            model.Property(
                id_short="Currency",
                value_type=str,
                description=model.MultiLanguageTextType(DESCRIPTION),
                display_name=model.MultiLanguageNameType(DISPLAY_NAME),
                qualifier=[model.Qualifier("ExampleValue", str, value=EXAMPLE_VALUE)],
            ),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "string_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("string_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_generated_strings_keep_values(generated_module):
    currency = generated_module.StringTest.Currency(value="EUR")

    assert dict(currency.description) == DESCRIPTION
    assert dict(currency.display_name) == DISPLAY_NAME
    assert currency.get_qualifier_by_type("ExampleValue").value == EXAMPLE_VALUE
