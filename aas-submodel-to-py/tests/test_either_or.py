"""Regression tests for SMT/EitherOr groups.

Elements with the same SMT/EitherOr value are alternatives, of which only one is used. Generated
classes accepted any number of them, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/45

Passing more than one member of a group raises a ValueError. A value used by a single element
(e.g. a list of values in Safety Instrumented Functions) isn't a group.
"""
import importlib.util

import pytest
from basyx.aas import model

from aas_submodel_to_py import SubmodelCodegen

SUBMODEL_ID = "https://example.com/ids/sm/either-or-test"
TEMPLATE = model.QualifierKind.TEMPLATE_QUALIFIER


def element(id_short, group=None):
    qualifiers = [model.Qualifier("SMT/Cardinality", str, value="ZeroToOne", kind=TEMPLATE)]
    if group is not None:
        qualifiers.append(model.Qualifier("SMT/EitherOr", str, value=group, kind=TEMPLATE))
    return model.Property(id_short, str, qualifier=qualifiers)


@pytest.fixture(scope="module")
def generated_module(tmp_path_factory):
    submodel = model.Submodel(
        id_=SUBMODEL_ID,
        id_short="EitherOrTest",
        submodel_element=[
            model.SubmodelElementCollection("Specification", value=[
                element("Tube", "Shape"), element("RoundBar", "Shape"), element("SheetMetal", "Shape"),
                element("Material"), element("FailureType", "independent failure, common cause failure"),
            ]),
            element("ComponentName", "Component"), element("ComponentId", "Component"),
        ],
    )
    output_file = tmp_path_factory.mktemp("generated") / "either_or_test.py"
    SubmodelCodegen().generate_from_obj_store(model.DictIdentifiableStore([submodel]), output_file)

    spec = importlib.util.spec_from_file_location("either_or_test", output_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def id_shorts(element) -> list:
    children = element.submodel_element if isinstance(element, model.Submodel) else element.value
    return [child.id_short for child in children]


@pytest.mark.parametrize("kwargs", [
    {},
    {"tube": "t"},
    {"roundBar": "r", "material": "steel"},
    {"sheetMetal": "s", "failureType": "independent failure"},
])
def test_one_member_of_a_group_may_be_passed(generated_module, kwargs):
    assert len(id_shorts(generated_module.EitherOrTest.Specification(**kwargs))) == len(kwargs)


def test_several_members_of_a_group_raise(generated_module):
    with pytest.raises(ValueError, match="Only one of tube, roundBar, sheetMetal may be given"):
        generated_module.EitherOrTest.Specification(tube="t", sheetMetal="s")


def test_groups_in_submodels(generated_module):
    cls = generated_module.EitherOrTest

    specification = cls.Specification()

    assert id_shorts(cls(id_=SUBMODEL_ID, specification=specification, componentId="C-1")) == \
        ["Specification", "ComponentId"]
    with pytest.raises(ValueError, match="Only one of componentName, componentId may be given"):
        cls(id_=SUBMODEL_ID, specification=cls.Specification(), componentName="Cell", componentId="C-1")
