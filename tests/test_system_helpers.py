
"""Tests for system facts helpers."""
import pytest

from fauxfactory.factories.systems import (
    add_memory_info,
    add_network_devices,
    add_operating_system,
    add_partitions,
    add_processor_info,
)


# Memory
def test_add_random_memory():
    """Get facts for random memory."""
    facts = add_memory_info()
    total_memory_mb = int(facts['memorysize_mb'])
    total_free_memory_mb = int(facts['memoryfree_mb'])
    total_swap_memory_mb = int(facts['swapsize_mb'])

    assert total_memory_mb >= (4 * 1024)
    assert total_memory_mb <= (128 * 1024)
    assert total_free_memory_mb <= total_memory_mb
    assert total_swap_memory_mb == total_memory_mb


def test_add_specific_memory():
    """Get facts for specific memory."""
    facts = add_memory_info(count=32)
    total_memory_mb = int(facts['memorysize_mb'])
    total_free_memory_mb = int(facts['memoryfree_mb'])
    total_swap_memory_mb = int(facts['swapsize_mb'])

    assert total_memory_mb == (32 * 1024)
    assert total_free_memory_mb <= total_memory_mb
    assert total_swap_memory_mb == total_memory_mb


def test_add_zero_memory():
    """Cannot add zero memory."""
    with pytest.raises(ValueError):
        add_memory_info(count=0)


def test_add_negative_memory():
    """Cannot add negative memory."""
    with pytest.raises(ValueError):
        add_memory_info(count=-1)


# Network
def test_add_network_devices():
    """Get facts for network devices."""
    facts = add_network_devices()
    assert facts['network_lo'] == '127.0.0.0'


# Operating Systems
def test_add_random_operating_system():
    """Get facts for a random operating system."""
    facts = add_operating_system()
    assert facts['operatingsystem']
    assert facts['osfamily']
    assert facts['os']['release']['major'] >= 0
    assert facts['os']['release']['major'] <= 9
    assert facts['os']['release']['minor'] >= 0
    assert facts['os']['release']['minor'] <= 9


# Operating Systems
def test_add_random_operating_system_with_attributes():
    """Get facts for a random operating system with all attributes."""
    facts = add_operating_system(
        name='Fedora',
        family='Red Hat',
        major=25,
        minor=1
    )
    assert facts['operatingsystem'] == 'Fedora'
    assert facts['osfamily'] == 'Red Hat'
    assert facts['os']['release']['major'] == 25
    assert facts['os']['release']['minor'] == 1


# Partitions
def test_add_single_partition():
    """Get facts for a single partition."""
    facts = add_partitions()
    assert 'sda1' in facts['partitions'].keys()


def test_add_three_partitions():
    """Get facts for three partition."""
    facts = add_partitions(extra_partitions=3)
    assert 'sda1' in facts['partitions'].keys()
    assert 'sdb1' in facts['partitions'].keys()
    assert 'sdb2' in facts['partitions'].keys()
    assert 'sdb3' in facts['partitions'].keys()


def test_add_zero_extra_partition():
    """Cannot add zero extra partitions."""
    with pytest.raises(ValueError):
        add_partitions(extra_partitions=0)


def test_add_negative_extra_partition():
    """Cannot add negative extra partitions."""
    with pytest.raises(ValueError):
        add_partitions(extra_partitions=-1)


# Processors
def test_add_random_processors():
    """Get facts for random number of processors."""
    facts = add_processor_info()
    assert facts['processorcount'] >= 2
    assert facts['processorcount'] <= 16
    assert len(facts['processors']['models']) >= 2
    assert len(facts['processors']['models']) <= 16


def test_add_one_processor():
    """Get facts for a single processor."""
    facts = add_processor_info(count=1)
    assert facts['processorcount'] == 1
    assert len(facts['processors']['models']) == 1


def test_add_two_processors():
    """Get facts for two processors."""
    facts = add_processor_info(count=2)
    assert facts['processorcount'] == 2
    assert len(facts['processors']['models']) == 2


def test_add_zero_processor():
    """Cannot add zero processors."""
    with pytest.raises(ValueError):
        add_processor_info(count=0)


def test_add_negative_processor():
    """Cannot add negative processors."""
    with pytest.raises(ValueError):
        add_processor_info(count=-1)
