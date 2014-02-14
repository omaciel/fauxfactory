# -*- coding: utf-8 -*-

"""
Tests for all string generators
"""

from fauxfactory import FauxFactory

import unittest


class TestStrings(unittest.TestCase):
    """
    Test string generators
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_alpha_1(self):
        """Create alpha string of varied length"""

        result = self.factory.generate_alpha()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_alpha_2(self):
        """Create alpha string of fixed length"""

        for length in xrange(2, 12, 2):
            result = self.factory.generate_alpha(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")
