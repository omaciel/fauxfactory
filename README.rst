FauxFactory
===========

.. image:: https://travis-ci.org/omaciel/fauxfactory.png?branch=master
   :target: https://travis-ci.org/omaciel/fauxfactory
   :alt: Build Status

.. image:: https://img.shields.io/pypi/pyversions/fauxfactory.svg
   :target: https://pypi.python.org/pypi/fauxfactory
   :alt: Python Compatibility

.. image:: https://badge.fury.io/py/fauxfactory.png
   :target: http://badge.fury.io/py/fauxfactory
   :alt: Current Version

.. image:: https://img.shields.io/pypi/dm/fauxfactory.svg
   :target: https://crate.io/packages/fauxfactory/
   :alt: Download Statistics

.. image:: https://coveralls.io/repos/omaciel/fauxfactory/badge.png?branch=master
   :target: https://coveralls.io/r/omaciel/fauxfactory?branch=master
   :alt: Test Coverage

.. image:: https://img.shields.io/pypi/l/fauxfactory.svg
   :target: https://pypi.python.org/pypi/fauxfactory/
   :alt: License

**FauxFactory** generates random data for your automated tests easily!

There are times when you're writing tests for your application when you need to
pass random, non-specific data to the areas you are testing. For these scenarios
when all you need is a random string, numbers, dates, times, email address, IP,
etc, then FauxFactory can help!

The `full documentation
<http://fauxfactory.readthedocs.org/en/latest/index.html>`_ is available on
ReadTheDocs. It can also be generated locally::

    pip install -r requirements-optional.txt
    make docs-html
