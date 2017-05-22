"""Tests for domain generator."""
from fauxfactory import gen_domain


def test_generate_domain():
    """Create valid domain names."""
    domain = gen_domain()
    assert len(domain.split('.')) == 3


def test_generate_domain_with_attributes():
    """Create valid domain names."""
    domain = gen_domain(
        name='faux',
        subdomain='example',
        tlds='biz'
    )
    assert len(domain.split('.')) == 3
    assert domain.split('.')[0] == 'faux'
    assert domain.split('.')[1] == 'example'
    assert domain.split('.')[2] == 'biz'


def test_generate_domain_with_name():
    """Create valid domain names."""
    domain = gen_domain(name='faux')
    assert len(domain.split('.')) == 3
    assert domain.split('.')[0] == 'faux'


def test_generate_domain_with_subdomain():
    """Create valid domain names."""
    domain = gen_domain(subdomain='example')
    assert len(domain.split('.')) == 3
    assert domain.split('.')[1] == 'example'


def test_generate_domain_with_tlds():
    """Create valid domain names."""
    domain = gen_domain(tlds='biz')
    assert len(domain.split('.')) == 3
    assert domain.split('.')[2] == 'biz'
