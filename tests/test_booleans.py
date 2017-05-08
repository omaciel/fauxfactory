"""Tests for all boolean generators."""
import pytest

from fauxfactory import gen_boolean


@pytest.mark.parametrize('item', range(10))
def test_gen_boolean(item):
    """Create a random boolean value."""
    assert isinstance(gen_boolean(), bool)
