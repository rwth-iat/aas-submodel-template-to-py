"""Clear the ABC caches of the BaSyx classes and of their generated subclasses regularly.

The BaSyx classes are ABCs. A failed isinstance check of an ABC is cached by each of its subclasses, which
are thousands of generated classes if all modules are imported: the caches grow with the square of the
number of generated classes and are never freed, see
https://github.com/rwth-iat/aas-submodel-template-to-py/issues/53
"""
import itertools
import os

import pytest
from basyx.aas import model

# Clearing after each test would recompute the checks too often
CLEAR_ABC_CACHES_EVERY = int(os.environ.get("CLEAR_ABC_CACHES_EVERY", 10))
_tests_run = itertools.count(1)


def subclasses(cls: type) -> set:
    found = set()
    for subclass in cls.__subclasses__():
        found |= {subclass} | subclasses(subclass)
    return found


def clear_abc_caches() -> None:
    for cls in subclasses(model.Referable):
        cls._abc_caches_clear()


@pytest.fixture(autouse=True)
def regularly_clear_abc_caches():
    yield
    if CLEAR_ABC_CACHES_EVERY and next(_tests_run) % CLEAR_ABC_CACHES_EVERY == 0:
        clear_abc_caches()
