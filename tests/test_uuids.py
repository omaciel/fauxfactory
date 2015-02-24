# -*- coding: utf-8 -*-

"""Tests for UUID generator."""

from sys import version_info
from fauxfactory import gen_uuid

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class TestUUID(unittest.TestCase):
    """Test UUID generator."""

    def test_gen_uuid_1(self):
        """
        @Test: Create a random UUID4 value
        @Feature: UUID Generator
        @Assert: A random UUID value is generated
        """

        for turn in range(100):
            result = gen_uuid()
            self.assertGreater(
                len(result), 0,
                "A valid UUID value was not generated.")
