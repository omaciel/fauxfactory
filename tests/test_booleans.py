# -*- coding: utf-8 -*-

"""
Tests for all boolean generators
"""

from fauxfactory import FauxFactory

import unittest


class TestBooleans(unittest.TestCase):
    """
    Test boolean generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_boolean_1(self):
        """
        @Test: Create a random boolean value
        @Feature: Boolean Generator
        @Assert: A random boolean value is generated
        """

        for turn in range(100):
            result = self.factory.generate_boolean()
            self.assertIsInstance(result, bool,
                                  "A valid boolean value was not generated.")
