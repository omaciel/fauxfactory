"""Check of the __dir__ of the fauxfactory modules/packages.

These tests are heavily just artificial tests to get 100% coverage.
"""


import os
import os.path
import fauxfactory.factories
from importlib import import_module


def check_all_dired_names_are_getattrable(obj):
    """Use dir to list symbol names and check getattr won't raise exception."""
    for symbol_name in dir(obj):
        getattr(obj, symbol_name)


def test_fauxfactory_factories_dir():
    """Check dir of fauxfactory factories."""
    for d in os.listdir(os.path.dirname(fauxfactory.factories.__file__)):
        if d.endswith('.py') and not d.startswith('__'):
            name = f'.{d[:-3]}'
            module = import_module(name, fauxfactory.factories.__package__)
            check_all_dired_names_are_getattrable(module)


def test_fauxfactory_dir():
    """Check dir of fauxfactory itself."""
    check_all_dired_names_are_getattrable(fauxfactory)
