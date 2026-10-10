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
Each module is named after the template, its part (if the template consists of several parts)
and its version, joined with underscores:

| Template file | Module |
|---|---|
| `Digital nameplate/3/0/1/...json` | `digital_nameplate_3_0_1` |
| `Contact Information/1/0/...json` | `contact_information_1_0` |
| `Digital Battery Passport/1_Digital Nameplate/1/0/...json` | `digital_battery_passport_1_digital_nameplate_1_0` |

Variants of a template file get a suffix:

| File name contains | Suffix | Example |
|---|---|---|
| `_forAASMetamodelV3.1` | `_metamodel_3_1` | `contact_information_1_0_1_metamodel_3_1` |
| `_without_examplevalues` | `_without_example_values` | `digital_battery_passport_1_digital_nameplate_1_0_without_example_values` |
| `Example` (instead of `Template`) | `_example` | `fire_protection_on_railway_vehicles_1_0_example` |
| `withOperations` | `_with_operations` | `time_series_data_1_1_1_with_operations` |

If names still collide, the additional modules get a double-underscore counter (`__1`, `__2`, ...).

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
(on schedule) to pick up newly published submodels. It commits the
regenerated modules only if all [tests](#running-tests) pass.

## Running Tests

The tests check that every module imports and defines a submodel class, and that instances of the
generated classes are valid AAS: they are serialized to JSON and XML with BaSyx, read back without
loss, and verified by [aas-core3.1](https://github.com/eclipse-aascw/aas-core3.1-python), an AAS SDK
independent of BaSyx:

```bash
pip install -e "./py-aas-submodels[test]"
python -m pytest py-aas-submodels/tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
