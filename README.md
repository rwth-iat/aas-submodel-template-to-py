# Sub2Py - AAS Submodel Python Code Generator

**Sub2Py**, built on [BaSyx-Python-SDK](https://github.com/eclipse-basyx/basyx-python-sdk), 
generates Submodel-Specific classes and classes for its submodel elements with filled metainformation
derived from submodel templates. The generated
classes serve as child classes of BaSyx-Python-SDK classes,
representing classes of the Asset Administration Shell Metamodel. 
The generated submodel-specific class has a hierarchical structure where all the required submodel element-specific classes are placed inside it.

## Examples

### Example of generated classes

Snippet of generated Submodel-class from [DigitalNameplate](https://github.com/admin-shell-io/submodel-templates/tree/main/published/Digital%20nameplate/2/0) Submodel-Template 
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
                         id_type=KeyType.IRDI,),)),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {"en": "Note: see also [IRDI] 0112/2///61987#ABA565#007 manufacturer Note: mandatory property according to EU Machine Directive 2006/42/EC. "}

            if qualifier is None:
                qualifier = {
                    Qualifier(type_="Multiplicity", value_type=str,
                              value="One", value_id=None, semantic_id=None,)
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

Instantiation of **DigitalNameplate**-Submodel 
```python
nameplate = Nameplate(
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

## Installation

**Sub2Py** can be installed from PyPI, the Python Package Index, just as nearly every other Python package:
```bash
pip install sub2py
```

For working with the current development version, you can also install the package directly from GitHub, using Pip's Git feature:
```bash
pip install git+https://github.com/zrgt/sub2py.git@main
```

## Usage

To generate code, you need to invoke the ``submodel_to_code.py`` script. If the generated code exists, you need to
specify ``--force`` command-line argument in order to overwrite the existing files.

To generate submodel classes for submodels saved in ``/some/path/DigitalNameplate.aasx``, invoke:

```bash
    submodel_to_code.py \
        --aas_path /some/path/DigitalNameplate.aasx \
        --outpath /some/path/output.py
```

You can also generate classes using **sub2py** in python scripts: 
```python
from sub2py import SubmodelCodegen

codegen = SubmodelCodegen()
codegen.generate_from(
    input_file="/some/path/DigitalNameplate.aasx",
    output_file="nameplate.py"
)
```

In the code above, `SubmodelCodegen` is the main class that provides the code generation functionality. The `generate_from` method generates Python classes from an AAS file (.AASX, .JSON, .XML). The generated classes are written to a Python file.

## Code Templates

- `code_templates`: This directory contains the Jinja templates for the classes that will be generated. You can add and use new templates or modify the existing ones to change the structure of the generated classes.

## Support and Contribution

If you encounter any issues, or want to contribute to the project, feel free to open an issue or a pull request. Your contributions are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
