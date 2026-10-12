"""Checks for all generated modules of py-aas-submodels, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/28

Modules identical to others are aliases re-exporting their classes, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/55
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


def submodel_classes(module) -> list:
    """Submodel classes generated in `module` or re-exported from the module it's an alias of"""
    return [obj for obj in vars(module).values() if inspect.isclass(obj) and issubclass(obj, model.Submodel)
            and obj.__module__.startswith(f"{py_aas_submodels.__name__}.")]


@pytest.mark.parametrize("module_name", MODULES)
def test_module_defines_submodel_classes(module_name):
    module = importlib.import_module(f"py_aas_submodels.{module_name}")

    assert submodel_classes(module)
    # Aliases re-export all classes of one other module
    assert len({cls.__module__ for cls in submodel_classes(module)}) == 1


def test_identical_modules_are_aliases():
    sources = {}
    for name in MODULES:
        module = importlib.import_module(f"py_aas_submodels.{name}")
        if submodel_classes(module)[0].__module__ != module.__name__:
            continue  # an alias
        source = pathlib.Path(module.__file__).read_text()
        assert source not in sources, f"{name} is identical to {sources.get(source)}"
        sources[source] = name


def test_aliases_reexport_the_same_classes():
    module = importlib.import_module("py_aas_submodels.software_nameplate_1_0_1_metamodel_3_1")
    original = importlib.import_module("py_aas_submodels.software_nameplate_1_0")

    assert module.SoftwareNameplate is original.SoftwareNameplate
    assert module.global_ref is original.global_ref
