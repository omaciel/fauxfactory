FauxFactory
===========

**FauxFactory** generates random data for your automated tests easily!

There are times when you're writing tests for your application when you need to
pass random, non-specific data to the areas you are testing. For these scenarios
when all you need is a random string, numbers, dates, times, email address, IP,
etc, then FauxFactory can help!

Installation
------------

FauxFactory is available in PyPi and can be installed using pip::

    $ pip install fauxfactory

You can install FauxFactory by downloading the latest version of the source
code::

    $ git clone git@github.com:omaciel/fauxfactory.git
    $ cd fauxfactory
    $ python setup.py build install

Usage
-----

.. testsetup::

    import os
    import sys
    ROOT_PATH = os.path.abspath(os.path.pardir)
    if ROOT_PATH not in sys.path:
        sys.path.append(ROOT_PATH)
    import fauxfactory

Need a 15 character string for one of your tests?

.. doctest::

    >>> string = fauxfactory.gen_string('alphanumeric', 15)
    >>> string.isalnum()
    True
    >>> len(string)
    15

Need a 5 character numeric string?

.. doctest::

    >>> string = fauxfactory.gen_string('numeric', 5)
    >>> string.isnumeric()
    True
    >>> len(string)
    5

Now, let's say you need a random date:

.. doctest::

    >>> import datetime
    >>> isinstance(fauxfactory.gen_date(), datetime.date)
    True
    >>> isinstance(fauxfactory.gen_datetime(), datetime.datetime)
    True

Or a fake email with your company domain:

.. doctest::

    >>> email = fauxfactory.gen_email(domain='mycompany')
    >>> '@mycompany' in email
    True

Simple, right?

Validation
----------

All string functions allow validation of inputs using 3 parameters:

#. validator: a callable or str with regex returning boolean signaling if
   random data is valid or not.
#. tries: maximum number of times random data will be generated after
   failing validation. If the limit is reached "default" parameter will be
   returned.
#. default: value to be returned if validation fails a "tries" number of times.


Example using callable:

.. doctest::

    >>> def start_a(value):
    ...     return value[0] == 'a'
    >>> email = fauxfactory.gen_email(validator=start_a, default = 'a@b.c')
    >>> email[0] == 'a'
    True


Example using regex:

.. doctest::

    >>> n = fauxfactory.gen_string(
    ... 'numeric', validator='[^0].*', default = '2')
    >>> n != '0'
    True

Example using tries and default:

.. doctest::

    >>> def always_false(value):
    ...     print('Executed')
    ...     return False
    >>> fauxfactory.gen_alpha(
    ... validator=always_false, default = 'default value', tries=1)
    Executed
    'default value'
    >>> fauxfactory.gen_alpha(
    ... validator=always_false, default = 'default value 2', tries=3)
    Executed
    Executed
    Executed
    'default value 2'

API
---

For a full list of available methods, see the :doc:`API documentation <./api>`.

.. toctree::
    :hidden:

    api

Contribute
----------

#. Fork `the repository`_ on GitHub and make some changes. Make sure to add
   yourself to `AUTHORS`_.
#. Install the development requirements. ``pip install -r
   requirements-optional.txt``.
#.  Test your changes.

    #. Run ``make test-all`` and make sure nothing has broken.
    #. Run ``coverage report --show-missing`` to check for untested code.
    #. Add tests to the ``tests/`` directory if appropriate.

    Repeat this cycle as needed.

#. Send a pull request and bug the maintainer until it gets merged and
   published. :)

.. _`the repository`: http://github.com/omaciel/fauxfactory
.. _`AUTHORS`: https://github.com/omaciel/fauxfactory/blob/master/AUTHORS.rst
