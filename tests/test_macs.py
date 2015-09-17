# -*- coding: utf-8 -*-

"""Tests for MAC generator."""

import random
import re
import string
from sys import version_info
from fauxfactory import gen_mac

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


mac = re.compile("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$")


class TestMacs(unittest.TestCase):
    """Test MAC generator."""

    def test_gen_mac_1(self):
        """
        @Test: Generate a MAC address using \":\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is generated using \":\" as the delimiter
        """

        result = gen_mac()
        self.assertTrue(
            len(result.split(":")) == 6,
            "Did not generate a MAC addrss")
        self.assertIsNotNone(
            mac.match(result),
            "Did not match regular expression for MAC address")

    def test_gen_mac_2(self):
        """
        @Test: Generate a MAC address using \":\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is generated using \":\" as the delimiter
        """

        result = gen_mac(delimiter=":")
        self.assertTrue(
            len(result.split(":")) == 6,
            "Did not generate a MAC addrss")
        self.assertIsNotNone(
            mac.match(result),
            "Did not match regular expression for MAC address")

    def test_gen_mac_3(self):
        """
        @Test: Generate a MAC address using \"-\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is generated using \"-\" as the delimiter
        """

        result = gen_mac(delimiter="-")
        self.assertTrue(
            len(result.split("-")) == 6,
            "Did not generate a MAC addrss")
        self.assertIsNotNone(
            mac.match(result),
            "Did not match regular expression for MAC address")

    def test_gen_mac_4(self):
        """
        @Test: Generate a MAC address using \".\" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            gen_mac(delimiter=".")

    def test_gen_mac_5(self):
        """
        @Test: Generate a MAC address using \" \" as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            gen_mac(delimiter=" ")

    def test_gen_mac_6(self):
        """
        @Test: Generate a MAC address using a number as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            gen_mac(delimiter=random.randint(0, 10))

    def test_gen_mac_7(self):
        """
        @Test: Generate a MAC address using a letter as the delimiter
        @Feature: MAC Generator
        @Assert: A MAC address is not generated using an invalid delimiter
        """

        with self.assertRaises(ValueError):
            gen_mac(
                delimiter=random.choice(string.ascii_letters))

    def test_gen_mac_unicast_globally_unique(self):
        """
        @Test: Generate a unicast and globally unique MAC address
        @Feature: MAC Generator
        @Assert: A unicast and globally unique MAC address is generated
        """
        mac = gen_mac(multicast=False, locally=False)
        first_octect = int(mac.split(':', 1)[0], 16)
        mask = 0b00000011
        self.assertEqual(first_octect & mask, 0)

    def test_gen_mac_multicast_globally_unique(self):
        """
        @Test: Generate a multicast and globally unique MAC address
        @Feature: MAC Generator
        @Assert: A multicast and globally unique MAC address is generated
        """
        mac = gen_mac(multicast=True, locally=False)
        first_octect = int(mac.split(':', 1)[0], 16)
        mask = 0b00000011
        self.assertEqual(first_octect & mask, 1)

    def test_gen_mac_unicast_locally_administered(self):
        """
        @Test: Generate a unicast and locally administered MAC address
        @Feature: MAC Generator
        @Assert: A unicast and locally administered MAC address is generated
        """
        mac = gen_mac(multicast=False, locally=True)
        first_octect = int(mac.split(':', 1)[0], 16)
        mask = 0b00000011
        self.assertEqual(first_octect & mask, 2)

    def test_gen_mac_multicast_locally_administered(self):
        """
        @Test: Generate a multicast and locally administered MAC address
        @Feature: MAC Generator
        @Assert: A multicast and locally administered MAC address is generated
        """
        mac = gen_mac(multicast=True, locally=True)
        first_octect = int(mac.split(':', 1)[0], 16)
        mask = 0b00000011
        self.assertEqual(first_octect & mask, 3)
