"""Constants used by :mod:`fauxfactory`.

.. data:: VALID_NETMASKS

    A tuple of netmasks. The tuple index corresponds to a CIDR value. For
    example, a CIDR of "/1" corresponds to `VALID_NETMASKS[1]`.

"""

# The above constant descriptions can be found by Sphinx and via help().
import datetime
import json
import string
from pathlib import Path
from typing import Any, Final

VALID_DIGITS: Final[str] = string.digits + string.ascii_letters

FACTS_JSON_FILE: Final[Path] = Path(__file__).parent / "facts.json"
with FACTS_JSON_FILE.open(encoding="utf-8") as data:
    FACTS_JSON: Final[dict[str, Any]] = json.load(data)

LOREM_IPSUM_TEXT: Final[str] = (
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do "
    "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad "
    "minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip "
    "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur "
    "sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
    "mollit anim id est laborum."
)

MIN_YEARS: Final[int] = datetime.MINYEAR
MAX_YEARS: Final[int] = 1000  # 1000 years into the future

SCHEMES: Final[tuple[str, ...]] = (
    "http",
    "https",
    "ftp",
)

SUBDOMAINS: Final[tuple[str, ...]] = (
    "example",
    "test",
)

TLDS: Final[tuple[str, ...]] = (
    "app",
    "au",
    "biz",
    "ca",
    "co",
    "com",
    "de",
    "dev",
    "edu",
    "gov",
    "info",
    "io",
    "jp",
    "net",
    "org",
    "tech",
    "uk",
)

VALID_NETMASKS: Final[tuple[str, ...]] = (
    "0.0.0.0",
    "128.0.0.0",
    "192.0.0.0",
    "224.0.0.0",
    "240.0.0.0",
    "248.0.0.0",
    "252.0.0.0",
    "254.0.0.0",
    "255.0.0.0",
    "255.128.0.0",
    "255.192.0.0",
    "255.224.0.0",
    "255.240.0.0",
    "255.248.0.0",
    "255.252.0.0",
    "255.254.0.0",
    "255.255.0.0",
    "255.255.128.0",
    "255.255.192.0",
    "255.255.224.0",
    "255.255.240.0",
    "255.255.248.0",
    "255.255.252.0",
    "255.255.254.0",
    "255.255.255.0",
    "255.255.255.128",
    "255.255.255.192",
    "255.255.255.224",
    "255.255.255.240",
    "255.255.255.248",
    "255.255.255.252",
    "255.255.255.254",
    "255.255.255.255",
)

HTML_TAGS: Final[tuple[str, ...]] = (
    "a",
    "abbr",
    "address",
    "area",
    "article",
    "aside",
    "b",
    "base",
    "bdo",
    "blockquote",
    "body",
    "br",
    "button",
    "canvas",
    "caption",
    "cite",
    "code",
    "col",
    "colgroup",
    "dd",
    "del",
    "details",
    "dfn",
    "dialog",
    "div",
    "dl",
    "dt",
    "em",
    "fieldset",
    "figcaption",
    "figure",
    "footer",
    "form",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "head",
    "header",
    "hr",
    "html",
    "i",
    "iframe",
    "img",
    "input",
    "ins",
    "kbd",
    "label",
    "legend",
    "li",
    "link",
    "main",
    "map",
    "mark",
    "menu",
    "meta",
    "nav",
    "noscript",
    "object",
    "ol",
    "optgroup",
    "option",
    "p",
    "param",
    "pre",
    "q",
    "samp",
    "script",
    "section",
    "select",
    "small",
    "span",
    "strong",
    "style",
    "sub",
    "summary",
    "sup",
    "table",
    "tbody",
    "td",
    "textarea",
    "tfoot",
    "th",
    "thead",
    "time",
    "title",
    "tr",
    "u",
    "ul",
    "var",
)
