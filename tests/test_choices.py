"""Tests for all choice generators."""

import string

import pytest

from fauxfactory import gen_choice


def test_gen_choice_1():
    """Select a random value from integer values."""
    choices = range(5)

    for _ in range(10):
        result = gen_choice(choices)
        assert result in choices


def test_gen_choice_2():
    """Select a random value from alphanumeric values."""
    choices = string.ascii_letters + string.digits

    for _ in range(10):
        result = gen_choice(choices)
        assert result in choices


def test_gen_choice_3():
    """Select a random value from short list."""
    choices = [1, ]

    for _ in range(10):
        result = gen_choice(choices)
        assert result == choices[0]


def test_gen_choice_4():
    """Select a random value from longer list."""
    choices = [1, 2, 3, 9, 10, 11, 100, 101, 102]

    for _ in range(10):
        result = gen_choice(choices)
        assert result in choices


def test_gen_choice_5():
    """Select a random value from short tuple."""
    choices = (1, )

    for _ in range(10):
        result = gen_choice(choices)
        assert result == choices[0]


def test_gen_choice_6():
    """Select a random value from longer tuple."""
    choices = (1, 2, 3, 9, 10, 11, 100, 101, 102, )

    for _ in range(10):
        result = gen_choice(choices)
        assert result in choices


def test_gen_choice_7():
    """Select a random value from empty list."""
    choices = []

    with pytest.raises(ValueError):
        gen_choice(choices)


def test_gen_choice_8():
    """Select a random value from empty tuple."""
    choices = ()

    with pytest.raises(ValueError):
        gen_choice(choices)


def test_gen_choice_9():
    """Select a random value from empty dictionary."""
    choices = {}

    with pytest.raises(ValueError):
        gen_choice(choices)


def test_gen_choice_10():
    """Select a random value from single dictionary."""
    choices = {'Name': 'Bob', 'Age': 39}

    with pytest.raises(ValueError):
        gen_choice(choices)


def test_gen_choice_11():
    """Select a random value from dictionary list."""
    choices = [
        {'Name': 'Bob', 'Age': 39},
        {'Name': 'Alice', 'Age': 23},
        {'Name': 'Pete', 'Age': 79},
    ]

    for _ in range(10):
        result = gen_choice(choices)
        assert result in choices


def test_gen_choice_12():
    """Select a random value from words list."""
    choices = ['green', 'yellow', 'blue' 'white']

    for _ in range(10):
        result = gen_choice(choices)
        assert result in choices


def test_gen_choice_13():
    """Cannot use None for Choice generator."""
    choices = None

    with pytest.raises(ValueError):
        gen_choice(choices)
