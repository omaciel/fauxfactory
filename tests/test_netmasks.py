"""Tests for the netmask generator."""

import re

import pytest

from fauxfactory.constants import VALID_NETMASKS
from fauxfactory import gen_netmask


NETMASK_REGEX = re.compile(
    '((255.){3}(0|128|192|224|240|248|252|254|255))|'
    '((255.){2}(0|128|192|224|240|248|252|254).0)|'
    '(255.(0|128|192|224|240|248|252|254)(.0){2})|'
    '((0|128|192|224|240|248|252|254)(.0){3})'
)


def test_gen_netmask():
    """Test if gen_netmask generates valid values."""
    result = gen_netmask()
    assert len(result.split('.')) == 4
    assert NETMASK_REGEX.match(result) is not None


def test_gen_netmask_boundary():
    """Test gen_netmask boundary cases."""
    assert gen_netmask(0, 0) == '0.0.0.0'
    assert gen_netmask(32, 32) == '255.255.255.255'
    with pytest.raises(ValueError):
        gen_netmask(-1, 16)
    with pytest.raises(ValueError):
        gen_netmask(16, 33)


def test_valid_netmasks():
    """Test if VALID_NETMASKS constant have valid netmask values."""
    for netmask in VALID_NETMASKS:
        assert NETMASK_REGEX.match(netmask) is not None
