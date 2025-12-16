FauxFactory
===========

.. image:: https://github.com/omaciel/fauxfactory/workflows/Fauxfactory%20Checks/badge.svg
   :target: https://github.com/omaciel/fauxfactory/actions
   :alt: Build Status

.. image:: https://img.shields.io/pypi/pyversions/fauxfactory.svg
   :target: https://pypi.python.org/pypi/fauxfactory
   :alt: Python Compatibility

.. image:: https://img.shields.io/pypi/v/fauxfactory.svg
   :target: https://pypi.org/project/fauxfactory/
   :alt: Current Version

.. image:: https://img.shields.io/pypi/dm/fauxfactory.svg
   :target: https://pypistats.org/packages/fauxfactory
   :alt: Download Statistics

.. image:: https://coveralls.io/repos/github/omaciel/fauxfactory/badge.svg?branch=master
   :target: https://coveralls.io/github/omaciel/fauxfactory?branch=master
   :alt: Test Coverage

.. image:: https://img.shields.io/pypi/l/fauxfactory.svg
   :target: https://pypi.org/project/fauxfactory/
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
