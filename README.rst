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
or even complex nested data structures, FauxFactory can help!

✨ What's New in 4.2.0
----------------------

FauxFactory 4.2.0 introduces powerful structured data generation capabilities:

**New in 4.2.0:**

- 🎯 ``gen_list()`` - Generate lists directly from item schemas
- Support for callable generators, dict/list schemas, and literal values
- Customizable list sizes with full validation support

**New in 4.1.0:**

- 🏗️ ``gen_dict()`` - Generate complex dictionaries from schema definitions
- 📄 ``gen_json()`` - Generate JSON strings from schemas
- Support for nested structures, callable generators, and custom list sizes
- Built-in validation with ``validator``, ``default``, and ``tries`` parameters

**New in 4.0.0:**

- 🐍 Python 3.10+ required (supports Python 3.13 and 3.14)
- Modernized codebase with improved performance

🚀 Quick Start
--------------

Installation
~~~~~~~~~~~~

.. code-block:: bash

    pip install fauxfactory

Or with modern package managers:

.. code-block:: bash

    uv add fauxfactory      # Using uv
    poetry add fauxfactory  # Using Poetry

Basic Usage
~~~~~~~~~~~

.. code-block:: python

    from fauxfactory import gen_alpha, gen_email, gen_integer, gen_ipaddr

    # Generate random data
    username = gen_alpha(length=10)          # 'xKjPqRmNoP'
    email = gen_email()                      # 'abc@example.com'
    age = gen_integer(min_value=18, max_value=100)  # 42
    ip = gen_ipaddr()                        # '192.168.1.1'

📚 Feature Highlights
---------------------

Simple Data Types
~~~~~~~~~~~~~~~~~

Generate various types of random data with ease:

.. code-block:: python

    from fauxfactory import (
        gen_alpha, gen_alphanumeric, gen_email, gen_url,
        gen_ipaddr, gen_mac, gen_date, gen_boolean, gen_uuid
    )

    # Strings
    name = gen_alpha(length=15)
    code = gen_alphanumeric(length=8)

    # Internet data
    email = gen_email()
    website = gen_url()
    ip_address = gen_ipaddr()
    mac_address = gen_mac()

    # Other types
    birth_date = gen_date()
    is_active = gen_boolean()
    user_id = gen_uuid()

Structured Data (New!)
~~~~~~~~~~~~~~~~~~~~~~~

Generate complex, nested data structures that mirror real-world scenarios:

**Lists**

.. code-block:: python

    from fauxfactory import gen_list, gen_alpha, gen_email, gen_integer

    # Simple list of strings
    tags = gen_list(gen_alpha, size=5)
    # ['xKjPqR', 'mNoPqR', 'aBcDeF', 'ghIjKl', 'mnOpQr']

    # List of dictionaries
    users = gen_list({
        'name': gen_alpha,
        'email': gen_email,
        'active': True,
    }, size=3)
    # [
    #     {'name': 'xKjPqR', 'email': 'abc@example.com', 'active': True},
    #     {'name': 'mNoPqR', 'email': 'def@example.com', 'active': True},
    #     {'name': 'aBcDeF', 'email': 'ghi@example.com', 'active': True},
    # ]

**Dictionaries**

.. code-block:: python

    from fauxfactory import gen_dict, gen_alpha, gen_email, gen_integer

    # Complex user profile
    user = gen_dict({
        'name': gen_alpha,
        'email': gen_email,
        'age': lambda: gen_integer(min_value=18, max_value=100),
        'active': True,
        'preferences': {
            'theme': 'dark',
            'notifications': True,
        },
        'tags': [gen_alpha],
    }, list_sizes={'tags': 5})

**JSON for API Testing**

.. code-block:: python

    from fauxfactory import gen_json, gen_alpha, gen_email, gen_integer

    # Generate API payload
    payload = gen_json({
        'user': {
            'name': gen_alpha,
            'email': gen_email,
        },
        'metadata': {
            'version': '1.0',
            'count': lambda: gen_integer(min_value=1, max_value=100),
        },
    }, indent=2)

Validation Support
~~~~~~~~~~~~~~~~~~

Many generators support validation to ensure generated data meets your criteria:

.. code-block:: python

    from fauxfactory import gen_alpha, gen_email

    # Generate username with specific pattern
    def is_valid_username(name):
        return name.isalnum() and 3 <= len(name) <= 20

    username = gen_alpha(
        length=15,
        validator=is_valid_username,
        default='default_user',
        tries=100
    )

    # Generate email matching domain pattern
    def is_corporate_email(email):
        return email.endswith('@company.com')

    email = gen_email(
        validator=is_corporate_email,
        default='user@company.com',
        tries=100
    )

💡 Why Use FauxFactory?
-----------------------

1. **Avoid Static Test Data**
   Static data can lead to false positives. Random data ensures your code handles various inputs correctly.

2. **Realistic Test Data Without Hassle**
   No more manually crafting test data or maintaining fixture files.

3. **Better Test Coverage**
   Generate edge cases and boundary values automatically.

4. **Simplify API Testing**
   Create complex JSON payloads for REST API tests effortlessly.

5. **Database Seeding**
   Populate test databases with hundreds or thousands of realistic records quickly.

6. **Framework Agnostic**
   Works seamlessly with pytest, unittest, nose, and any other testing framework.

🎯 Real-World Examples
----------------------

E-Commerce Testing
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from fauxfactory import gen_dict, gen_alpha, gen_email, gen_integer

    # Generate complete order data
    order = gen_dict({
        'order_id': lambda: gen_integer(min_value=10000, max_value=99999),
        'customer': {
            'name': gen_alpha,
            'email': gen_email,
        },
        'products': [{
            'sku': lambda: gen_alpha(length=8).upper(),
            'quantity': lambda: gen_integer(min_value=1, max_value=5),
            'price': lambda: gen_integer(min_value=500, max_value=50000) / 100,
        }],
        'status': 'pending',
    }, list_sizes={'products': 3})

API Integration Testing
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from fauxfactory import gen_json, gen_alpha, gen_email

    # Test API with random payloads
    payload = gen_json({
        'users': [{
            'name': gen_alpha,
            'email': gen_email,
            'role': 'user',
        }]
    }, list_sizes={'users': 5}, indent=2)

    response = api_client.post('/users/batch', data=payload)
    assert response.status_code == 201

Database Seeding
~~~~~~~~~~~~~~~~

.. code-block:: python

    from fauxfactory import gen_list, gen_alpha, gen_email, gen_boolean

    # Generate 100 test users
    users = gen_list({
        'username': gen_alpha,
        'email': gen_email,
        'is_active': gen_boolean,
        'role': 'user',
    }, size=100)

    db.users.insert_many(users)

Pytest Fixtures
~~~~~~~~~~~~~~~

.. code-block:: python

    import pytest
    from fauxfactory import gen_alpha, gen_email, gen_integer

    @pytest.fixture
    def random_user():
        """Provide fresh random user for each test."""
        return {
            'id': gen_integer(min_value=1, max_value=10000),
            'username': gen_alpha(length=10),
            'email': gen_email(),
        }

    def test_user_creation(random_user):
        user = create_user(random_user)
        assert user.username == random_user['username']

📖 Available Generators
-----------------------

Strings
~~~~~~~
- ``gen_alpha()`` - Alphabetic strings
- ``gen_alphanumeric()`` - Alphanumeric strings
- ``gen_numeric_string()`` - Numeric strings
- ``gen_utf8()`` - UTF-8 strings
- ``gen_latin1()`` - Latin-1 strings
- ``gen_cjk()`` - CJK (Chinese, Japanese, Korean) characters
- ``gen_cyrillic()`` - Cyrillic strings
- ``gen_html()`` - HTML strings
- ``gen_special()`` - Special characters
- ``gen_lorem_ipsum()`` - Lorem ipsum text

Numbers
~~~~~~~
- ``gen_integer()`` - Random integers with min/max
- ``gen_float()`` - Random floats

Internet
~~~~~~~~
- ``gen_email()`` - Email addresses
- ``gen_url()`` - URLs
- ``gen_ipaddr()`` - IP addresses (IPv4/IPv6)
- ``gen_mac()`` - MAC addresses
- ``gen_netmask()`` - Network masks
- ``gen_domain()`` - Domain names

Dates & Times
~~~~~~~~~~~~~
- ``gen_date()`` - Random dates
- ``gen_time()`` - Random times
- ``gen_datetime()`` - Random datetimes

Identifiers
~~~~~~~~~~~
- ``gen_uuid()`` - UUIDs

Choices
~~~~~~~
- ``gen_choice()`` - Random choice from a list
- ``gen_boolean()`` - Random boolean

Structures (New!)
~~~~~~~~~~~~~~~~~
- ``gen_dict()`` - Dictionaries from schemas
- ``gen_json()`` - JSON from schemas
- ``gen_list()`` - Lists from item schemas

📝 Documentation
----------------

The `full documentation <http://fauxfactory.readthedocs.org/en/latest/index.html>`_
is available on ReadTheDocs.

Generate documentation locally::

    pip install -r requirements-optional.txt
    make docs-html

🤝 Contributing
---------------

Contributions are welcome! Please feel free to submit a Pull Request.

📜 License
----------

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

🔗 Links
--------

- **Documentation:** https://fauxfactory.readthedocs.org
- **PyPI:** https://pypi.org/project/fauxfactory/
- **Source Code:** https://github.com/omaciel/fauxfactory
- **Issue Tracker:** https://github.com/omaciel/fauxfactory/issues
