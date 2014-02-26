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
        """Create a random URL"""

        for turn in xrange(10):
            result = self.factory.generate_url()
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(":")[0] in SCHEMES,
                "URL does not start with a valid scheme"
            )

    def test_generate_url_2(self):
        """Create a random URL with http scheme"""

        for turn in xrange(10):
            result = self.factory.generate_url(scheme='http')
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(":")[0] == 'http',
                "URL does not start with http"
            )

    def test_generate_url_3(self):
        """Create a random URL with https scheme"""

        for turn in xrange(10):
            result = self.factory.generate_url(scheme='https')
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            print result, result.split(":")
            self.assertTrue(
                result.split(":")[0] == 'https',
                "URL does not start with https"
            )

    def test_generate_url_4(self):
        """Create a random URL with ftp scheme"""

        for turn in xrange(10):
            result = self.factory.generate_url(scheme='ftp')
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            self.assertTrue(
                result.split(":")[0] == 'ftp',
                "URL does not start with ftp"
            )

    def test_generate_url_5(self):
        """Create a random URL with invalid scheme"""

        for turn in xrange(10):
            scheme = self.factory.generate_alphanumeric()
            with self.assertRaises(ValueError):
                self.factory.generate_url(scheme=scheme)

    def test_generate_url_6(self):
        """Create a random URL with valid subdomain"""

        for turn in xrange(10):
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
        """Create a random URL with empty subdomain"""

        result = self.factory.generate_url(subdomain='')
        self.assertTrue(
            len(result) > 0,
            "A valid URL was not generated.")

    def test_generate_url_8(self):
        """Create a random URL with whitespace subdomain"""

        with self.assertRaises(ValueError):
            self.factory.generate_url(subdomain=' ')

    def test_generate_url_9(self):
        """Create a random URL with invalid subdomain"""

        for turn in xrange(10):
            subdomain = self.factory.generate_cjk()
            with self.assertRaises(ValueError):
                self.factory.generate_url(subdomain=subdomain)

    def test_generate_url_10(self):
        """Create a random URL with valid TLDS"""

        for turn in xrange(10):
            tlds = self.factory.generate_alpha(length=3)
            result = self.factory.generate_url(tlds=tlds)
            self.assertTrue(
                len(result) > 0,
                "A valid URL was not generated.")
            print result, result.split(":")
            self.assertTrue(
                result.split(":")[-1] == tlds,
                "URL does not have the TLDS specified"
            )

    def test_generate_url_11(self):
        """Create a random URL with numeric TLDS"""

        for turn in xrange(10):
            with self.assertRaises(ValueError):
                tlds = self.factory.generate_numeric(length=3)
                self.factory.generate_url(tlds=tlds)

    def test_generate_url_12(self):
        """Create a random URL with whitespace TLDS"""

        for turn in xrange(10):
            with self.assertRaises(ValueError):
                tlds = self.factory.generate_alpha(length=3)
                self.factory.generate_url(tlds=tlds)
