# -*- coding: utf-8 -*-
"""Generate random data for your tests."""

import datetime
import random
import re
import string
import sys
import unicodedata
import uuid
import warnings

from collections import Iterable
from functools import wraps

from fauxfactory.constants import (
    HTML_TAGS, LOREM_IPSUM_TEXT,
    MAX_YEARS, MIN_YEARS,
    SCHEMES, SUBDOMAINS, TLDS, VALID_NETMASKS
)

__all__ = (
    'gen_alpha',
    'gen_alphanumeric',
    'gen_boolean',
    'gen_choice',
    'gen_cjk',
    'gen_cyrillic',
    'gen_date',
    'gen_datetime',
    'gen_email',
    'gen_html',
    'gen_integer',
    'gen_ipaddr',
    'gen_iplum',
    'gen_latin1',
    'gen_mac',
    'gen_netmask',
    'gen_negative_integer',
    'gen_numeric_string',
    'gen_positive_integer',
    'gen_string',
    'gen_time',
    'gen_url',
    'gen_utf8',
    'gen_uuid',
)

# Private Functions -----------------------------------------------------------


def _make_unicode(data):
    """Convert ``data`` to a unicode string if running Python 2.

    :param str data: A string to be type cast.
    :return: ``data``, but as unicode. ``data`` is never modified: if a type
        cast is necessary, a copy of ``data`` is returned.

    """
    if sys.version_info[0] == 2:
        return unicode(data)  # flake8:noqa pylint:disable=undefined-variable
    return data

def _is_positive_int(length):
    """Check that ``length`` argument is an integer greater than zero.

    :param int length: The desired length of the string
    :raises: ``ValueError`` if ``length`` is not an ``int`` or is less than 1.
    :returns: Nothing.
    :rtype: None

    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("{0} is an invalid 'length'.".format(length))

def _unicode_letters_generator():
    """Generates unicode characters in the letters category

    :return: a generator which will generates all unicode letters available

    """
    if sys.version_info[0] == 2:
        chr_function = unichr  # pylint:disable=undefined-variable
        range_function = xrange  # pylint:disable=undefined-variable
    else:
        chr_function = chr
        range_function = range  # pylint:disable=redefined-variable-type

    # Use sys.maxunicode instead of 0x10FFFF to avoid the exception below, in a
    # narrow Python build (before Python 3.3)
    # ValueError: unichr() arg not in range(0x10000) (narrow Python build)
    # For more information, read PEP 261.
    for i in range_function(sys.maxunicode):
        char = chr_function(i)
        if unicodedata.category(char).startswith('L'):
            yield char

UNICODE_LETTERS = [c for c in _unicode_letters_generator()]

# Public Functions ------------------------------------------------------------


def gen_string(str_type, length=None):
    """A simple wrapper that calls other string generation methods.

    :param str str_type: The type of string which should be generated.
    :param int length: The length of the generated string. Must be 1 or
        greater.
    :raises: ``ValueError`` if an invalid ``str_type`` is specified.
    :returns: A string.
    :rtype: str

    Valid values for ``str_type`` are as follows:

    * alpha
    * alphanumeric
    * cjk
    * cyrillic
    * html
    * latin1
    * numeric
    * utf8

    """
    str_types_functions = {
        u'alpha': gen_alpha,
        u'alphanumeric': gen_alphanumeric,
        u'cjk': gen_cjk,
        u'cyrillic': gen_cyrillic,
        u'html': gen_html,
        u'latin1': gen_latin1,
        u'numeric': gen_numeric_string,
        u'utf8': gen_utf8,
    }
    str_type_lower = str_type.lower()  # do not modify user data
    if str_type_lower not in str_types_functions.keys():
        raise ValueError(
            '{0} is not a supported string type. Valid string types are {1}.'
            ''.format(str_type_lower, u','.join(str_types_functions.keys()))
        )
    method = str_types_functions[str_type_lower]
    if length is None:
        return method()
    return method(length)


def gen_alpha(length=10):
    """Returns a random string made up of alpha characters.

    :param int length: Length for random data.
    :returns: A random string made up of alpha characters.
    :rtype: str

    """

    # Validate length argument
    _is_positive_int(length)

    random.seed()
    output_string = u''.join(
        random.choice(string.ascii_letters) for i in range(length)
    )

    return _make_unicode(output_string)


def gen_alphanumeric(length=10):
    """Returns a random string made up of alpha and numeric characters.

    :param int length: Length for random data.
    :returns: A random string made up of alpha and numeric characters.
    :rtype: str

    """

    # Validate length argument
    _is_positive_int(length)

    random.seed()
    output_string = u''.join(
        random.choice(
            string.ascii_letters + string.digits
        ) for i in range(length))

    return _make_unicode(output_string)


def gen_boolean():
    """Returns a random Boolean value.

    :returns: A random Boolean value.
    :rtype: bool

    """

    choices = (True, False)

    return gen_choice(choices)


def gen_choice(choices):
    """Returns a random choice from the available choices.

    :param list choices: List of choices from which select a random value.
    :raises: ``ValueError`` if ``choices`` is ``None`` or not ``Iterable`` or
        a ``dict``.
    :returns: A random element from ``choices``.

    """

    # Validation for 'choices'
    if choices is None:
        raise ValueError("Choices argument cannot be None.")
    # We don't want a single dictionary value.
    if not isinstance(choices, Iterable) or isinstance(choices, dict):
        raise ValueError("Choices argument is not iterable.")
    if len(choices) == 0:
        raise ValueError("Choices argument cannot be empty.")
    # If only 1 item is present, return it right away
    if len(choices) == 1:
        return choices[0]

    random.seed()
    return random.choice(choices)


def gen_cjk(length=10):
    """Returns a random string made up of CJK characters.
    (Source: Wikipedia - CJK Unified Ideographs)

    :param int length: Length for random data.
    :returns: A random string made up of CJK characters.
    :rtype: str

    """

    # Validate length argument
    _is_positive_int(length)

    random.seed()

    # Generate codepoints, then convert the codepoints to a string. The
    # valid range of CJK codepoints is 0x4E00 - 0x9FCC, inclusive. Python 2
    # and 3 support the `unichr` and `chr` functions, respectively.
    codepoints = [random.randint(0x4E00, 0x9FCC) for _ in range(length)]
    if sys.version_info[0] == 2:
        # pylint:disable=undefined-variable
        output = u''.join(unichr(codepoint) for codepoint in codepoints)
    else:
        output = u''.join(chr(codepoint) for codepoint in codepoints)
    return _make_unicode(output)

def gen_cyrillic(length=10):
    """Returns a random string made up of Cyrillic characters.

    :param int length: Length for random data.
    :returns: A random string made up of Cyrillic characters.
    :rtype: str

    """

    # Validate length argument
    _is_positive_int(length)

    random.seed()

    # Generate codepoints, then convert the codepoints to a string. The
    # valid range of Cyrillic codepoints is 0x410 - 0x4ff, inclusive. Python 2
    # and 3 support the `unichr` and `chr` functions, respectively.
    codepoints = [random.randint(0x0400, 0x04FF) for _ in range(length)]
    try:
        # (undefined-variable) pylint:disable=E0602
        output = u''.join(unichr(codepoint) for codepoint in codepoints)
    except NameError:
        output = u''.join(chr(codepoint) for codepoint in codepoints)
    return _make_unicode(output)


def gen_date(min_date=None, max_date=None):
    """Returns a random date value

    :param min_date: A valid ``datetime.date`` object.
    :param max_date: A valid ``datetime.date`` object.
    :raises: ``ValueError`` if arguments are not valid ``datetime.date``
        objects.
    :returns: Random ``datetime.date`` object.

    """

    _min_value = (datetime.date.today() -
                  datetime.timedelta(365 * MIN_YEARS))
    _max_value = (datetime.date.today() +
                  datetime.timedelta(365 * MAX_YEARS))

    if min_date is None:
        min_date = _min_value
    if max_date is None:
        max_date = _max_value

    # Validation
    if not isinstance(min_date, datetime.date):
        raise ValueError("%s is not a valid datetime.date object")
    if not isinstance(max_date, datetime.date):
        raise ValueError("%s is not a valid datetime.date object")

    # Check that max_date is not before min_date
    assert min_date < max_date

    random.seed()

    # Pick a day between min and max dates
    diff = max_date - min_date
    days = random.randint(0, diff.days)
    date = min_date + datetime.timedelta(days=days)

    return date


def gen_datetime(min_date=None, max_date=None):
    """Returns a random datetime value

    :param min_date: A valid ``datetime.datetime`` object.
    :param max_date: A valid ``datetime.datetime`` object.
    :raises: ``ValueError`` if arguments are not valid ``datetime.datetime``
        objects.
    :returns: Random ``datetime.datetime`` object.

    """

    _min_value = (datetime.datetime.now() -
                  datetime.timedelta(365 * MIN_YEARS))
    _max_value = (datetime.datetime.now() +
                  datetime.timedelta(365 * MAX_YEARS))

    if min_date is None:
        min_date = _min_value
    if max_date is None:
        max_date = _max_value

    # Validation
    if not isinstance(min_date, datetime.datetime):
        raise ValueError("%s is not a valid datetime.datetime object")
    if not isinstance(max_date, datetime.datetime):
        raise ValueError("%s is not a valid datetime.datetime object")

    # Check that max_date is not before min_date
    assert min_date < max_date

    random.seed()

    # Pick a time between min and max dates
    diff = max_date - min_date
    seconds = random.randint(0, diff.days * 3600 * 24 + diff.seconds)

    return min_date + datetime.timedelta(seconds=seconds)


def gen_email(name=None, domain=None, tlds=None):
    """Generates a random email address.

    :param str name: Email name.
    :param str domain: Domain name.
    :param str tlds: Top Level Domain Server
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

    email = u"{0}@{1}.{2}".format(name, domain, tlds)

    return _make_unicode(email)


def gen_integer(min_value=None, max_value=None):
    """Returns a random integer value based on the current platform.

    :param int min_value: The minimum allowed value.
    :param int max_value: The maximum allowed value.
    :raises: ``ValueError`` if arguments are not integers or if they are
        less or greater than the system's allowed range for integers.
    :returns: Returns a random integer value.
    :rtype: int

    """

    # Platform-specific value range for integers
    _min_value = - sys.maxsize - 1
    _max_value = sys.maxsize

    if min_value is None:
        min_value = _min_value
    if max_value is None:
        max_value = _max_value

    if sys.version_info[0] < 3:
        integer_types = (int, long,)  # pylint:disable=undefined-variable
    else:
        integer_types = (int,)

    # Perform some validations
    if not isinstance(min_value, integer_types) or min_value < _min_value:
        raise ValueError("\'%s\' is not a valid minimum." % min_value)
    if not isinstance(max_value, integer_types) or max_value > _max_value:
        raise ValueError("\'%s\' is not a valid maximum." % max_value)

    random.seed()
    value = random.randint(min_value, max_value)

    return value


def gen_iplum(words=None, paragraphs=None):
    """Returns a lorem ipsum string. If no arguments are passed, then
    return the entire default lorem ipsum string.

    :param int words: The number of words to return.
    :param int paragraphs: The number of paragraphs to return.
    :raises: ``ValueError`` if ``words`` is not a valid positive integer.
    :returns: A ``lorem ipsum`` string containing either the number of ``words``
        or ``paragraphs``, extending and wrapping around the text as needed to
        make sure that it has the specified length.
    :rtype: str

    """

    # Check parameters
    if words is None or words == 0:
        words = len(LOREM_IPSUM_TEXT.split())
    if paragraphs is None:
        paragraphs = 1

    if not isinstance(words, int) or words < 0:
        raise ValueError(
            "Cannot generate a string with negative number of words.")
    _is_positive_int(paragraphs)

    # Original Lorem Ipsum string
    all_words = LOREM_IPSUM_TEXT.split()
    # How many words do we need?
    total_words_needed = words * paragraphs

    quotient = int(total_words_needed / len(all_words))
    modulus = total_words_needed % len(all_words)

    # Pool of words to use
    all_words = all_words * (quotient + modulus)

    result = u""
    start_pos = 0
    for _ in range(0, paragraphs):
        sentence = u" ".join(
            all_words[start_pos:start_pos + words])

        # Remove comma from the end, if it exists
        if sentence.endswith(','):
            sentence = sentence.rstrip(',')
        # Remove period from the end, if it exists
        if sentence.endswith('.'):
            sentence = sentence.rstrip('.')

        # Each sentence should be properly capitalized
        cap_sentence = [
            frag.capitalize() + u'.' for frag in sentence.split('. ')]

        # Add newline at the end
        result += " ".join(cap_sentence) + u"\n"

        # Increment positional counter
        start_pos += words
    return _make_unicode(result.rstrip())


def gen_latin1(length=10):
    """Returns a random string made up of UTF-8 characters.
    (Font: Wikipedia - Latin-1 Supplement Unicode Block)

    :param int length: Length for random data.
    :returns: A random string made up of ``Latin1`` characters.
    :rtype: str

    """

    # Validate length argument
    _is_positive_int(length)

    range0 = range1 = range2 = []
    range0 = ['00C0', '00D6']
    range1 = ['00D8', '00F6']
    range2 = ['00F8', '00FF']
    output_array = []

    for i in range(int(range0[0], 16), int(range0[1], 16)):
        output_array.append(i)
    for i in range(int(range1[0], 16), int(range1[1], 16)):
        output_array.append(i)
    for i in range(int(range2[0], 16), int(range2[1], 16)):
        output_array.append(i)

    random.seed()

    if sys.version_info[0] == 2:
        output_string = u''.join(
            # pylint:disable=E0602
            unichr(random.choice(output_array)) for _ in range(length)
        )
    else:
        output_string = u''.join(
            chr(random.choice(output_array)) for _ in range(length)
        )

    return _make_unicode(output_string)


def gen_negative_integer():
    """Returns a random negative integer based on the current platform.

    :returns: Returns a random negative integer value.
    :rtype: int

    """

    max_value = 0

    return gen_integer(max_value=max_value)


def gen_ipaddr(ip3=False, ipv6=False, prefix=()):
    """Generates a random IP address.

    You can also specify an IP address prefix if you are interested in
    local network address generation, etc.

    :param bool ip3: Whether to generate a 3 or 4 group IP.
    :param bool ipv6: Whether to generate IPv6 or IPv4
    :param list prefix: A prefix to be used for an IP (e.g. [10, 0, 1]). It
        must be an iterable with strings or integers. Can be left unspecified or
        empty.
    :returns: An IP address.
    :rtype: str
    :raises: ``ValueError`` if ``prefix`` would lead to no random fields at all.
        This means the length that triggers the ``ValueError`` is 4 for regular
        IPv4, 3 for IPv4 with ip3 and 8 for IPv6. It will be raised in any case
        the prefix length reaches or exceeds those values.

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
            "Prefix {} would lead to no randomness at all".format(
                repr(prefix)))
    elif rng < 0:
        raise ValueError(
            "Prefix {} is too long for this configuration".format(
                repr(prefix)))

    random.seed()

    if ipv6:
        # StackOverflow.com questions: generate-random-ipv6-address
        random_fields = [
            '{0:x}'.format(random.randint(0, 2**16 - 1)) for _ in range(rng)]
        ipaddr = u':'.join(prefix + random_fields)
    else:
        random_fields = [str(random.randrange(0, 255, 1)) for _ in range(rng)]
        ipaddr = u".".join(prefix + random_fields)

        if ip3:
            ipaddr = ipaddr + u".0"

    return _make_unicode(ipaddr)


def gen_mac(delimiter=':', multicast=None, locally=None):
    """Generates a random MAC address.

    For more information about how unicast or multicast and globally unique and
    locally administered MAC addresses are generated check this link
    https://en.wikipedia.org/wiki/MAC_address.

    :param str delimeter: Valid MAC delimeter (e.g ':', '-').
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
    octets.extend([
        random.randint(0, 255) for _ in range(5)
    ])
    mac = delimiter.join(['{0:02x}'.format(octet) for octet in octets])

    return _make_unicode(mac)


def gen_netmask(min_cidr=1, max_cidr=31):
    """Generates a random valid netmask.

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


def gen_numeric_string(length=10):
    """Returns a random string made up of numbers.

    :param int length: Length for random data.
    :returns: A random string made up of numbers.
    :rtype: str

    """

    # Validate length argument
    _is_positive_int(length)

    random.seed()
    output_string = u''.join(
        random.choice(string.digits) for i in range(length)
    )

    return _make_unicode(output_string)


def gen_positive_integer():
    """Returns a random positive integer based on the current platform.

    :returns: A random positive integer value.
    :rtype: int

    """

    min_value = 0

    return gen_integer(min_value=min_value)


def gen_time():
    """Generates a random time.

    :returns: A random ``datetime.time`` object.

    """

    random.seed()
    return datetime.time(
        random.randint(0, 23),
        random.randint(0, 59),
        random.randint(0, 59),
        random.randint(0, 999999),
    )


def gen_url(scheme=None, subdomain=None, tlds=None):
    """Generates a random URL address

    :param str scheme: Either http, https or ftp.
    :param str subdomain: A valid subdmain
    :param str tlds: A qualified top level domain name (e.g. 'com', 'net')
    :raises: ``ValueError`` if arguments are not valid.
    :returns: A random URL address.
    :rtype: str

    """

    # Regex for subdomain names
    subdomainator = re.compile(r"^[a-zA-Z0-9][-\w.~]*$")
    # Regex for URL scheme
    schemenator = re.compile(r"^(https?|ftp)$")
    # Regex for TLDS
    tldsnator = re.compile(r"^[a-zA-Z]{1,3}$")

    if scheme:
        if schemenator.match(scheme) is None:
            raise ValueError("Protocol {0} is not valid.".format(scheme))
    else:
        scheme = gen_choice(SCHEMES)

    if subdomain:
        if subdomainator.match(subdomain) is None:
            raise ValueError("Subdomain {0} is invalid.".format(subdomain))
    else:
        subdomain = gen_choice(SUBDOMAINS)

    if tlds:
        if tldsnator.match(tlds) is None:
            raise ValueError("TLDS name {0} is invalid.".format(tlds))
    else:
        tlds = gen_choice(TLDS)

    url = u"{0}://{1}.{2}".format(scheme, subdomain, tlds)

    return _make_unicode(url)


def gen_utf8(length=10):
    """Returns a random string made up of UTF-8 letters characters, as per
    `RFC 3629`_.

    :param int length: Length for random data.
    :returns: A random string made up of ``UTF-8`` letters characters.
    :rtype: str

    .. _`RFC 3629`: http://www.rfc-editor.org/rfc/rfc3629.txt

    """
    # Validate length argument
    _is_positive_int(length)

    random.seed()
    return u''.join([random.choice(UNICODE_LETTERS) for _ in range(length)])


def gen_uuid():
    """Generates a UUID string (universally unique identifiers).

    :returns: Returns a string representation for a UUID.
    :rtype: str

    """

    output_uuid = _make_unicode(str(uuid.uuid4()))

    return output_uuid


def gen_html(length=10):
    """Returns a random string made up of html characters.

    :param int length: Length for random data.
    :returns: A random string made up of html characters.
    :rtype: str

    """

    # Validate length argument
    _is_positive_int(length)

    random.seed()
    html_tag = random.choice(HTML_TAGS)
    output_string = u'<{0}>{1}</{2}>'.format(
        html_tag, gen_string("alpha", length), html_tag)

    return _make_unicode(output_string)


# Backward Compatibility ------------------------------------------------------


# Code borrowed from http://code.activestate.com/recipes/391367-deprecated/
def deprecated(func):
    """A decorator used to mark functions as deprecated.

    Emit a warning when the decorated function is called.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Emit a warning, then call ``func``."""
        old_name = func.__name__
        if old_name == 'codify':
            new_name = '_make_unicode'
        else:
            new_name = old_name.replace('generate', 'gen')
        warnings.warn(
            '{0} is deprecated! Please use {1} instead.'
            .format(old_name, new_name),
            category=Warning
        )
        return func(*args, **kwargs)
    return wrapper


@deprecated
def codify(data):
    # pylint:disable=missing-docstring
    return _make_unicode(data)


class FauxFactory(object):
    # This issue is no longer relevant, as the class has been turned into a set
    # of functions.
    # pylint:disable=too-many-public-methods
    #
    # This code is not imported when `from fauxfactory import *` is called, nor
    # does this code show up in Sphinx's output. See `__all__`.
    # pylint:disable=missing-docstring

    @classmethod
    @deprecated
    def generate_string(cls, str_type, length):
        return gen_string(str_type, length)

    @classmethod
    @deprecated
    def generate_alpha(cls, length=10):
        return gen_alpha(length)

    @classmethod
    @deprecated
    def generate_alphanumeric(cls, length=10):
        return gen_alphanumeric(length)

    @classmethod
    @deprecated
    def generate_boolean(cls):
        return gen_boolean()

    @classmethod
    @deprecated
    def generate_choice(cls, choices):
        return gen_choice(choices)

    @classmethod
    @deprecated
    def generate_cjk(cls, length=10):
        return gen_cjk(length)

    @classmethod
    @deprecated
    def generate_date(cls, min_date=None, max_date=None):
        return gen_date(min_date, max_date)

    @classmethod
    @deprecated
    def generate_datetime(cls, min_date=None, max_date=None):
        return gen_datetime(min_date, max_date)

    @classmethod
    @deprecated
    def generate_email(cls, name=None, domain=None, tlds=None):
        return gen_email(name, domain, tlds)

    @classmethod
    @deprecated
    def generate_integer(cls, min_value=None, max_value=None):
        return gen_integer(min_value, max_value)

    @classmethod
    @deprecated
    def generate_iplum(cls, words=None, paragraphs=None):
        return gen_iplum(words, paragraphs)

    @classmethod
    @deprecated
    def generate_latin1(cls, length=10):
        return gen_latin1(length)

    @classmethod
    @deprecated
    def generate_negative_integer(cls):
        return gen_negative_integer()

    @classmethod
    @deprecated
    def generate_ipaddr(cls, ip3=False, ipv6=False):
        return gen_ipaddr(ip3, ipv6)

    @classmethod
    @deprecated
    def generate_mac(cls, delimiter=":"):
        return gen_mac(delimiter)

    @classmethod
    @deprecated
    def generate_numeric_string(cls, length=10):
        return gen_numeric_string(length)

    @classmethod
    @deprecated
    def generate_positive_integer(cls):
        return gen_integer()

    @classmethod
    @deprecated
    def generate_time(cls):
        return gen_time()

    @classmethod
    @deprecated
    def generate_url(cls, scheme=None, subdomain=None, tlds=None):
        return gen_url(scheme, subdomain, tlds)

    @classmethod
    @deprecated
    def generate_utf8(cls, length=10):
        return gen_utf8(length)

    @classmethod
    @deprecated
    def generate_uuid(cls):
        return gen_uuid()

    @classmethod
    @deprecated
    def generate_html(cls, length=10):
        return gen_html(length)
