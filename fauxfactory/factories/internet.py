"""Methods related to generating internet related values."""

import random
import re

from fauxfactory.constants import SCHEMES, SUBDOMAINS, TLDS, VALID_NETMASKS
from fauxfactory.helpers import check_validation

from .choices import gen_choice
from .strings import gen_alpha


def gen_domain(name=None, subdomain=None, tlds=None):
    """Generate a random domain name.

    :param str name: Name for your host.
    :param str subdomain: Name for the subdomain.
    :param str tlds: Top Level Domain Server.
    :returns: A random domain name.
    :rtype: str

    """
    # Generate a new name if needed
    if name is None:
        name = gen_alpha(8).lower()
    # Obtain a random subdomain if needed
    if subdomain is None:
        subdomain = gen_choice(SUBDOMAINS)
    # Obtain a random top level domain if needed
    if tlds is None:
        tlds = gen_choice(TLDS)

    return '{}.{}.{}'.format(name, subdomain, tlds)


@check_validation
def gen_email(name=None, domain=None, tlds=None):
    """Generate a random email address.

    :param str name: Email name.
    :param str domain: Domain name.
    :param str tlds: Top Level Domain Server.
    :returns: An email address.
    :rtype: str

    """
    # Generate a new name if needed
    if name is None:
        name = gen_alpha(8)
    # Obtain a random domain if needed
    if domain is None:
        domain = gen_choice(SUBDOMAINS)
    # Obtain a random top level domain if needed
    if tlds is None:
        tlds = gen_choice(TLDS)

    email = '{0}@{1}.{2}'.format(name, domain, tlds)

    return email


@check_validation
def gen_ipaddr(ip3=False, ipv6=False, prefix=()):
    """Generate a random IP address.

    You can also specify an IP address prefix if you are interested in
    local network address generation, etc.

    :param bool ip3: Whether to generate a 3 or 4 group IP.
    :param bool ipv6: Whether to generate IPv6 or IPv4
    :param list prefix: A prefix to be used for an IP (e.g. [10, 0, 1]). It
        must be an iterable with strings or integers. Can be left
        unspecified or empty.
    :returns: An IP address.
    :rtype: str
    :raises: ``ValueError`` if ``prefix`` would lead to no random fields at
        all. This means the length that triggers the ``ValueError`` is 4 for
        regular IPv4, 3 for IPv4 with ip3 and 8 for IPv6. It will be raised in
        any case the prefix length reaches or exceeds those values.

    """
    # Set the lengths of the randomly generated sections
    if ipv6:
        rng = 8
    elif ip3:
        rng = 3
    else:
        rng = 4
    prefix = [str(field) for field in prefix]
    # Prefix reduces number of random fields generated, so subtract the length
    # of it from the rng to keep the IP address have correct number of fields
    rng -= len(prefix)
    if rng == 0:
        raise ValueError(
            'Prefix {} would lead to no randomness at all'.format(
                repr(prefix)))
    if rng < 0:
        raise ValueError(
            'Prefix {} is too long for this configuration'.format(
                repr(prefix)))

    random.seed()

    if ipv6:
        # StackOverflow.com questions: generate-random-ipv6-address
        random_fields = [
            '{0:x}'.format(random.randint(0, 2 ** 16 - 1)) for _ in range(rng)]
        ipaddr = ':'.join(prefix + random_fields)
    else:
        random_fields = [str(random.randrange(0, 255, 1)) for _ in range(rng)]
        ipaddr = '.'.join(prefix + random_fields)

        if ip3:
            ipaddr = ipaddr + '.0'

    return ipaddr


@check_validation
def gen_mac(delimiter=':', multicast=None, locally=None):
    """Generate a random MAC address.

    For more information about how unicast or multicast and globally unique and
    locally administered MAC addresses are generated check this link
    https://en.wikipedia.org/wiki/MAC_address.

    :param str delimiter: Valid MAC delimiter (e.g ':', '-').
    :param bool multicast: Indicates if the generated MAC address should be
        unicast or multicast. If no value is provided a random one will be
        chosen.
    :param bool locally: Indicates if the generated MAC address should be
        globally unique or locally administered. If no value is provided a
        random one will be chosen.
    :returns: A random MAC address.
    :rtype: str

    """
    if delimiter not in [':', '-']:
        raise ValueError('Delimiter is not a valid option: %s' % delimiter)
    random.seed()
    if multicast is None:
        multicast = bool(random.randint(0, 1))
    if locally is None:
        locally = bool(random.randint(0, 1))

    first_octet = random.randint(0, 255)
    if multicast:
        # Ensure that the first least significant bit is 1
        first_octet |= 0b00000001
    else:
        # Ensure that the first least significant bit is 0
        first_octet &= 0b11111110
    if locally:
        # Ensure that the second least significant bit is 1
        first_octet |= 0b00000010
    else:
        # Ensure that the second least significant bit is 0
        first_octet &= 0b11111101

    octets = [first_octet]
    octets.extend(random.randint(0, 255) for _ in range(5))
    mac = delimiter.join(['{0:02x}'.format(octet) for octet in octets])

    return mac


@check_validation
def gen_netmask(min_cidr=1, max_cidr=31):
    """Generate a random valid netmask.

    For more info: http://www.iplocation.net/tools/netmask.php

    :param int min_cidr: Inferior CIDR limit
    :param int max_cidr: Superior CIDR limit
    :returns: The netmask is chosen from
        :data:`fauxfactory.constants.VALID_NETMASKS` respecting the CIDR range
    :rtype: str
    :raises: ``ValueError`` if ``min_cidr`` or ``max_cidr`` have an invalid
        value. For example, ``max_cidr`` cannot be 33.

    """
    if min_cidr < 0:
        raise ValueError(
            'min_cidr must be 0 or greater, but is {0}'.format(min_cidr)
        )
    if max_cidr >= len(VALID_NETMASKS):
        raise ValueError(
            'max_cidr must be less than {0}, but is {1}'
            .format(len(VALID_NETMASKS), max_cidr)
        )
    random.seed()
    return VALID_NETMASKS[random.randint(min_cidr, max_cidr)]


@check_validation
def gen_url(scheme=None, subdomain=None, tlds=None):
    """Generate a random URL address.

    :param str scheme: Either http, https or ftp.
    :param str subdomain: A valid subdomain
    :param str tlds: A qualified top level domain name (e.g. 'com', 'net')
    :raises: ``ValueError`` if arguments are not valid.
    :returns: A random URL address.
    :rtype: str

    """
    # Regex for subdomain names
    subdomainator = re.compile(r'^[a-zA-Z0-9][-\w.~]*$')
    # Regex for URL scheme
    schemenator = re.compile(r'^(https?|ftp)$')
    # Regex for TLDS
    tldsnator = re.compile(r'^[a-zA-Z]{1,3}$')

    if scheme:
        if schemenator.match(scheme) is None:
            raise ValueError('Protocol {0} is not valid.'.format(scheme))
    else:
        scheme = gen_choice(SCHEMES)

    if subdomain:
        if subdomainator.match(subdomain) is None:
            raise ValueError('Subdomain {0} is invalid.'.format(subdomain))
    else:
        subdomain = gen_choice(SUBDOMAINS)

    if tlds:
        if tldsnator.match(tlds) is None:
            raise ValueError('TLDS name {0} is invalid.'.format(tlds))
    else:
        tlds = gen_choice(TLDS)

    url = u'{0}://{1}.{2}'.format(scheme, subdomain, tlds)

    return url


__all__ = tuple(name for name in locals() if name.startswith('gen_'))


def __dir__():
    return __all__
