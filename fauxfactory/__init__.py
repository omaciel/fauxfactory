"""Generate random data for your tests."""

# Note flake8 do not like star imports. It makes tracking down the file/module
# containg the symbol much harder than with explicit imports. This is an issue
# especially for a human reader. As symbols in this file were always taken from
# submodules dynamically this problem was there before introducing the start
# imports. Star imports seem to not be a problem for (perhaps) smarter tools
# like PyCharm and using them improves the analysis and navigation trough
# the code.

from fauxfactory.factories.booleans import *  # noqa: F403
from fauxfactory.factories.choices import *  # noqa: F403
from fauxfactory.factories.dates import *  # noqa: F403
from fauxfactory.factories.internet import *  # noqa: F403
from fauxfactory.factories.numbers import *  # noqa: F403
from fauxfactory.factories.strings import *  # noqa: F403
from fauxfactory.factories.structures import *  # noqa: F403
from fauxfactory.factories.systems import *  # noqa: F403

__factories = {name: obj for name, obj in locals().items() if name.startswith("gen_")}

# Add all method names to __all__
__all__ = tuple(__factories.keys())


def __dir__():
    return __all__


def __getattr__(name):
    if name in __factories:
        return __factories[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
