# -*- coding: utf-8 -*-

"""
Tests for Email generator
"""

from fauxfactory import FauxFactory

import re
import unittest

REGEX = r"^[a-zA-Z][a-zA-Z-.]*[^.-]@\w*\.[a-zA-Z]{2,3}"


class TestEmails(unittest.TestCase):
    """
    Test Email generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_email_1(self):
        """
        @Test: Create a random email value
        @Feature: Email Generator
        @Assert: A random email value is generated
        """

        # Regex for email validation
        emailinator = re.compile(REGEX)
        for turn in range(100):
            result = self.factory.generate_email()

            self.assertIsNotNone(emailinator.match(result),
                                 "A valid email value was not generated.")
