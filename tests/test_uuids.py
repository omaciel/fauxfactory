"""Tests for UUID generator."""

from fauxfactory import gen_uuid
from fauxfactory import gen_alpha


def test_gen_uuid_1():
    """Create a random UUID4 value."""
    for _ in range(100):
        assert gen_uuid()


def test_gen_uuid_start():
    """Create a UUID4 value with a start value and a separator."""
    start = gen_alpha(length=5)
    separator = "_"
    uuid = gen_uuid(start=start, separator=separator)
    assert uuid[: len(start)] == start
    assert uuid[len(start)] == separator
