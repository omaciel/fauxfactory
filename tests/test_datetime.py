# -*- coding: utf-8 -*-

"""Tests for datetime generator."""

import datetime
from fauxfactory import gen_date, gen_datetime
from fauxfactory.constants import MAX_YEARS, MIN_YEARS
from sys import version_info

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class TestDates(unittest.TestCase):
    """
    Test datetime generator
    """

    def test_gen_datetime_1(self):
        """
        @Test: Create a datetime with no arguments
        @Feature: DateTime Generator
        @Assert: Datetime is created with random values
        """

        result = gen_datetime()
        self.assertTrue(
            isinstance(result, datetime.datetime),
            "Data is not instance of datetime.date.")

    def test_gen_datetime_2(self):
        """
        @Test: Create a datetime with only min_date
        @Feature: DateTime Generator
        @Assert: Datetime is created and falls after minimum datetime
        """

        # Today is...
        today = datetime.datetime.now()
        # Five minutes ago
        min_date = today - datetime.timedelta(seconds=5*60)

        for turn in range(10):
            result = gen_datetime(min_date=min_date)
            self.assertTrue(result >= min_date)

    def test_gen_datetime_3(self):
        """
        @Test: Create a datetime with only max_date
        @Feature: DateTime Generator
        @Assert: Datetime is created and falls before minumum datetime
        """

        # Today is...
        today = datetime.datetime.now()
        # Five minutes into the future
        max_date = today + datetime.timedelta(seconds=5*60)

        for turn in range(10):
            result = gen_datetime(max_date=max_date)
            self.assertTrue(result <= max_date)

    def test_gen_datetime_4(self):
        """
        @Test: Create a datetime with a 5-days datetime range
        @Feature: DateTime Generator
        @Assert: Datetime is created and falls within the datetime range
        """

        # Today is...
        today = datetime.datetime.now()
        # Five minutes ago
        min_date = today - datetime.timedelta(seconds=5*60)
        # Five minutes into the future
        max_date = today + datetime.timedelta(seconds=5*60)

        for turn in range(10):
            result = gen_datetime(
                min_date=min_date,
                max_date=max_date
            )
            self.assertTrue(result >= min_date)
            self.assertTrue(result <= max_date)

    def test_gen_datetime_5(self):
        """
        @Test: Create a datetime with min_date = None
        @Feature: DateTime Generator
        @Assert: Datetime is created and falls within the datetime range
        """

        # min_date for the platform
        min_date = (datetime.datetime.now() -
                    datetime.timedelta(365 * MIN_YEARS))
        # max_date = min_date + 1 year
        max_date = min_date + datetime.timedelta(365 * 1)

        for turn in range(20):
            result = gen_datetime(
                min_date=None,
                max_date=max_date
            )
            self.assertTrue(result.year <= max_date.year)
            self.assertTrue(result.year >= min_date.year)

    def test_gen_datetime_6(self):
        """
        @Test: Create a datetime with max_date == None
        @Feature: DateTime Generator
        @Assert: Datetime is after minimum and before system max
        """

        # max_date for the platform
        max_date = (datetime.datetime.now() +
                    datetime.timedelta(365 * MAX_YEARS))
        # min_date  = max_date - 1 year
        min_date = max_date - datetime.timedelta(365 * 1)

        for turn in range(20):
            result = gen_datetime(
                min_date=min_date,
                max_date=None
            )
            self.assertTrue(result.year <= max_date.year, result)
            self.assertTrue(result.year >= min_date.year, result)

    def test_gen_datetime_7(self):
        """
        @Test: Create a datetime with specified datetime ranges
        @Feature: DateTime Generator
        @Assert: Datetime is created and falls in the specified datetime range
        """

        # min_date for the platform
        min_date = (datetime.datetime.now() -
                    datetime.timedelta(365 * MIN_YEARS))
        # max_date for the platform
        max_date = (datetime.datetime.now() +
                    datetime.timedelta(365 * MAX_YEARS))

        for turn in range(20):
            result = gen_datetime(
                min_date=min_date,
                max_date=max_date
            )
            self.assertTrue(result.year <= max_date.year, result)
            self.assertTrue(result.year >= min_date.year, result)

    def test_gen_datetime_8(self):
        """
        @Test: Create a datetime with non-Date arguments
        @Feature: DateTime Generator
        @Assert: Datetime is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_datetime(
                min_date='',
                max_date=''
            )

    def test_gen_datetime_9(self):
        """
        @Test: Create a datetime with non-Date arguments
        @Feature: DateTime Generator
        @Assert: Datetime is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_datetime(
                min_date='abc',
                max_date='def'
            )

    def test_gen_datetime_10(self):
        """
        @Test: Create a datetime with non-Date arguments
        @Feature: DateTime Generator
        @Assert: Datetime is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_datetime(
                min_date=1,
                max_date=1
            )

    def test_gen_datetime_11(self):
        """
        @Test: Create a datetime with non-Date arguments
        @Feature: DateTime Generator
        @Assert: Datetime is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_datetime(
                min_date=(1,),
                max_date=(2, 3, 4)
            )

    def test_gen_datetime_12(self):
        """
        @Test: Create a datetime with non-Date arguments
        @Feature: DateTime Generator
        @Assert: Datetime is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_datetime(
                min_date=['a', 'b'],
                max_date=['c', 'd', 'e']
            )

    def test_gen_datetime_13(self):
        """
        @Test: Create a datetime with min_date > max_date
        @Feature: DateTime Generator
        @Assert: Datetime should not be created due to assertion error
        """

        # Today is...
        today = datetime.datetime.now()
        # Five minutes into the future
        min_date = today + datetime.timedelta(seconds=5*60)

        with self.assertRaises(AssertionError):
            gen_datetime(
                min_date=min_date,
                max_date=today
            )

    def test_gen_date_14(self):
        """
        @Test: max-date must be a Datetime type
        @Feature: DateTime Generator
        @Assert: Datetime should not be created due to value error
        """

        with self.assertRaises(ValueError):
            gen_date(
                min_date=datetime.datetime.now(),
                max_date='foo'
            )
