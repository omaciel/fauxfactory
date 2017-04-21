"""Tests for URL generator."""

import pytest

from fauxfactory import (
    gen_alpha,
    gen_alphanumeric,
    gen_cjk,
    gen_numeric_string,
    gen_url,
)
from fauxfactory.constants import SCHEMES


def test_gen_url_1():
    """Create a random URL."""
    for _ in range(10):
        result = gen_url()
        assert result
        assert result.split(':')[0] in SCHEMES


def test_gen_url_2():
    """Create a random URL with http scheme."""
    for _ in range(10):
        result = gen_url(scheme='http')
        assert result
        assert result.split(':')[0] == 'http'


def test_gen_url_3():
    """Create a random URL with https scheme."""
    for _ in range(10):
        result = gen_url(scheme='https')
        assert result
        assert result.split(':')[0] == 'https'


def test_gen_url_4():
    """Create a random URL with ftp scheme."""
    for _ in range(10):
        result = gen_url(scheme='ftp')
        assert result
        assert result.split(':')[0] == 'ftp'


def test_gen_url_5():
    """Create a random URL with invalid scheme."""
    for _ in range(10):
        scheme = gen_alphanumeric()
        with pytest.raises(ValueError):
            gen_url(scheme=scheme)


def test_gen_url_6():
    """Create a random URL with valid subdomain."""
    for _ in range(10):
        subdomain = gen_alphanumeric()
        result = gen_url(subdomain=subdomain)
        assert result

        # Breakdown the generated URL
        scheme_breakdown = result.split('//')
        domain = scheme_breakdown[1].split('.')
        assert domain[0] == subdomain


def test_gen_url_7():
    """Create a random URL with empty subdomain."""
    result = gen_url(subdomain='')
    assert result


def test_gen_url_8():
    """Create a random URL with whitespace subdomain."""
    with pytest.raises(ValueError):
        gen_url(subdomain=' ')


def test_gen_url_9():
    """Create a random URL with invalid subdomain."""
    for _ in range(10):
        subdomain = gen_cjk()
        with pytest.raises(ValueError):
            gen_url(subdomain=subdomain)


def test_gen_url_10():
    """Create a random URL with valid TLDS."""
    for _ in range(10):
        tlds = gen_alpha(length=3)
        result = gen_url(tlds=tlds)
        assert result
        assert result.split('.')[-1] == tlds


def test_gen_url_11():
    """Create a random URL with numeric TLDS."""
    for _ in range(10):
        with pytest.raises(ValueError):
            tlds = gen_numeric_string(length=3)
            gen_url(tlds=tlds)


def test_gen_url_12():
    """Create a random URL with whitespace TLDS."""
    for _ in range(10):
        with pytest.raises(ValueError):
            gen_url(tlds=' ')
