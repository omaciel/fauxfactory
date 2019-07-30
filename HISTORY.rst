.. :changelog:

Release History
===============

3.0.6 (2019-07-30)
------------------

- Change travis deploy credentials to token

3.0.5 (2019-07-30)
------------------

- Update setuptools versioning, add travis deployment

3.0.4 (2019-07-30)
------------------

- Resolve flake failures in travis

3.0.3 (2019-07-30)
------------------

- Fixes for warnings on file resources

3.0.2 (2018-04-10)
------------------

- Really include facts.json to the package

3.0.1 (2018-04-10)
------------------

- Add facts.json to manifest (2217706, @m-bucher)

3.0.0 (2018-04-10)
------------------

- Make `gen_utf8` return optionally only BMP characters
  (6201b63)
- Don't install tests into the binary distribution 
  (b291873, @evgeni)
- Use floor division operator in base_repr for Python 3
  compatibility (914178a, @gshefer)
- New `gen_octagonal` and `gen_hexadecimal` methods added
  (57f5d17,  @gshefer)

2.1.0 (2017-03-30)
------------------

- All methods now allow you to provide a callable which will be
  used to filter values being returned, the number of tries, and
  a default value to be returned if the filter cannot match the
  values being generated after the number of tries. (2a7523, @renzon)

2.0.9 (2016-01-12)
------------------

- Force randomness every time `random` is used to make sure
  that unique values are generated when running on multi-process
  environments, such as py.test with the pytest-xdist plugin.

2.0.8 (2015-09-18)
------------------

- Updated the `gen_mac` method to allow the generation of
  unicast/multicast and globally/locally MAC addresses.

2.0.7 (2015-05-28)
------------------

- Updated the `gen_ipaddr` method to allow the generation of IP
  addresses that start with a valid range prefix. (048715d, @mfalesni)

2.0.6 (2015-02-24)
------------------

- Added support for **Python 2.6**.
- Cleaned up the MANIFEST file.

2.0.5 (2015-02-16)
------------------

- Improved the unicode letters generator to avoid returning control
  characters and other non-letter characters.

2.0.4 (2014-12-19)
------------------

- Altered `gen_integer` to properly check for long() on Python 2.

2.0.3 (2014-12-17)
------------------

- Dropped the class-wide FauxFactory deprecation warning.
- Refactored the `deprecated` decorator function to comply with pylint
  and flake8.
- Make gen_netmask verify function arguments.
-  Make `gen_netmask` raise a `ValueError` if `min_cidr` is less than
   0 or `max_cidr` is greater than 32. Add tests for this boundary
   checking code.
- Improvements to constants and documentation.


2.0.2 (2014-10-06)
------------------

- Added new netmask random generator.

2.0.1 (2014-09-30)
------------------

- Added a default length of 10 to all string generator functions.
- Display deprecation warnings if ``FauxFactory`` and any of its
  functions are used, instructing the user to use the newer functions
  instead.

2.0.0 (2014-09-23)
------------------

- All generators are now stand-alone functions and can be imported
  directly from ``fauxfactory``. For example, ``from fauxfactory
  import gen_date``
- Renamed all generator functions to use the prefix "gen\_" instead of
  "generate\_". For example, ``generate_date`` is now ``gen_date``.
- Backwards compatibility with version 1.x.
- Polished documentation.

1.0.1 (2014-09-18)
------------------

- Updated ``generate_string`` to also accept ``html`` strings.

1.0.0 (2014-09-17)
------------------

- Added new method generate_html
- Added new makefile

0.3.1 (2014-07-10)
------------------

- Check for sys.maxunicode when generating utf8 characters.

0.3.0 (2014-06-15)
------------------

- FauxFactory is now Python 3 compatible
- Added new method generate_utf8

0.2.1 (2014-05-09)
------------------

- Fixed issue that prevented strings longer than the full length of
  LOREM_IPSUM_TEXT from being generated (Github Issue #16).

0.2.0 (2014-05-08)
------------------

- Added new 'Lorem Ipsum' generator.
- Changed license from LGPL3+ to Apache 2.0

0.1.3 (2014-04-16)
------------------

- Updated character range for CJK generator to avoid generating 'tofu'
  characters.
- Added Contributors section to README.
- New `documentation
  <http://fauxfactory.readthedocs.org/en/latest/>`_ (@faustovaz)

**Bugfixes:**

- Fixed generate_string function (@faustovaz)

0.1.2 (2014-03-19)
------------------

**Bugfixes:**

- Generators for ``email``, ``url`` and ``IP`` should return a unicode
  string.

0.1.1 (2014-03-17)
------------------

- Fixed formatting of README for better display on Pypi.

0.1.0 (2014-03-17)
------------------

- Initial Release.
