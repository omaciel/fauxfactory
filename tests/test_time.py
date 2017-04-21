"""Tests for Time generator."""

import datetime

from fauxfactory import gen_time


def test_gen_uuid_1():
    """Create a random UUID value."""
    for _ in range(100):
        assert isinstance(gen_time(), datetime.time)
