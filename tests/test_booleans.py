"""Tests for all boolean generators."""

from fauxfactory import gen_boolean


def test_gen_boolean():
    """Create a random boolean value."""
    for _ in range(100):
        assert isinstance(gen_boolean(), bool)
