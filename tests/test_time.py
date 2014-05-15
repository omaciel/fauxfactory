# -*- coding: utf-8 -*-

"""
Tests for Time generator
"""

from fauxfactory import FauxFactory

import unittest
import datetime


class TestTime(unittest.TestCase):
    """
    Test Time generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_uuid_1(self):
        """
        @Test: Create a random UUID value
        @Feature: UUID Generator
        @Assert: A random UUID value is generated
        """

        for turn in range(100):
            result = self.factory.generate_time()
            self.assertIsInstance(result, datetime.time,
                                  "A valid Time value was not generated.")
