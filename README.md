# aas-submodel-template-to-py - AAS Submodel Python Code Generator

**aas-submodel-template-to-py** is a code generator tool built on top of the 
[BaSyx-Python-SDK](https://github.com/eclipse-basyx/basyx-python-sdk). 
It is designed to generate Submodel-specific classes and classes for its 
submodel elements with filled meta-information derived from submodel templates. 
These generated classes act as child classes of the BaSyx-Python-SDK classes and 
represent classes of the Asset Administration Shell Metamodel. 
The hierarchical structure of the generated submodel-specific class includes 
all the required submodel element-specific classes.

## Missing Features
aas-submodel-template-to-py currently works only with AAS files that are consistent with the AAS Metamodel V2.0.1. However, we plan to introduce the following improvements:
- Support AAS Metamodel V3.0 
- Simultaneous support for multiple AAS-Metamodel versions 
  - Simultaneous support for multiple basyx-python-sdk versions 

## Examples

### Example of generated classes

Here's a snippet of a generated Submodel class from the [DigitalNameplate](https://github.com/admin-shell-io/submodel-templates/tree/main/published/Digital%20nameplate/2/0) Submodel Template: 
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

Here's an example of instantiating the **DigitalNameplate** Submodel: 
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

To work with the current development version, you can install the package directly from GitHub using Pip's Git feature:
```bash
pip install git+https://github.com/zrgt/aas-submodel-template-to-py.git@master
```

## Usage

To generate code, you need to invoke the ``submodel_to_code.py`` script. If the generated code exists, you need to
specify ``--force`` command-line argument in order to overwrite the existing files.

To generate submodel classes for submodels saved in ``/some/path/DigitalNameplate.aasx`` and output the generated code to ``/some/path/output.py``, run the following command:
```bash
    submodel_to_code.py \
        --aas_path /some/path/DigitalNameplate.aasx \
        --outpath /some/path/output.py
```

Alternatively, you can generate classes using **aas-submodel-template-to-py** in Python scripts as well:
```python
from asttp import SubmodelCodegen

codegen = SubmodelCodegen()
codegen.generate_from(
    input_file="/some/path/DigitalNameplate.aasx",
    output_file="nameplate.py"
)
```

In the code above, `SubmodelCodegen` is the main class that provides the code generation functionality. The `generate_from` method generates Python classes from an AAS file (.AASX, .JSON, .XML). The generated classes are written to a Python file.

## Code Templates

The `code_templates` directory contains the Jinja templates for the classes that will be generated. You can add new templates, modify existing ones, or change the structure of the generated classes according to your requirements.

## Support and Contribution

If you encounter any issues, or want to contribute to the project, feel free to open an issue or a pull request. Your contributions are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
