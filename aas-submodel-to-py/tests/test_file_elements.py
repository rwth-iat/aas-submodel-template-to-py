"""Regression tests for code generation of File and Blob submodel elements.

The BaSyx Python SDK renamed ``File.mime_type``/``Blob.mime_type`` to
``content_type``. Generated classes must use the new attribute name, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/2
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/file-test"


@pytest.fixture(scope="module")
def generated_file(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="FileTest",
        submodel_element=[
            model.File(id_short="Manual", content_type="application/pdf"),
            model.File(id_short="AnyFile", content_type="{arbitrary}"),
            model.Blob(id_short="Thumbnail", content_type="image/png"),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "file_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)
    return output_file


@pytest.fixture(scope="module")
def generated_module(generated_file):
    spec = importlib.util.spec_from_file_location("file_test", generated_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_generated_code_does_not_use_mime_type(generated_file):
    assert "mime_type" not in generated_file.read_text(encoding="utf-8")


def test_file_with_fixed_content_type(generated_module):
    manual = generated_module.FileTest.Manual(value="/aasx/manual.pdf")

    assert isinstance(manual, model.File)
    assert manual.content_type == "application/pdf"
    assert manual.value == "/aasx/manual.pdf"


def test_file_with_arbitrary_content_type_requires_content_type(generated_module):
    any_file = generated_module.FileTest.AnyFile(value="/aasx/photo.jpg", content_type="image/jpeg")

    assert any_file.content_type == "image/jpeg"
    with pytest.raises(TypeError):
        generated_module.FileTest.AnyFile(value="/aasx/photo.jpg")


def test_blob_with_fixed_content_type(generated_module):
    thumbnail = generated_module.FileTest.Thumbnail(value=b"\x89PNG")

    assert isinstance(thumbnail, model.Blob)
    assert thumbnail.content_type == "image/png"
    assert thumbnail.value == b"\x89PNG"


def test_submodel_with_file_elements(generated_module):
    cls = generated_module.FileTest
    submodel = cls(
        id_=SUBMODEL_ID,
        manual=cls.Manual(value="/aasx/manual.pdf"),
        anyFile=cls.AnyFile(value="/aasx/photo.jpg", content_type="image/jpeg"),
        thumbnail=cls.Thumbnail(),
    )

    elements = {se.id_short: se for se in submodel.submodel_element}
    assert elements["Manual"].content_type == "application/pdf"
    assert elements["AnyFile"].content_type == "image/jpeg"
    assert elements["Thumbnail"].content_type == "image/png"
