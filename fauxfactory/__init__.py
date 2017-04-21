"""Generate random data for your tests."""

from fauxfactory.booleans import gen_boolean
from fauxfactory.choices import gen_choice, gen_uuid
from fauxfactory.dates import gen_date, gen_datetime, gen_time
from fauxfactory.internet import (
    gen_email,
    gen_ipaddr,
    gen_mac,
    gen_netmask,
    gen_url,
    )
from fauxfactory.numbers import (
    gen_integer,
    gen_negative_integer,
    gen_positive_integer,
    )
from fauxfactory.strings import (
    gen_alpha,
    gen_alphanumeric,
    gen_cjk,
    gen_cyrillic,
    gen_html,
    gen_iplum,
    gen_latin1,
    gen_numeric_string,
    gen_string,
    gen_utf8,
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
