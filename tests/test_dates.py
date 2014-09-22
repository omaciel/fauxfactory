# -*- coding: utf-8 -*-

"""Tests for date generator."""

from fauxfactory import gen_date
from fauxfactory.constants import MAX_YEARS, MIN_YEARS

import datetime
import unittest


class TestDates(unittest.TestCase):
    """Test date generator."""

    def test_gen_date_1(self):
        """
        @Test: Create a date with no arguments
        @Feature: Date Generator
        @Assert: Date is created with random values.
        """
        result = gen_date()
        self.assertTrue(
            isinstance(result, datetime.date),
            "Data is not instance of datetime.date.")

    def test_gen_date_2(self):
        """
        @Test: Create a date with only min_date
        @Feature: Date Generator
        @Assert: Date should be created and not be before minimum date
        """

        # Today is...
        today = datetime.date.today()
        # Five days ago
        min_date = today - datetime.timedelta(5)

        for turn in range(10):
            result = gen_date(min_date=min_date)
            self.assertTrue(result >= min_date)

    def test_gen_date_3(self):
        """
        @Test: Create a date with only max_date
        @Feature: Date Generator
        @Assert: Date should be created and not be after maximum date
        """

        # Today is...
        today = datetime.date.today()
        # Five days into the future
        max_date = today + datetime.timedelta(5)

        for turn in range(10):
            result = gen_date(max_date=max_date)
            self.assertTrue(result <= max_date)

    def test_gen_date_4(self):
        """
        @Test: Create a date with both arguments
        @Feature: Date Generator
        @Assert: Date should be created and fall within specified range
        """

        # Today is...
        today = datetime.date.today()
        # Five days ago
        min_date = today - datetime.timedelta(5)
        # Five days into the future
        max_date = today + datetime.timedelta(5)

        for turn in range(10):
            result = gen_date(
                min_date=min_date,
                max_date=max_date
            )
            self.assertTrue(result >= min_date)
            self.assertTrue(result <= max_date)

    def test_gen_date_5(self):
        """
        @Test: Create a date with min_date == 'None'
        @Feature: Date Generator
        @Assert: Date should be created and fall before maximum date
        """

        # min_date for the platform
        min_date = (datetime.date.today() -
                    datetime.timedelta(365 * MIN_YEARS))
        # max_date = min_date + 1 year
        max_date = min_date + datetime.timedelta(365 * 1)

        for turn in range(20):
            result = gen_date(
                min_date=None,
                max_date=max_date
            )
            self.assertTrue(result.year <= max_date.year)
            self.assertTrue(result.year >= min_date.year)

    def test_gen_date_6(self):
        """
        @Test: Create a date with max_date == 'None'
        @Feature: Date Generator
        @Assert: Date should be created and fall after minimum date
        """

        # max_date for the platform
        max_date = (datetime.date.today() +
                    datetime.timedelta(365 * MAX_YEARS))
        # min_date  = max_date - 1 year
        min_date = max_date - datetime.timedelta(365 * 1)

        for turn in range(20):
            result = gen_date(
                min_date=min_date,
                max_date=None
            )
            self.assertTrue(result.year <= max_date.year, result)
            self.assertTrue(result.year >= min_date.year, result)

    def test_gen_date_7(self):
        """
        @Test: Create a date with specific date ranges
        @Feature: Date Generator
        @Assert: Date should be created and fall inside the date range
        """

        # min_date for the platform
        min_date = (datetime.date.today() -
                    datetime.timedelta(365 * MIN_YEARS))
        # max_date for the platform
        max_date = (datetime.date.today() +
                    datetime.timedelta(365 * MAX_YEARS))

        for turn in range(20):
            result = gen_date(
                min_date=min_date,
                max_date=max_date
            )
            self.assertTrue(result.year <= max_date.year, result)
            self.assertTrue(result.year >= min_date.year, result)

    def test_gen_date_8(self):
        """
        @Test: Create a date with non-Date arguments
        @Feature: Date Generator
        @Assert: Date should not be created due to value error
        """

        with self.assertRaises(ValueError):
            gen_date(
                min_date='',
                max_date=''
            )

    def test_gen_date_9(self):
        """
        @Test: Create a date with non-Date arguments
        @Feature: Date Generator
        @Assert: Date should not be created due to value error
        """

        with self.assertRaises(ValueError):
            gen_date(
                min_date='abc',
                max_date='def'
            )

    def test_gen_date_10(self):
        """
        @Test: Create a date with non-Date arguments
        @Feature: Date Generator
        @Assert: Date should not be created due to value error
        """

        with self.assertRaises(ValueError):
            gen_date(
                min_date=1,
                max_date=1
            )

    def test_gen_date_11(self):
        """
        @Test: Create a date with non-Date arguments
        @Feature: Date Generator
        @Assert: Date should not be created due to value error
        """

        with self.assertRaises(ValueError):
            gen_date(
                min_date=(1,),
                max_date=(2, 3, 4)
            )

    def test_gen_date_12(self):
        """
        @Test: Create a date with non-Date arguments
        @Feature: Date Generator
        @Assert: Date should not be created due to value error
        """

        with self.assertRaises(ValueError):
            gen_date(
                min_date=['a', 'b'],
                max_date=['c', 'd', 'e']
            )

    def test_gen_date_13(self):
        """
        @Test: Create a date with min_date > max_date
        @Feature: Date Generator
        @Assert: Date should not be created due to assertion error
        """

        # Today is...
        today = datetime.date.today()
        # Five days into the future
        min_date = today + datetime.timedelta(5)

        with self.assertRaises(AssertionError):
            gen_date(
                min_date=min_date,
                max_date=today
            )

    def test_gen_date_14(self):
        """
        @Test: max-date must be a Date type
        @Feature: Date Generator
        @Assert: Date should not be created due to value error
        """

        with self.assertRaises(ValueError):
            gen_date(
                min_date=datetime.date.today(),
                max_date='foo'
            )
