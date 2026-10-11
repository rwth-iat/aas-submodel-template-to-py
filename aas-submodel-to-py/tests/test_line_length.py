"""Regression tests for the line length of generated modules.

Generated modules were formatted with Black's default line length of 88, which wraps many lines of
deeply nested classes; every additional line repeats the indentation. They are formatted with a line
length of 120, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/47
"""
import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

LONG_NAME = "ElementWithAVeryLongNameForTests"


def generate(tmp_path, **kwargs) -> str:
    submodel = model.Submodel(
        id_="https://example.com/ids/sm/line-length-test",
        id_short="LineLengthTest",
        submodel_element=[model.Property(LONG_NAME, str, qualifier=[
            model.Qualifier("SMT/Cardinality", str, value="ZeroToOne")])],
    )
    output_file = tmp_path / "line_length_test.py"
    SubmodelCodegen(**kwargs).generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)
    return output_file.read_text()


# 104 characters with the indentation of the init arguments of the submodel class
ARGUMENT_LINE = f"        elementWithAVeryLongNameForTests: Optional[Union[str, {LONG_NAME}]] = None,"


def test_lines_of_up_to_120_characters_are_kept(tmp_path):
    assert ARGUMENT_LINE in generate(tmp_path).splitlines()


@pytest.mark.parametrize("line_length", [88, 100])
def test_line_length_can_be_set(tmp_path, line_length):
    assert ARGUMENT_LINE not in generate(tmp_path, line_length=line_length).splitlines()
