# -*- coding: utf-8 -*-

"""
Generate random data for your tests.
"""

__all__ = ("FauxFactory",)

import datetime
import random
import re
import string
import sys
import uuid

from collections import Iterable
from fauxfactory.constants import (
    MAX_YEARS, MIN_YEARS,
    SCHEMES, SUBDOMAINS, TLDS
)


class FauxFactory(object):
    """
    Generate random data for your tests.
    """

    @classmethod
    def generate_string(cls, str_type, length):
        """
        Create of a wide variety of string types, of arbitrary length.

        @type str_type: str
        @param str_type: A valid string type.
        @type length: int
        @param length: Length for generated strng.

        @rtype: int
        @return: A random string of the type and length specified.
        """

        # First lowercase the selected str type
        str_type = str_type.lower()

        if str_type == "alphanumeric":
            cls.generate_alphanumeric(length)
        elif str_type == "alpha":
            cls.generate_alpha(length)
        elif str_type == "latin1":
            cls.generate_latin1(length)
        elif str_type == 'numeric':
            cls.generate_numeric_string(length)
        elif str_type == "utf8":
            cls.generate_cjk(length)
        else:
            raise Exception("%s is not a supported string type." % str_type)

    @classmethod
    def generate_alpha(cls, length=5):
        """
        Returns a random string made up of alpha characters.

        @rtype length: int
        @param length: Length for random data.

        @rtype: str
        @return: A random string made up of alpha characters.
        """

        # Validate length argument
        if not isinstance(length, int) or length <= 0:
            raise ValueError("%s is an invalid \'length\'." % length)

        output_string = ''.join(
            random.choice(string.ascii_letters) for i in range(length)
        )

        return unicode(output_string)

    @classmethod
    def generate_alphanumeric(cls, length=5):
        """
        Returns a random string made up of alpha and numeric characters.

        @rtype length: int
        @param length: Length for random data.

        @rtype: str
        @return: A random string made up of alpha and numeric characters.
        """

        # Validate length argument
        if not isinstance(length, int) or length <= 0:
            raise ValueError("%s is an invalid \'length\'." % length)

        output_string = ''.join(
            random.choice(
                string.ascii_letters + string.digits
            ) for i in range(length))

        return unicode(output_string)

    @classmethod
    def generate_boolean(cls):
        """
        Returns a random Boolean value.

        @rtype: bool
        @return: A random Boolean value.
        """

        choices = (True, False)

        return cls.generate_choice(choices)

    @classmethod
    def generate_choice(cls, choices):
        """
        Returns a random choice from the available choices.

        @type choices: list
        @param choices: List of choices from which select a random value.
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

        return random.choice(choices)

    @classmethod
    def generate_cjk(cls, length=5):
        """
        Returns a random string made up of CJK characters.
        (Source: Wikipedia - CJK Unified Ideographs)

        @rtype length: int
        @param length: Length for random data.

        @rtype: str
        @return: A random string made up of CJK characters.
        """

        # Validate length argument
        if not isinstance(length, int) or length <= 0:
            raise ValueError("%s is an invalid \'length\'." % length)

        cjk_range = []
        cjk_range = ['4E00', '9FFF']
        output_array = []

        for i in range(int(cjk_range[0], 16), int(cjk_range[1], 16)):
            output_array.append(i)

        output_string = ''.join(
            unichr(random.choice(output_array)) for x in xrange(length))

        return unicode(output_string)

    @classmethod
    def generate_date(cls, min_date=None, max_date=None):
        """
        Returns a random date value

        @type min_date: object
        @param max_date: A valid datetime.date object
        @type min_date: object
        @param max_date: A valid datetime.date object

        @rtype: object
        @return: Random datetime.date object.
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

        # Pick a day between min and max dates
        diff = max_date - min_date
        days = random.randint(0, diff.days)
        date = min_date + datetime.timedelta(days=days)

        return date

    @classmethod
    def generate_datetime(cls, min_date=None, max_date=None):
        """
        Returns a random datetime value

        @type min_date: object
        @param max_date: A valid datetime.datetime object
        @type min_date: object
        @param max_date: A valid datetime.datetime object

        @rtype: object
        @return: Random datetime.datetime object.
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

        # Pick a time between min and max dates
        diff = max_date - min_date
        seconds = random.randint(0, diff.days * 3600 * 24 + diff.seconds)

        return min_date + datetime.timedelta(seconds=seconds)

    @classmethod
    def generate_email(cls, name=None, domain=None, tlds=None):
        """
        Generates a random email address.

        @type name: str
        @param name: Email name.
        @type domain: str
        @param domain: Domain name.
        @type tlds: str
        @param tlds: Top Level Domain Server

        @rtype: str
        @return: An email address.
        """

        # Generate a new name if needed
        if name is None:
            name = cls.generate_alpha(8)
        # Obtain a random domain if needed
        if domain is None:
            domain = cls.generate_choice(SUBDOMAINS)
        # Obtain a random top level domain if needed
        if tlds is None:
            tlds = cls.generate_choice(TLDS)

        return "%s@%s.%s" % (name, domain, tlds)

    @classmethod
    def generate_integer(cls, min_value=None, max_value=None):
        """
        Returns a random integer value based on the current platform.

        @type min_value: int
        @param min_value: The minimum allowed value.
        @type max_value: int
        @param max_value: The maximum allowed value.

        @rtype: int
        @return: Returns a random integer value.
        """

        # Platform-specific value range for integers
        _min_value = - sys.maxint - 1
        _max_value = sys.maxint

        if min_value is None:
            min_value = _min_value
        if max_value is None:
            max_value = _max_value

        # Perform some validations
        if not isinstance(min_value, int) or min_value < _min_value:
            raise ValueError("\'%s\' is not a valid minimum." % min_value)
        if not isinstance(max_value, int) or max_value > _max_value:
            raise ValueError("\'%s\' is not a valid maximum." % max_value)

        value = random.randint(min_value, max_value)

        return value

    @classmethod
    def generate_latin1(cls, length=5):
        """
        Returns a random string made up of UTF-8 characters.
        (Font: Wikipedia - Latin-1 Supplement Unicode Block)

        @rtype length: int
        @param length: Length for random data.

        @rtype: str
        @return: A random string made up of Latin1 characters.
        """

        # Validate length argument
        if not isinstance(length, int) or length <= 0:
            raise ValueError("%s is an invalid \'length\'." % length)

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

        output_string = ''.join(
            unichr(random.choice(output_array)) for x in xrange(length))

        return unicode(output_string)

    @classmethod
    def generate_negative_integer(cls):
        """
        Returns a random negative integer based on the current platform.

        @rtype: int
        @return: Returns a random negative integer value.
        """

        max_value = 0

        return cls.generate_integer(max_value=max_value)

    @classmethod
    def generate_ipaddr(cls, ip3=False, ipv6=False):
        """
        Generates a random IP address.

        @type ip3: bool
        @param ip3: Whether to generate a 3 or 4 group IP.
        @type ipv6: bool
        @param ipv6: Whether to generate IPv6 or IPv4

        @rtype: str
        @return: An IP address.
        """

        if ipv6:
            # StackOverflow.com questions: generate-random-ipv6-address
            ipaddr = ':'.join('{:x}'.format(
                random.randint(0, 2**16 - 1)
            ) for i in range(8))
        else:
            rng = 3 if ip3 else 4
            ipaddr = ".".join(
                str(random.randrange(0, 255, 1)) for x in range(rng))

            if ip3:
                ipaddr = ipaddr + ".0"

        return ipaddr

    @classmethod
    def generate_mac(cls, delimiter=":"):
        """
        Generates a random MAC address.

        @type delimeter: str
        @param delimeter: Valid MAC delimeter (e.g \':\', \'-\').

        @rtype: str
        @return: A random MAC address.
        """

        if delimiter not in [":", "-"]:
            raise ValueError("Delimiter is not a valid option: %s" % delimiter)

        chars = ['a', 'b', 'c', 'd', 'e', 'f',
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        mac = delimiter.join(
            chars[random.randrange(0, len(chars), 1)]+chars[random.randrange(
                0, len(chars), 1)] for x in range(6))

        return mac

    @classmethod
    def generate_numeric_string(cls, length=5):
        """
        Returns a random string made up of numbers.

        @type length: int
        @param length: Length for random data.

        @rtype: str
        @return: A random string made up of numbers.
        """

        # Validate length argument
        if not isinstance(length, int) or length <= 0:
            raise ValueError("%s is an invalid \'length\'." % length)

        output_string = ''.join(
            random.choice(string.digits) for i in range(length)
        )

        return unicode(output_string)

    @classmethod
    def generate_positive_integer(cls):
        """
        Returns a random positive integer based on the current platform.

        @rtype: int
        @return: Returns a random positive integer value.
        """

        min_value = 0

        return cls.generate_integer(min_value=min_value)

    @classmethod
    def generate_time(cls):
        """
        Generates a random time.

        @rtype: object
        @return: A datetime.time object.
        """

        return datetime.time(
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59),
            random.randint(0, 999999),
        )

    @classmethod
    def generate_url(cls, scheme=None, subdomain=None, tlds=None):
        """
        Generates a random URL address

        @type scheme: str
        @param scheme: Either http, https or ftp
        @type subdomain: str
        @param subdomain: A valid subdmain
        @type tlds: str
        @param tlds: A qualified top level domain name (e.g. \'com\', \'net\')

        @rtype: str
        @return: A random URL address.
        """

        # Regex for subdomain names
        subdomainator = re.compile(r"^[a-zA-Z0-9][-\w.~]*$")
        # Regex for URL scheme
        schemenator = re.compile(r"^(https?|ftp)$")
        # Regex for TLDS
        tldsnator = re.compile(r"^[a-zA-Z]{1,3}$")

        if scheme:
            if schemenator.match(scheme) is None:
                raise ValueError("Protocol \'%s\' is not valid" % scheme)
        else:
            scheme = cls.generate_choice(SCHEMES)

        if subdomain:
            if subdomainator.match(subdomain) is None:
                raise ValueError("Subdomain \'%s\ is invalid'" % subdomain)
        else:
            subdomain = cls.generate_choice(SUBDOMAINS)

        if tlds:
            if tldsnator.match(tlds) is None:
                raise ValueError("TLDS name \'%s\' is invalid" % tlds)
        else:
            tlds = cls.generate_choice(TLDS)

        return "%s://%s.%s" % (scheme, subdomain, tlds)

    @classmethod
    def generate_uuid(cls):
        """
        Generates a UUID string (universally unique identifiers).

        @rtype: str
        @return: Returns a string representation for a UUID.
        """

        output_uuid = unicode(uuid.uuid4())

        return output_uuid
