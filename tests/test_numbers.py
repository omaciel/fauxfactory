# -*- coding: utf-8 -*-

"""
Tests for all number generators
"""

from fauxfactory import FauxFactory

import sys
import unittest


class TestNumbers(unittest.TestCase):
    """
    Test number generators
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_integer_1(self):
        """Create a random integer with no range limits"""

        result = self.factory.generate_integer()
        self.assertTrue(
            isinstance(result, int), "A valid integer was not generated.")

    def test_generate_integer_2(self):
        """Create a random integer with set minimum limit"""

        try:
            # Change system max int to a smaller number
            old_sys_maxint = sys.maxint
            sys.maxint = 5

            for turn in xrange(10):
                result = self.factory.generate_integer(min_value=1)
                self.assertTrue(
                    result <= sys.maxint, "Integer is greater than max_value"
                )
                self.assertTrue(
                    result >= 1, "Integer is less than specified minimum"
                )
        finally:
            # Reset system max int back to original value
            sys.maxint = old_sys_maxint

    def test_generate_integer_3(self):
        """Create a random integer with set maximum limit"""

        try:
            # Change system max int to a smaller number
            old_sys_maxint = sys.maxint
            sys.maxint = 5
            min_value = - sys.maxint - 1

            for turn in xrange(10):
                result = self.factory.generate_integer(max_value=1)
                self.assertTrue(
                    result >= min_value, "Integer is less than min_value"
                )
                self.assertTrue(
                    result <= 1, "Integer is greater than specified maximum"
                )
        finally:
            # Reset system max int back to original value
            sys.maxint = old_sys_maxint

    def test_generate_integer_4(self):
        """Create a random integer with set min/max limits"""

        for turn in xrange(10):
            result = self.factory.generate_integer(
                min_value=1, max_value=3)
            self.assertTrue(
                result >= 1, "Integer is less than min_value"
            )
            self.assertTrue(
                result <= 3, "Integer is greater than specified maximum"
            )

    def test_generate_integer_5(self):
        """Create a random integer with disallowed minimum limit"""

        # This is lower than allowed platform minimum
        low_min = - sys.maxint - 2

        with self.assertRaises(ValueError):
            self.factory.generate_integer(min_value=low_min)

    def test_generate_integer_6(self):
        """Create a random integer with disallowed maximum limit"""

        # This is greater than allowed platform maximum
        high_max = sys.maxint + 1

        with self.assertRaises(ValueError):
            self.factory.generate_integer(max_value=high_max)

    def test_generate_integer_7(self):
        """Create a random integer using empty strings as args"""

        with self.assertRaises(ValueError):
            self.factory.generate_integer(min_value='')
            self.factory.generate_integer(max_value='')
            self.factory.generate_integer(min_value='', max_value='')

    def test_generate_integer_8(self):
        """Create a random integer using whitespace as args"""

        with self.assertRaises(ValueError):
            self.factory.generate_integer(min_value=' ')
            self.factory.generate_integer(max_value=' ')
            self.factory.generate_integer(min_value=' ', max_value=' ')

    def test_generate_integer_9(self):
        """Create a random integer using alpha strings as args"""

        with self.assertRaises(ValueError):
            self.factory.generate_integer(min_value='a')
            self.factory.generate_integer(max_value='a')
            self.factory.generate_integer(min_value='a', max_value='b')
