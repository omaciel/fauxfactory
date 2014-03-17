FauxFactory
===========

.. |build| image:: https://travis-ci.org/omaciel/fauxfactory.png?branch=master   :target: https://travis-ci.org/omaciel/fauxfactory


**FauxFactory** generates random data for your automated tests easily!

**Build Status** |build|

Available methods are:

* FauxFactory.generate_alpha
* FauxFactory.generate_alphanumeric
* FauxFactory.generate_boolean
* FauxFactory.generate_choice
* FauxFactory.generate_cjk
* FauxFactory.generate_date
* FauxFactory.generate_datetime
* FauxFactory.generate_email
* FauxFactory.generate_integer
* FauxFactory.generate_ipaddr
* FauxFactory.generate_latin1
* FauxFactory.generate_mac
* FauxFactory.generate_negative_integer
* FauxFactory.generate_numeric_string
* FauxFactory.generate_positive_integer
* FauxFactory.generate_string
* FauxFactory.generate_time
* FauxFactory.generate_url
* FauxFactory.generate_uuid

Examples
--------

>>> In [1]: from fauxfactory import FauxFactory

>>> In [2]: FauxFactory.generate_alphanumeric()
>>> Out[2]: '3MVWA'

>>> In [3]: FauxFactory.generate_alphanumeric(length=15)
>>> Out[3]: 'Cxju7QlNhLMSzaV'

>>> In [4]: FauxFactory.generate_cjk()
>>> Out[4]: u'\u7914\u4f5e\u58cb\u63e5\u56ef'

>>> In [5]: FauxFactory.generate_latin1()
>>> Out[5]: u'\xea\xd4\xf2\xfa\xe5'

>>> In [6]: FauxFactory.generate_url()
>>> Out[6]: 'http://test.edu'

>>> In [7]: FauxFactory.generate_url(scheme='https', tlds='io')
>>> Out[7]: 'https://test.io'

>>> In [8]: FauxFactory.generate_ipaddr()
>>> Out[8]: '42.237.22.59'

>>> In [9]: FauxFactory.generate_datetime()
>>> Out[9]: datetime.datetime(2225, 5, 22, 18, 19, 12, 452661)

>>> In [10]: FauxFactory.generate_uuid()
>>> Out[10]: u'81670150-ed11-4b28-88a0-7f61ba8338c4'

>>> In [11]: FauxFactory.generate_email()
>>> Out[11]: 'lVYREmpx@example.biz'

>>> In [12]: FauxFactory.generate_time()
>>> Out[12]: datetime.time(22, 51, 2, 154172)

>>> In [13]: FauxFactory.generate_choice(['green', 'yellow', 'blue', 'white'])
>>> Out[13]: 'white'

>>> In [14]: FauxFactory.generate_url(subdomain=FauxFactory.generate_alpha())
>>> Out[14]: 'ftp://GtDPI.gov'

Installation
------------

`FauxFactory is available at PyPI <http://pypi.python.org/pypi/fauxfactory>`_, so
installing it is as simple as executing::

    pip install fauxfactory

Or you can download the latest version and install it using ``setup.py``::

    git clone git@github.com:omaciel/fauxfactory.git
    cd fauxfactory
    python setup.py build install
