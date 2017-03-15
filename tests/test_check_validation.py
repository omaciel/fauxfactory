# -*- coding: utf-8 -*-

from sys import version_info

from fauxfactory import _check_validation

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest
    if version_info[0] == 2:
        from mock import Mock
    else:
        from unittest.mock import Mock


@_check_validation
def decorated_f():
    return 'not a number'


class CheckValidationTestCase(unittest.TestCase):
    """_check_validation decorator tests"""

    def test_no_validator_defined(self):
        """Check result value of decorated function is returned when no
        validator is provided
        """
        self.assertEqual('not a number', decorated_f())

    def test_validator_defined_but_default_is_none(self):
        """Check defining validator but not default raises an error"""
        self.assertRaises(ValueError, decorated_f, validator=lambda _: True)

    def test_regex(self):
        """Check regex validation when validator is a string"""
        self.assertEqual(
            'my default', decorated_f(validator=r'\d.*', default='my default'))
        self.assertEqual(
            'not a number', decorated_f(validator=r'.*', default='my default'))

    def test_callable(self):
        """Check validation when validator is a callable"""
        callable = Mock(return_value=False)

        # Default of 10 unsuccessful tries
        self.assertEqual(
            'my default',
            decorated_f(validator=callable, default='my default')
        )
        callable.assert_called_with('not a number')
        self.assertEqual(10, callable.call_count)

        # 1 unsuccessful try
        callable.reset_mock()
        self.assertEqual(
            'my default',
            decorated_f(validator=callable, default='my default', tries=1)
        )
        callable.assert_called_once_with('not a number')

        # 1 successful try
        callable.reset_mock()
        callable.return_value = True
        self.assertEqual(
            'not a number',
            decorated_f(validator=callable, default='my default', tries=10)
        )
        callable.assert_called_once_with('not a number')
