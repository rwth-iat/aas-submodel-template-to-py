# aas-submodel-to-py - AAS Submodel Python Code Generator

**aas-submodel-to-py** is a code generator tool built on top of the
[BaSyx-Python-SDK](https://github.com/eclipse-basyx/basyx-python-sdk).
It is designed to generate Submodel-specific classes and classes for its
submodel elements with filled meta-information derived from submodel templates.
These generated classes act as child classes of the BaSyx-Python-SDK classes and
represent classes of the Asset Administration Shell Metamodel.
The hierarchical structure of the generated submodel-specific class includes
all the required submodel element-specific classes. Input files can be `.aasx`,
`.json`, or `.xml` format.

## Examples

### Example of generated classes

Here's a snippet of a generated Submodel class from
the [DigitalNameplate](https://github.com/admin-shell-io/submodel-templates/tree/main/published/Digital%20nameplate/2/0)
Submodel Template:

```python
class Nameplate(Submodel):
    class ManufacturerName(MultiLanguageProperty):
        def __init__(
                self,
                value: LangStringSet,
                id_short: str = "ManufacturerName",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION,
                             local=True,
                             value="0173-1#02-AAO677#002",
                             id_type=KeyType.IRDI, ),)),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA565#007 manufacturer Note: mandatory property according to EU Machine Directive 2006/42/EC. "}

            if qualifier is None:
                qualifier = {
                    Qualifier(type_="Multiplicity", value_type=str,
                              value="One", value_id=None, semantic_id=None, )
                }

            super().__init__(
                value=value,
                id_short=id_short,
                value_id=value_id,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    ...
```

### Usage Example of the generated class

Here's an example of instantiating the **DigitalNameplate** Submodel:

```python
nameplate = Nameplate(
    identification=Identifier(id_="www.example.com/ids/sm/1234", id_type=IdentifierType.IRI),
    uRIOfTheProduct="https://www.domain-abc.com/Model-Nr-1234/Serial-Nr-5678",
    manufacturerName={'de': 'Muster AG'},
    manufacturerProductDesignation={'en': 'ABC-123'},
    yearOfConstruction="2022",
    contactInformation=Nameplate.ContactInformation(
        nationalCode={'en': 'DE'},
        cityTown={'de': 'Musterstadt'},
        street={'de': 'Musterstrasse 1'},
        zipcode={'de': '12345'})
)
```

All required submodel elements are positional arguments; optional elements default to `None`.
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

## Usage

### Command Line

```bash
# Specify the output file explicitly
submodel_to_code -i /some/path/DigitalNameplate.aasx -o /some/path/output.py

# Let the filename be derived from the input (hyphens/spaces → underscores)
# e.g. IDTA-02006-2-0_Submodel_Digital Nameplate.aasx → IDTA_02006_2_0_Submodel_Digital_Nameplate.py
submodel_to_code -i /some/path/DigitalNameplate.aasx -d /some/path/

# Overwrite an existing output file
submodel_to_code -i /some/path/DigitalNameplate.aasx -o /some/path/output.py --force
```

| Flag | Long form | Description | Required |
|---|---|---|---|
| `-i` | `--aas_path` | Input AAS file (`.aasx`, `.json`, or `.xml`) | Yes |
| `-o` | `--outpath` | Output `.py` file path (mutually exclusive with `-d`) | One of `-o`/`-d` |
| `-d` | `--outdir` | Output directory; filename is derived from the input filename (mutually exclusive with `-o`) | One of `-o`/`-d` |
| `-f` | `--force` | Overwrite the output file if it already exists | No |

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

## Support and Contribution

If you encounter any issues, or want to contribute to the project, feel free to open an issue or a pull request. Your
contributions are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
