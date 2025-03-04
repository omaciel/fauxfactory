"""Collection of helper methods and functions."""

import re
import unicodedata
from collections import namedtuple
from functools import wraps

from fauxfactory.constants import VALID_DIGITS

UnicodePlane = namedtuple("UnicodePlane", ["min", "max"])

BMP = UnicodePlane(int("0x0000", 16), int("0xffff", 16))
SMP = UnicodePlane(int("0x10000", 16), int("0x1ffff", 16))


def base_repr(number, base):
    """Return the base representation of a decimal number.

    As shared here: https://stackoverflow.com/a/2267446

    Conversion steps:

    1) Divide the number by the base
    2) Get the integer quotient for the next iteration
    3) Get the remainder for the hex digit
    4) Repeat the steps until quotient is equal to zero

    :param number: (int) The decimal number to be converted.
    :param base: The base to convert.

    :return: The base representation of <number>.
    """
    if base <= 1:
        raise ValueError("Cannot represent number with base smaller than 2.")
    if number < 0:
        sign = -1
    elif number == 0:
        return VALID_DIGITS[0]
    else:
        sign = 1

    number *= sign
    digits = []

    while number:
        digits.append(VALID_DIGITS[number % base])
        number //= base

    if sign < 0:
        digits.append("-")

    digits.reverse()

    return "".join(digits)


def check_len(fnc):
    """Validate generators requiring a `length` argument."""

    @wraps(fnc)
    def wrapped(*args, **kwargs):
        """Make sure that we verify the `length` argument."""
        if args and len(args) == 1:
            is_positive_int(args[0])
        if "length" in kwargs:
            if kwargs.get("length") is not None:
                is_positive_int(kwargs.get("length"))

        result = fnc(*args, **kwargs)

        return result

    return wrapped


def check_validation(fcn):
    """Decorate functions requiring validation.

    Simple decorator to validate values generated by function `fnc`
    according to parameters `validator`, `default` and `tries`.

    :param fcn: function to be enhanced
    :return: decorated function
    """

    @wraps(fcn)
    def validate(*args, **kwargs):
        """Perform the validation on decorated function."""
        validator = kwargs.get("validator")
        default = kwargs.get("default")
        tries = kwargs.get("tries", 10)
        if validator and default is None:
            raise ValueError(
                'If "validator" param is defined, "default" parameter must not be None'
            )
        if validator is None:

            def validator_fcn(_):
                """No validation passed."""
                return True

        else:
            validator_fcn = validator

        if not callable(validator_fcn):

            def regex_validator(value):
                """Perform RegEx validation."""
                return re.match(validator, value)

            validator_fcn = regex_validator

        # Removing params related to validation but not fcn
        for key in ("validator", "default", "tries"):
            if key in kwargs:
                kwargs.pop(key)

        for _ in range(tries):
            value = fcn(*args, **kwargs)
            if validator_fcn(value):
                return value

        return default

    return validate


def is_positive_int(length):
    """Check that `length` argument is an integer greater than zero.

    :param int length: The desired length of the string
    :raises: `ValueError` if `length` is not an `int` or is less than 1.

    """
    if not isinstance(length, int):
        raise ValueError(f"{length} is not numeric.")
    if length <= 0:
        raise ValueError(f"{length} is an invalid length.")


def unicode_letters_generator(smp=True):
    """Generate unicode characters in the letters category.

    :param bool smp: Include Supplementary Multilingual Plane (SMP)
        characters
    :return: a generator which will generates all unicode letters available

    """
    for i in range(BMP.min, SMP.max if smp else BMP.max):
        char = chr(i)
        if unicodedata.category(char).startswith("L"):
            yield char
