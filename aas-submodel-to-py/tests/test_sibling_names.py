"""Tests for names of sibling elements differing only in trailing numbers.

Trailing numbers are removed from idShorts of elements that may occur several
times, as they mark an example of a repeated element (e.g. `Document01`).
Siblings like `AddressLine1`, `AddressLine2` and `AddressLine3` are different
elements though, which used to be mapped to the same argument name, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/19

Elements that occur once keep their numbers (#41).
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen
from aas_submodel_to_py.util import NamingGenerator

SUBMODEL_ID = "https://example.com/ids/sm/sibling-test"


def optional():
    return [model.Qualifier("SMT/Cardinality", str, value="ZeroToOne")]


def several():
    return [model.Qualifier("SMT/Cardinality", str, value="ZeroToMany")]


def collection(*id_shorts, qualifier=optional):
    elements = [model.Property(id_short=id_short, value_type=str, qualifier=qualifier()) for id_short in id_shorts]
    model.SubmodelElementCollection(id_short="Container", value=elements)
    return elements


@pytest.mark.parametrize("id_shorts, cls_names, arg_names", [
    # Siblings that would collide keep their numbers
    (["AddressLine1", "AddressLine2", "AddressLine3"],
     ["AddressLine1", "AddressLine2", "AddressLine3"], ["addressLine1", "addressLine2", "addressLine3"]),
    (["ProcessInstrumentationFunction_1", "ProcessInstrumentationFunction_2"],
     ["ProcessInstrumentationFunction_1", "ProcessInstrumentationFunction_2"],
     ["processInstrumentationFunction_1", "processInstrumentationFunction_2"]),
    (["PhysicalAddress__0__", "PhysicalAddress__1__"],
     ["PhysicalAddress__0__", "PhysicalAddress__1__"], ["physicalAddress__0__", "physicalAddress__1__"]),
    (["Document", "Document01"], ["Document", "Document01"], ["document", "document01"]),
    (["language1", "Language2"], ["Language1", "Language2"], ["language1", "language2"]),
    # Elements occurring once keep their number (#41)
    (["Document01", "Name"], ["Document01", "Name"], ["document01", "name"]),
])
def test_names_of_siblings(id_shorts, cls_names, arg_names):
    elements = collection(*id_shorts)

    assert [NamingGenerator.create_specific_referable_cls_name(se) for se in elements] == cls_names
    assert [NamingGenerator.create_arg_name_for_referable(se) for se in elements] == arg_names


@pytest.mark.parametrize("id_shorts, cls_names", [
    # Without collision, the number of elements occurring several times is removed
    (["Document01", "Name"], ["Document", "Name"]),
    (["Document01", "Document02"], ["Document01", "Document02"]),
])
def test_names_of_siblings_occurring_several_times(id_shorts, cls_names):
    elements = collection(*id_shorts, qualifier=several)

    assert [NamingGenerator.create_specific_referable_cls_name(se) for se in elements] == cls_names


def test_name_without_parent():
    assert NamingGenerator.create_specific_referable_cls_name(model.Property("Document01", str)) == "Document01"
    assert NamingGenerator.create_specific_referable_cls_name(model.Property("Document01", str, qualifier=several())) == \
        "Document"


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="SiblingTest",
        submodel_element=[
            model.SubmodelElementCollection(
                id_short="Address",
                value=[model.Property(id_short=f"AddressLine{n}", value_type=str, qualifier=optional())
                       for n in (1, 2, 3)],
            ),
            model.Property(id_short="Document01", value_type=str, qualifier=several()),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "sibling_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("sibling_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_siblings_are_separate_arguments(generated_module):
    cls = generated_module.SiblingTest
    address = cls.Address(addressLine1="Musterstrasse 1", addressLine3="c/o Muster AG")
    elements = {se.id_short: se.value for se in address.value}

    assert elements == {"AddressLine1": "Musterstrasse 1", "AddressLine3": "c/o Muster AG"}


def test_default_id_short_without_collision(generated_module):
    # Document01 may occur several times: its number is replaced by an index
    cls = generated_module.SiblingTest
    submodel = cls(id_=SUBMODEL_ID, address=cls.Address(), document=["doc"])

    assert submodel.get_referable("Document0").value == "doc"
