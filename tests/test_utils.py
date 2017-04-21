"""Unittests for all methods found in `utils.py`."""
import pytest

from fauxfactory.helpers import is_positive_int


@pytest.mark.parametrize('length', [1, 2, 3, 30, 100])
def test_positive_value(length):
    """Positive values are allowed."""
    assert is_positive_int(length) is None


@pytest.mark.parametrize('length', [-1, -2, -3, -30, -100])
def test_negative_value(length):
    """Negative values are not allowed."""
    with pytest.raises(ValueError):
        is_positive_int(length)


def test_zero_value():
    """Zero is not an allowed value."""
    with pytest.raises(ValueError):
        is_positive_int(0)


def test_none_value():
    """None is not an allowed value."""
    with pytest.raises(ValueError):
        is_positive_int(None)


def test_empty_value():
    """Empty list is not an allowed value."""
    with pytest.raises(ValueError):
        is_positive_int([])


@pytest.mark.parametrize('length', ['a', 'foo', ' ', '1', '0', '-1'])
def test_non_numeric_value(length):
    """Non-numeric values are not allowed."""
    with pytest.raises(ValueError):
        is_positive_int(length)
