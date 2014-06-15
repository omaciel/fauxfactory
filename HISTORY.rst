.. :changelog:

Release History
```````````````

0.3.0 (2014-06-15)
++++++++++++++++++

- FauxFactory is now Python 3 compatible
- Added new method generate_utf8

0.2.1 (2014-05-09)
++++++++++++++++++

- Fixed issue that prevented strings longer than the full length of
  LOREM_IPSUM_TEXT from being generated (Guthub Issue #16).

0.2.0 (2014-05-08)
++++++++++++++++++

- Added new 'Lorem Ipsum' generator.
- Changed license from LGPL3+ to Apache 2.0

0.1.3 (2014-04-16)
++++++++++++++++++

- Updated character range for CJK generator to avoid generating 'tofu'
  characters.
- Added Contributors section to README.
- New `documentation
  <http://fauxfactory.readthedocs.org/en/latest/>`_ (@faustovaz)

**Bugfixes:**

- Fixed generate_string function (@faustovaz)

0.1.2 (2014-03-19)
++++++++++++++++++

**Bugfixes:**

- Generators for ``email``, ``url`` and ``IP`` should return a unicode
  string.

0.1.1 (2014-03-17)
++++++++++++++++++

- Fixed formatting of README for better display on Pypi.

0.1.0 (2014-03-17)
++++++++++++++++++

- Initial Release.
