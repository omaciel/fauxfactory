# -*- coding: utf-8 -*-

"""
Tests for MAC generator
"""

from fauxfactory import FauxFactory

import random
import re
import string
import unittest

mac = re.compile("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$")


class TestMacs(unittest.TestCase):
    """
    Test MAC generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_mac_1(self):
        """
        @Test: Generate a MAC address using \":\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is generated using \":\" as the delimiter
        """

        result = self.factory.generate_mac()
        self.assertTrue(
            len(result.split(":")) == 6,
            "Did not generate a MAC addrss")
        self.assertIsNotNone(
            mac.match(result),
            "Did not match regular expression for MAC address")

    def test_generate_mac_2(self):
        """
        @Test: Generate a MAC address using \":\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is generated using \":\" as the delimiter
        """

        result = self.factory.generate_mac(delimiter=":")
        self.assertTrue(
            len(result.split(":")) == 6,
            "Did not generate a MAC addrss")
        self.assertIsNotNone(
            mac.match(result),
            "Did not match regular expression for MAC address")

    def test_generate_mac_3(self):
        """
        @Test: Generate a MAC address using \"-\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is generated using \"-\" as the delimiter
        """

        result = self.factory.generate_mac(delimiter="-")
        self.assertTrue(
            len(result.split("-")) == 6,
            "Did not generate a MAC addrss")
        self.assertIsNotNone(
            mac.match(result),
            "Did not match regular expression for MAC address")

    def test_generate_mac_4(self):
        """
        @Test: Generate a MAC address using \".\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            self.factory.generate_mac(delimiter=".")

    def test_generate_mac_5(self):
        """
        @Test: Generate a MAC address using \" \" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            self.factory.generate_mac(delimiter=" ")

    def test_generate_mac_6(self):
        """
        @Test: Generate a MAC address using a number as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            self.factory.generate_mac(delimiter=random.randint(0, 10))

    def test_generate_mac_7(self):
        """
        @Test: Generate a MAC address using a letter as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            self.factory.generate_mac(
                delimiter=random.choice(string.ascii_letters))
