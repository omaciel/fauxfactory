FauxFactory
===========

.. image:: https://travis-ci.org/omaciel/fauxfactory.png?branch=master
   :target: https://travis-ci.org/omaciel/fauxfactory

.. image:: https://badge.fury.io/py/fauxfactory.png
   :target: http://badge.fury.io/py/fauxfactory

.. image:: https://pypip.in/d/fauxfactory/badge.png
   :target: https://crate.io/packages/fauxfactory/

.. image:: https://coveralls.io/repos/omaciel/fauxfactory/badge.png?branch=master
   :target: https://coveralls.io/r/omaciel/fauxfactory?branch=master

**FauxFactory** generates random data for your automated tests easily!

There are times when you're writing tests for your application when
you need to pass random, non-specific data to the areas you are
testing. For these scenarios when all you need is a random string,
numbers, dates, times, email address, IP, etc, then FauxFactory can
help!

Available methods
-----------------

- generate_alpha
- generate_alphanumeric
- generate_boolean
- generate_choice
- generate_cjk
- generate_date
- generate_datetime
- generate_email
- generate_integer
- generate_ipaddr
- generate_iplum
- generate_latin1
- generate_mac
- generate_negative_integer
- generate_numeric_string
- generate_positive_integer
- generate_string
- generate_time
- generate_url
- generate_utf8
- generate_uuid

Examples
--------

Some examples::

    >>> In [0]: from fauxfactory import FauxFactory

    >>> In [2]: FauxFactory.generate_alphanumeric()
    >>> Out[2]: u'3MVWA'

    >>> In [3]: FauxFactory.generate_alphanumeric(length=15)
    >>> Out[3]: u'Cxju7QlNhLMSzaV'

    >>> In [4]: FauxFactory.generate_cjk()
    >>> Out[4]: u'\u7914\u4f5e\u58cb\u63e5\u56ef'

    >>> In [5]: FauxFactory.generate_latin1()
    >>> Out[5]: u'\xea\xd4\xf2\xfa\xe5'

    >>> In [6]: FauxFactory.generate_url()
    >>> Out[6]: u'http://test.edu'

    >>> In [7]: FauxFactory.generate_url(scheme='https', tlds='io')
    >>> Out[7]: u'https://test.io'

    >>> In [8]: FauxFactory.generate_ipaddr()
    >>> Out[8]: u'42.237.22.59'

    >>> In [9]: FauxFactory.generate_datetime()
    >>> Out[9]: datetime.datetime(2225, 5, 22, 18, 19, 12, 452661)

    >>> In [10]: FauxFactory.generate_uuid()
    >>> Out[10]: u'81670150-ed11-4b28-88a0-7f61ba8338c4'

    >>> In [11]: FauxFactory.generate_email()
    >>> Out[11]: u'lVYREmpx@example.biz'

    >>> In [12]: FauxFactory.generate_time()
    >>> Out[12]: datetime.time(22, 51, 2, 154172)

    >>> In [13]: FauxFactory.generate_choice(['green', 'yellow', 'blue', 'white'])
    >>> Out[13]: 'white'

    >>> In [14]: FauxFactory.generate_url(subdomain=FauxFactory.generate_alpha())
    >>> Out[14]: u'ftp://GtDPI.gov'

    >>> In [15]: FauxFactory.generate_iplum()
    >>> Out[15]: u'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    >>> In [16]: FauxFactory.generate_utf8()
    >>> Out[16]: u'\U00042a80\U000fb486\U00010c58\U000f2b5e\U00051c5c'

Installation
------------

`FauxFactory is available at PyPI <http://pypi.python.org/pypi/fauxfactory>`_, so
installing it is as simple as executing::

    $ pip install fauxfactory

Or you can download the latest version and install it using ``setup.py``::

    $ git clone git@github.com:omaciel/fauxfactory.git
    $ cd fauxfactory
    $ python setup.py build install

Contribute
----------

#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to `AUTHORS`_.

.. _`the repository`: http://github.com/omaciel/fauxfactory
.. _`AUTHORS`: https://github.com/omaciel/fauxfactory/blob/master/AUTHORS.rst
