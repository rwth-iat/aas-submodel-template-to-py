"""Checks for all generated modules of py-aas-submodels, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/28
"""
import importlib
import inspect
import pathlib

import pytest
from basyx.aas import model

import py_aas_submodels

MODULES = sorted(
    path.stem for path in pathlib.Path(py_aas_submodels.__file__).parent.glob("*.py")
    if path.stem != "__init__"
)


def test_modules_found():
    assert MODULES


@pytest.mark.parametrize("module_name", MODULES)
def test_module_defines_submodel_classes(module_name):
    module = importlib.import_module(f"py_aas_submodels.{module_name}")

    submodel_classes = [
        obj for obj in vars(module).values()
        if inspect.isclass(obj) and issubclass(obj, model.Submodel) and obj.__module__ == module.__name__
    ]
    assert submodel_classes
