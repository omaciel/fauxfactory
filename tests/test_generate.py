# -*- coding: utf-8 -*-

"""Tests parametrized string format."""

import re
from fauxfactory import generate
from sys import version_info

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class TestGenerate(unittest.TestCase):
    """Test the formatted string generators."""

    def test_generate_1_empty(self):
        """
        @Test: Create a correct string
        @Feature: Formatted String Generator
        @Assert: A parametrized format string is generated
        """

        self.assertTrue(len(generate("")) == 0)

    def test_generate_2_no_parametrization(self):
        """
        @Test: Create a correct string
        @Feature: Formatted String Generator
        @Assert: A parametrized format string is generated
        """

        self.assertTrue(len(generate("asdf")) == 4)

    def test_generate_3_basic(self):
        """
        @Test: Create a correct string
        @Feature: Formatted String Generator
        @Assert: A parametrized format string is generated
        """

        generated = generate("asdf_{alpha}")
        self.assertTrue(generated.startswith("asdf_"))
        self.assertTrue(re.search(r"_[a-zA-Z]+$", generated) is not None)

    def test_generate_4_param(self):
        """
        @Test: Create a correct string
        @Feature: Formatted String Generator
        @Assert: A parametrized format string is generated
        """

        generated = generate("asdf_{alpha:4}")
        self.assertTrue(generated.startswith("asdf_"))
        self.assertTrue(re.search(r"_[a-zA-Z]{4}$", generated) is not None)

    def test_generate_5_filter(self):
        """
        @Test: Create a correct string
        @Feature: Formatted String Generator
        @Assert: A parametrized format string is generated
        """

        generated = generate("asdf_{alpha|.lower}")
        self.assertTrue(generated.startswith("asdf_"))
        self.assertTrue(re.search(r"_[a-z]+$", generated) is not None)

    def test_generate_6_params_and_filter(self):
        """
        @Test: Create a correct string
        @Feature: Formatted String Generator
        @Assert: A parametrized format string is generated
        """

        generated = generate("asdf_{alpha:5|.lower}")
        self.assertTrue(generated.startswith("asdf_"))
        self.assertTrue(re.search(r"_[a-z]{5}$", generated) is not None)

    def test_generate_7_wrong_field_name(self):
        """
        @Test: Fail on wrong field name
        @Feature: Formatted String Generator
        @Assert: A ValueError is raised
        """

        with self.assertRaises(ValueError):
            generate("{-}")

    def test_generate_8_wrong_generator_name(self):
        """
        @Test: Fail on wrong generator name
        @Feature: Formatted String Generator
        @Assert: A NameError is raised
        """

        with self.assertRaises(NameError):
            generate("{foo}")

    def test_generate_9_nonnumeric_param(self):
        """
        @Test: Pass a non-numeric parameter to the generator
        @Feature: Formatted String Generator
        @Assert: The randomized string is generated
        """

        url = generate("The URL: {url:ftp:subdom:com}")
        self.assertEqual(url, "The URL: ftp://subdom.com")

    def test_generate_10_nonmethod_filter_unsupported(self):
        """
        @Test: Fail on unsupported filter kind
        @Feature: Formatted String Generator
        @Assert: A TypeError is raised
        """

        with self.assertRaises(TypeError):
            generate("{alpha|unsupported}")
