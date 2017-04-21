"""Tests related to generator validation methods."""

from unittest import mock

import pytest

from fauxfactory.helpers import check_validation


# pylint: disable=invalid-name
# pylint: disable=E1123

@check_validation
def decorated_f():
    """Simple decorated function to test validation method."""
    return 'not a number'


def test_no_validator_defined():
    """Check result value of decorated function is returned."""
    assert decorated_f() == 'not a number'


def test_validator_defined_with_no_default():
    """Check defining validator but not default raises an error."""
    with pytest.raises(ValueError):
        decorated_f(validator=lambda _: True)


def test_regex():
    """Check regex validation when validator is a string."""
    assert decorated_f(validator=r'\d.*', default='my default') == 'my default'
    assert decorated_f(validator=r'.*', default='my default') == 'not a number'


def test_callable():
    """Check validation when validator is a callable."""
    my_callable = mock.Mock(return_value=False)

    # Default of 10 unsuccessful tries
    assert decorated_f(
        validator=my_callable,
        default='my default') == 'my default'
    my_callable.assert_called_with('not a number')
    assert my_callable.call_count == 10

    # 1 unsuccessful try
    my_callable.reset_mock()
    assert decorated_f(
        validator=my_callable,
        default='my default',
        tries=1) == 'my default'
    my_callable.assert_called_once_with('not a number')

    # 1 successful try
    my_callable.reset_mock()
    my_callable.return_value = True
    assert decorated_f(
        validator=my_callable,
        default='my default',
        tries=10) == 'not a number'
    my_callable.assert_called_once_with('not a number')
