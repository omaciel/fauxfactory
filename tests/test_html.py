# -*- coding: utf-8 -*-

"""Tests for HTML generator."""

from fauxfactory import gen_html, gen_integer
import re
import sys
import unittest
# (too-many-public-methods) pylint:disable=R0904


class TestHTML(unittest.TestCase):
    """Test HTML generator."""

    @classmethod
    def setUpClass(cls):
        """Instantiate a factory and compile a regex.

        The compiled regex can be used to find the contents of an HTML tag.

        """
        cls.matcher = re.compile('^<.*?>(.*?)</.*>$')

    def test_length_arg_omitted(self):
        """
        @Test: Generate a random HTML tag and provide no value for the
            ``length`` argument.
        @Feature: HTML Generator
        @Assert: The contents of the HTML tag are at least one character long.
        """

        match = self.matcher.search(gen_html())
        self.assertGreaterEqual(len(match.group(1)), 1)

    def test_length_arg_provided(self):
        """
        @Test: Generate a random HTML tag and provide a value for the
            ``length`` argument.
        @Feature: HTML Generator
        @Assert: The contents of the HTML tag are ``length`` characters long.
        """

        length = gen_integer(1, 25)
        match = self.matcher.search(gen_html(length))
        self.assertEqual(len(match.group(1)), length)

    def test_unicode(self):
        """
        @Test: Generate a random HTML tag.
        @Feature: HTML Generator
        @Assert: A unicode string is generated.
        """

        result = gen_html()
        if sys.version_info[0] is 2:
            # (undefined-variable) pylint:disable=E0602
            self.assertIsInstance(result, unicode)  # flake8:noqa
        else:
            self.assertIsInstance(result, str)
