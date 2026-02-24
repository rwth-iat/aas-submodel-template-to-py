# aas-submodel-template-to-py

[![PyPI aas-submodel-to-py](https://img.shields.io/pypi/v/aas-submodel-to-py.svg?label=aas-submodel-to-py)](https://pypi.org/project/aas-submodel-to-py/)
[![PyPI py-aas-submodels](https://img.shields.io/pypi/v/py-aas-submodels.svg?label=py-aas-submodels)](https://pypi.org/project/py-aas-submodels/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)

**aas-submodel-template-to-py** is a project providing an automatic Python code generator for Asset Administration
Shell (AAS) submodel templates.

## Packages

| Package | Description |
|---|---|
| [`aas-submodel-to-py`](aas-submodel-to-py/) | Code generator: reads `.aasx` / `.json` / `.xml` AAS files and emits typed Python classes |
| [`py-aas-submodels`](py-aas-submodels/) | Pre-generated classes for 8 official IDTA submodel templates |

Both packages are built on top of the [BaSyx Python SDK](https://github.com/eclipse-basyx/basyx-python-sdk).

## Quick Start

**Use a pre-generated submodel class:**

```bash
pip install py-aas-submodels
```

```python
from py_aas_submodels.nameplate_02006_2_0 import Nameplate
```

**Generate classes from your own template:**

```bash
pip install aas-submodel-to-py
submodel_to_code -i template.aasx -o output.py
```

## Repository Structure

```
aas-submodel-template-to-py/
├── aas-submodel-to-py/          # Code generator (pip install aas-submodel-to-py)
└── py-aas-submodels/      # Pre-generated classes (pip install py-aas-submodels)
```

## Support and Contribution

If you encounter any issues, or want to contribute to the project, feel free to open an issue or a pull request. Your
contributions are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
