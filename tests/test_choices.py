# -*- coding: utf-8 -*-

"""
Tests for all choice generators
"""

from fauxfactory import FauxFactory

import string
import unittest


class TestChoices(unittest.TestCase):
    """
    Test choices generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_choice_1(self):
        """Select a random value from integer values"""

        choices = xrange(5)

        for turn in xrange(10):
            result = self.factory.generate_choice(choices)
            self.assertTrue(
                result in choices,
                "An invalid value was selected from available choices.")

    def test_generate_choice_2(self):
        """Select a random value from alphanumeric values"""

        choices = string.ascii_letters + string.digits

        for turn in xrange(10):
            result = self.factory.generate_choice(choices)
            self.assertTrue(
                result in choices,
                "An invalid value was selected from available choices.")

    def test_generate_choice_3(self):
        """Select a random value from short list"""

        choices = [1, ]

        for turn in xrange(10):
            result = self.factory.generate_choice(choices)
            self.assertEqual(
                result,
                choices[0],
                "An invalid value was selected from available choices.")

    def test_generate_choice_4(self):
        """Select a random value from longer list"""

        choices = [1, 2, 3, 9, 10, 11, 100, 101, 102]

        for turn in xrange(10):
            result = self.factory.generate_choice(choices)
            self.assertTrue(
                result in choices,
                "An invalid value was selected from available choices.")

    def test_generate_choice_5(self):
        """Select a random value from short tuple"""

        choices = (1, )

        for turn in xrange(10):
            result = self.factory.generate_choice(choices)
            self.assertEqual(
                result,
                choices[0],
                "An invalid value was selected from available choices.")

    def test_generate_choice_6(self):
        """Select a random value from longer tuple"""

        choices = (1, 2, 3, 9, 10, 11, 100, 101, 102, )

        for turn in xrange(10):
            result = self.factory.generate_choice(choices)
            self.assertTrue(
                result in choices,
                "An invalid value was selected from available choices.")

    def test_generate_choice_7(self):
        """Select a random value from empty list"""

        choices = []

        with self.assertRaises(ValueError):
            self.factory.generate_choice(choices)

    def test_generate_choice_8(self):
        """Select a random value from empty tuple"""

        choices = ()

        with self.assertRaises(ValueError):
            self.factory.generate_choice(choices)

    def test_generate_choice_9(self):
        """Select a random value from empty dictionary"""

        choices = {}

        with self.assertRaises(ValueError):
            self.factory.generate_choice(choices)

    def test_generate_choice_10(self):
        """Select a random value from single dictionary"""

        choices = {'Name': 'Bob', 'Age': 39}

        with self.assertRaises(ValueError):
            self.factory.generate_choice(choices)

    def test_generate_choice_11(self):
        """Select a random value from dictionary list"""

        choices = [
            {'Name': 'Bob', 'Age': 39},
            {'Name': 'Alice', 'Age': 23},
            {'Name': 'Pete', 'Age': 79},
        ]

        for turn in xrange(10):
            result = self.factory.generate_choice(choices)
            self.assertTrue(
                result in choices,
                "An invalid value was selected from available choices.")
