"""Tests for all number generators."""

import sys

import pytest

from fauxfactory import (
    gen_integer,
    gen_negative_integer,
    gen_positive_integer,
)


def test_gen_integer_1():
    """Create a random integer with no range limits."""
    integer_types = (int,)
    result = gen_integer()
    assert isinstance(result, integer_types)


def test_gen_integer_2():
    """Create a random integer with set minimum limit."""
    try:
        # Change system max int to a smaller number
        old_sys_maxsize = sys.maxsize
        sys.maxsize = 5

        for _ in range(10):
            result = gen_integer(min_value=1)
            assert result <= sys.maxsize
            assert result >= 1
    finally:
        # Reset system max int back to original value
        sys.maxsize = old_sys_maxsize


def test_gen_integer_3():
    """Create a random integer with set maximum limit."""
    try:
        # Change system max int to a smaller number
        old_sys_maxsize = sys.maxsize
        sys.maxsize = 5
        min_value = - sys.maxsize - 1

        for _ in range(10):
            result = gen_integer(max_value=1)
            assert result >= min_value
            assert result <= 1
    finally:
        # Reset system max int back to original value
        sys.maxsize = old_sys_maxsize


def test_gen_integer_4():
    """Create a random integer with set min/max limits."""
    for _ in range(10):
        result = gen_integer(
            min_value=1, max_value=3)
        assert result >= 1
        assert result <= 3


def test_gen_integer_5():
    """Create a random integer with disallowed minimum limit."""
    # This is lower than allowed platform minimum
    low_min = - sys.maxsize - 2

    with pytest.raises(ValueError):
        gen_integer(min_value=low_min)


def test_gen_integer_6():
    """Create a random integer with disallowed maximum limit."""
    # This is greater than allowed platform maximum
    high_max = sys.maxsize + 1

    with pytest.raises(ValueError):
        gen_integer(max_value=high_max)


def test_gen_integer_7_0():
    """Create a random integer using empty strings as args."""
    with pytest.raises(ValueError):
        gen_integer(min_value='')


def test_gen_integer_7_1():
    """Create a random integer using empty strings as args."""
    with pytest.raises(ValueError):
        gen_integer(max_value='')


def test_gen_integer_7_2():
    """Create a random integer using empty strings as args."""
    with pytest.raises(ValueError):
        gen_integer(min_value='', max_value='')


def test_gen_integer_8_0():
    """Create a random integer using whitespace as args."""
    with pytest.raises(ValueError):
        gen_integer(min_value=' ')


def test_gen_integer_8_1():
    """Create a random integer using whitespace as args."""
    with pytest.raises(ValueError):
        gen_integer(max_value=' ')


def test_gen_integer_8_2():
    """Create a random integer using whitespace as args."""
    with pytest.raises(ValueError):
        gen_integer(min_value=' ', max_value=' ')


def test_gen_integer_9_0():
    """Create a random integer using alpha strings as args."""
    with pytest.raises(ValueError):
        gen_integer(min_value='a')


def test_gen_integer_9_1():
    """Create a random integer using alpha strings as args."""
    with pytest.raises(ValueError):
        gen_integer(max_value='a')


def test_gen_integer_9_2():
    """Create a random integer using alpha strings as args."""
    with pytest.raises(ValueError):
        gen_integer(min_value='a', max_value='b')


def test_gen_positive_integer_1():
    """Create a random positive integer."""
    assert gen_positive_integer() >= 0


def test_gen_negative_integer_1():
    """Create a random negative integer."""
    assert gen_negative_integer() <= 0
