"""Generate random data for your tests."""

# Note flake8 do not like star imports. It makes tracking down the file/module
# containg the symbol much harder than with explicit imports. This is an issue
# especially for a human reader. As symbols in this file were always taken from
# submodules dynamically this problem was there before introducing the start
# imports. Star imports seem to not be a problem for (perhaps) smarter tools
# like PyCharm and using them improves the analysis and navigation trough
# the code.

from fauxfactory.factories.booleans import *  # noqa: F401, F403
from fauxfactory.factories.choices import *  # noqa: F401, F403
from fauxfactory.factories.dates import *  # noqa: F401, F403
from fauxfactory.factories.internet import *  # noqa: F401, F403
from fauxfactory.factories.numbers import *  # noqa: F401, F403
from fauxfactory.factories.strings import *  # noqa: F401, F403
from fauxfactory.factories.systems import *  # noqa: F401, F403


# Add all method names to __all__
__all__ = tuple(name for name in locals() if name.startswith('gen_'))


def __dir__():
    return __all__
