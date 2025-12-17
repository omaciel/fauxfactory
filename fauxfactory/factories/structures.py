"""Collection of structured data generating functions."""

import json
from collections.abc import Callable
from typing import Any

from fauxfactory.helpers import check_validation

# Type aliases for schema definition
SchemaValue = Callable[[], Any] | dict[str, "SchemaValue"] | list["SchemaValue"] | Any
Schema = dict[str, SchemaValue]


def _process_schema_value(
    value: SchemaValue,
    list_sizes: dict[str, int] | None = None,
    current_path: str = "",
    depth: int = 0,
    max_depth: int = 10,
) -> Any:
    """Process a single schema value recursively.

    :param value: The schema value to process
    :param list_sizes: Dictionary mapping field paths to list sizes
    :param current_path: Current field path for list size lookup
    :param depth: Current recursion depth
    :param max_depth: Maximum allowed recursion depth
    :returns: The generated value
    :raises: ValueError if max_depth is exceeded
    """
    if depth > max_depth:
        raise ValueError(
            f"Maximum recursion depth ({max_depth}) exceeded. "
            "This may indicate a circular reference in your schema."
        )

    # Handle callables (generators like gen_alpha, gen_email, or lambdas)
    if callable(value):
        return value()

    # Handle nested dictionaries
    if isinstance(value, dict):
        result = {}
        for key, val in value.items():
            field_path = f"{current_path}.{key}" if current_path else key
            result[key] = _process_schema_value(
                val, list_sizes, field_path, depth + 1, max_depth
            )
        return result

    # Handle lists
    if isinstance(value, list):
        if len(value) == 0:
            return []

        # Check if this is a literal list (all elements are not callables/dicts)
        # If any element is callable or dict, treat as schema pattern
        has_schema_element = any(
            callable(item) or isinstance(item, (dict, list)) for item in value
        )

        if not has_schema_element:
            # This is a literal list, return as-is
            return value

        if len(value) > 1:
            raise ValueError(
                f"List schema at '{current_path}' must contain exactly one element "
                f"(the generator pattern), but got {len(value)} elements"
            )

        # Determine list size
        if list_sizes and current_path in list_sizes:
            size = list_sizes[current_path]
        else:
            size = 3  # Default list size

        # Generate list items
        generator = value[0]
        return [
            _process_schema_value(
                generator, list_sizes, current_path, depth + 1, max_depth
            )
            for _ in range(size)
        ]

    # Handle literal values
    return value


@check_validation
def gen_dict(
    schema: dict[str, Any],
    *,
    list_sizes: dict[str, int] | None = None,
    max_depth: int = 10,
    validator: Callable[[dict[str, Any]], bool] | None = None,
    default: dict[str, Any] | None = None,
    tries: int = 10,
) -> dict[str, Any]:
    """Generate a dictionary based on a schema definition.

    The schema is a dictionary where:

    - Keys are the field names in the output
    - Values can be:

      - Callable: Will be invoked to generate the value
      - dict: Recursively generates nested dictionary
      - list: Generates list of items (first element defines generator pattern)
      - Any other value: Used as-is (literal value)

    :param schema: Schema definition for the dictionary structure
    :param list_sizes: Dictionary mapping field paths to list sizes.
        For example, ``{'tags': 5, 'user.hobbies': 3}`` would generate
        5 items for the 'tags' field and 3 items for the nested
        'user.hobbies' field. Default list size is 3 if not specified.
    :param max_depth: Maximum recursion depth to prevent infinite loops.
        Default is 10.
    :param validator: Optional validation function for the entire dict.
        Should accept a dict and return True if valid.
    :param default: Default value if validation fails after ``tries`` attempts
    :param tries: Number of generation attempts before returning default
    :returns: Generated dictionary matching the schema
    :rtype: dict[str, Any]
    :raises: ValueError if schema is None or max_depth is exceeded

    Example::

        from fauxfactory import gen_dict, gen_alpha, gen_email, gen_integer

        # Simple flat schema
        user = gen_dict({
            'name': gen_alpha,
            'email': gen_email,
            'age': lambda: gen_integer(min_value=18, max_value=100),
            'status': 'active',  # literal value
        })

        # Nested schema
        user = gen_dict({
            'name': gen_alpha,
            'contact': {
                'email': gen_email,
                'phone': gen_alpha,
            },
            'tags': [gen_alpha],  # list of random alpha strings
        }, list_sizes={'tags': 5})

    """
    if schema is None:
        raise ValueError("Schema cannot be None")

    if not isinstance(schema, dict):
        raise ValueError(f"Schema must be a dict, got {type(schema).__name__}")

    result = {}
    for key, value in schema.items():
        result[key] = _process_schema_value(value, list_sizes, key, 0, max_depth)

    return result


@check_validation
def gen_json(
    schema: dict[str, Any],
    *,
    indent: int | None = None,
    list_sizes: dict[str, int] | None = None,
    max_depth: int = 10,
    validator: Callable[[str], bool] | None = None,
    default: str | None = None,
    tries: int = 10,
) -> str:
    """Generate JSON string based on a schema definition.

    Uses the same schema format as :func:`gen_dict`. The generated
    dictionary is serialized to JSON.

    :param schema: Schema definition (same format as gen_dict)
    :param indent: JSON indentation level (None for compact output,
        integer for pretty-printing with that many spaces)
    :param list_sizes: Dictionary mapping field paths to list sizes
    :param max_depth: Maximum recursion depth to prevent infinite loops
    :param validator: Optional validation function for the JSON string.
        Should accept a string and return True if valid.
    :param default: Default value if validation fails after ``tries`` attempts
    :param tries: Number of generation attempts before returning default
    :returns: JSON string matching the schema
    :rtype: str
    :raises: ValueError if schema is None or max_depth is exceeded

    Example::

        from fauxfactory import gen_json, gen_alpha, gen_email

        json_str = gen_json({
            'user': {
                'name': gen_alpha,
                'email': gen_email,
            }
        }, indent=2)

        # With list sizes
        json_str = gen_json({
            'users': [{
                'name': gen_alpha,
                'email': gen_email,
            }]
        }, list_sizes={'users': 5}, indent=2)

    """
    # Generate the dict structure (without validation since we'll validate JSON)
    data = gen_dict(
        schema,
        list_sizes=list_sizes,
        max_depth=max_depth,
        validator=None,  # Don't validate dict, we'll validate JSON
        default=None,
        tries=1,
    )

    # Serialize to JSON
    return json.dumps(data, indent=indent)


__all__ = tuple(name for name in locals() if name.startswith("gen_"))


def __dir__():
    return __all__
