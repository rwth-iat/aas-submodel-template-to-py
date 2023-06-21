"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sub2py',
    version='0.1.1',
    description='Generate Submodel-Specific classes with filled metainformation derived from submodel templates',
    long_description=long_description,
    url='https://github.com/zrgt/sub2py',
    author='Igor Garmaev',
    author_email='garmaev@gmx.net',
    classifiers=[
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="License :: OSI Approved :: MIT License",
    keywords='aas submodel class code generation python',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=3.7',
    install_requires=['git+https://github.com/zrgt/basyx-python-sdk@improve/V30RC02', 'jinja2>=3.1.2,<4', 'black>=23.3.0'],
    py_modules=['sub2py'],
    package_data={'sub2py': ['code_templates/*.pyi']},
    entry_points={
        'console_scripts': [
            'submodel_to_code.py = sub2py.submodel_to_code:main',
        ],
    })
