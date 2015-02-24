# -*- coding: utf-8 -*-

"""Tests for all choice generators."""

import string
from fauxfactory import gen_choice
from sys import version_info

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class TestChoices(unittest.TestCase):
    """Test choices generator."""

    def test_gen_choice_1(self):
        """
        @Test: Select a random value from integer values
        @Feature: Choice Generator
        @Assert: Selects a random choice from options
        """

        choices = range(5)

        for turn in range(10):
            result = gen_choice(choices)
            self.assertIn(
                result,
                choices,
                "An invalid value was selected from available choices.")

    def test_gen_choice_2(self):
        """
        @Test: Select a random value from alphanumeric values
        @Feature: Choice Generator
        @Assert: Selects a random choice from alphanumeric options
        """

        choices = string.ascii_letters + string.digits

        for turn in range(10):
            result = gen_choice(choices)
            self.assertIn(
                result,
                choices,
                "An invalid value was selected from available choices.")

    def test_gen_choice_3(self):
        """
        @Test: Select a random value from short list
        @Feature: Choice Generator
        @Assert: Selects a random choice from short list
        """

        choices = [1, ]

        for turn in range(10):
            result = gen_choice(choices)
            self.assertEqual(
                result,
                choices[0],
                "An invalid value was selected from available choices.")

    def test_gen_choice_4(self):
        """
        @Test: Select a random value from longer list
        @Feature: Choice Generator
        @Assert: Selects a random choice from longer list
        """

        choices = [1, 2, 3, 9, 10, 11, 100, 101, 102]

        for turn in range(10):
            result = gen_choice(choices)
            self.assertIn(
                result,
                choices,
                "An invalid value was selected from available choices.")

    def test_gen_choice_5(self):
        """
        @Test: Select a random value from short tuple
        @Feature: Choice Generator
        @Assert: Selects a random choice from short tuple
        """

        choices = (1, )

        for turn in range(10):
            result = gen_choice(choices)
            self.assertEqual(
                result,
                choices[0],
                "An invalid value was selected from available choices.")

    def test_gen_choice_6(self):
        """
        @Test: Select a random value from longer tuple
        @Feature: Choice Generator
        @Assert: Selects a random choice from longer tuple
        """

        choices = (1, 2, 3, 9, 10, 11, 100, 101, 102, )

        for turn in range(10):
            result = gen_choice(choices)
            self.assertIn(
                result,
                choices,
                "An invalid value was selected from available choices.")

    def test_gen_choice_7(self):
        """
        @Test: Select a random value from empty list
        @Feature: Choice Generator
        @Assert: No choice from empty list
        """

        choices = []

        with self.assertRaises(ValueError):
            gen_choice(choices)

    def test_gen_choice_8(self):
        """
        @Test: Select a random value from empty tuple
        @Feature: Choice Generator
        @Assert: No choice from empty tuple
        """

        choices = ()

        with self.assertRaises(ValueError):
            gen_choice(choices)

    def test_gen_choice_9(self):
        """
        @Test: Select a random value from empty dictionary
        @Feature: Choice Generator
        @Assert: No choice from empty dictionary
        """

        choices = {}

        with self.assertRaises(ValueError):
            gen_choice(choices)

    def test_gen_choice_10(self):
        """
        @Test: Select a random value from single dictionary
        @Feature: Choice Generator
        @Assert: No choice from single dictionary
        """

        choices = {'Name': 'Bob', 'Age': 39}

        with self.assertRaises(ValueError):
            gen_choice(choices)

    def test_gen_choice_11(self):
        """
        @Test: Select a random value from dictionary list
        @Feature: Choice Generator
        @Assert: Selects a value from a list of dictionaries
        """

        choices = [
            {'Name': 'Bob', 'Age': 39},
            {'Name': 'Alice', 'Age': 23},
            {'Name': 'Pete', 'Age': 79},
        ]

        for turn in range(10):
            result = gen_choice(choices)
            self.assertIn(
                result,
                choices,
                "An invalid value was selected from available choices.")

    def test_gen_choice_12(self):
        """
        @Test: Select a random value from words list
        @Feature: Choice Generator
        @Assert: Selects a random choice from list
        """

        choices = ['green', 'yellow', 'blue' 'white']

        for turn in range(10):
            result = gen_choice(choices)
            self.assertIn(
                result,
                choices,
                "An invalid value was selected from available choices.")

    def test_gen_choice_13(self):
        """
        @Test: Cannot use None for Choice generator
        @Feature: Choice Generator
        @Assert: ValueError is raised
        """

        choices = None

        with self.assertRaises(ValueError):
            gen_choice(choices)
