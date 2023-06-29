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
    name='aas-submodel-template-to-py',
    version='0.1.1',
    description='Generate Submodel-Specific classes with filled metainformation derived from submodel templates',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/zrgt/aas-submodel-template-to-py',
    author='Igor Garmaev',
    author_email='garmaev@gmx.net',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license="License :: OSI Approved :: MIT License",
    keywords='aas submodel class code generation python',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=3.7',
    install_requires=['basyx-python-sdk @ git+https://github.com/zrgt/basyx-python-sdk@main', 'jinja2>=3.1.2,<4', 'black'],
    py_modules=['asttp'],
    package_data={'asttp': ['code_templates/*.pyi']},
    entry_points={
        'console_scripts': [
            'submodel_to_code.py = asttp.submodel_to_code:main',
        ],
    })
