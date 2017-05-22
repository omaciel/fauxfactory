
"""Tests for system facts generator."""

import re

from fauxfactory import gen_system_facts

REGEX = r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$'


def test_gen_system_facts():
    """Create a random system facts."""
    # Regex for domain validation
    validator = re.compile(REGEX)
    facts = gen_system_facts()

    assert validator.match(facts['fqdn'])


def test_gen_system_facts_with_name():
    """Create a random system facts using a name."""
    # Regex for domain validation
    facts = gen_system_facts(name='faux')

    assert facts['fqdn'].startswith('faux')
    assert facts['hostname'] == 'faux'


def test_gen_system_facts_with_name_subdomain():
    """Create a random system facts using name and subdomain."""
    # Regex for domain validation
    facts = gen_system_facts(name='faux.example')

    assert facts['fqdn'].startswith('faux.example')
    assert facts['hostname'] == 'faux'
    assert facts['domain'].startswith('example')


def test_gen_system_facts_with_fqdn():
    """Create a random system facts using FQDN."""
    # Regex for domain validation
    validator = re.compile(REGEX)
    facts = gen_system_facts(name='faux.example.com')

    assert validator.match(facts['fqdn'])
    assert facts['fqdn'] == 'faux.example.com'
    assert facts['domain'] == 'example.com'
    assert facts['hostname'] == 'faux'
