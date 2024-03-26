"""Check of the __getattr__ of the fauxfactory package.

These tests are heavily just artificial tests to get 100% coverage.
"""

import fauxfactory
import pytest


def test_fauxfactory_getattr():
    """Check __getattr__ returns expected objects."""
    assert fauxfactory.__getattr__('gen_integer') is fauxfactory.gen_integer


def test_fauxfactory_getattr_raises_attributeerror():
    """Check __getattr__ raises AttributeError."""
    with pytest.raises(AttributeError):
        fauxfactory.nonexistentattribute
