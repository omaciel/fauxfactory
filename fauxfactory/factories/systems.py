"""Collection of computer systems generating functions."""
from copy import deepcopy

from fauxfactory.constants import FACTS_JSON
from fauxfactory.helpers import is_positive_int

from .choices import gen_choice, gen_uuid
from .internet import gen_domain, gen_ipaddr, gen_mac, gen_netmask
from .numbers import gen_integer
from .strings import gen_alpha, gen_alphanumeric


def add_memory_info(count=None):
    """Generate fake memory facts.

    :param int count: The total amount of RAM for a system.
    :returns: A dictionary representing memory facts.
    :rtype: dict

    """
    if count is None:
        count = gen_choice(range(4, 128, 2))
    else:
        is_positive_int(count)

    free_ram = (gen_integer(min_value=4, max_value=count))

    return {
        'dmi::memory::size': '{}'.format(free_ram * 1024),
        'memoryfree': '{} GB'.format(free_ram),
        'memoryfree_mb': '{}'.format(free_ram * 1024),
        'memorysize': '{} GB'.format(count),
        'memorysize_mb': '{}'.format(count * 1024),
        'swapfree': '{} GB'.format(free_ram),
        'swapfree_mb': '{}'.format(free_ram * 1024),
        'swapsize': '{} GB'.format(count),
        'swapsize_mb': '{}'.format(count * 1024),
    }


def add_network_devices():
    """Generate fake network device facts.

    :returns: A dictionary representing a Host's network devices.
    :rtype: dict

    """
    return {
        'dhcp_servers': {
            'system': gen_ipaddr(),
            'enp11s0': gen_ipaddr(),
        },
        'interfaces': 'enp11s0',
        'ipaddress': gen_ipaddr(),
        'ipaddress6': gen_ipaddr(ipv6=True),
        'ipaddress6_enp11s0': gen_ipaddr(ipv6=True),
        'macaddress': gen_mac(),
        'macaddress_enp11s0': gen_mac(),
        'mtu_enp11s0': '1500',
        'netmask': gen_netmask(),
        'netmask_enp11s0': gen_netmask(),
        'netmask_lo': gen_netmask(),
        'network_enp11s0': gen_ipaddr(),
        'network_lo': '127.0.0.0',
    }


def add_operating_system(name=None, family=None, major=None, minor=None):
    """Generate fake operating system facts.

    :param str name: The name for an operating system.
    :param str family: The operating system family.
    :param int major: The major release of the operating system.
    :param int minor: The minor release of the operating system.
    :returns: A dictionary representing an Operating System.
    :rtype: dict

    """
    if name is None:
        name = gen_alpha()
    if family is None:
        family = gen_alpha()
    if major is None:
        major = gen_integer(min_value=0, max_value=9)
    if minor is None:
        minor = gen_integer(min_value=0, max_value=9)
    return {
        'os': {
            'name': name,
            'family': family,
            'release': {
                'major': major,
                'minor': minor,
                'full': '{}.{}'.format(major, minor)
            }
        },
        'operatingsystem': name,
        'operatingsystemmajrelease': major,
        'operatingsystemrelease': '{}.{}'.format(major, minor),
        'osfamily': family,
        'distribution::id': gen_alpha(),
        'distribution::name': name,
        'distribution::version': '{}.{}'.format(major, minor),

    }


def add_partitions(extra_partitions=None):
    """Generate fake partitions facts."""
    partitions = {
        'partitions': {
            'sda1': {
                'uuid': gen_uuid(),
                'size': '1024000',
                'mount': '/boot',
                'filesystem': 'xfs'
            },
        }
    }

    if extra_partitions is not None:
        is_positive_int(extra_partitions)
        for idx in range(extra_partitions):
            device_id = idx + 1
            partitions['partitions'].update(
                {
                    'sdb{}'.format(device_id): {
                        'size': '975747072',
                        'filesystem': 'LVM2_member',
                    }})
    return partitions


def add_processor_info(count=None):
    """Generate fake processor facts.

    :param int count: Number of processors for a system.
    :returns: A dictionary containing fake processor facts.
    :rtype: dict

    """
    if count is None:
        count = gen_choice(range(2, 16, 2))
    else:
        is_positive_int(count)

    processors = {
        'physicalprocessorcount': count,
        'processorcount': count,
        'cpu::topology_source': 'kernel /sys cpu sibling lists',
        'cpu::cpu(s)': count,
        'lscpu::cpu(s)': count,
        'processors': {
            'models': [],
            'count': count,
            'physicalcount': count,
        },
    }

    # Add processors info based on total processors
    for idx in range(count):
        processors['processor{}'.format(
            idx)] = 'Intel(R) Xeon(R) CPU E31220 @ 3.10GHz'
        processors['processors']['models'].append(
            'Intel(R) Xeon(R) CPU E31220 @ 3.10GHz')
    return processors


def gen_system_facts(name=None):
    """Generate system facts.

    See https://docs.puppet.com/facter/3.6/core_facts.html for more
    information.

    :param str name: Name to be used as the system's hostname.
    :returns: A Dictionary representing a system's facts.
    :rtype: dict
    """
    if name is None or name == '':
        fqdn = gen_domain()
    else:
        fqdn = gen_domain(*name.split('.'))

    kernel = '{}.{}.{}'.format(
        *[gen_integer(min_value=0, max_value=9) for _ in range(3)])

    host = deepcopy(FACTS_JSON)

    host['architecture'] = gen_choice(('i386', 'x86_64'))
    host['domain'] = '.'.join(fqdn.split('.')[1:])
    host['fqdn'] = fqdn
    host['hostname'] = fqdn.split('.')[0]

    host['hardwareisa'] = host['architecture']
    host['hardwaremodel'] = host['architecture']
    host['kernelmajversion'] = '.'.join(kernel.split('.')[:2])
    host['kernelrelease'] = '{}-{}.{}'.format(
        kernel,
        gen_integer(min_value=0, max_value=999),
        host['architecture']
    )
    host['kernelversion'] = kernel

    host.update(add_memory_info())

    host.update(add_network_devices())

    host.update(add_operating_system())

    host.update(add_partitions())

    host.update(add_processor_info())

    host['path'] = (
        '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/sbin')

    host['productname'] = '{}'.format(gen_alpha())
    host['dmi::system::product_name'] = host['productname']
    host['dmi::baseboard::product_name'] = host['productname']
    host['serialnumber'] = '{}'.format(gen_alphanumeric())
    host['timezone'] = 'EDT'
    host['uniqueid'] = '{}'.format(gen_alphanumeric())
    host['uptime_days'] = gen_integer(min_value=1, max_value=1974)
    host['uptime_hours'] = host['uptime_days'] * 24
    host['uptime_seconds'] = host['uptime_hours'] * 3600
    host['uptime'] = '{} days'.format(host['uptime_days'])
    host['system_uptime'] = {
        'seconds': host['uptime_seconds'],
        'hours': host['uptime_hours'],
        'days': host['uptime_days'],
        'uptime': host['uptime']}
    host['uuid'] = gen_uuid()
    host['dmi::system::uuid'] = host['uuid']

    return host


__all__ = tuple(name for name in locals() if name.startswith('gen_'))


def __dir__():
    return __all__
