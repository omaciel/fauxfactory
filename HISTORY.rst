.. :changelog:

Release History
===============

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
