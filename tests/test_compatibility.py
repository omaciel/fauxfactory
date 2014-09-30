"""Tests to help ensure that FauxFactory remains backward compatible."""
from fauxfactory import codify, FauxFactory
from functools import partial
from unittest import TestCase
import datetime
import warnings
# (too-many-public-methods) pylint:disable=R0904

GENERATORS = (
    partial(codify, 'make-me-unicode'),
    partial(FauxFactory.generate_string, 'alpha', 3),
    partial(FauxFactory.generate_alpha, 3),
    partial(FauxFactory.generate_alphanumeric, 3),
    FauxFactory.generate_boolean,
    partial(FauxFactory.generate_choice, (1, 2)),
    partial(FauxFactory.generate_cjk, 3),
    partial(
        FauxFactory.generate_date,
        datetime.date.today() - datetime.timedelta(1),
        datetime.date.today()
    ),
    partial(
        FauxFactory.generate_datetime,
        datetime.datetime.now() - datetime.timedelta(1),
        datetime.datetime.today()
    ),
    partial(FauxFactory.generate_email, 'Alice', 'example', 'com'),
    partial(FauxFactory.generate_integer, 1, 10),
    partial(FauxFactory.generate_iplum, 1, 1),
    partial(FauxFactory.generate_latin1, 3),
    FauxFactory.generate_negative_integer,
    partial(FauxFactory.generate_ipaddr, True, True),
    partial(FauxFactory.generate_mac, '-'),
    partial(FauxFactory.generate_numeric_string, 3),
    FauxFactory.generate_positive_integer,
    FauxFactory.generate_time,
    partial(FauxFactory.generate_url, 'ftp', 'example', 'com'),
    partial(FauxFactory.generate_utf8, 3),
    FauxFactory.generate_uuid,
    partial(FauxFactory.generate_html, 3),
)


class FauxFactoryTestCase(TestCase):
    """Call methods on class ``FauxFactory``."""
    def test_not_none(self):
        """Call every method on ``FauxFactory`` and provide arguments.

        This test does very little: it simply calls each method on
        ``FauxFactory``, provides a value for each possible argument, and
        asserts that the return value is not ``None``. This is not amazingly
        useful. However, it does provide a basic sanity check. It tells us that
        each wrapper method:

        * can run without raising an exception,
        * can accept an appropriate number of arguments, and
        * returns an "interesting" value.

        """

        for generator in GENERATORS:
            self.assertIsNotNone(generator())

    def test_deprecated_warning(self):
        """Check that ``FauxFactory`` functions show deprecation message.

        """

        for generator in GENERATORS:
            with warnings.catch_warnings(record=True) as faux_warn:
                self.assertIsNotNone(generator())
                self.assertIn('deprecated', str(faux_warn[-1].message))
