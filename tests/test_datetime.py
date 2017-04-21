"""Tests for datetime generator."""

import datetime

import pytest

from fauxfactory.constants import MAX_YEARS, MIN_YEARS
from fauxfactory import gen_datetime


def test_gen_datetime_1():
    """Create a datetime with no arguments."""
    assert isinstance(gen_datetime(), datetime.datetime)


def test_gen_datetime_2():
    """Create a datetime with only min_date."""
    # Today is...
    today = datetime.datetime.now()
    # Five minutes ago
    min_date = today - datetime.timedelta(seconds=5*60)

    for _ in range(10):
        assert gen_datetime(min_date=min_date) >= min_date


def test_gen_datetime_3():
    """Create a datetime with only max_date."""
    # Today is...
    today = datetime.datetime.now()
    # Five minutes into the future
    max_date = today + datetime.timedelta(seconds=5*60)

    for _ in range(10):
        assert gen_datetime(max_date=max_date) <= max_date


def test_gen_datetime_4():
    """Create a datetime with a 5-days datetime range."""
    # Today is...
    today = datetime.datetime.now()
    # Five minutes ago
    min_date = today - datetime.timedelta(seconds=5*60)
    # Five minutes into the future
    max_date = today + datetime.timedelta(seconds=5*60)

    for _ in range(10):
        result = gen_datetime(
            min_date=min_date,
            max_date=max_date
        )
        assert result >= min_date
        assert result <= max_date


def test_gen_datetime_5():
    """Create a datetime with min_date = None."""
    # min_date for the platform
    min_date = (datetime.datetime.now() -
                datetime.timedelta(365 * MIN_YEARS))
    # max_date = min_date + 1 year
    max_date = min_date + datetime.timedelta(365 * 1)

    for _ in range(20):
        result = gen_datetime(
            min_date=None,
            max_date=max_date
        )
        assert result.year <= max_date.year
        assert result.year >= min_date.year


def test_gen_datetime_6():
    """Create a datetime with max_date == None."""
    # max_date for the platform
    max_date = (datetime.datetime.now() +
                datetime.timedelta(365 * MAX_YEARS))
    # min_date  = max_date - 1 year
    min_date = max_date - datetime.timedelta(365 * 1)

    for _ in range(20):
        result = gen_datetime(
            min_date=min_date,
            max_date=None
        )
        assert result.year <= max_date.year
        assert result.year >= min_date.year


def test_gen_datetime_7():
    """Create a datetime with specified datetime ranges."""
    # min_date for the platform
    min_date = (datetime.datetime.now() -
                datetime.timedelta(365 * MIN_YEARS))
    # max_date for the platform
    max_date = (datetime.datetime.now() +
                datetime.timedelta(365 * MAX_YEARS))

    for _ in range(20):
        result = gen_datetime(
            min_date=min_date,
            max_date=max_date
        )
        assert result.year <= max_date.year
        assert result.year >= min_date.year


def test_gen_datetime_8():
    """Create a datetime with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_datetime(
            min_date='',
            max_date=''
        )


def test_gen_datetime_9():
    """Create a datetime with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_datetime(
            min_date='abc',
            max_date='def'
        )


def test_gen_datetime_10():
    """Create a datetime with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_datetime(
            min_date=1,
            max_date=1
        )


def test_gen_datetime_11():
    """Create a datetime with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_datetime(
            min_date=(1,),
            max_date=(2, 3, 4)
        )


def test_gen_datetime_12():
    """Create a datetime with non-Date arguments."""
    with pytest.raises(ValueError):
        gen_datetime(
            min_date=['a', 'b'],
            max_date=['c', 'd', 'e']
        )


def test_gen_datetime_13():
    """Create a datetime with min_date > max_date."""
    # Today is...
    today = datetime.datetime.now()
    # Five minutes into the future
    min_date = today + datetime.timedelta(seconds=5*60)

    with pytest.raises(AssertionError):
        gen_datetime(
            min_date=min_date,
            max_date=today
        )


def test_gen_date_14():
    """max-date must be a Datetime type."""
    with pytest.raises(ValueError):
        gen_datetime(
            min_date=datetime.datetime.now(),
            max_date='foo'
        )
