# -*- coding: utf-8 -*-

"""
Tests for UUID generator
"""

from fauxfactory import FauxFactory

import unittest


class TestUUID(unittest.TestCase):
    """
    Test UUID generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_uuid_1(self):
        """
        @Test: Create a random UUID4 value
        @Feature: UUID Generator
        @Assert: A random UUID value is generated
        """

        for turn in range(100):
            result = self.factory.generate_uuid()
            self.assertGreater(len(result), 0,
                               "A valid UUID value was not generated.")
