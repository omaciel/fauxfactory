"""Module to keep methods related to selecting values."""

import random
import uuid

from collections.abc import Iterable

from fauxfactory.helpers import check_validation


def gen_choice(choices):
    """Return a random choice from the available choices.

    :param list choices: List of choices from which select a random value.
    :raises: ``ValueError`` if ``choices`` is ``None`` or not ``Iterable`` or
        a ``dict``.
    :returns: A random element from ``choices``.

    """
    # Validation for 'choices'
    if choices is None:
        raise ValueError('Choices argument cannot be None.')
    # We don't want a single dictionary value.
    if not isinstance(choices, Iterable) or isinstance(choices, dict):
        raise ValueError('Choices argument is not iterable.')
    if not choices:
        raise ValueError('Choices argument cannot be empty.')
    # If only 1 item is present, return it right away
    if len(choices) == 1:
        return choices[0]

    random.seed()
    return random.choice(choices)


@check_validation
def gen_uuid():
    """Generate a UUID string (universally unique identifiers).

    :returns: Returns a string representation for a UUID.
    :rtype: str

    """
    return str(uuid.uuid4())


__all__ = tuple(name for name in locals() if name.startswith('gen_'))


def __dir__():
    return __all__
