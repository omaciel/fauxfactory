"""Generate random data for your tests."""
from fauxfactory.factories.booleans import *
from fauxfactory.factories.choices import *
from fauxfactory.factories.dates import *
from fauxfactory.factories.internet import *
from fauxfactory.factories.numbers import *
from fauxfactory.factories.strings import *
from fauxfactory.factories.systems import *


# Add all method names to __all__
__all__ = tuple(name for name in locals() if name.startswith('gen_'))


def __dir__():
    return __all__