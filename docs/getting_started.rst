Getting Started
===============

.. testsetup::

    import os
    import sys
    ROOT_PATH = os.path.abspath(os.path.pardir)
    if ROOT_PATH not in sys.path:
        sys.path.append(ROOT_PATH)
    from fauxfactory import FauxFactory

FauxFactory generates random data for your automated tests easily!

Need a 10 characters string for one of your tests?

.. doctest::

    >>> string = FauxFactory.generate_string('alphanumeric', 10)
    >>> string.isalnum()
    True
    >>> len(string)
    10

Need a 5 character numeric string?

.. doctest::

    >>> string = FauxFactory.generate_string('numeric', 5)
    >>> string.isnumeric()
    True
    >>> len(string)
    5

Now, let's say you need a random date:

.. doctest::

    >>> import datetime
    >>> isinstance(FauxFactory.generate_date(), datetime.date)
    True
    >>> isinstance(FauxFactory.generate_datetime(), datetime.datetime)
    True

Or a fake email with your company domain:

.. doctest::

    >>> email = FauxFactory.generate_email(domain='mycompany')
    >>> '@mycompany' in email
    True

Simple, right?
