"""Tests for date generator."""

import datetime

import pytest

from fauxfactory.constants import MAX_YEARS, MIN_YEARS
from fauxfactory import gen_date


def test_gen_date_1():
    """Create a date with no arguments."""
    result = gen_date()
    assert isinstance(result, datetime.date)


@pytest.mark.parametrize('item', range(10))
def test_gen_date_2(item):
    """Create a date with only min_date."""
    # Today is...
    today = datetime.date.today()
    # Five days ago
    min_date = today - datetime.timedelta(5)

    assert gen_date(min_date=min_date) >= min_date


@pytest.mark.parametrize('item', range(10))
def test_gen_date_3(item):
    """Create a date with only max_date."""
    # Today is...
    today = datetime.date.today()
    # Five days into the future
    max_date = today + datetime.timedelta(5)

    assert gen_date(max_date=max_date) <= max_date


@pytest.mark.parametrize('item', range(10))
def test_gen_date_4(item):
    """Create a date with both arguments."""
    # Today is...
    today = datetime.date.today()
    # Five days ago
    min_date = today - datetime.timedelta(5)
    # Five days into the future
    max_date = today + datetime.timedelta(5)

    result = gen_date(
        min_date=min_date,
        max_date=max_date
    )
    assert result >= min_date
    assert result <= max_date


@pytest.mark.parametrize('item', range(20))
def test_gen_date_5(item):
    """Create a date with min_date == 'None'."""
    # min_date for the platform
    min_date = (datetime.date.today() -
                datetime.timedelta(365 * MIN_YEARS))
    # max_date = min_date + 1 year
    max_date = min_date + datetime.timedelta(365 * 1)

    result = gen_date(
        min_date=None,
        max_date=max_date
    )
    assert result.year <= max_date.year
    assert result.year >= min_date.year


@pytest.mark.parametrize('item', range(20))
def test_gen_date_6(item):
    """Create a date with max_date == 'None'."""
    # max_date for the platform
    max_date = (datetime.date.today() +
                datetime.timedelta(365 * MAX_YEARS))
    # min_date  = max_date - 1 year
    min_date = max_date - datetime.timedelta(365 * 1)

    result = gen_date(
        min_date=min_date,
        max_date=None
    )
    assert result.year <= max_date.year
    assert result.year >= min_date.year


@pytest.mark.parametrize('item', range(20))
def test_gen_date_7(item):
    """Create a date with specific date ranges."""
    # min_date for the platform
    min_date = (datetime.date.today() -
                datetime.timedelta(365 * MIN_YEARS))
    # max_date for the platform
    max_date = (datetime.date.today() +
                datetime.timedelta(365 * MAX_YEARS))

    result = gen_date(
        min_date=min_date,
        max_date=max_date
    )
    assert result.year <= max_date.year
    assert result.year >= min_date.year


def test_gen_date_8():
    """Create a date with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_date(
            min_date='',
            max_date=''
        )


def test_gen_date_9():
    """Create a date with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_date(
            min_date='abc',
            max_date='def'
        )


def test_gen_date_10():
    """Create a date with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_date(
            min_date=1,
            max_date=1
        )


def test_gen_date_11():
    """Create a date with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_date(
            min_date=(1,),
            max_date=(2, 3, 4)
        )


def test_gen_date_12():
    """Create a date with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_date(
            min_date=['a', 'b'],
            max_date=['c', 'd', 'e']
        )


def test_gen_date_13():
    """Create a date with min_date > max_date."""
    # Today is...
    today = datetime.date.today()
    # Five days into the future
    min_date = today + datetime.timedelta(5)

    with pytest.raises(AssertionError):
        gen_date(
            min_date=min_date,
            max_date=today
        )


def test_gen_date_14():
    """max-date must be a Date type."""
    with pytest.raises(ValueError):
        gen_date(
            min_date=datetime.date.today(),
            max_date='foo'
        )
