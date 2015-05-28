# -*- coding: utf-8 -*-

"""Tests for ipaddr generator."""

from sys import version_info
from fauxfactory import gen_ipaddr

if version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class TestIpaddr(unittest.TestCase):
    """Test ipaddr generator."""

    def test_gen_ipv4_1(self):
        """
        @Test: Generate a 3 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 3-group IPv4 address is generated (addr
                 will always end with a \'.0\')
        """

        result = gen_ipaddr(ip3=True)
        self.assertTrue(
            result.split(".")[-1] == '0',
            "Did not generate a 3-group IPv4 addrss")

    def test_gen_ipv4_2(self):
        """
        @Test: Generate a 4 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = gen_ipaddr()
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")

    def test_gen_ipv4_3(self):
        """
        @Test: Generate a 4 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = gen_ipaddr(ip3=False)
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")

    def test_gen_ipv4_4(self):
        """
        @Test: Generate a 4 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = gen_ipaddr(ip3=False, ipv6=False)
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")

    def test_gen_ipv4_5(self):
        """
        @Test: Generate a 4 group IPv4 address with good prefix
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = gen_ipaddr(ip3=False, ipv6=False, prefix=[10])
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")
        self.assertTrue(result.startswith("10."))

    def test_gen_ipv4_6(self):
        """
        @Test: Generate a 4 group IPv4 address with good prefix
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10])
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")
        self.assertTrue(result.startswith("10.10."))

    def test_gen_ipv4_7(self):
        """
        @Test: Generate a 4 group IPv4 address with good prefix
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10, 10])
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")
        self.assertTrue(result.startswith("10.10.10."))

    def test_gen_ipv4_8(self):
        """
        @Test: Generate a 4 group IPv4 address with prefix disabling randomness
        @Feature: IPAddr Generator
        @Assert: An exception is raised
        """

        with self.assertRaises(ValueError):
            gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10, 10, 10])

    def test_gen_ipv4_9(self):
        """
        @Test: Generate a 4 group IPv4 address with prefix too long
        @Feature: IPAddr Generator
        @Assert: An exception is raised
        """

        with self.assertRaises(ValueError):
            gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10, 10, 10, 10])

    def test_gen_ipv4_10(self):
        """
        @Test: Generate a 3 group IPv4 address with good prefix
        @Feature: IPAddr Generator
        @Assert: A 3-group IPv4 address is generated
        """

        result = gen_ipaddr(ip3=True, ipv6=False, prefix=[10, 10])
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")
        self.assertTrue(result.startswith("10.10."))
        self.assertTrue(result.endswith(".0"))

    def test_gen_ipv4_11(self):
        """
        @Test: Generate a 3 group IPv4 address with prefix disabling randomness
        @Feature: IPAddr Generator
        @Assert: An exception is raised
        """

        with self.assertRaises(ValueError):
            gen_ipaddr(ip3=True, ipv6=False, prefix=[10, 10, 10])

    def test_gen_ipv4_12(self):
        """
        @Test: Generate a 3 group IPv4 address with prefix too long
        @Feature: IPAddr Generator
        @Assert: An exception is raised
        """

        with self.assertRaises(ValueError):
            gen_ipaddr(ip3=True, ipv6=False, prefix=[10, 10, 10, 10])

    def test_gen_ipv6_1(self):
        """
        @Test: Generate a IPv6 address
        @Feature: IPAddr Generator
        @Assert: A IPv6 address is generated
        """

        result = gen_ipaddr(ipv6=True)
        self.assertTrue(
            len(result.split(":")) == 8,
            "Did not generate a IPv6 addrss")

    def test_gen_ipv6_2(self):
        """
        @Test: Generate a IPv6 address
        @Feature: IPAddr Generator
        @Assert: A IPv6 address is generated
        """

        result = gen_ipaddr(ip3=True, ipv6=True)
        self.assertTrue(
            len(result.split(":")) == 8,
            "Did not generate a IPv6 addrss")

    def test_gen_ipv6_3(self):
        """
        @Test: Generate a IPv6 address with custom prefix
        @Feature: IPAddr Generator
        @Assert: A IPv6 address is generated
        """

        result = gen_ipaddr(ipv6=True, prefix=["e2d3"])
        self.assertTrue(
            len(result.split(":")) == 8,
            "Did not generate a IPv6 addrss")
        self.assertTrue(result.startswith("e2d3:"))

    def test_gen_ipv6_4(self):
        """
        @Test: Generate a IPv6 address with custom (very long) prefix
        @Feature: IPAddr Generator
        @Assert: A IPv6 address is generated
        """

        prefix = 7 * ["e2d3"]
        result = gen_ipaddr(ipv6=True, prefix=prefix)
        self.assertTrue(
            len(result.split(":")) == 8,
            "Did not generate a IPv6 addrss")
        self.assertTrue(result.startswith(":".join(prefix)))

    def test_gen_ipv6_5(self):
        """
        @Test: Generate a IPv6 address with too long prefix
        @Feature: IPAddr Generator
        @Assert: ValueError raised
        """

        prefix = 8 * ["e2d3"]
        with self.assertRaises(ValueError):
            gen_ipaddr(ipv6=True, prefix=prefix)

    def test_gen_ipv6_6(self):
        """
        @Test: Generate a IPv6 address with even longer prefix
        @Feature: IPAddr Generator
        @Assert: ValueError raised
        """

        prefix = 9 * ["e2d3"]
        with self.assertRaises(ValueError):
            gen_ipaddr(ipv6=True, prefix=prefix)
