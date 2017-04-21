"""Tests for Email generator."""

import re

from fauxfactory import gen_email

REGEX = r'^[a-zA-Z][a-zA-Z-.]*[^.-]@\w*\.[a-zA-Z]{2,3}'


def test_gen_email_1():
    """Create a random email value."""
    # Regex for email validation
    emailinator = re.compile(REGEX)
    for _ in range(100):
        assert emailinator.match(gen_email())
