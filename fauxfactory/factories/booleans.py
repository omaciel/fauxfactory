"""Method for generating random boolean values."""

from .choices import gen_choice


def gen_boolean():
    """Return a random Boolean value.

    :returns: A random Boolean value.
    :rtype: bool

    """
    choices = (True, False)

    return gen_choice(choices)


__all__ = tuple(name for name in locals() if name.startswith('gen_'))
