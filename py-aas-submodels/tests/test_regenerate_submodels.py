"""Tests for the module names assigned by regenerate_submodels.py.

Module names must tell which template part, version and variant they were
generated from, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/31
"""
import importlib.util
import pathlib

import pytest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "regenerate_submodels.py"
spec = importlib.util.spec_from_file_location("regenerate_submodels", SCRIPT)
regenerate_submodels = importlib.util.module_from_spec(spec)
spec.loader.exec_module(regenerate_submodels)

PUBLISHED = pathlib.Path("/templates/published")


@pytest.mark.parametrize("path, module_name", [
    ("Digital nameplate/3/0/1/IDTA 02006-3-0-1_Template_Digital Nameplate.json",
     "digital_nameplate_3_0_1.py"),
    ("Contact Information/1/0/IDTA 02002-1-0_Template_ContactInformation.json",
     "contact_information_1_0.py"),
    # Variants of a template get a suffix
    ("Digital nameplate/3/0/1/IDTA 02006-3-0-1_Template_Digital Nameplate_forAASMetamodelV3.1.json",
     "digital_nameplate_3_0_1_metamodel_3_1.py"),
    ("Time Series Data/1/1/1/IDTA 02008-1-1-1_Template_withOperations_TimeSeriesData_forAASMetamodelV3.1.json",
     "time_series_data_1_1_1_with_operations_metamodel_3_1.py"),
    ("Safety Instrumented Functions/Part 1 Safety Instrumented Function/1/0/"
     "IDTA 02064_Example_SafetyInstrumentedFunction.json",
     "safety_instrumented_functions_part_1_safety_instrumented_function_1_0_example.py"),
    ("Safety Instrumented Functions/Part 1 Safety Instrumented Function/1/0/"
     "IDTA 02064_Template_SafetyInstrumentedFunction.json",
     "safety_instrumented_functions_part_1_safety_instrumented_function_1_0.py"),
    ("Provision of Simulation Models/1/0/IDTA 02005-1-0_GenericForm_ProvisionOfSimulationModels.json",
     "provision_of_simulation_models_1_0_generic_form.py"),
    # Parts of a template are part of the name
    ("Digital Battery Passport/1_Digital Nameplate/1/0/IDTA 02035-1_DBP-Part-1_Digital Nameplate.json",
     "digital_battery_passport_1_digital_nameplate_1_0.py"),
    ("Digital Battery Passport/4_Technical Data/1/0/1/"
     "IDTA 02035-4_DBP-Part-4_TechnicalData_without_examplevalues.json",
     "digital_battery_passport_4_technical_data_1_0_1_without_example_values.py"),
    ("Hierarchical Structures enabling Bills of Material/Extension based on IEC 81346/1/0/2/"
     "IDTA 02011-1-1-2 _Template_BoM_ExtensionbasedonIEC81346.json",
     "hierarchical_structures_enabling_bills_of_material_extension_based_on_iec_81346_1_0_2.py"),
    ("sensor4.0/Part 1 Measurement Value/1/0/IDTA 02057-1-0_Template_Sensor4.0.json",
     "sensor4_0_part_1_measurement_value_1_0.py"),
    # A part repeating the template name isn't repeated in the module name
    ("Digital Product Passport/Digital Product Passport Part-1/1/0/0/IDTA 02068-1-0-0_Template_DPP.json",
     "digital_product_passport_part_1_1_0_0.py"),
])
def test_output_file_name(path, module_name):
    assert regenerate_submodels.output_file_name(PUBLISHED / path, PUBLISHED) == module_name


def test_assign_output_names_counts_remaining_collisions():
    files = [PUBLISHED / "Some Template/1/0/IDTA_A.json",
             PUBLISHED / "Some Template/1/0/IDTA_B.json",
             PUBLISHED / "Some Template/1/0/IDTA_C_forAASMetamodelV3.1.json",
             PUBLISHED / "Some Template/1/0/IDTA_D.json"]

    names = regenerate_submodels.assign_output_names(files, PUBLISHED)

    assert list(names.values()) == ["some_template_1_0.py", "some_template_1_0__1.py",
                                    "some_template_1_0_metamodel_3_1.py", "some_template_1_0__2.py"]
