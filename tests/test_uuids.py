"""Tests for UUID generator."""

from fauxfactory import gen_uuid


def test_gen_uuid_1():
    """Create a random UUID4 value."""
    for _ in range(100):
        assert gen_uuid()
