# -*- coding: utf-8 -*-

"""
Tests for HTML generator
"""

from fauxfactory import FauxFactory

import unittest


class TestHTML(unittest.TestCase):
    """
    Test HTML generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_html_1(self):
        """
        @Test: Create a random HTML value
        @Feature: HTML Generator
        @Assert: A string at least one character long is generated.
        """

        result = self.factory.generate_html()
        self.assertGreater(len(result), 0,
                           "A valid HTML value was not generated.")
