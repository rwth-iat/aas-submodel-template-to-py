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

Modules are generated from every `.json` template published in
[`admin-shell-io/submodel-templates`](https://github.com/admin-shell-io/submodel-templates/tree/main/published)
that contains a submodel (files containing only concept descriptions or a generic form are skipped).
Each module is named after the template and its version, joined with underscores:

| Template | Module |
|---|---|
| `Digital nameplate/3/0/1/...json` | `digital_nameplate_3_0_1` |
| `Handover Documentation/2/0/1/...json` | `handover_documentation_2_0_1` |
| `Contact Information/1/0/...json` | `contact_information_1_0` |

If several templates share the same name and version (e.g. a template and its
`_forAASMetamodelV3.1` variant), the additional modules get a double-underscore
suffix: `contact_information_1_0_1`, `contact_information_1_0_1__1`.

## Usage

```python
from basyx.aas.model import MultiLanguageTextType
from py_aas_submodels.digital_nameplate_3_0_1 import Nameplate

nameplate = Nameplate(
    id_="https://example.com/ids/sm/nameplate-001",
    uRIOfTheProduct="https://www.domain-abc.com/Model-Nr-1234",
    manufacturerName=MultiLanguageTextType({"de": "Muster AG"}),
    manufacturerProductDesignation=MultiLanguageTextType({"en": "ABC-123"}),
    addressInformation=Nameplate.AddressInformation(),
    orderCodeOfManufacturer="ABC-123-XYZ",
    companyLogo=Nameplate.CompanyLogo(value="/aasx/logo.png"),
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

## Regenerating All Published Submodels

Use the repository script to regenerate all submodels from the
`published` directory of
[`admin-shell-io/submodel-templates`](https://github.com/admin-shell-io/submodel-templates):

```bash
python py-aas-submodels/regenerate_submodels.py
```

The script:
- Collects every `.json` template below `published/**`.
- Generates Python classes via `aas-submodel-to-py`.
- Applies file-name normalization/replacement for generated Python modules.
- Skips files without a submodel.
- Logs any conversion failures to `py-aas-submodels/generation_failures.log`.

A GitHub Actions workflow (`.github/workflows/regenerate-submodels.yml`) runs this
automatically whenever files under `aas-submodel-to-py/**` change on `master`, and daily
(on schedule) to pick up newly published submodels.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
