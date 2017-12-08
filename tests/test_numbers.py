"""Tests for all number generators."""

import sys
from collections import namedtuple
from functools import partial

import pytest

from fauxfactory.helpers import base_repr, VALID_DIGITS
from fauxfactory import (
    gen_hexadecimal,
    gen_integer,
    gen_number,
    gen_octagonal,
    gen_negative_integer,
    gen_positive_integer,
)


GenFuncDataSet = namedtuple('GenFuncDataSet',
                            ['gen_func', 'expect_type', 'base'])
GenFuncDataSets = [
    GenFuncDataSet(gen_hexadecimal, str, 16),
    GenFuncDataSet(gen_integer, int, 10),
    GenFuncDataSet(gen_octagonal, str, 8),
    GenFuncDataSet(partial(gen_number, base=2), str, 2),
    GenFuncDataSet(partial(gen_number, base=5), str, 5),
    GenFuncDataSet(partial(gen_number, base=19), str, 19)
]


@pytest.mark.parametrize('base', [0, 1])
def test_base_repr_small_base(base):
    """Testing the base_repr helper."""
    with pytest.raises(ValueError):
        base_repr(1, base)


@pytest.mark.parametrize('number, base, result', [
    (10, 10, '10'),
    (1, 2, '1'),
    (7, 6, '11'),
    (16, 8, '20'),
    (3, 3, '10'),
    (21, 20, '11'),
    (123, 12, 'a3'),
    (139, 16, '8b'),
    (0, 10, '0'),
])
def test_base_repr(number, base, result):
    """Return base representation for a number."""
    assert base_repr(number, base) == result


@pytest.mark.parametrize('data_set', GenFuncDataSets)
def test_gen_number_1(data_set):
    """Create a random number with no range limits."""
    result = data_set.gen_func()
    assert isinstance(result, data_set.expect_type)
    assert set(str(result).lower()).issubset(
        set(VALID_DIGITS[:data_set.base] + '-'))


@pytest.mark.parametrize('data_set', GenFuncDataSets)
def test_gen_number_2(data_set):
    """Create a random number with set minimum limit."""
    try:
        # Change system max int to a smaller number
        old_sys_maxsize = sys.maxsize
        sys.maxsize = 5

        for _ in range(10):
            result = int(str(data_set.gen_func(min_value=1)),
                         base=data_set.base)
            assert result <= sys.maxsize
            assert result >= 1
    finally:
        # Reset system max int back to original value
        sys.maxsize = old_sys_maxsize


@pytest.mark.parametrize('data_set', GenFuncDataSets)
def test_gen_number_3(data_set):
    """Create a random number with set maximum limit."""
    try:
        # Change system max int to a smaller number
        old_sys_maxsize = sys.maxsize
        sys.maxsize = 1000
        min_value = - sys.maxsize - 1

        max_value_based = (1000 if data_set.gen_func is gen_integer
                           else base_repr(1000, data_set.base))
        for _ in range(10):
            result = int(str(data_set.gen_func(
                max_value=max_value_based)), base=data_set.base)
            assert result >= min_value
            assert result <= 1000
    finally:
        # Reset system max int back to original value
        sys.maxsize = old_sys_maxsize


@pytest.mark.parametrize('data_set', GenFuncDataSets)
def test_gen_number_4(data_set):
    """Create a random number with set min/max limits."""
    max_value_based = (3000 if data_set.gen_func is gen_integer
                       else base_repr(3000, data_set.base))
    for _ in range(10):
        result = int(str(data_set.gen_func(
            min_value=1, max_value=max_value_based)),
                     base=data_set.base)
        assert result >= 1
        assert result <= 3000


def test_gen_integer_1():
    """Create a random integer with disallowed minimum limit."""
    # This is lower than allowed platform minimum
    low_min = - sys.maxsize - 2

    with pytest.raises(ValueError):
        gen_integer(min_value=low_min)


def test_gen_integer_2():
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
