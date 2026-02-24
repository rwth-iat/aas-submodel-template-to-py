# py-aas-submodels

**py-aas-submodels** is a collection of typed Python classes for AAS submodel templates,
automatically generated from official [IDTA](https://industrialdigitaltwin.org/) templates
using [aas-submodel-to-py](../aas-submodel-to-py/). The classes extend the
[BaSyx Python SDK](https://github.com/eclipse-basyx/basyx-python-sdk) base classes and
pre-fill semantic metadata (semantic IDs, descriptions, qualifiers) from the templates.

## Installation

```bash
pip install py-aas-submodels
```

## Available Submodels

| Module | Class | IDTA Template |
|---|---|---|
| `nameplate_02006_2_0` | `Nameplate` | Digital Nameplate 2.0 |
| `contact_information_02002_1_0` | `ContactInformations` | Contact Information 1.0 |
| `control_component_instance_02016_1_0` | `ControlComponentInstance` | Control Component Instance 1.0 |
| `control_component_type_02015_1_0` | `ControlComponentType` | Control Component Type 1.0 |
| `functional_safety_02014_1_0` | `FunctionalSafety` | Functional Safety 1.0 |
| `handover_documentation_02004_1_2` | `HandoverDocumentation` | Handover Documentation 1.2 |
| `provision_of_simulation_models_02005_1_0` | `SimulationModels` | Provision of Simulation Models 1.0 |
| `reliability_02013_1_0` | `Reliability` | Reliability 1.0 |

## Usage

```python
from basyx.aas.model import Identifier, IdentifierType
from py_aas_submodels.nameplate_02006_2_0 import Nameplate

nameplate = Nameplate(
    identification=Identifier(id_="https://example.com/ids/sm/nameplate-001",
                              id_type=IdentifierType.IRI),
    uRIOfTheProduct="https://www.domain-abc.com/Model-Nr-1234",
    manufacturerName={"de": "Muster AG"},
    manufacturerProductDesignation={"en": "ABC-123"},
    yearOfConstruction="2022",
    contactInformation=Nameplate.ContactInformation(
        nationalCode={"en": "DE"},
        cityTown={"de": "Musterstadt"},
        street={"de": "Musterstrasse 1"},
        zipcode={"de": "12345"},
    ),
)
```

Required arguments are those specified as mandatory in the IDTA template (e.g. `Multiplicity=One`).
Optional submodel elements default to `None` and can be passed as keyword arguments.

## Generating Additional Submodels

To generate classes for your own submodel templates, use the
[aas-submodel-to-py](../aas-submodel-to-py/) code generator:

```bash
pip install aas-submodel-to-py
submodel_to_code -i path/to/template.aasx -o output.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
