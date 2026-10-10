"""Check that the examples in the READMEs match the current generator and BaSyx.

The examples showed code of the pre-v3 BaSyx API, which the generator no longer
produces, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/27

The examples use the classes generated from Digital Nameplate 3.0.1, which are
part of py-aas-submodels.
"""
import pathlib
import re

import pytest

pytest.importorskip("py_aas_submodels")
from basyx.aas import model  # noqa: E402

from py_aas_submodels import digital_nameplate_3_0_1  # noqa: E402

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
GENERATOR_README = REPO_ROOT / "aas-submodel-to-py" / "README.md"
LIBRARY_README = REPO_ROOT / "py-aas-submodels" / "README.md"
ROOT_README = REPO_ROOT / "README.md"


def python_blocks(readme: pathlib.Path, heading: str) -> list:
    """Return the Python code blocks in the section of `readme` below `heading`"""
    text = readme.read_text(encoding="utf-8")
    match = re.search(rf"^#+ {re.escape(heading)}\n(.*?)(?=^#+ |\Z)", text, re.MULTILINE | re.DOTALL)
    assert match, f"No section {heading!r} in {readme}"
    return re.findall(r"```python\n(.*?)```", match.group(1), re.DOTALL)


@pytest.mark.parametrize("readme, heading", [
    (GENERATOR_README, "Usage Example of the generated class"),
    (LIBRARY_README, "Usage"),
    (ROOT_README, "Quick Start"),
])
def test_usage_example_runs(readme, heading):
    blocks = python_blocks(readme, heading)
    assert blocks

    namespace = {}
    for block in blocks:
        exec(block, namespace)

    submodels = [obj for obj in namespace.values() if isinstance(obj, model.Submodel)]
    assert all(isinstance(submodel, digital_nameplate_3_0_1.Nameplate) for submodel in submodels)


def test_generated_class_example_is_current_generator_output():
    """The lines of the example (except elisions "...") appear in this order in the generated module"""
    [example] = python_blocks(GENERATOR_README, "Example of generated classes")
    generated_lines = [line.strip() for line in pathlib.Path(digital_nameplate_3_0_1.__file__).read_text().splitlines()]

    position = 0
    for line in example.splitlines():
        line = line.strip()
        if not line or line == "...":
            continue
        assert line in generated_lines[position:], f"{line!r} not found in order in the generated module"
        position = generated_lines.index(line, position) + 1
