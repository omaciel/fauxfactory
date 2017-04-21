"""Tests for Lorem Ipsum generator."""

import random

import pytest

from fauxfactory.constants import LOREM_IPSUM_TEXT
from fauxfactory import gen_iplum


def test_gen_loremipsum_1():
    """Create a complete lorem ipsum string."""
    result = gen_iplum()
    assert result == LOREM_IPSUM_TEXT
    assert result.startswith('Lorem ipsum')


def test_gen_loremipsum_2():
    """Create a lorem ipsum string with fixed number of words."""
    for _ in range(20):
        length = random.randint(1, 500)
        result = gen_iplum(words=length)
        assert len(result.split()) == length


def test_gen_loremipsum_3():
    """Create a lorem ipsum string with fixed number of paragraphs."""
    for _ in range(20):
        length = random.randint(1, 20)
        result = gen_iplum(paragraphs=length)
        assert len(result.split('\n')) == length


def test_gen_loremipsum_4():
    """Create a lorem ipsum string with zero words."""
    result = gen_iplum(words=0)
    assert result == LOREM_IPSUM_TEXT


def test_gen_loremipsum_5():
    """Create a lorem ipsum string with zero paragraphs."""
    with pytest.raises(ValueError):
        gen_iplum(paragraphs=0)


def test_gen_loremipsum_6():
    """Create a lorem ipsum string with 1 word and 0 paragragh."""
    with pytest.raises(ValueError):
        gen_iplum(words=1, paragraphs=0)


def test_gen_loremipsum_7():
    """Create a lorem ipsum string with 1 word and 1 paragragh."""
    result = gen_iplum(words=1, paragraphs=1)
    assert len(result.split()) == 1
    assert len(result.split()) == 1


def test_gen_loremipsum_8():
    """Create a lorem ipsum string with non-integer words."""
    with pytest.raises(ValueError):
        gen_iplum(words='a')


def test_gen_loremipsum_9():
    """Create a lorem ipsum string with non-integer paragraphs."""
    with pytest.raises(ValueError):
        gen_iplum(paragraphs='a')


def test_gen_loremipsum_10():
    """Create a lorem ipsum string with random words/paragraphs."""
    for _ in range(20):
        words = random.randint(1, 500)
        paragraphs = random.randint(1, 500)
        result = gen_iplum(
            words=words, paragraphs=paragraphs)
        assert len(result.split('\n')) == paragraphs
        for sentence in result.split('\n'):
            assert len(sentence.split()) == words
