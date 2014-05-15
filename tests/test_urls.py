# -*- coding: utf-8 -*-

"""
Tests for URL generator
"""

import unittest

from fauxfactory import FauxFactory
from fauxfactory.constants import SCHEMES


class TestURLs(unittest.TestCase):
    """
    Test URL generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_url_1(self):
        """
        @Test: Create a random URL
        @Feature: URL Generator
        @Assert:  URL should be created with random values
        """

        for turn in range(10):
            result = self.factory.generate_url()
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(":")[0] in SCHEMES,
                "URL does not start with a valid scheme"
            )

    def test_generate_url_2(self):
        """
        @Test: Create a random URL with http scheme
        @Feature: URL Generator
        @Assert:  URL should be created with \'http\' scheme
        """

        for turn in range(10):
            result = self.factory.generate_url(scheme='http')
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(":")[0] == 'http',
                "URL does not start with http"
            )

    def test_generate_url_3(self):
        """
        @Test: Create a random URL with https scheme
        @Feature: URL Generator
        @Assert: URL should be created with \'https\' scheme
        """

        for turn in range(10):
            result = self.factory.generate_url(scheme='https')
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(":")[0] == 'https',
                "URL does not start with https"
            )

    def test_generate_url_4(self):
        """
        @Test: Create a random URL with ftp scheme
        @Feature: URL Generator
        @Assert: URL should be created with \'ftp\' scheme
        """

        for turn in range(10):
            result = self.factory.generate_url(scheme='ftp')
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(":")[0] == 'ftp',
                "URL does not start with ftp"
            )

    def test_generate_url_5(self):
        """
        @Test: Create a random URL with invalid scheme
        @Feature: URL Generator
        @Assert: URL should be created with a random scheme
        """

        for turn in range(10):
            scheme = self.factory.generate_alphanumeric()
            with self.assertRaises(ValueError):
                self.factory.generate_url(scheme=scheme)

    def test_generate_url_6(self):
        """
        @Test: Create a random URL with valid subdomain
        @Feature: URL Generator
        @Assert: URL should be created with provided subdomain
        """

        for turn in range(10):
            subdomain = self.factory.generate_alphanumeric()
            result = self.factory.generate_url(subdomain=subdomain)
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")

            # Breakdown the generated URL
            scheme_breakdown = result.split("//")
            domain = scheme_breakdown[1].split(".")
            self.assertTrue(
                domain[0] == subdomain
            )

    def test_generate_url_7(self):
        """
        @Test: Create a random URL with empty subdomain
        @Feature: URL Generator
        @Assert: URL should be created with a random subdomain
        """

        result = self.factory.generate_url(subdomain='')
        self.assertTrue(
            len(result) > 0,
            "A valid URL was not generated.")

    def test_generate_url_8(self):
        """
        @Test: Create a random URL with whitespace subdomain
        @Feature: URL Generator
        @Assert: URL should not be created
        """

        with self.assertRaises(ValueError):
            self.factory.generate_url(subdomain=" ")

    def test_generate_url_9(self):
        """
        @Test: Create a random URL with invalid subdomain
        @Feature: URL Generator
        @Assert: URL should not be created
        """

        for turn in range(10):
            subdomain = self.factory.generate_cjk()
            with self.assertRaises(ValueError):
                self.factory.generate_url(subdomain=subdomain)

    def test_generate_url_10(self):
        """
        @Test: Create a random URL with valid TLDS
        @Feature: URL Generator
        @Assert: URL should be created with the TLDS provided
        """

        for turn in range(10):
            tlds = self.factory.generate_alpha(length=3)
            result = self.factory.generate_url(tlds=tlds)
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(".")[-1] == tlds,
                "URL does not have the TLDS specified"
            )

    def test_generate_url_11(self):
        """
        @Test: Create a random URL with numeric TLDS
        @Feature: URL Generator
        @Assert: URL should not be created
        """

        for turn in range(10):
            with self.assertRaises(ValueError):
                tlds = self.factory.generate_numeric_string(length=3)
                self.factory.generate_url(tlds=tlds)

    def test_generate_url_12(self):
        """
        @Test: Create a random URL with whitespace TLDS
        @Feature: URL Generator
        @Assert: URL should not be created
        """

        for turn in range(10):
            with self.assertRaises(ValueError):
                self.factory.generate_url(tlds=" ")
