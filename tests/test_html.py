"""Tests for HTML generator."""

import re

import pytest

from fauxfactory import gen_html, gen_integer


# pylint disable:W0621
@pytest.fixture
def matcher():
    """Instantiate a factory and compile a regex.

    The compiled regex can be used to find the contents of an HTML tag.
    """
    return re.compile('^<.*?>(.*?)</.*>$')


def test_length_arg_omitted(matcher):
    """Generate a random HTML tag with no ``length`` argument."""
    match = matcher.search(gen_html())
    assert len(match.group(1)) >= 1


def test_length_arg_provided(matcher):
    """Generate a random HTML tag with ``length`` argument."""
    length = gen_integer(1, 25)
    match = matcher.search(gen_html(length))
    assert len(match.group(1)) == length


def test_unicode():
    """Generate a random HTML tag."""
    assert isinstance(gen_html(), str)


# pylint: disable=C0103
def test_generate_html_with_len_less_than_min():
    """Cannot generate a HTML string with length less than minimum."""
    for value in range(8):
        with pytest.raises(ValueError):
            gen_html(value, include_tags=False)


@pytest.mark.parametrize('length', [8, 10, 12, 20, 100])
def test_generate_html_with_len_more_than_min(length):
    """Cannot generate a HTML string with length more than minimum."""
    assert length == len(gen_html(length, include_tags=False))
