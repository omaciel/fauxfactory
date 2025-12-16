"""Methods that generate random number values."""

import random
import sys
from functools import partial

from fauxfactory.helpers import base_repr


def gen_integer(min_value: int | None = None, max_value: int | None = None) -> int:
    """Return a random integer value based on the current platform.

    :param int min_value: The minimum allowed value.
    :param int max_value: The maximum allowed value.
    :raises: ``ValueError`` if arguments are not integers or if they are
        less or greater than the system's allowed range for integers.
    :returns: Returns a random integer value.
    :rtype: int

    """
    # Platform-specific value range for integers
    _min_value = -sys.maxsize - 1
    _max_value = sys.maxsize

    if min_value is None:
        min_value = _min_value
    if max_value is None:
        max_value = _max_value

    integer_types = (int,)

    # Perform some validations
    if not isinstance(min_value, integer_types) or min_value < _min_value:
        raise ValueError(f'"{min_value}" is not a valid minimum.')
    if not isinstance(max_value, integer_types) or max_value > _max_value:
        raise ValueError(f'"{max_value}" is not a valid maximum.')

    value = random.randint(min_value, max_value)

    return value


def gen_negative_integer() -> int:
    """Return a random negative integer based on the current platform.

    :returns: Returns a random negative integer value.
    :rtype: int

    """
    max_value = 0

    return gen_integer(max_value=max_value)


def gen_positive_integer() -> int:
    """Return a random positive integer based on the current platform.

    :returns: A random positive integer value.
    :rtype: int

    """
    min_value = 0

    return gen_integer(min_value=min_value)


def gen_number(
    min_value: str | None = None, max_value: str | None = None, base: int = 10
) -> str:
    """Return a random number (with <base> representation).

    :returns: A random number with base of <base>.
    :rtype: str

    """
    return base_repr(
        gen_integer(
            int(str(min_value), base=base) if min_value is not None else min_value,
            int(str(max_value), base=base) if max_value is not None else max_value,
        ),
        base,
    )


gen_octagonal: partial[str] = partial(gen_number, base=8)
gen_hexadecimal: partial[str] = partial(gen_number, base=16)


__all__ = tuple(name for name in locals() if name.startswith("gen_"))


def __dir__():
    return __all__
