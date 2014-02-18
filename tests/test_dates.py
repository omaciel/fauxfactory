# -*- coding: utf-8 -*-

"""
Tests for date generator
"""

from fauxfactory import FauxFactory
from fauxfactory.constants import MAX_YEARS, MIN_YEARS

import datetime
import unittest


class TestDates(unittest.TestCase):
    """
    Test date generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_date_1(self):
        """Create a date with no arguments"""
        result = self.factory.generate_date()
        self.assertTrue(
            isinstance(result, datetime.date),
            "Data is not instance of datetime.date.")

    def test_generate_date_2(self):
        """Create a date with only min_date"""

        # Today is...
        today = datetime.date.today()
        # Five days ago
        min_date = today - datetime.timedelta(5)

        for turn in xrange(10):
            result = self.factory.generate_date(min_date=min_date)
            self.assertTrue(result >= min_date)

    def test_generate_date_3(self):
        """Create a date with only max_date"""

        # Today is...
        today = datetime.date.today()
        # Five days into the future
        max_date = today + datetime.timedelta(5)

        for turn in xrange(10):
            result = self.factory.generate_date(max_date=max_date)
            self.assertTrue(result <= max_date)

    def test_generate_date_4(self):
        """Create a date with both arguments"""

        # Today is...
        today = datetime.date.today()
        # Five days ago
        min_date = today - datetime.timedelta(5)
        # Five days into the future
        max_date = today + datetime.timedelta(5)

        for turn in xrange(10):
            result = self.factory.generate_date(
                min_date=min_date,
                max_date=max_date
            )
            self.assertTrue(result >= min_date)
            self.assertTrue(result <= max_date)

    def test_generate_date_5(self):
        """Create a date with min_date == 'None'"""

        # min_date for the platform
        min_date = (datetime.date.today() -
                    datetime.timedelta(365 * MIN_YEARS))
        # max_date = min_date + 1 year
        max_date = min_date + datetime.timedelta(365 * 1)

        for turn in xrange(20):
            result = self.factory.generate_date(
                min_date=None,
                max_date=max_date
            )
            self.assertTrue(result.year <= max_date.year)
            self.assertTrue(result.year >= min_date.year)

    def test_generate_date_6(self):
        """Create a date with max_date == 'None'"""

        # max_date for the platform
        max_date = (datetime.date.today() +
                    datetime.timedelta(365 * MAX_YEARS))
        # min_date  = max_date - 1 year
        min_date = max_date - datetime.timedelta(365 * 1)

        for turn in xrange(20):
            result = self.factory.generate_date(
                min_date=min_date,
                max_date=None
            )
            self.assertTrue(result.year <= max_date.year, result)
            self.assertTrue(result.year >= min_date.year, result)

    def test_generate_date_7(self):
        """Create a date with both arguments == 'None'"""

        # min_date for the platform
        min_date = (datetime.date.today() -
                    datetime.timedelta(365 * MIN_YEARS))
        # max_date for the platform
        max_date = (datetime.date.today() +
                    datetime.timedelta(365 * MAX_YEARS))

        for turn in xrange(20):
            result = self.factory.generate_date(
                min_date=min_date,
                max_date=max_date
            )
            self.assertTrue(result.year <= max_date.year, result)
            self.assertTrue(result.year >= min_date.year, result)

    def test_generate_date_8(self):
        """Create a date with non-Date arguments"""

        with self.assertRaises(ValueError):
            self.factory.generate_date(
                min_date='',
                max_date=''
            )
            self.factory.generate_date(
                min_date='abc',
                max_date='def'
            )
            self.factory.generate_date(
                min_date=1,
                max_date=1
            )
            self.factory.generate_date(
                min_date=(1,),
                max_date=(2, 3, 4)
            )
            self.factory.generate_date(
                min_date=['a', 'b'],
                max_date=['c', 'd', 'e']
            )

    def test_generate_date_9(self):
        """Create a date with min_date > max_date"""

        # Today is...
        today = datetime.date.today()
        # Five days into the future
        min_date = today + datetime.timedelta(5)

        with self.assertRaises(AssertionError):
            self.factory.generate_date(
                min_date=min_date,
                max_date=today
            )
