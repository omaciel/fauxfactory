"""Tests for ipaddr generator."""

import pytest

from fauxfactory import gen_ipaddr


def test_gen_ipv4_1():
    """Generate a 3 group IPv4 address."""
    result = gen_ipaddr(ip3=True)
    assert result.split('.')[-1] == '0'


def test_gen_ipv4_2():
    """Generate a 4 group IPv4 address."""
    result = gen_ipaddr()
    assert len(result.split('.')) == 4


def test_gen_ipv4_3():
    """Generate a 4 group IPv4 address."""
    result = gen_ipaddr(ip3=False)
    assert len(result.split('.')) == 4


def test_gen_ipv4_4():
    """Generate a 4 group IPv4 address."""
    result = gen_ipaddr(ip3=False, ipv6=False)
    assert len(result.split('.')) == 4


def test_gen_ipv4_5():
    """Generate a 4 group IPv4 address with good prefix."""
    result = gen_ipaddr(ip3=False, ipv6=False, prefix=[10])
    assert len(result.split('.')) == 4
    assert result.startswith('10.')


def test_gen_ipv4_6():
    """Generate a 4 group IPv4 address with good prefix."""
    result = gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10])
    assert len(result.split('.')) == 4
    assert result.startswith('10.10.')


def test_gen_ipv4_7():
    """Generate a 4 group IPv4 address with good prefix."""
    result = gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10, 10])
    assert len(result.split('.')) == 4
    assert result.startswith('10.10.10.')


def test_gen_ipv4_8():
    """Generate a 4 group IPv4 address with prefix disabling randomness."""
    with pytest.raises(ValueError):
        gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10, 10, 10])


def test_gen_ipv4_9():
    """Generate a 4 group IPv4 address with prefix too long."""
    with pytest.raises(ValueError):
        gen_ipaddr(ip3=False, ipv6=False, prefix=[10, 10, 10, 10, 10])


def test_gen_ipv4_10():
    """Generate a 3 group IPv4 address with good prefix."""
    result = gen_ipaddr(ip3=True, ipv6=False, prefix=[10, 10])
    assert len(result.split('.')) == 4
    assert result.startswith('10.10.')
    assert result.endswith('.0')


def test_gen_ipv4_11():
    """Generate a 3 group IPv4 address with prefix disabling randomness."""
    with pytest.raises(ValueError):
        gen_ipaddr(ip3=True, ipv6=False, prefix=[10, 10, 10])


def test_gen_ipv4_12():
    """Generate a 3 group IPv4 address with prefix too long."""
    with pytest.raises(ValueError):
        gen_ipaddr(ip3=True, ipv6=False, prefix=[10, 10, 10, 10])


def test_gen_ipv6_1():
    """Generate a IPv6 address."""
    result = gen_ipaddr(ipv6=True)
    assert len(result.split(':')) == 8


def test_gen_ipv6_2():
    """Generate a IPv6 address."""
    result = gen_ipaddr(ip3=True, ipv6=True)
    assert len(result.split(':')) == 8


def test_gen_ipv6_3():
    """Generate a IPv6 address with custom prefix."""
    result = gen_ipaddr(ipv6=True, prefix=['e2d3'])
    assert len(result.split(':')) == 8
    assert result.startswith('e2d3:')


def test_gen_ipv6_4():
    """Generate a IPv6 address with custom (very long) prefix."""
    prefix = 7 * ['e2d3']
    result = gen_ipaddr(ipv6=True, prefix=prefix)
    assert len(result.split(':')) == 8
    assert result.startswith(':'.join(prefix))


def test_gen_ipv6_5():
    """Generate a IPv6 address with too long prefix."""
    prefix = 8 * ['e2d3']
    with pytest.raises(ValueError):
        gen_ipaddr(ipv6=True, prefix=prefix)


def test_gen_ipv6_6():
    """Generate a IPv6 address with even longer prefix."""
    prefix = 9 * ['e2d3']
    with pytest.raises(ValueError):
        gen_ipaddr(ipv6=True, prefix=prefix)
