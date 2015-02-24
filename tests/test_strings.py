# -*- coding: utf-8 -*-

"""Tests for all string generators."""

import random
import unicodedata
from fauxfactory import (
    gen_alpha,
    gen_alphanumeric,
    gen_cjk,
    gen_cyrillic,
    gen_html,
    gen_latin1,
    gen_numeric_string,
    gen_string,
    gen_utf8,
    _unicode_letters_generator,
)
from sys import version_info

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class TestStrings(unittest.TestCase):
    """Test string generators."""

    def test_gen_alpha_1(self):
        """
        @Test: Create alpha string of varied length
        @Feature: String Generator
        @Assert: Alpha string is created
        """

        result = gen_alpha()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_alpha_2(self):
        """
        @Test: Create alpha string of fixed length
        @Feature: String Generator
        @Assert: Alpha string of fixed length is generated
        """

        for length in range(2, 12, 2):
            result = gen_alpha(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_gen_alpha_3_0(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alpha(length=0)

    def test_gen_alpha_3_1(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alphanumeric(length=0)

    def test_gen_alpha_3_2(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cjk(length=0)

    def test_gen_alpha_3_3(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_latin1(length=0)

    def test_gen_alpha_3_4(self):
        """
        @Test: Create alpha string with zero length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_numeric_string(length=0)

    def test_gen_alpha_4(self):
        """
        @Test: Create alpha string with negative length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alpha(length=-1)

    def test_gen_alpha_5(self):
        """
        @Test: Create alpha string with None length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alpha(length=None)

    def test_gen_alpha_6(self):
        """
        @Test: Create alpha string with empty string length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alpha(length='')

    def test_gen_alpha_7(self):
        """
        @Test: Create alpha string with white space length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alpha(length=' ')

    def test_gen_alpha_8(self):
        """
        @Test: Create alpha string with alpha string length
        @Feature: String Generator
        @Assert: String is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alpha(length='a')

    def test_gen_alpha_9(self):
        """
        @Test: Create alpha string of varied length
        @Feature: String Generator
        @Assert: Alpha string is created
        """

        result = gen_string('alpha', 15)
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_alphanumeric_1(self):
        """
        @Test: Create alphanumeric string of varied length
        @Feature: String Generator
        @Assert: Alphanumeric string is generated
        """

        result = gen_alphanumeric()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_alphanumeric_2(self):
        """
        @Test: Create alphanumeric string of fixed length
        @Feature: String Generator
        @Assert: Alphanumeric string with fixed length is created
        """

        for length in range(2, 12, 2):
            result = gen_alphanumeric(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_gen_alphanumeric_3(self):
        """
        @Test: Create alphanumeric string with zero length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alphanumeric(length=0)

    def test_gen_alphanumeric_4(self):
        """
        @Test: Create alphanumeric string with negative length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alphanumeric(length=-1)

    def test_gen_alphanumeric_5(self):
        """
        @Test: Create alphanumeric string with None length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alphanumeric(length=None)

    def test_gen_alphanumeric_6(self):
        """
        @Test: Create alphanumeric string with empty string length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alphanumeric(length='')

    def test_gen_alphanumeric_7(self):
        """
        @Test: Create alphanumeric string with white space length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alphanumeric(length=' ')

    def test_gen_alphanumeric_8(self):
        """
        @Test: Create alphanumeric string with alpha string length
        @Feature: String Generator
        @Assert: Alphanumeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_alphanumeric(length='a')

    def test_gen_cjk_1(self):
        """
        @Test: Create CJK string of varied length
        @Feature: String Generator
        @Assert: CJK string is generated
        """

        result = gen_cjk()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_cjk_2(self):
        """
        @Test: Create CJK string of fixed length
        @Feature: String Generator
        @Assert: CJK string with fixed length is generated
        """

        for length in range(2, 12, 2):
            result = gen_cjk(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_gen_cjk_3(self):
        """
        @Test: Create CJK string with zero length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cjk(length=0)

    def test_gen_cjk_4(self):
        """
        @Test: Create CJK string with negative length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cjk(length=-1)

    def test_gen_cjk_5(self):
        """
        @Test: Create CJK string with None length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cjk(length=None)

    def test_gen_cjk_6(self):
        """
        @Test: Create CJK string with empty string length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cjk(length='')

    def test_gen_cjk_7(self):
        """
        @Test: Create CJK string with white space length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cjk(length=' ')

    def test_gen_cjk_8(self):
        """
        @Test: Create CJK string with alpha string length
        @Feature: String Generator
        @Assert: CJK string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cjk(length='a')

    def test_gen_cjk_9(self):
        """
        @Test: Create CJK string of varied length
        @Feature: String Generator
        @Assert: CJK string is generated
        """

        result = gen_string('cjk', 15)
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_cyrillic_1(self):
        """
        @Test: Create Cyrillic string of varied length
        @Feature: String Generator
        @Assert: Cyrillic string is generated
        """

        result = gen_cyrillic()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_cyrillic_2(self):
        """
        @Test: Create Cyrillic string of fixed length
        @Feature: String Generator
        @Assert: Cyrillic string with fixed length is generated
        """

        for length in range(2, 12, 2):
            result = gen_cyrillic(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_gen_cyrillic_3(self):
        """
        @Test: Create Cyrillic string with zero length
        @Feature: String Generator
        @Assert: Cyrillic string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cyrillic(length=0)

    def test_gen_cyrillic_4(self):
        """
        @Test: Create Cyrillic string with negative length
        @Feature: String Generator
        @Assert: Cyrillic string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cyrillic(length=-1)

    def test_gen_cyrillic_5(self):
        """
        @Test: Create Cyrillic string with None length
        @Feature: String Generator
        @Assert: Cyrillic string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cyrillic(length=None)

    def test_gen_cyrillic_6(self):
        """
        @Test: Create Cyrillic string with empty string length
        @Feature: String Generator
        @Assert:  Cyrillic string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cyrillic(length='')

    def test_gen_cyrillic_7(self):
        """
        @Test: Create Cyrillic string with white space length
        @Feature: String Generator
        @Assert: Cyrillic string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cyrillic(length=' ')

    def test_gen_cyrillic_8(self):
        """
        @Test: Create Cyrillic string with alpha string length
        @Feature: String Generator
        @Assert: Cyrillic string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_cyrillic(length='a')

    def test_gen_cyrillic_9(self):
        """
        @Test: Create Cyrillic string of varied length
        @Feature: String Generator
        @Assert: Cyrillic string is generated
        """

        result = gen_string('cyrillic', 15)
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_utf8_1(self):
        """
        @Test: Create a unicode string.
        @Feature: String Generator
        @Assert: A unicode string is generated.
        """

        result = gen_string('utf8', 5)
        if version_info[0] == 2:
            self.assertTrue(isinstance(result, unicode))  # flake8:noqa
        else:
            self.assertTrue(isinstance(result, str))

    def test_gen_utf8_2(self):
        """
        @Test: Create a unicode string and specify a length.
        @Feature: String Generator
        @Assert: A unicode string of the specified length is generated.
        """

        length = random.randint(1, 100)
        self.assertEqual(
            len(gen_string('utf8', length)),
            length
        )

    def test_gen_utf8_3(self):
        """
        @Test: Create a unicode string and specify an invalid length.
        @Feature: String Generator
        @Assert: A ``ValueError`` exception is raised.
        """

        with self.assertRaises(ValueError):
            gen_string('utf8', 'foo')

    def test_gen_latin1_1(self):
        """
        @Test: Create latin1 string of varied length
        @Feature: String Generator
        @Assert: Latin1 string is generated
        """

        result = gen_latin1()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_latin1_2(self):
        """
        @Test: Create latin1 string of fixed length
        @Feature: String Generator
        @Assert: Latin1 string with fixed length is created
        """

        for length in range(2, 12, 2):
            result = gen_latin1(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_gen_latin1_3(self):
        """
        @Test: Create latin1 string with zero length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_latin1(length=0)

    def test_gen_latin1_4(self):
        """
        @Test: Create latin1 string with negative length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_latin1(length=-1)

    def test_gen_latin1_5(self):
        """
        @Test: Create latin1 string with None length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_latin1(length=None)

    def test_gen_latin1_6(self):
        """
        @Test: Create latin1 string with empty string length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_latin1(length='')

    def test_gen_latin1_7(self):
        """
        @Test: Create latin1 string with white space length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_latin1(length=' ')

    def test_gen_latin1_8(self):
        """
        @Test: Create latin1 string with alpha string length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_latin1(length='a')

    def test_gen_latin1_9(self):
        """
        @Test: Create latin1 string of varied length
        @Feature: String Generator
        @Assert: Latin1 string is generated
        """

        result = gen_string('latin1', 15)
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_numeric_string_1(self):
        """
        @Test: Create numeric string of varied length
        @Feature: String Generator
        @Assert: Latin1 string is not created due to value error
        """

        result = gen_numeric_string()
        self.assertTrue(
            len(result) > 0, "Empty string was generated")

    def test_gen_numeric_string_2(self):
        """
        @Test: Create numeric string of fixed length
        @Feature: String Generator
        @Assert: Numeric string is created
        """

        for length in range(2, 12, 2):
            result = gen_numeric_string(length)
            self.assertEqual(
                len(result),
                length,
                "Generate string does not have the expected length")

    def test_gen_numeric_string_3(self):
        """
        @Test: Create numeric string with zero length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_numeric_string(length=0)

    def test_gen_numeric_string_4(self):
        """
        @Test: Create numeric string with negative length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_numeric_string(length=-1)

    def test_gen_numeric_string_5(self):
        """
        @Test: Create numeric string with None length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_numeric_string(length=None)

    def test_gen_numeric_string_6(self):
        """
        @Test: Create numeric string with empty string length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_numeric_string(length='')

    def test_gen_numeric_string_7(self):
        """
        @Test: Create numeric string with white space length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_numeric_string(length=' ')

    def test_gen_numeric_string_8(self):
        """
        @Test: Create numeric string with alpha string length
        @Feature: String Generator
        @Assert: Numeric string is not created due to value error
        """

        with self.assertRaises(ValueError):
            gen_numeric_string(length='a')

    def test_gen_string(self):
        """
        @Test: Create alphanumeric string with given length
        @Feature: String Generator
        @Assert: Alphanumeric string is created with size of 15 chars
        """
        alphanumeric_string = gen_string('alphanumeric', 15)
        self.assertEqual(15, len(alphanumeric_string),
                         "Generated string does not have the expected length")

    def test_gen_string2(self):
        """
        @Test: Create alpha string with given length
        @Feature: String generator
        @Assert: Alpha string is not created due to the lack of parameter type
        """
        with self.assertRaises(Exception):
            gen_string('', 15)

    def test_gen_string3(self):
        """
        @Test: Create a numeric string with the given length
        @Feature: String generator
        @Assert: Numeric string is created with size of 20 chars
        """
        numeric_string = gen_string('numeric', 20)
        self.assertEqual(20, len(numeric_string),
                         "Generated string does not have the expected length")

    def test_gen_string4(self):
        """
        @Test: Create a html string with the given length
        @Feature: String generator
        @Assert: HTML string is created and should greater than given length
        """
        html_string = gen_string('html', 10)
        self.assertTrue(len(html_string) > 10,
                        "Generated string does not have the expected length")

    def test_gen_string5(self):
        """@Test: Call ``gen_string`` with an invalid string type.
        @Feature: String generator
        @Assert: ``ValueError`` is raised.
        """
        invalid_string_type = gen_string('alpha', 10)
        with self.assertRaises(ValueError):
            gen_string(invalid_string_type, 10)

    def test_gen_string6(self):
        """
        @Test: Create a numeric string with no length
        @Feature: String generator
        @Assert: Alphanumeric string is created with same size
                 as default string created by gen_alphanumeric()
        """
        alphanumeric_string = gen_string('alphanumeric')
        control_string = gen_alphanumeric()
        self.assertEqual(len(control_string), len(alphanumeric_string),)


class UnicodeLettersGenerator(unittest.TestCase):
    """Test unicode letters generator"""

    def test_chars_in_letters_category(self):
        """@Test: Unicode letters generator generates only unicode letters
        @Feature: String Generator
        @Assert: All generated characters are unicode letters
        """
        # Categories extracted from section 5.5.1 of
        # http://www.unicode.org/reports/tr44/tr44-4.html
        for char in _unicode_letters_generator():
            self.assertIn(
                unicodedata.category(char), ('Lu', 'Ll', 'Lt', 'Lm', 'Lo')
            )
