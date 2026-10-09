"""Tests for generating code from .aasx, .json and .xml files.

Reading AASX files must not use object stores deprecated in the BaSyx Python
SDK, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/25.
Files without submodels, e.g. AASX/XML files of AAS metamodel 3.0, which the
BaSyx Python SDK reads as empty, must raise an error instead of producing a
module without classes, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/29
"""
import importlib.util
import subprocess
import sys
import warnings
import zipfile

import pytest
from basyx.aas import model
from basyx.aas.adapter import aasx
from basyx.aas.adapter.json import write_aas_json_file
from basyx.aas.adapter.xml import write_aas_xml_file

from aas_submodel_to_py import NoSubmodelError, SubmodelCodegen

AAS_ID = "https://example.com/ids/aas/format-test"
SUBMODEL_ID = "https://example.com/ids/sm/format-test"


def write_aasx(path, store):
    with aasx.AASXWriter(path) as writer:
        writer.write_aas(AAS_ID, store, aasx.DictSupplementaryFileContainer())


WRITERS = {
    "aasx": write_aasx,
    "json": write_aas_json_file,
    "xml": write_aas_xml_file,
}


@pytest.fixture(scope="module")
def object_store():
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="FormatTest",
        submodel_element=[model.Property(id_short="Name", value_type=str)],
    )
    aas = model.AssetAdministrationShell(
        asset_information=model.AssetInformation(global_asset_id="https://example.com/ids/asset"),
        id_=AAS_ID,
        submodel={model.ModelReference.from_referable(submodel)},
    )
    return model.DictIdentifiableStore([aas, submodel])


@pytest.mark.parametrize("extension", WRITERS)
def test_generate_from_file(tmp_path, object_store, extension):
    input_file = tmp_path / f"format_test.{extension}"
    WRITERS[extension](input_file, object_store)
    output_file = tmp_path / f"format_test_{extension}.py"

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        SubmodelCodegen().generate_from(input_file, output_file)

    assert not [w for w in caught if issubclass(w.category, DeprecationWarning)]
    spec = importlib.util.spec_from_file_location(f"format_test_{extension}", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    submodel = module.FormatTest(id_=SUBMODEL_ID, name="foo")
    assert submodel.get_referable("Name").value == "foo"


def downgrade_to_metamodel_3_0(path):
    """Rewrite the XML of an .xml or .aasx file to the namespace of AAS metamodel 3.0"""
    def downgrade(xml: bytes) -> bytes:
        return xml.replace(b"https://admin-shell.io/aas/3/1", b"https://admin-shell.io/aas/3/0")

    if path.suffix == ".xml":
        path.write_bytes(downgrade(path.read_bytes()))
        return
    with zipfile.ZipFile(path) as package:
        parts = {info: package.read(info) for info in package.infolist()}
    with zipfile.ZipFile(path, "w") as package:
        for info, data in parts.items():
            package.writestr(info, downgrade(data) if info.filename.endswith(".xml") else data)


@pytest.mark.parametrize("extension", ["aasx", "xml"])
def test_metamodel_3_0_file_raises(tmp_path, object_store, extension):
    input_file = tmp_path / f"format_test.{extension}"
    WRITERS[extension](input_file, object_store)
    downgrade_to_metamodel_3_0(input_file)
    output_file = tmp_path / "format_test.py"

    with pytest.raises(NoSubmodelError, match="metamodel 3.0.*JSON"):
        SubmodelCodegen().generate_from(input_file, output_file)
    assert not output_file.exists()


def test_obj_store_without_submodel_raises(tmp_path):
    output_file = tmp_path / "empty.py"

    with pytest.raises(NoSubmodelError):
        SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore(), output_file)
    assert not output_file.exists()


def test_cli_fails_for_metamodel_3_0_file(tmp_path, object_store):
    input_file = tmp_path / "format_test.aasx"
    write_aasx(input_file, object_store)
    downgrade_to_metamodel_3_0(input_file)
    output_file = tmp_path / "format_test.py"

    result = subprocess.run(
        [sys.executable, "-m", "aas_submodel_to_py.submodel_to_code", "-i", str(input_file), "-o", str(output_file)],
        capture_output=True, text=True)

    assert result.returncode != 0
    assert "metamodel 3.0" in result.stderr
    assert "Traceback" not in result.stderr
    assert not output_file.exists()
