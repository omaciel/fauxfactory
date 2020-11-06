"""Collection of string generating functions."""
import random
import string

from fauxfactory.constants import HTML_TAGS, LOREM_IPSUM_TEXT
from fauxfactory.helpers import (
    check_len,
    check_validation,
    is_positive_int,
    unicode_letters_generator,
    )


def gen_string(str_type, length=None, validator=None, default=None, tries=10):
    """A simple wrapper that calls other string generation methods.

    :param str str_type: The type of string which should be generated.
    :param int length: The length of the generated string. Must be 1 or
        greater.
    :param validator: Function or regex (str).
        If a function it must receive one parameter and return True if value
        can be used and False of another value need to be generated.
        If str it will be used as regex to validate the generated value.
        Default is None which will not validate the value.
    :param tries: number of times validator must be called before returning
        `default`. Default is 10.
    :param default: If validator returns false a number of `tries` times, this
        value is returned instead. Must be defined if validator is not None
    :raises: ``ValueError`` if an invalid ``str_type`` is specified.
    :returns: A string.
    :rtype: str

    Valid values for ``str_type`` are as follows:

    * alpha
    * alphanumeric
    * cjk
    * cyrillic
    * html
    * latin1
    * numeric
    * utf8
    * punctuation

    """
    str_types_functions = {
        'alpha': gen_alpha,
        'alphanumeric': gen_alphanumeric,
        'cjk': gen_cjk,
        'cyrillic': gen_cyrillic,
        'html': gen_html,
        'latin1': gen_latin1,
        'numeric': gen_numeric_string,
        'utf8': gen_utf8,
        'punctuation': gen_special,
    }
    str_type_lower = str_type.lower()  # do not modify user data
    if str_type_lower not in str_types_functions.keys():
        raise ValueError(
            '{0} is not a supported string type. Valid string types are {1}.'
            ''.format(str_type_lower, ','.join(str_types_functions.keys()))
        )
    method = str_types_functions[str_type_lower]
    if length is None:
        return method(validator=validator, default=default, tries=tries)
    return method(length, validator=validator, default=default, tries=tries)


@check_len
@check_validation
def gen_alpha(length=10, start=None, separator=''):
    """Return a random string made up of alpha characters.

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :returns: A random string made up of alpha characters.
    :rtype: str

    """
    random.seed()
    output_string = ''.join(
        random.choice(string.ascii_letters) for _ in range(length)
    )

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


@check_len
@check_validation
def gen_alphanumeric(length=10, start=None, separator=''):
    """Return a random string made up of alpha and numeric characters.

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :returns: A random string made up of alpha and numeric characters.
    :rtype: str

    """
    random.seed()
    output_string = ''.join(
        random.choice(
            string.ascii_letters + string.digits
        ) for _ in range(length))

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


@check_len
@check_validation
def gen_cjk(length=10, start=None, separator=''):
    """Return a random string made up of CJK characters.

    (Source: Wikipedia - CJK Unified Ideographs)

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :returns: A random string made up of CJK characters.
    :rtype: str

    """
    random.seed()

    # Generate codepoints, then convert the codepoints to a string. The
    # valid range of CJK codepoints is 0x4E00 - 0x9FCC, inclusive.
    codepoints = [random.randint(0x4E00, 0x9FCC) for _ in range(length)]
    output_string = ''.join(chr(codepoint) for codepoint in codepoints)

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


@check_len
@check_validation
def gen_cyrillic(length=10, start=None, separator=''):
    """Return a random string made up of Cyrillic characters.

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :returns: A random string made up of Cyrillic characters.
    :rtype: str

    """
    random.seed()

    # Generate codepoints, then convert the codepoints to a string. The
    # valid range of Cyrillic codepoints is 0x0400 - 0x04FF, inclusive.
    codepoints = [random.randint(0x0400, 0x04FF) for _ in range(length)]
    output_string = ''.join(chr(codepoint) for codepoint in codepoints)

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


@check_len
@check_validation
def gen_html(length=10, include_tags=True):
    """Return a random string made up of html characters.

    :param int length: Length for random data.
    :returns: A random string made up of html characters.
    :rtype: str

    """
    random.seed()
    html_tag = random.choice(HTML_TAGS)

    if not include_tags:
        if length < 8:
            raise ValueError('Cannot generate html with less than 7 chars')
        maybe_len = length - len('<{0}></{0}>'.format(html_tag))
        if maybe_len <= 0:
            length -= 7
            html_tag = 'a'
        else:
            length = maybe_len
        output_string = u'<{0}>{1}</{0}>'.format(
            html_tag, gen_string('alpha', length))
    else:
        output_string = '<{0}>{1}</{0}>'.format(
            html_tag, gen_string('alpha', length))

    return output_string


def gen_iplum(words=None, paragraphs=None):
    """Return a lorem ipsum string.

    If no arguments are passed, then return the entire default lorem ipsum
    string.

    :param int words: The number of words to return.
    :param int paragraphs: The number of paragraphs to return.
    :raises: ``ValueError`` if ``words`` is not a valid positive integer.
    :returns: A ``lorem ipsum`` string containing either the number of
        ``words`` or ``paragraphs``, extending and wrapping around the text
        as needed to make sure that it has the specified length.
    :rtype: str

    """
    # Check parameters
    if words is None or words == 0:
        words = len(LOREM_IPSUM_TEXT.split())
    if paragraphs is None:
        paragraphs = 1

    if not isinstance(words, int) or words < 0:
        raise ValueError(
            'Cannot generate a string with negative number of words.')
    is_positive_int(paragraphs)

    # Original Lorem Ipsum string
    all_words = LOREM_IPSUM_TEXT.split()
    # How many words do we need?
    total_words_needed = words * paragraphs

    quotient = int(total_words_needed / len(all_words))
    modulus = total_words_needed % len(all_words)

    # Pool of words to use
    all_words = all_words * (quotient + modulus)

    result = u''
    start_pos = 0
    for _ in range(0, paragraphs):
        sentence = u' '.join(
            all_words[start_pos:start_pos + words])

        # Remove comma from the end, if it exists
        if sentence.endswith(','):
            sentence = sentence.rstrip(',')
        # Remove period from the end, if it exists
        if sentence.endswith('.'):
            sentence = sentence.rstrip('.')

        # Each sentence should be properly capitalized
        cap_sentence = [
            frag.capitalize() + u'.' for frag in sentence.split('. ')]

        # Add newline at the end
        result += ' '.join(cap_sentence) + u'\n'

        # Increment positional counter
        start_pos += words
    return result.rstrip()


@check_len
@check_validation
def gen_latin1(length=10, start=None, separator=''):
    """Return a random string made up of UTF-8 characters.

    (Font: Wikipedia - Latin-1 Supplement Unicode Block)

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :returns: A random string made up of ``Latin1`` characters.
    :rtype: str

    """
    range0 = range1 = range2 = []
    range0 = ['00C0', '00D6']
    range1 = ['00D8', '00F6']
    range2 = ['00F8', '00FF']
    output_array = []

    for i in range(int(range0[0], 16), int(range0[1], 16)):
        output_array.append(i)
    for i in range(int(range1[0], 16), int(range1[1], 16)):
        output_array.append(i)
    for i in range(int(range2[0], 16), int(range2[1], 16)):
        output_array.append(i)

    random.seed()
    output_string = ''.join(
        chr(random.choice(output_array)) for _ in range(length)
    )

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


@check_len
@check_validation
def gen_numeric_string(length=10, start=None, separator=''):
    """Return a random string made up of numbers.

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :returns: A random string made up of numbers.
    :rtype: str

    """
    random.seed()
    output_string = ''.join(
        random.choice(string.digits) for _ in range(length)
    )

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


@check_len
@check_validation
def gen_utf8(length=10, smp=True, start=None, separator=''):
    """Return a random string made up of UTF-8 letters characters.

    Follows `RFC 3629`_.

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :param bool smp: Include Supplementary Multilingual Plane (SMP)
        characters
    :returns: A random string made up of ``UTF-8`` letters characters.
    :rtype: str

    .. _`RFC 3629`: http://www.rfc-editor.org/rfc/rfc3629.txt

    """
    UNICODE_LETTERS = list(unicode_letters_generator(smp))
    random.seed()
    output_string = ''.join(
        [random.choice(UNICODE_LETTERS) for _ in range(length)]
    )

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


@check_len
@check_validation
def gen_special(length=10, start=None, separator=''):
    """Return a random special characters string.

    :param int length: Length for random data.
    :param str start: Random data start with.
    :param str separator: Separator character for start and random data.
    :returns: A random string made up of special characters.
    :rtype: str
    """
    random.seed()
    output_string = ''.join(
        random.choice(string.punctuation) for _ in range(length)
    )

    if start:
        output_string = '{0}{1}{2}'.format(
            start, separator, output_string)[0:length]
    return output_string


__all__ = tuple(name for name in locals() if name.startswith('gen_'))


def __dir__():
    return __all__
