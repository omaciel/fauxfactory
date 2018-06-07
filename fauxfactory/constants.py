"""Constants used by :mod:`fauxfactory`.

.. data:: VALID_NETMASKS

    A tuple of netmasks. The tuple index corresponds to a CIDR value. For
    example, a CIDR of "/1" corresponds to `VALID_NETMASKS[1]`.

"""
# The above constant descriptions can be found by Sphinx and via help().
import datetime
import json
import os
import string


VALID_DIGITS = string.digits + string.ascii_letters

FACTS_JSON_FILE = os.path.join(os.path.dirname(__file__), 'facts.json')
with open(FACTS_JSON_FILE) as data:
    FACTS_JSON = json.load(data)

LOREM_IPSUM_TEXT = (
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
    'eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad '
    'minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip '
    'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
    'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur '
    'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt '
    'mollit anim id est laborum.'
)

MIN_YEARS = datetime.MINYEAR
MAX_YEARS = 1000  # 1000 years into the future

SCHEMES = (
    'http',
    'https',
    'ftp',
)

SUBDOMAINS = (
    'example',
    'test',
)

TLDS = (
    'biz',
    'com',
    'edu',
    'gov',
    'info',
    'org',
)

VALID_NETMASKS = (
    u'0.0.0.0',
    u'128.0.0.0',
    u'192.0.0.0',
    u'224.0.0.0',
    u'240.0.0.0',
    u'248.0.0.0',
    u'252.0.0.0',
    u'254.0.0.0',
    u'255.0.0.0',
    u'255.128.0.0',
    u'255.192.0.0',
    u'255.224.0.0',
    u'255.240.0.0',
    u'255.248.0.0',
    u'255.252.0.0',
    u'255.254.0.0',
    u'255.255.0.0',
    u'255.255.128.0',
    u'255.255.192.0',
    u'255.255.224.0',
    u'255.255.240.0',
    u'255.255.248.0',
    u'255.255.252.0',
    u'255.255.254.0',
    u'255.255.255.0',
    u'255.255.255.128',
    u'255.255.255.192',
    u'255.255.255.224',
    u'255.255.255.240',
    u'255.255.255.248',
    u'255.255.255.252',
    u'255.255.255.254',
    u'255.255.255.255',
)

HTML_TAGS = (
    'a', 'abbr', 'acronym', 'address', 'applet', 'area', 'b',
    'base', 'basefont', 'bdo', 'big', 'blink', 'blockquote', 'body', 'br',
    'button', 'caption', 'center', 'cite', 'code', 'col', 'colgroup',
    'dd', 'del', 'dfn', 'dir', 'div', 'dl', 'dt',
    'em', 'fieldset', 'font', 'form', 'frame', 'frameset', 'h1',
    'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'hr',
    'html', 'i', 'iframe', 'img', 'input', 'ins', 'isindex',
    'kbd', 'label', 'legend', 'li', 'link', 'map', 'menu',
    'meta', 'noframes', 'noscript', 'object', 'ol', 'optgroup', 'option',
    'p', 'param', 'pre', 'q', 's', 'samp', 'script',
    'select', 'small', 'span', 'strike', 'strong', 'style', 'sub',
    'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th',
    'thead', 'title', 'tr', 'tt', 'u', 'ul', 'var',
)
