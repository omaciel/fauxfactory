"""Check of the __dir__ of the fauxfactory modules/packages.

These tests are heavily just artificial tests to get 100% coverage.
"""

from importlib import import_module
from pathlib import Path

import fauxfactory.factories


def check_all_dired_names_are_getattrable(obj):
    """Use dir to list symbol names and check getattr won't raise exception."""
    for symbol_name in dir(obj):
        getattr(obj, symbol_name)


def test_fauxfactory_factories_dir():
    """Check dir of fauxfactory factories."""
    factories_dir = Path(fauxfactory.factories.__file__).parent
    for path in factories_dir.iterdir():
        if path.suffix == ".py" and not path.name.startswith("__"):
            name = f".{path.stem}"
            module = import_module(name, fauxfactory.factories.__package__)
            check_all_dired_names_are_getattrable(module)


def test_fauxfactory_dir():
    """Check dir of fauxfactory itself."""
    check_all_dired_names_are_getattrable(fauxfactory)
