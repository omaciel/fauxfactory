# -*- coding: utf-8 -*-

"""Tests for all number generators."""

from fauxfactory import (
    gen_integer,
    gen_negative_integer,
    gen_positive_integer,
)

import sys
import unittest


class TestNumbers(unittest.TestCase):
    """Test number generators."""

    def test_gen_integer_1(self):
        """
        @Test: Create a random integer with no range limits
        @Feature: Numbers Generator
        @Assert: A random integer is created
        """

        if sys.version_info[0] == 2:
            integer_types = (int, long,)  # flake8:noqa
        else:
            integer_types = (int,)
        result = gen_integer()
        self.assertTrue(
            isinstance(result, integer_types),
            "A valid integer was not generated."
        )

    def test_gen_integer_2(self):
        """
        @Test: Create a random integer with set minimum limit
        @Feature: Numbers Generator
        @Assert: Integer is created and greater than minimum
        """

        try:
            # Change system max int to a smaller number
            old_sys_maxsize = sys.maxsize
            sys.maxsize = 5

            for turn in range(10):
                result = gen_integer(min_value=1)
                self.assertTrue(
                    result <= sys.maxsize, "Integer is greater than max_value"
                )
                self.assertTrue(
                    result >= 1, "Integer is less than specified minimum"
                )
        finally:
            # Reset system max int back to original value
            sys.maxsize = old_sys_maxsize

    def test_gen_integer_3(self):
        """
        @Test: Create a random integer with set maximum limit
        @Feature: Numbers Generator
        @Assert: Integer is created and less than maximum value
        """

        try:
            # Change system max int to a smaller number
            old_sys_maxsize = sys.maxsize
            sys.maxsize = 5
            min_value = - sys.maxsize - 1

            for turn in range(10):
                result = gen_integer(max_value=1)
                self.assertTrue(
                    result >= min_value, "Integer is less than min_value"
                )
                self.assertTrue(
                    result <= 1, "Integer is greater than specified maximum"
                )
        finally:
            # Reset system max int back to original value
            sys.maxsize = old_sys_maxsize

    def test_gen_integer_4(self):
        """
        @Test: Create a random integer with set min/max limits
        @Feature: Numbers Generator
        @Assert: An integer is created and falls within the specified range
        """

        for turn in range(10):
            result = gen_integer(
                min_value=1, max_value=3)
            self.assertTrue(
                result >= 1, "Integer is less than min_value"
            )
            self.assertTrue(
                result <= 3, "Integer is greater than specified maximum"
            )

    def test_gen_integer_5(self):
        """
        @Test: Create a random integer with disallowed minimum limit
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        # This is lower than allowed platform minimum
        low_min = - sys.maxsize - 2

        with self.assertRaises(ValueError):
            gen_integer(min_value=low_min)

    def test_gen_integer_6(self):
        """
        @Test: Create a random integer with disallowed maximum limit
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        # This is greater than allowed platform maximum
        high_max = sys.maxsize + 1

        with self.assertRaises(ValueError):
            gen_integer(max_value=high_max)

    def test_gen_integer_7_0(self):
        """
        @Test: Create a random integer using empty strings as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(min_value='')

    def test_gen_integer_7_1(self):
        """
        @Test: Create a random integer using empty strings as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(max_value='')

    def test_gen_integer_7_2(self):
        """
        @Test: Create a random integer using empty strings as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(min_value='', max_value='')

    def test_gen_integer_8_0(self):
        """
        @Test: Create a random integer using whitespace as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(min_value=' ')

    def test_gen_integer_8_1(self):
        """
        @Test: Create a random integer using whitespace as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(max_value=' ')

    def test_gen_integer_8_2(self):
        """
        @Test: Create a random integer using whitespace as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(min_value=' ', max_value=' ')

    def test_gen_integer_9_0(self):
        """
        @Test: Create a random integer using alpha strings as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(min_value='a')

    def test_gen_integer_9_1(self):
        """
        @Test: Create a random integer using alpha strings as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(max_value='a')

    def test_gen_integer_9_2(self):
        """
        @Test: Create a random integer using alpha strings as args
        @Feature: Numbers Generator
        @Assert: An integer number is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_integer(min_value='a', max_value='b')

    def test_gen_positive_integer_1(self):
        """
        @Test: Create a random positive integer
        @Feature: Numbers Generator
        @Assert: A positive number is created
        """

        result = gen_positive_integer()

        self.assertTrue(result >= 0, "Generated integer is not positive")

    def test_gen_negative_integer_1(self):
        """
        @Test: Create a random negative integer
        @Feature: Numbers Generator
        @Assert: A negative number is created
        """

        result = gen_negative_integer()

        self.assertTrue(result <= 0, "Generated integer is not negative")
