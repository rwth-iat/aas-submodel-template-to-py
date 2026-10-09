"""Tests for generating code from .aasx, .json and .xml files.

Reading AASX files must not use object stores deprecated in the BaSyx Python
SDK, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/25
"""
import importlib.util
import warnings

import pytest
from basyx.aas import model
from basyx.aas.adapter import aasx
from basyx.aas.adapter.json import write_aas_json_file
from basyx.aas.adapter.xml import write_aas_xml_file

from aas_submodel_to_py import SubmodelCodegen

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
