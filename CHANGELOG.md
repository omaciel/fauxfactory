# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.1.0] - 2025-12-17

### Added
- **New Structure Generators**: Added `gen_dict()` and `gen_json()` functions for generating complex nested data structures
  - `gen_dict()`: Generate dictionaries from schema definitions
    - Supports callable generators (e.g., `gen_alpha`, `gen_email`)
    - Supports lambda functions for parameterized generators
    - Supports nested dictionaries and lists
    - Supports literal values (strings, numbers, booleans, None)
    - Customizable list sizes via `list_sizes` parameter
    - Full validation support with `validator`, `default`, and `tries` parameters
    - Max depth protection to prevent infinite recursion (default: 10)
  - `gen_json()`: Generate JSON strings from schema definitions
    - Built on `gen_dict()` for consistency
    - Supports indentation via `indent` parameter for pretty-printing
    - Full validation support

  **Examples:**
  ```python
  from fauxfactory import gen_dict, gen_json, gen_alpha, gen_email, gen_integer

  # Simple flat dictionary
  user = gen_dict({
      'name': gen_alpha,
      'email': gen_email,
      'age': lambda: gen_integer(min_value=18, max_value=100),
      'active': True,  # literal value
  })
  # Returns: {'name': 'xKjPqR', 'email': 'abc@example.com', 'age': 42, 'active': True}

  # Nested structure with lists
  api_data = gen_dict({
      'users': [{
          'name': gen_alpha,
          'email': gen_email,
      }],
      'metadata': {
          'version': '1.0',
          'count': lambda: gen_integer(min_value=1, max_value=100),
      },
  }, list_sizes={'users': 3})

  # Generate JSON for API testing
  json_str = gen_json({
      'user': {
          'name': gen_alpha,
          'email': gen_email,
      },
      'tags': [gen_alpha],
  }, list_sizes={'tags': 5}, indent=2)
  ```

## [4.0.0] - 2025-12-16

### Changed
- **BREAKING**: Dropped support for Python 3.9
- Updated minimum Python version requirement to 3.10+

### Added
- Added support for Python 3.13 and 3.14

### Removed
- Removed obsolete Travis CI configuration

## [3.1.2] - 2025-03-04

### Added
- Add option to disable random seed

## [3.1.1] - 2024-03-26

### Changed
- Dropping support for Python 3.6, 3.7; added 3.11, 3.12
- Improve execution time of some key methods
- Better selection for CJK characters

### Fixed
- Several code linting and smell checks

## [3.1.0] - 2020-11-10

### Added
- Support static analysis and type annotation

### Changed
- CI dropped Python 3.5

## [3.0.6] - 2019-07-30

### Changed
- Change travis deploy credentials to token

## [3.0.5] - 2019-07-30

### Changed
- Update setuptools versioning, add travis deployment

## [3.0.4] - 2019-07-30

### Fixed
- Resolve flake failures in travis

## [3.0.3] - 2019-07-30

### Fixed
- Fixes for warnings on file resources

## [3.0.2] - 2018-04-10

### Fixed
- Really include facts.json to the package

## [3.0.1] - 2018-04-10

### Fixed
- Add facts.json to manifest (2217706, @m-bucher)

## [3.0.0] - 2018-04-10

### Added
- New `gen_octagonal` and `gen_hexadecimal` methods (57f5d17, @gshefer)

### Changed
- Make `gen_utf8` return optionally only BMP characters (6201b63)
- Use floor division operator in base_repr for Python 3 compatibility (914178a, @gshefer)
- Don't install tests into the binary distribution (b291873, @evgeni)

## [2.1.0] - 2017-03-30

### Added
- All methods now allow you to provide a callable which will be used to filter values being returned, the number of tries, and a default value to be returned if the filter cannot match the values being generated after the number of tries (2a7523, @renzon)

## [2.0.9] - 2016-01-12

### Changed
- Force randomness every time `random` is used to make sure that unique values are generated when running on multi-process environments, such as py.test with the pytest-xdist plugin

## [2.0.8] - 2015-09-18

### Changed
- Updated the `gen_mac` method to allow the generation of unicast/multicast and globally/locally MAC addresses

## [2.0.7] - 2015-05-28

### Changed
- Updated the `gen_ipaddr` method to allow the generation of IP addresses that start with a valid range prefix (048715d, @mfalesni)

## [2.0.6] - 2015-02-24

### Added
- Added support for **Python 2.6**

### Changed
- Cleaned up the MANIFEST file

## [2.0.5] - 2015-02-16

### Changed
- Improved the unicode letters generator to avoid returning control characters and other non-letter characters

## [2.0.4] - 2014-12-19

### Fixed
- Altered `gen_integer` to properly check for long() on Python 2

## [2.0.3] - 2014-12-17

### Changed
- Dropped the class-wide FauxFactory deprecation warning
- Refactored the `deprecated` decorator function to comply with pylint and flake8
- Make gen_netmask verify function arguments
- Improvements to constants and documentation

### Fixed
- Make `gen_netmask` raise a `ValueError` if `min_cidr` is less than 0 or `max_cidr` is greater than 32. Add tests for this boundary checking code

## [2.0.2] - 2014-10-06

### Added
- Added new netmask random generator

## [2.0.1] - 2014-09-30

### Added
- Added a default length of 10 to all string generator functions

### Changed
- Display deprecation warnings if `FauxFactory` and any of its functions are used, instructing the user to use the newer functions instead

## [2.0.0] - 2014-09-23

### Changed
- **BREAKING**: Renamed all generator functions to use the prefix "gen_" instead of "generate_". For example, `generate_date` is now `gen_date`
- All generators are now stand-alone functions and can be imported directly from `fauxfactory`. For example, `from fauxfactory import gen_date`
- Backwards compatibility with version 1.x maintained
- Polished documentation

## [1.0.1] - 2014-09-18

### Changed
- Updated `generate_string` to also accept `html` strings

## [1.0.0] - 2014-09-17

### Added
- Added new method generate_html
- Added new makefile

## [0.3.1] - 2014-07-10

### Fixed
- Check for sys.maxunicode when generating utf8 characters

## [0.3.0] - 2014-06-15

### Added
- FauxFactory is now Python 3 compatible
- Added new method generate_utf8

## [0.2.1] - 2014-05-09

### Fixed
- Fixed issue that prevented strings longer than the full length of LOREM_IPSUM_TEXT from being generated (Github Issue #16)

## [0.2.0] - 2014-05-08

### Added
- Added new 'Lorem Ipsum' generator

### Changed
- Changed license from LGPL3+ to Apache 2.0

## [0.1.3] - 2014-04-16

### Added
- Added Contributors section to README
- New [documentation](http://fauxfactory.readthedocs.org/en/latest/) (@faustovaz)

### Changed
- Updated character range for CJK generator to avoid generating 'tofu' characters

### Fixed
- Fixed generate_string function (@faustovaz)

## [0.1.2] - 2014-03-19

### Fixed
- Generators for `email`, `url` and `IP` should return a unicode string

## [0.1.1] - 2014-03-17

### Fixed
- Fixed formatting of README for better display on Pypi

## [0.1.0] - 2014-03-17

### Added
- Initial Release

[4.1.0]: https://github.com/omaciel/fauxfactory/compare/v4.0.0...v4.1.0
[4.0.0]: https://github.com/omaciel/fauxfactory/compare/v3.1.2...v4.0.0
[3.1.2]: https://github.com/omaciel/fauxfactory/compare/v3.1.1...v3.1.2
[3.1.1]: https://github.com/omaciel/fauxfactory/compare/v3.1.0...v3.1.1
[3.1.0]: https://github.com/omaciel/fauxfactory/compare/v3.0.6...v3.1.0
[3.0.6]: https://github.com/omaciel/fauxfactory/compare/v3.0.5...v3.0.6
[3.0.5]: https://github.com/omaciel/fauxfactory/compare/v3.0.4...v3.0.5
[3.0.4]: https://github.com/omaciel/fauxfactory/compare/v3.0.3...v3.0.4
[3.0.3]: https://github.com/omaciel/fauxfactory/compare/v3.0.2...v3.0.3
[3.0.2]: https://github.com/omaciel/fauxfactory/compare/v3.0.1...v3.0.2
[3.0.1]: https://github.com/omaciel/fauxfactory/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.com/omaciel/fauxfactory/compare/v2.1.0...v3.0.0
[2.1.0]: https://github.com/omaciel/fauxfactory/compare/v2.0.9...v2.1.0
[2.0.9]: https://github.com/omaciel/fauxfactory/compare/v2.0.8...v2.0.9
[2.0.8]: https://github.com/omaciel/fauxfactory/compare/v2.0.7...v2.0.8
[2.0.7]: https://github.com/omaciel/fauxfactory/compare/v2.0.6...v2.0.7
[2.0.6]: https://github.com/omaciel/fauxfactory/compare/v2.0.5...v2.0.6
[2.0.5]: https://github.com/omaciel/fauxfactory/compare/v2.0.4...v2.0.5
[2.0.4]: https://github.com/omaciel/fauxfactory/compare/v2.0.3...v2.0.4
[2.0.3]: https://github.com/omaciel/fauxfactory/compare/v2.0.2...v2.0.3
[2.0.2]: https://github.com/omaciel/fauxfactory/compare/v2.0.1...v2.0.2
[2.0.1]: https://github.com/omaciel/fauxfactory/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/omaciel/fauxfactory/compare/v1.0.1...v2.0.0
[1.0.1]: https://github.com/omaciel/fauxfactory/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/omaciel/fauxfactory/compare/v0.3.1...v1.0.0
[0.3.1]: https://github.com/omaciel/fauxfactory/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/omaciel/fauxfactory/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/omaciel/fauxfactory/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/omaciel/fauxfactory/compare/v0.1.3...v0.2.0
[0.1.3]: https://github.com/omaciel/fauxfactory/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/omaciel/fauxfactory/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/omaciel/fauxfactory/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/omaciel/fauxfactory/releases/tag/v0.1.0
