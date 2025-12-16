"""Tests for all string generators."""

import string
import unicodedata
from random import randint

import pytest

from fauxfactory import (
    gen_alpha,
    gen_alphanumeric,
    gen_cjk,
    gen_cyrillic,
    gen_html,
    gen_latin1,
    gen_numeric_string,
    gen_special,
    gen_string,
    gen_utf8,
)
from fauxfactory.helpers import BMP, unicode_letters_generator

GENERATORS = [
    gen_html,
    gen_alpha,
    gen_alphanumeric,
    gen_cjk,
    gen_cyrillic,
    gen_latin1,
    gen_numeric_string,
    gen_utf8,
    gen_special,
]

STRING_TYPES = [
    "html",
    "alpha",
    "alphanumeric",
    "cjk",
    "cyrillic",
    "latin1",
    "numeric",
    "utf8",
    "punctuation",
]


@pytest.mark.parametrize("fnc", GENERATORS)
def test_positive_string(fnc):
    """Default string generated is longer than zero characters."""
    assert fnc()


@pytest.mark.parametrize("fnc", GENERATORS[1:])
def test_fixed_length_positional(fnc):
    """String generated has correct length of characters."""
    assert len(fnc(10)) == 10


@pytest.mark.parametrize("fnc", GENERATORS[1:])
def test_fixed_length_keyword(fnc):
    """String generated has correct length of characters."""
    assert len(fnc(length=10)) == 10


@pytest.mark.parametrize("fnc", GENERATORS)
def test_negative_length(fnc):
    """Cannot generate string with negative length of characters."""
    with pytest.raises(ValueError):
        fnc(-1)


@pytest.mark.parametrize("fnc", GENERATORS)
def test_zero_length(fnc):
    """Cannot generate string with zero length of characters."""
    with pytest.raises(ValueError):
        fnc(0)


@pytest.mark.parametrize("fnc", GENERATORS)
def test_alpha_length(fnc):
    """Cannot generate string with alpha length of characters."""
    with pytest.raises(ValueError):
        fnc("a")


@pytest.mark.parametrize("fnc", GENERATORS)
def test_alphanumeric_length(fnc):
    """Cannot generate string with alphanumeric length of characters."""
    with pytest.raises(ValueError):
        fnc("-1")


@pytest.mark.parametrize("fnc", GENERATORS)
def test_empty_length(fnc):
    """Cannot generate string with empty length of characters."""
    with pytest.raises(ValueError):
        fnc("")


@pytest.mark.parametrize("fnc", GENERATORS)
def test_space_length(fnc):
    """Cannot generate string with space length of characters."""
    with pytest.raises(ValueError):
        fnc(" ")


@pytest.mark.parametrize("fnc", STRING_TYPES)
def test_gen_string(fnc):
    """Use `gen_string` to generate supported string."""
    assert gen_string(fnc)


# pylint: disable=invalid-name
@pytest.mark.parametrize("fnc", STRING_TYPES[1:])
def test_gen_string_fixed_length_positional(fnc):
    """Use `gen_string` to generate supported string with expected length."""
    assert len(gen_string(fnc, 5)) == 5


# pylint: disable=invalid-name
@pytest.mark.parametrize("fnc", STRING_TYPES[1:])
def test_gen_string_fixed_length_keyword(fnc):
    """Use `gen_string` to generate supported string with explict `length`."""
    assert len(gen_string(fnc, length=5)) == 5


def test_chars_in_letters_category():
    """Unicode letters generator generates only unicode letters."""
    # Categories extracted from section 5.5.1 of
    # http://www.unicode.org/reports/tr44/tr44-4.html
    for char in unicode_letters_generator():
        assert unicodedata.category(char) in ("Lu", "Ll", "Lt", "Lm", "Lo")


def test_bmp_chars_only():
    """Unicode letters generator generates only BMP unicode letters."""
    for char in gen_utf8(length=50, smp=False):
        assert ord(char) <= BMP.max


def test_gen_cjk_bmp_only():
    """gen_cjk with bmp_only=True generates only BMP CJK characters."""
    result = gen_cjk(50, bmp_only=True)
    for char in result:
        codepoint = ord(char)
        # Verify character is in BMP range
        assert 0x0000 <= codepoint <= 0xFFFF
        # Verify it's in the allowed CJK BMP blocks
        assert (0x3400 <= codepoint <= 0x4DBF) or (0x4E00 <= codepoint <= 0x9FFF)


def test_gen_cjk_default_includes_all_blocks():
    """gen_cjk default behavior includes all CJK blocks."""
    # Test that default behavior still works (includes all blocks)
    result = gen_cjk(50)
    assert len(result) == 50
    # All characters should be valid CJK characters
    for char in result:
        codepoint = ord(char)
        # Verify it's in one of the valid CJK blocks (BMP or non-BMP)
        in_valid_block = (
            (0x3400 <= codepoint <= 0x4DBF)
            or (0x4E00 <= codepoint <= 0x9FFF)
            or (0x20000 <= codepoint <= 0x2A6DF)
            or (0x2A700 <= codepoint <= 0x2B73F)
            or (0x2B740 <= codepoint <= 0x2B81F)
        )
        assert in_valid_block


def test_invalid_string_type():
    """Only valid string types can be generated."""
    with pytest.raises(ValueError):
        gen_string("foo")


def test_special_string():
    """Assert that only punctuation strings are returned."""
    VALID_CHARS = string.punctuation
    special_str = gen_special()
    for char in special_str:
        assert char in VALID_CHARS


@pytest.mark.parametrize("fnc", GENERATORS[1:])
def test_start_string(fnc):
    """String generated has start with specific keyword."""
    start = fnc(randint(1, 5))
    separator = fnc(1)
    random_str = fnc(start=start, separator=separator)
    assert start == random_str[: len(start)]
    assert separator == random_str[len(start)]
    assert len(random_str) == 10
