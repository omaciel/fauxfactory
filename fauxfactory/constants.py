# -*- coding: utf-8 -*-

"""
Defines various constants.
"""

import datetime


# standard Lorem Ipsum passage, used since the 1500s
LOREM_IPSUM_TEXT = (u"Lorem ipsum dolor sit amet, consectetur adipisicing"
                    " elit, sed do eiusmod tempor incididunt ut labore et"
                    " dolore magna aliqua. Ut enim ad minim veniam, quis "
                    "nostrud exercitation ullamco laboris nisi ut aliquip"
                    " ex ea commodo consequat. Duis aute irure dolor in"
                    " reprehenderit in voluptate velit esse cillum dolore "
                    "eu fugiat nulla pariatur. Excepteur sint occaecat "
                    "cupidatat non proident, sunt in culpa qui officia "
                    "deserunt mollit anim id est laborum.")

# Range for YEARS
MIN_YEARS = datetime.MINYEAR
MAX_YEARS = 1000  # 1000 years into the future

SCHEMES = [
    'http',
    'https',
    'ftp',
]

SUBDOMAINS = [
    'example',
    'test',
]

TLDS = [
    'biz',
    'com',
    'edu',
    'gov',
    'info',
    'org',
]

HTML_TAGS = [
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
]
