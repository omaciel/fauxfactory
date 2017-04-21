"""Tests for MAC generator."""

import random
import re
import string

import pytest

from fauxfactory import gen_mac

MAC = re.compile('[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$')


def test_gen_mac_1():
    r"""Generate a MAC address using \":\" as the delimiter."""
    result = gen_mac()
    assert len(result.split(':')) == 6
    assert MAC.match(result) is not None


def test_gen_mac_2():
    r"""Generate a MAC address using \":\" as the delimiter."""
    result = gen_mac(delimiter=':')
    assert len(result.split(':')) == 6
    assert MAC.match(result) is not None


def test_gen_mac_3():
    r"""Generate a MAC address using \"-\" as the delimiter."""
    result = gen_mac(delimiter='-')
    assert len(result.split('-')) == 6
    assert MAC.match(result) is not None


def test_gen_mac_4():
    r"""Generate a MAC address using \".\" as the delimiter."""
    with pytest.raises(ValueError):
        gen_mac(delimiter='.')


def test_gen_mac_5():
    r"""Generate a MAC address using \" \" as the delimiter."""
    with pytest.raises(ValueError):
        gen_mac(delimiter=' ')


def test_gen_mac_6():
    """Generate a MAC address using a number as the delimiter."""
    with pytest.raises(ValueError):
        gen_mac(delimiter=random.randint(0, 10))


def test_gen_mac_7():
    """Generate a MAC address using a letter as the delimiter."""
    with pytest.raises(ValueError):
        gen_mac(
            delimiter=random.choice(string.ascii_letters))


# pylint: disable=C0103
def test_gen_mac_unicast_globally_unique():
    """Generate a unicast and globally unique MAC address."""
    mac = gen_mac(multicast=False, locally=False)
    first_octect = int(mac.split(':', 1)[0], 16)
    mask = 0b00000011
    assert first_octect & mask == 0


def test_gen_mac_multicast_globally_unique():
    """Generate a multicast and globally unique MAC address."""
    mac = gen_mac(multicast=True, locally=False)
    first_octect = int(mac.split(':', 1)[0], 16)
    mask = 0b00000011
    assert first_octect & mask == 1


def test_gen_mac_unicast_locally_administered():
    """Generate a unicast and locally administered MAC address."""
    mac = gen_mac(multicast=False, locally=True)
    first_octect = int(mac.split(':', 1)[0], 16)
    mask = 0b00000011
    assert first_octect & mask == 2


def test_gen_mac_multicast_locally_administered():
    """Generate a multicast and locally administered MAC address."""
    mac = gen_mac(multicast=True, locally=True)
    first_octect = int(mac.split(':', 1)[0], 16)
    mask = 0b00000011
    assert first_octect & mask == 3
