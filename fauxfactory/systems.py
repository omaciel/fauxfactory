"""Collection of computer systems generating functions."""
from copy import deepcopy

from fauxfactory.choices import gen_choice, gen_uuid
from fauxfactory.constants import (
    FACTS_JSON,
    SUBDOMAINS,
    TLDS,
)
from fauxfactory.internet import gen_ipaddr, gen_mac, gen_netmask
from fauxfactory.numbers import gen_integer
from fauxfactory.strings import gen_alpha, gen_alphanumeric


# pylint: disable=too-many-statements
def gen_system_facts(name=None):
    """Generate system facts.

    See https://docs.puppet.com/facter/3.6/core_facts.html for more
    information.

    :param str name: Name to be used as the system's hostname.
    :returns: A Dictionary representing a system's facts.
    :rtype: dict
    """
    if name is None or name == '':
        domain = '{}.{}'.format(gen_choice(SUBDOMAINS), gen_choice(TLDS))
        host_name = gen_alpha().lower()
    else:
        host_name = name.split('.')[0]
        domain = '.'.join(name.split('.')[1:])

    system_name = '{}.{}'.format(host_name, domain) if domain else host_name
    kernel = '{}.{}.{}'.format(
        *[gen_integer(min_value=0, max_value=9) for _ in range(3)])
    total_ram = gen_choice(range(4, 128, 2))
    free_ram = (gen_integer(min_value=4, max_value=total_ram))

    host = deepcopy(FACTS_JSON)

    host['architecture'] = gen_choice(('i386', 'x86_64'))
    host['dhcp_servers'] = {
        'system': gen_ipaddr(),
        'enp11s0': gen_ipaddr(),
    }
    host['domain'] = domain
    host['fqdn'] = system_name
    host['hardwareisa'] = host['architecture']
    host['hardwaremodel'] = host['architecture']
    host['hostname'] = host_name
    host['interfaces'] = 'enp11s0'
    host['ipaddress'] = gen_ipaddr()
    host['ipaddress6'] = gen_ipaddr(ipv6=True)
    host['ipaddress6_enp11s0'] = gen_ipaddr(ipv6=True)
    host['kernelmajversion'] = '.'.join(kernel.split('.')[:2])
    host['kernelrelease'] = '{}-{}.{}'.format(
        kernel,
        gen_integer(min_value=0, max_value=999),
        host['architecture']
    )
    host['kernelversion'] = kernel
    host['macaddress'] = gen_mac()
    host['macaddress_enp11s0'] = gen_mac()
    host['memoryfree'] = '{} GB'.format(free_ram)
    host['memoryfree_mb'] = '{}'.format(free_ram * 1024)
    host['dmi.memory.size'] = host['memoryfree_mb']
    host['memorysize'] = '{} GB'.format(total_ram)
    host['memorysize_mb'] = '{}'.format(total_ram * 1024)
    host['mtu_enp11s0'] = '1500'
    host['netmask'] = gen_netmask()
    host['netmask_enp11s0'] = gen_netmask()
    host['netmask_lo'] = gen_netmask()
    host['network_enp11s0'] = gen_ipaddr()
    host['network_lo'] = '127.0.0.0'

    op_release_major = gen_integer(min_value=0, max_value=9)
    op_release_minor = gen_integer(min_value=0, max_value=9)
    host['os'] = {
        'name': gen_alpha(),
        'family': gen_alpha(),
        'release': {
            'major': op_release_major,
            'minor': op_release_minor,
            'full': '{}.{}'.format(op_release_major, op_release_minor)
        }}
    host['operatingsystem'] = host['os']['name']
    host['operatingsystemmajrelease'] = gen_integer(min_value=0, max_value=9)
    host['operatingsystemrelease'] = host['os']['release']['full']
    host['osfamily'] = host['os']['family']
    host['distribution.name'] = host['operatingsystem']
    host['distribution.version'] = host['operatingsystemrelease']
    host['partitions'] = {
        'sda1': {
            'uuid': gen_uuid(),
            'size': '1024000',
            'mount': '/boot',
            'filesystem': 'xfs'
        },
        'sda2': {
            'size':
            '975747072',
            'filesystem':
            'LVM2_member'
        }}
    host['path'] = (
        '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/sbin')
    host['physicalprocessorcount'] = '1'
    host['processorcount'] = gen_choice(range(2, 16, 2))
    host['processors'] = {
        'models': [],
        'count': host['processorcount'],
        'physicalcount': host['physicalprocessorcount'],
    }
    host['cpu.cpu(s)'] = host['processorcount']
    host['lscpu.cpu(s)'] = host['cpu.cpu(s)']
    # Add processors info based on total processors
    for idx in range(host['processorcount']):
        host[f'processor{idx}'] = 'Intel(R) Xeon(R) CPU E31220 @ 3.10GHz'
        host['processors']['models'].append(
            'Intel(R) Xeon(R) CPU E31220 @ 3.10GHz')

    host['productname'] = '{}'.format(gen_alpha())
    host['dmi.system.product_name'] = host['productname']
    host['dmi.baseboard.product_name'] = host['productname']
    host['serialnumber'] = '{}'.format(gen_alphanumeric())
    host['swapfree'] = '{} GB'.format(free_ram)
    host['swapfree_mb'] = '{}'.format(free_ram * 1024)
    host['swapsize'] = '{} GB'.format(total_ram)
    host['swapsize_mb'] = '{}'.format(total_ram * 1024)
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
    host['dmi.system.uuid'] = host['uuid']

    return host
