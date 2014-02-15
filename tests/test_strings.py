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

    def test_generate_alpha_3(self):
        """Create alpha string with zero length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=0)
            self.factory.generate_alphanumeric(length=0)
            self.factory.generate_cjk(length=0)
            self.factory.generate_latin1(length=0)
            self.factory.generate_numeric_string(length=0)

    def test_generate_alpha_4(self):
        """Create alpha string with negative length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=-1)

    def test_generate_alpha_5(self):
        """Create alpha string with None length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=None)

    def test_generate_alpha_6(self):
        """Create alpha string with empty string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length='')

    def test_generate_alpha_7(self):
        """Create alpha string with white space length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=' ')

    def test_generate_alpha_8(self):
        """Create alpha string with alpha string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length='a')

    def test_generate_alphanumeric_1(self):
        """Create alphanumeric string of varied length"""

        result = self.factory.generate_alphanumeric()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_alphanumeric_2(self):
        """Create alphanumeric string of fixed length"""

        for length in xrange(2, 12, 2):
            result = self.factory.generate_alphanumeric(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_alphanumeric_3(self):
        """Create alphanumeric string with zero length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=0)

    def test_generate_alphanumeric_4(self):
        """Create alphanumeric string with negative length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=-1)

    def test_generate_alphanumeric_5(self):
        """Create alphanumeric string with None length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=None)

    def test_generate_alphanumeric_6(self):
        """Create alphanumeric string with empty string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length='')

    def test_generate_alphanumeric_7(self):
        """Create alphanumeric string with white space length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=' ')

    def test_generate_alphanumeric_8(self):
        """Create alphanumeric string with alpha string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length='a')

    def test_generate_cjk_1(self):
        """Create CJK string of varied length"""

        result = self.factory.generate_cjk()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_cjk_2(self):
        """Create CJK string of fixed length"""

        for length in xrange(2, 12, 2):
            result = self.factory.generate_cjk(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_cjk_3(self):
        """Create CJK string with zero length"""

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=0)

    def test_generate_cjk_4(self):
        """Create CJK string with negative length"""

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=-1)

    def test_generate_cjk_5(self):
        """Create CJK string with None length"""

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=None)

    def test_generate_cjk_6(self):
        """Create CJK string with empty string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length='')

    def test_generate_cjk_7(self):
        """Create CJK string with white space length"""

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=' ')

    def test_generate_cjk_8(self):
        """Create CJK string with alpha string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length='a')

    def test_generate_latin1_1(self):
        """Create latin1 string of varied length"""

        result = self.factory.generate_latin1()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_latin1_2(self):
        """Create latin1 string of fixed length"""

        for length in xrange(2, 12, 2):
            result = self.factory.generate_latin1(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_latin1_3(self):
        """Create latin1 string with zero length"""

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=0)

    def test_generate_latin1_4(self):
        """Create latin1 string with negative length"""

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=-1)

    def test_generate_latin1_5(self):
        """Create latin1 string with None length"""

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=None)

    def test_generate_latin1_6(self):
        """Create latin1 string with empty string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length='')

    def test_generate_latin1_7(self):
        """Create latin1 string with white space length"""

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=' ')

    def test_generate_latin1_8(self):
        """Create latin1 string with alpha string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length='a')

    def test_generate_numeric_string_1(self):
        """Create numeric string of varied length"""

        result = self.factory.generate_numeric_string()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_numeric_string_2(self):
        """Create numeric string of fixed length"""

        for length in xrange(2, 12, 2):
            result = self.factory.generate_numeric_string(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_numeric_string_3(self):
        """Create numeric string with zero length"""

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=0)

    def test_generate_numeric_string_4(self):
        """Create numeric string with negative length"""

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=-1)

    def test_generate_numeric_string_5(self):
        """Create numeric string with None length"""

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=None)

    def test_generate_numeric_string_6(self):
        """Create numeric string with empty string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length='')

    def test_generate_numeric_string_7(self):
        """Create numeric string with white space length"""

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=' ')

    def test_generate_numeric_string_8(self):
        """Create numeric string with alpha string length"""

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length='a')
