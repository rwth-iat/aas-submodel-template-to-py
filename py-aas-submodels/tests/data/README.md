# Test data

`published/` holds a few submodel templates, which `tests/test_template_conformance.py` compares
with instances of the classes generated from them. They are copies of files in the `published`
directory of [admin-shell-io/submodel-templates](https://github.com/admin-shell-io/submodel-templates)
at commit `f3790038b6c9c2d7e5ebbb4609997468fadf3e85`, licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by the
[Industrial Digital Twin Association (IDTA)](https://industrialdigitaltwin.org/). They are unchanged.

| Template | File |
|---|---|
| Digital Nameplate 3.0.1 | `Digital nameplate/3/0/1/IDTA 02006-3-0-1_Template_Digital Nameplate.json` |
| Carbon Footprint 1.0.2 | `Carbon Footprint/1/0/2/IDTA 02023-1-0-2 _Template_CarbonFootprint.json` |
| Hierarchical Structures enabling Bills of Material 1.1.1 | `Hierarchical Structures enabling Bills of Material/1/1/1/IDTA 02011-1-1-1_Template_HSEBoM.json` |
| Time Series Data 1.1.1 (with operations) | `Time Series Data/1/1/1/IDTA 02008-1-1-1_Template_withOperations_TimeSeriesData.json` |
| Contact Information 1.0.1 | `Contact Information/1/0/1/IDTA 02002-1-0-1_Template_ContactInformation.json` |
| Technical Data 2.0.1 | `Technical_Data/2/0/1/IDTA 02003_2-0-1_Template_TechnicalData.json` |
| Handover Documentation 2.0.1 | `Handover Documentation/2/0/1/IDTA 02004-2-0-1_Template_HandoverDocumentation.json` |

They cover lists (also with the cardinality on the list), entities with nested entities,
operations, elements occurring several times and placeholder elements.

To compare all published templates, set `SUBMODEL_TEMPLATES_DIR` to the `published` directory
of a clone of admin-shell-io/submodel-templates.
