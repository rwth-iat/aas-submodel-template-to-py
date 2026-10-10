# aas-submodel-to-py - AAS Submodel Python Code Generator

**aas-submodel-to-py** is a code generator tool built on top of the
[BaSyx-Python-SDK](https://github.com/eclipse-basyx/basyx-python-sdk).
It is designed to generate Submodel-specific classes and classes for its
submodel elements with filled meta-information derived from submodel templates.
These generated classes act as child classes of the BaSyx-Python-SDK classes and
represent classes of the Asset Administration Shell Metamodel.
The hierarchical structure of the generated submodel-specific class includes
all the required submodel element-specific classes. Input files can be `.aasx`,
`.json`, or `.xml` format (see [Supported Input](#supported-input)).

## Examples

### Example of generated classes

Here's a snippet of the classes generated from the
[Digital Nameplate 3.0.1](https://github.com/admin-shell-io/submodel-templates/tree/main/published/Digital%20nameplate/3/0/1)
submodel template (`...` marks omitted lines). Each submodel element gets a class nested in the class of
its submodel or collection, with the semantic IDs, descriptions and other metadata of the template as defaults.
The classes build instances (`kind=Instance`), so template qualifiers like `SMT/Cardinality`, which are only
allowed in templates, aren't taken over:

```python
from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class Nameplate(aas.Submodel):

    class URIOfTheProduct(aas.Property):
        ...

    class ManufacturerName(aas.MultiLanguageProperty):

        def __init__(
            self,
            value: aas.LangStringSet,
            id_short: Optional[str] = r"ManufacturerName",
            ...
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0112/2///61987#ABA565#009",
                    ),
                ),
                referred_semantic_id=None,
            ),
            ...
        ):
            ...

    ...

    def __init__(
        self,
        id_: str,
        uRIOfTheProduct: Union[xsd.AnyURI, URIOfTheProduct],
        manufacturerName: Union[aas.LangStringSet, ManufacturerName],
        ...
        yearOfConstruction: Optional[Union[str, YearOfConstruction]] = None,
        ...
        markings: Optional[Union[Iterable[Markings.Markings_item], Markings]] = None,
        ...
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        ...
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Contains the nameplate information attached to the product"
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"3",
                revision=r"0",
                ...
                template_id=r"https://admin-shell.io/idta-02006-3-0",
                ...
            )
        ...
```

### Usage Example of the generated class

Here's an example of instantiating the generated `Nameplate` submodel. The classes generated from
Digital Nameplate 3.0.1 are part of [py-aas-submodels](../py-aas-submodels/README.md):

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
    yearOfConstruction="2022",
    serialNumber=Nameplate.SerialNumber("12345678"),
)
```

All required submodel elements are positional arguments; optional elements default to `None`.
Instead of submodel elements (e.g. `Nameplate.SerialNumber("12345678")`), raw values can be passed
(e.g. `yearOfConstruction="2022"`); multi-language values are passed as `MultiLanguageTextType`.
Lists (`SubmodelElementList`) take an iterable of their items or raw values, e.g. `phases=["A1", "B2"]`.
List items have no idShort by default, as it is optional since AAS metamodel 3.1.
The output is auto-formatted with Black.

## Installation

Using PyPI:

```bash
pip install aas-submodel-to-py
```

Or from the repository root:

```bash
pip install -e ./aas-submodel-to-py
```

## Supported Input

| Format | AAS metamodel 3.1 | AAS metamodel 3.0 |
|---|---|---|
| `.json` | ✅ | ✅ |
| `.aasx` | ✅ | ❌ |
| `.xml` | ✅ | ❌ |

Files are read with the BaSyx Python SDK (≥ 2.1.0), which implements AAS metamodel 3.1 and can't
read AASX and XML files of metamodel 3.0. Many templates on the IDTA website are still such files.
For those, use the JSON version of the template, or its `_forAASMetamodelV3.1` variant; both are
published in [admin-shell-io/submodel-templates](https://github.com/admin-shell-io/submodel-templates/tree/main/published).

For such files, as for any file without a submodel, the generator raises a `NoSubmodelError`
(`submodel_to_code` exits with an error message) instead of writing a module.

## Usage

### Command Line

```bash
# Minimal: output .py is generated next to the input file
# e.g. IDTA-02006-2-0_Submodel_Digital Nameplate.aasx → IDTA_02006_2_0_Submodel_Digital_Nameplate.py
submodel_to_code -i /some/path/DigitalNameplate.aasx

# Write to a specific output directory (filename still auto-derived)
submodel_to_code -i /some/path/DigitalNameplate.aasx -d /some/other/path/

# Write to an explicit output file path
submodel_to_code -i /some/path/DigitalNameplate.aasx -o /some/path/output.py

# Overwrite an existing output file
submodel_to_code -i /some/path/DigitalNameplate.aasx --force
```

| Flag | Long form | Description | Required |
|---|---|---|---|
| `-i` | `--aas_path` | Input AAS file (`.aasx`, `.json`, or `.xml`) | Yes |
| `-o` | `--outpath` | Output `.py` file path (mutually exclusive with `-d`) | No |
| `-d` | `--outdir` | Output directory; filename is derived from the input filename (mutually exclusive with `-o`) | No |
| `-f` | `--force` | Overwrite the output file if it already exists | No |

If neither `-o` nor `-d` is given, the output file is written next to the input file with hyphens and spaces in the name replaced by underscores.

If the entry-point is not on PATH, use the module invocation:

```bash
python -m aas_submodel_to_py.submodel_to_code \
    -i /some/path/DigitalNameplate.aasx \
    -o /some/path/output.py
```

### Python API

```python
from aas_submodel_to_py import SubmodelCodegen

codegen = SubmodelCodegen()

# Generate from an AAS file (.aasx, .json, or .xml)
codegen.generate_from(
    input_file="/some/path/DigitalNameplate.aasx",
    output_file="nameplate.py"
)

# If you already have an AAS object store loaded in memory
codegen.generate_from_obj_store(
    obj_store=my_existing_store,
    output_file="output.py"
)
```

## Running Tests

From the repository root:

```bash
pip install -e "./aas-submodel-to-py[test]"
python -m pytest aas-submodel-to-py/tests
```

The [Tests workflow](../.github/workflows/tests.yml) runs these tests, and the import checks of all
modules in [py-aas-submodels](../py-aas-submodels/README.md#running-tests), on Python 3.10 and 3.14
for every push to `master`/`develop` and every pull request.

## Support and Contribution

If you encounter any issues, or want to contribute to the project, feel free to open an issue or a pull request. Your
contributions are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
