# -*- coding: utf-8 -*-

"""Tests for Time generator."""

import datetime
from sys import version_info
from fauxfactory import gen_time

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class TestTime(unittest.TestCase):
    """Test Time generator."""

    def test_gen_uuid_1(self):
        """
        @Test: Create a random UUID value
        @Feature: UUID Generator
        @Assert: A random UUID value is generated
        """

        for turn in range(100):
            result = gen_time()
            self.assertIsInstance(
                result, datetime.time,
                "A valid Time value was not generated.")
