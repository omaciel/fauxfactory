# -*- coding: utf-8 -*-
"""Tests for the netmask generator"""

import re
import unittest

from fauxfactory import gen_netmask, VALID_NETMASKS


NETMASK_REGEX = re.compile(
    '((255.){3}(0|128|192|224|240|248|252|254|255))|'
    '((255.){2}(0|128|192|224|240|248|252|254).0)|'
    '(255.(0|128|192|224|240|248|252|254)(.0){2})|'
    '((0|128|192|224|240|248|252|254)(.0){3})'
)


class NetmaskTestCase(unittest.TestCase):
    """Tests for ``gen_netmask`` generator."""

    def test_gen_netmask(self):
        """Test if gen_netmask generates valid values"""
        result = gen_netmask()
        self.assertEqual(len(result.split('.')), 4)
        self.assertIsNotNone(NETMASK_REGEX.match(result))

    def test_gen_netmask_boundary(self):
        """Test gen_netmask boundary cases"""
        self.assertEqual(u'0.0.0.0', gen_netmask(0, 0))
        self.assertEqual(u'255.255.255.255', gen_netmask(32, 32))
        with self.assertRaises(ValueError):
            gen_netmask(-1, 16)
        with self.assertRaises(ValueError):
            gen_netmask(16, 33)

    def test_valid_netmasks(self):
        """Test if VALID_NETMASKS constant have valid netmask values"""
        for netmask in VALID_NETMASKS:
            self.assertIsNotNone(NETMASK_REGEX.match(netmask))
