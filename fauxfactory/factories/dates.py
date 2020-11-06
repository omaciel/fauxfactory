"""Methods related to generating date/time related values."""

import datetime
import random

from fauxfactory.constants import MAX_YEARS, MIN_YEARS


def gen_date(min_date=None, max_date=None):
    """Return a random date value.

    :param min_date: A valid ``datetime.date`` object.
    :param max_date: A valid ``datetime.date`` object.
    :raises: ``ValueError`` if arguments are not valid ``datetime.date``
        objects.
    :returns: Random ``datetime.date`` object.

    """
    _min_value = (datetime.date.today() -
                  datetime.timedelta(365 * MIN_YEARS))
    _max_value = (datetime.date.today() +
                  datetime.timedelta(365 * MAX_YEARS))

    if min_date is None:
        min_date = _min_value
    if max_date is None:
        max_date = _max_value

    # Validation
    if not isinstance(min_date, datetime.date):
        raise ValueError('%s is not a valid datetime.date object')
    if not isinstance(max_date, datetime.date):
        raise ValueError('%s is not a valid datetime.date object')

    # Check that max_date is not before min_date
    assert min_date < max_date

    random.seed()

    # Pick a day between min and max dates
    diff = max_date - min_date
    days = random.randint(0, diff.days)
    date = min_date + datetime.timedelta(days=days)

    return date


def gen_datetime(min_date=None, max_date=None):
    """Return a random datetime value.

    :param min_date: A valid ``datetime.datetime`` object.
    :param max_date: A valid ``datetime.datetime`` object.
    :raises: ``ValueError`` if arguments are not valid ``datetime.datetime``
        objects.
    :returns: Random ``datetime.datetime`` object.

    """
    _min_value = (datetime.datetime.now() -
                  datetime.timedelta(365 * MIN_YEARS))
    _max_value = (datetime.datetime.now() +
                  datetime.timedelta(365 * MAX_YEARS))

    if min_date is None:
        min_date = _min_value
    if max_date is None:
        max_date = _max_value

    # Validation
    if not isinstance(min_date, datetime.datetime):
        raise ValueError('%s is not a valid datetime.datetime object')
    if not isinstance(max_date, datetime.datetime):
        raise ValueError('%s is not a valid datetime.datetime object')

    # Check that max_date is not before min_date
    assert min_date < max_date

    random.seed()

    # Pick a time between min and max dates
    diff = max_date - min_date
    seconds = random.randint(0, diff.days * 3600 * 24 + diff.seconds)

    return min_date + datetime.timedelta(seconds=seconds)


def gen_time():
    """Generate a random time.

    :returns: A random ``datetime.time`` object.

    """
    random.seed()
    return datetime.time(
        random.randint(0, 23),
        random.randint(0, 59),
        random.randint(0, 59),
        random.randint(0, 999999),
    )


__all__ = tuple(name for name in locals() if name.startswith('gen_'))


def __dir__():
    return __all__
