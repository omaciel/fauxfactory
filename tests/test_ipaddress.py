# -*- coding: utf-8 -*-

"""Tests for ipaddr generator."""

from fauxfactory import gen_ipaddr, gen_local_ipaddr

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

    def test_local_addr(self):
        """
        @Test: Generate a local IPv4 address
        @Feature: IPAddr Generator
        @Assert: A local IPv4 address is generated
        """
        addr = gen_local_ipaddr()
        self.assertTrue(
            len(addr.split(".")) == 4, "IP address does not have 4 fields")
        self.assertTrue(
            addr.startswith("10."), "IP address does not start with 10")
        fields = addr.split(".")
        self.assertTrue(
            all(int(field) < 256 and int(field) >= 0 for field in fields),
            "IP address' field is bigger than 255!")
