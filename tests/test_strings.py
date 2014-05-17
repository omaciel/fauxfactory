# -*- coding: utf-8 -*-

"""
Tests for all string generators
"""

from fauxfactory import FauxFactory
from sys import version_info

import unittest
import random


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
        """
        @Test: Create alpha string of varied length
        @Feature: String Generator
        @Assert: Alpha string is created
        """

        result = self.factory.generate_alpha()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_alpha_2(self):
        """
        @Test: Create alpha string of fixed length
        @Feature: String Generator
        @Assert: Alpha string of fixed length is generated
        """

        for length in range(2, 12, 2):
            result = self.factory.generate_alpha(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_alpha_3_0(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=0)

    def test_generate_alpha_3_1(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=0)

    def test_generate_alpha_3_2(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=0)

    def test_generate_alpha_3_3(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=0)

    def test_generate_alpha_3_4(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=0)

    def test_generate_alpha_4(self):
        """
        @Test: Create alpha string with negative length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=-1)

    def test_generate_alpha_5(self):
        """
        @Test: Create alpha string with None length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=None)

    def test_generate_alpha_6(self):
        """
        @Test: Create alpha string with empty string length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length='')

    def test_generate_alpha_7(self):
        """
        @Test: Create alpha string with white space length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length=' ')

    def test_generate_alpha_8(self):
        """
        @Test: Create alpha string with alpha string length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alpha(length='a')

    def test_generate_alpha_9(self):
        """
        @Test: Create alpha string of varied length
        @Feature: String Generator
        @Assert: Alpha string is created
        """

        result = self.factory.generate_string('alpha', 15)
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_alphanumeric_1(self):
        """
        @Test: Create alphanumeric string of varied length
        @Feature: String Generator
        @Assert: Alphanumeric string is generated
        """

        result = self.factory.generate_alphanumeric()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_alphanumeric_2(self):
        """
        @Test: Create alphanumeric string of fixed length
        @Feature: String Generator
        @Assert: Alphanumeric string with fixed length is created
        """

        for length in range(2, 12, 2):
            result = self.factory.generate_alphanumeric(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_alphanumeric_3(self):
        """
        @Test: Create alphanumeric string with zero length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=0)

    def test_generate_alphanumeric_4(self):
        """
        @Test: Create alphanumeric string with negative length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=-1)

    def test_generate_alphanumeric_5(self):
        """
        @Test: Create alphanumeric string with None length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=None)

    def test_generate_alphanumeric_6(self):
        """
        @Test: Create alphanumeric string with empty string length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length='')

    def test_generate_alphanumeric_7(self):
        """
        @Test: Create alphanumeric string with white space length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length=' ')

    def test_generate_alphanumeric_8(self):
        """
        @Test: Create alphanumeric string with alpha string length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_alphanumeric(length='a')

    def test_generate_cjk_1(self):
        """
        @Test: Create CJK string of varied length
        @Feature: String Generator
        @Assert: CJK string is generated
        """

        result = self.factory.generate_cjk()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_cjk_2(self):
        """
        @Test: Create CJK string of fixed length
        @Feature: String Generator
        @Assert: CJK string with fixed length is generated
        """

        for length in range(2, 12, 2):
            result = self.factory.generate_cjk(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_cjk_3(self):
        """
        @Test: Create CJK string with zero length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=0)

    def test_generate_cjk_4(self):
        """
        @Test: Create CJK string with negative length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=-1)

    def test_generate_cjk_5(self):
        """
        @Test: Create CJK string with None length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=None)

    def test_generate_cjk_6(self):
        """
        @Test: Create CJK string with empty string length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length='')

    def test_generate_cjk_7(self):
        """
        @Test: Create CJK string with white space length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length=' ')

    def test_generate_cjk_8(self):
        """
        @Test: Create CJK string with alpha string length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_cjk(length='a')

    def test_generate_cjk_9(self):
        """
        @Test: Create CJK string of varied length
        @Feature: String Generator
        @Assert: CJK string is generated
        """

        result = self.factory.generate_string('cjk', 15)
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_utf8_1(self):
        """
        @Test: Create a unicode string.
        @Feature: String Generator
        @Assert: A unicode string is generated.
        """

        result = self.factory.generate_string('utf8', 5)
        if version_info[0] == 2:
            self.assertTrue(isinstance(result, unicode))
        else:
            self.assertTrue(isinstance(result, str))

    def test_generate_utf8_2(self):
        """
        @Test: Create a unicode string and specify a length.
        @Feature: String Generator
        @Assert: A unicode string of the specified length is generated.
        """

        length = random.randint(1, 100)
        self.assertEqual(
            len(self.factory.generate_string('utf8', length)),
            length
        )

    def test_generate_utf8_3(self):
        """
        @Test: Create a unicode string and specify an invalid length.
        @Feature: String Generator
        @Assert: A ``ValueError`` exception is raised.
        """

        with self.assertRaises(ValueError):
            self.factory.generate_string('utf8', 'foo')

    def test_generate_latin1_1(self):
        """
        @Test: Create latin1 string of varied length
        @Feature: String Generator
        @Assert: Latin1 string is generated
        """

        result = self.factory.generate_latin1()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_latin1_2(self):
        """
        @Test: Create latin1 string of fixed length
        @Feature: String Generator
        @Assert: Latin1 string with fixed length is created
        """

        for length in range(2, 12, 2):
            result = self.factory.generate_latin1(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_latin1_3(self):
        """
        @Test: Create latin1 string with zero length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=0)

    def test_generate_latin1_4(self):
        """
        @Test: Create latin1 string with negative length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=-1)

    def test_generate_latin1_5(self):
        """
        @Test: Create latin1 string with None length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=None)

    def test_generate_latin1_6(self):
        """
        @Test: Create latin1 string with empty string length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length='')

    def test_generate_latin1_7(self):
        """
        @Test: Create latin1 string with white space length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length=' ')

    def test_generate_latin1_8(self):
        """
        @Test: Create latin1 string with alpha string length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_latin1(length='a')

    def test_generate_latin1_9(self):
        """
        @Test: Create latin1 string of varied length
        @Feature: String Generator
        @Assert: Latin1 string is generated
        """

        result = self.factory.generate_string('latin1', 15)
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_numeric_string_1(self):
        """
        @Test: Create numeric string of varied length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        result = self.factory.generate_numeric_string()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_generate_numeric_string_2(self):
        """
        @Test: Create numeric string of fixed length
        @Feature: String Generator
        @Assert: Numeric string is created
        """

        for length in range(2, 12, 2):
            result = self.factory.generate_numeric_string(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_generate_numeric_string_3(self):
        """
        @Test: Create numeric string with zero length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=0)

    def test_generate_numeric_string_4(self):
        """
        @Test: Create numeric string with negative length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=-1)

    def test_generate_numeric_string_5(self):
        """
        @Test: Create numeric string with None length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=None)

    def test_generate_numeric_string_6(self):
        """
        @Test: Create numeric string with empty string length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length='')

    def test_generate_numeric_string_7(self):
        """
        @Test: Create numeric string with white space length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length=' ')

    def test_generate_numeric_string_8(self):
        """
        @Test: Create numeric string with alpha string length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            self.factory.generate_numeric_string(length='a')

    def test_generate_string(self):
        """
        @Test: Create alphanumeric string with given lenght
        @Feature: String Generator
        @Assert: Alphanumeric string is created with size of 15 chars
        """
        alphanumeric_string = self.factory.generate_string('alphanumeric', 15)
        self.assertEqual(15, len(alphanumeric_string),
                         "Generated string does not have the expected length")

    def test_generate_string2(self):
        """
        @Test: Create alpha string with given length
        @Feature: String generator
        @Assert: Alpha string is not created due to the lack of parameter type
        """
        with self.assertRaises(Exception):
            self.factory.generate_string('', 15)

    def test_generate_string3(self):
        """
        @Test: Create a numeric string with the given length
        @Feature: String generator
        @Assert: Numeric string is created with size of 20 chars
        """
        numeric_string = self.factory.generate_string('numeric', 20)
        self.assertEqual(20, len(numeric_string),
                         "Generated string does not have the expected length")


