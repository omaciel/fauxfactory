"""Tests for structured data generators."""

import json

import pytest

from fauxfactory import (
    gen_alpha,
    gen_boolean,
    gen_dict,
    gen_email,
    gen_integer,
    gen_json,
    gen_list,
    gen_uuid,
)


def test_gen_dict_empty_schema():
    """Test gen_dict with an empty schema."""
    result = gen_dict({})
    assert result == {}
    assert isinstance(result, dict)


def test_gen_dict_none_schema():
    """Test gen_dict raises ValueError for None schema."""
    with pytest.raises(ValueError, match="Schema cannot be None"):
        gen_dict(None)  # type: ignore[arg-type]


def test_gen_dict_invalid_schema_type():
    """Test gen_dict raises ValueError for non-dict schema."""
    with pytest.raises(ValueError, match="Schema must be a dict"):
        gen_dict("not a dict")  # type: ignore[arg-type]


def test_gen_dict_with_literals():
    """Test dict generation with literal values."""
    schema = {
        "name": "Alice",
        "age": 30,
        "active": True,
        "score": 95.5,
        "tags": None,
    }
    result = gen_dict(schema)

    assert result == schema
    assert result["name"] == "Alice"
    assert result["age"] == 30
    assert result["active"] is True
    assert result["score"] == 95.5
    assert result["tags"] is None


def test_gen_dict_with_callables():
    """Test dict generation with generator functions."""
    result = gen_dict(
        {
            "username": gen_alpha,
            "email": gen_email,
            "is_active": gen_boolean,
            "id": gen_uuid,
        }
    )

    assert isinstance(result, dict)
    assert isinstance(result["username"], str)
    assert isinstance(result["email"], str)
    assert "@" in result["email"]
    assert isinstance(result["is_active"], bool)
    assert isinstance(result["id"], str)
    # UUID format check
    assert len(result["id"]) == 36  # UUID with dashes


def test_gen_dict_with_lambdas():
    """Test dict generation with lambda functions for parameterized generators."""
    result = gen_dict(
        {
            "username": lambda: gen_alpha(length=5),
            "age": lambda: gen_integer(min_value=18, max_value=100),
            "score": lambda: gen_integer(min_value=0, max_value=10),
        }
    )

    assert isinstance(result, dict)
    assert len(result["username"]) == 5
    assert 18 <= result["age"] <= 100
    assert 0 <= result["score"] <= 10


def test_gen_dict_nested():
    """Test nested dictionary generation."""
    result = gen_dict(
        {
            "user": {
                "name": gen_alpha,
                "email": gen_email,
                "profile": {
                    "age": lambda: gen_integer(min_value=18, max_value=100),
                    "city": gen_alpha,
                },
            },
            "metadata": {
                "created": "2024-01-01",
                "version": 1,
            },
        }
    )

    assert isinstance(result, dict)
    assert isinstance(result["user"], dict)
    assert isinstance(result["user"]["profile"], dict)
    assert isinstance(result["user"]["name"], str)
    assert "@" in result["user"]["email"]
    assert 18 <= result["user"]["profile"]["age"] <= 100
    assert isinstance(result["user"]["profile"]["city"], str)
    assert result["metadata"]["created"] == "2024-01-01"
    assert result["metadata"]["version"] == 1


def test_gen_dict_with_lists_default_size():
    """Test list generation with default size (3)."""
    result = gen_dict(
        {
            "tags": [gen_alpha],
        }
    )

    assert isinstance(result, dict)
    assert isinstance(result["tags"], list)
    assert len(result["tags"]) == 3  # Default size
    for tag in result["tags"]:
        assert isinstance(tag, str)


def test_gen_dict_with_lists_custom_size():
    """Test list generation with custom size via list_sizes parameter."""
    result = gen_dict(
        {
            "tags": [gen_alpha],
            "scores": [lambda: gen_integer(min_value=0, max_value=100)],
        },
        list_sizes={"tags": 5, "scores": 2},
    )

    assert isinstance(result, dict)
    assert len(result["tags"]) == 5
    assert len(result["scores"]) == 2
    for tag in result["tags"]:
        assert isinstance(tag, str)
    for score in result["scores"]:
        assert 0 <= score <= 100


def test_gen_dict_with_nested_lists():
    """Test list generation in nested structures."""
    result = gen_dict(
        {
            "user": {
                "name": gen_alpha,
                "hobbies": [gen_alpha],
            },
            "metadata": {
                "tags": [gen_alpha],
            },
        },
        list_sizes={"user.hobbies": 4, "metadata.tags": 2},
    )

    assert len(result["user"]["hobbies"]) == 4
    assert len(result["metadata"]["tags"]) == 2


def test_gen_dict_with_empty_list():
    """Test list schema with empty list."""
    result = gen_dict(
        {
            "tags": [],
        }
    )

    assert result["tags"] == []


def test_gen_dict_list_with_multiple_elements_raises():
    """Test that list schema with >1 element raises ValueError."""
    with pytest.raises(ValueError, match="must contain exactly one element"):
        gen_dict(
            {
                "tags": [gen_alpha, gen_email],  # Ambiguous which to use
            }
        )


def test_gen_dict_complex_nested_structure():
    """Test complex nested structure with mixed types."""
    result = gen_dict(
        {
            "api_version": "v1",
            "user": {
                "id": gen_uuid,
                "username": lambda: gen_alpha(length=8),
                "contact": {
                    "email": gen_email,
                    "verified": gen_boolean,
                },
                "tags": [gen_alpha],
            },
            "permissions": ["read", "write"],  # Literal list
            "settings": {
                "notifications": True,
                "theme": "dark",
            },
        },
        list_sizes={"user.tags": 3},
    )

    assert result["api_version"] == "v1"
    assert isinstance(result["user"]["id"], str)
    assert len(result["user"]["username"]) == 8
    assert "@" in result["user"]["contact"]["email"]
    assert isinstance(result["user"]["contact"]["verified"], bool)
    assert len(result["user"]["tags"]) == 3
    assert result["permissions"] == ["read", "write"]  # Literals unchanged
    assert result["settings"]["notifications"] is True


def test_gen_dict_with_list_of_dicts():
    """Test generating list of dictionaries."""
    result = gen_dict(
        {
            "users": [
                {
                    "name": gen_alpha,
                    "email": gen_email,
                }
            ],
        },
        list_sizes={"users": 2},
    )

    assert len(result["users"]) == 2
    for user in result["users"]:
        assert isinstance(user, dict)
        assert isinstance(user["name"], str)
        assert "@" in user["email"]


def test_gen_dict_max_depth():
    """Test max_depth parameter prevents infinite recursion."""
    # This should work with depth 2 (depth increments for each nested dict)
    result = gen_dict(
        {
            "level1": {
                "level2": {
                    "value": gen_alpha,
                },
            },
        },
        max_depth=3,
    )
    assert isinstance(result["level1"]["level2"]["value"], str)

    # This should raise with max_depth=0 (no nesting allowed)
    with pytest.raises(ValueError, match="Maximum recursion depth"):
        gen_dict(
            {
                "level1": {
                    "level2": gen_alpha,
                },
            },
            max_depth=0,
        )


def test_gen_dict_validation():
    """Test validator/default/tries behavior."""

    def valid_user(d: dict) -> bool:
        """Validate user dict has required fields."""
        return "name" in d and len(d["name"]) > 0

    # Valid schema
    result = gen_dict(
        {"name": gen_alpha, "email": gen_email},
        validator=valid_user,
        default={"name": "default", "email": "default@example.com"},
    )
    assert "name" in result
    assert len(result["name"]) > 0

    # Invalid schema (name always empty)
    result = gen_dict(
        {"name": lambda: "", "email": gen_email},
        validator=valid_user,
        default={"name": "default", "email": "default@example.com"},
        tries=3,
    )
    assert result == {"name": "default", "email": "default@example.com"}


def test_gen_dict_validation_requires_default():
    """Test that providing validator without default raises ValueError."""
    with pytest.raises(ValueError, match=r"default.*must not be None"):
        gen_dict(
            {"name": gen_alpha},
            validator=lambda d: True,
        )


def test_gen_json_basic():
    """Test basic JSON generation."""
    json_str = gen_json(
        {
            "name": lambda: "Alice",
            "age": lambda: 30,
            "active": lambda: True,
        }
    )

    assert isinstance(json_str, str)
    data = json.loads(json_str)
    assert data["name"] == "Alice"
    assert data["age"] == 30
    assert data["active"] is True


def test_gen_json_with_generators():
    """Test JSON generation with actual generators."""
    json_str = gen_json(
        {
            "id": gen_uuid,
            "username": gen_alpha,
            "email": gen_email,
        }
    )

    assert isinstance(json_str, str)
    data = json.loads(json_str)
    assert isinstance(data["id"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)
    assert "@" in data["email"]


def test_gen_json_indent():
    """Test JSON with indentation."""
    json_str = gen_json(
        {
            "user": {
                "name": lambda: "Alice",
                "email": lambda: "alice@example.com",
            },
        },
        indent=2,
    )

    assert isinstance(json_str, str)
    assert "\n" in json_str  # Indented JSON has newlines
    assert "  " in json_str  # Has indentation
    data = json.loads(json_str)
    assert data["user"]["name"] == "Alice"


def test_gen_json_compact():
    """Test JSON without indentation (compact)."""
    json_str = gen_json(
        {
            "name": lambda: "Alice",
            "age": lambda: 30,
        }
    )

    assert isinstance(json_str, str)
    # Compact JSON should not have unnecessary whitespace
    data = json.loads(json_str)
    assert data["name"] == "Alice"
    assert data["age"] == 30


def test_gen_json_with_lists():
    """Test JSON generation with lists."""
    json_str = gen_json(
        {
            "users": [
                {
                    "name": gen_alpha,
                    "active": gen_boolean,
                }
            ],
        },
        list_sizes={"users": 3},
        indent=2,
    )

    assert isinstance(json_str, str)
    data = json.loads(json_str)
    assert len(data["users"]) == 3
    for user in data["users"]:
        assert isinstance(user["name"], str)
        assert isinstance(user["active"], bool)


def test_gen_json_validation():
    """Test JSON validator behavior."""

    def is_valid_json_length(s: str) -> bool:
        """Check if JSON string is reasonably long."""
        return len(s) > 10

    # Valid JSON
    result = gen_json(
        {"name": gen_alpha, "email": gen_email},
        validator=is_valid_json_length,
        default='{"name":"default"}',
    )
    assert len(result) > 10

    # Invalid JSON (too short)
    result = gen_json(
        {"a": lambda: "b"},
        validator=lambda s: len(s) > 100,  # Always fails
        default='{"fallback":"value"}',
        tries=2,
    )
    assert result == '{"fallback":"value"}'


def test_gen_json_validation_requires_default():
    """Test that providing validator without default raises ValueError."""
    with pytest.raises(ValueError, match=r"default.*must not be None"):
        gen_json(
            {"name": gen_alpha},
            validator=lambda s: True,
        )


def test_gen_json_complex_structure():
    """Test JSON generation with complex nested structure."""
    json_str = gen_json(
        {
            "api": {
                "version": "v2",
                "endpoints": [lambda: gen_alpha(5)],
            },
            "users": [
                {
                    "id": gen_uuid,
                    "profile": {
                        "name": gen_alpha,
                        "verified": gen_boolean,
                    },
                }
            ],
            "count": lambda: gen_integer(min_value=1, max_value=100),
        },
        list_sizes={"api.endpoints": 2, "users": 2},
        indent=2,
    )

    assert isinstance(json_str, str)
    data = json.loads(json_str)
    assert data["api"]["version"] == "v2"
    assert len(data["api"]["endpoints"]) == 2
    assert len(data["users"]) == 2
    assert 1 <= data["count"] <= 100
    for user in data["users"]:
        assert isinstance(user["id"], str)
        assert isinstance(user["profile"]["name"], str)
        assert isinstance(user["profile"]["verified"], bool)


def test_gen_dict_all_generator_types():
    """Test using all available generator types in one schema."""
    result = gen_dict(
        {
            "string": gen_alpha,
            "email": gen_email,
            "uuid": gen_uuid,
            "number": lambda: gen_integer(min_value=1, max_value=10),
            "boolean": gen_boolean,
            "literal_string": "constant",
            "literal_number": 42,
            "literal_bool": False,
            "literal_null": None,
            "nested": {
                "value": gen_alpha,
            },
            "list": [gen_alpha],
        }
    )

    assert isinstance(result["string"], str)
    assert "@" in result["email"]
    assert isinstance(result["uuid"], str)
    assert 1 <= result["number"] <= 10
    assert isinstance(result["boolean"], bool)
    assert result["literal_string"] == "constant"
    assert result["literal_number"] == 42
    assert result["literal_bool"] is False
    assert result["literal_null"] is None
    assert isinstance(result["nested"]["value"], str)
    assert isinstance(result["list"], list)


# Tests for gen_list()


def test_gen_list_with_callable():
    """Test list generation with a callable generator."""
    result = gen_list(gen_alpha, size=5)

    assert isinstance(result, list)
    assert len(result) == 5
    for item in result:
        assert isinstance(item, str)


def test_gen_list_default_size():
    """Test list generation with default size (3)."""
    result = gen_list(gen_alpha)

    assert isinstance(result, list)
    assert len(result) == 3
    for item in result:
        assert isinstance(item, str)


def test_gen_list_with_lambda():
    """Test list generation with lambda for parameterized generators."""
    result = gen_list(lambda: gen_integer(min_value=0, max_value=100), size=10)

    assert isinstance(result, list)
    assert len(result) == 10
    for item in result:
        assert isinstance(item, int)
        assert 0 <= item <= 100


def test_gen_list_with_dict_schema():
    """Test generating list of dictionaries."""
    result = gen_list(
        {
            "name": gen_alpha,
            "email": gen_email,
            "active": True,
        },
        size=3,
    )

    assert isinstance(result, list)
    assert len(result) == 3
    for item in result:
        assert isinstance(item, dict)
        assert isinstance(item["name"], str)
        assert "@" in item["email"]
        assert item["active"] is True


def test_gen_list_with_nested_dict():
    """Test generating list with nested dictionary schemas."""
    result = gen_list(
        {
            "user": {
                "name": gen_alpha,
                "contact": {
                    "email": gen_email,
                },
            },
            "status": "active",
        },
        size=2,
    )

    assert len(result) == 2
    for item in result:
        assert isinstance(item["user"]["name"], str)
        assert "@" in item["user"]["contact"]["email"]
        assert item["status"] == "active"


def test_gen_list_with_list_schema():
    """Test generating list of lists (matrix)."""
    result = gen_list([lambda: gen_integer(min_value=0, max_value=9)], size=3)

    assert isinstance(result, list)
    assert len(result) == 3
    for row in result:
        assert isinstance(row, list)
        assert len(row) == 3  # Default inner list size
        for item in row:
            assert isinstance(item, int)
            assert 0 <= item <= 9


def test_gen_list_with_literal():
    """Test generating list with literal values."""
    result = gen_list("constant", size=5)

    assert isinstance(result, list)
    assert len(result) == 5
    for item in result:
        assert item == "constant"


def test_gen_list_zero_size():
    """Test generating empty list with size=0."""
    result = gen_list(gen_alpha, size=0)

    assert isinstance(result, list)
    assert len(result) == 0
    assert result == []


def test_gen_list_negative_size_raises():
    """Test that negative size raises ValueError."""
    with pytest.raises(ValueError, match="Size must be non-negative"):
        gen_list(gen_alpha, size=-1)


def test_gen_list_max_depth():
    """Test max_depth parameter prevents infinite recursion."""
    # This should work with nested dicts
    result = gen_list(
        {
            "level1": {
                "level2": {
                    "value": gen_alpha,
                },
            },
        },
        size=2,
        max_depth=3,
    )
    assert len(result) == 2
    assert isinstance(result[0]["level1"]["level2"]["value"], str)

    # This should raise with max_depth=0
    with pytest.raises(ValueError, match="Maximum recursion depth"):
        gen_list(
            {
                "level1": {
                    "value": gen_alpha,
                },
            },
            size=1,
            max_depth=0,
        )


def test_gen_list_validation():
    """Test validator/default/tries behavior."""

    def all_positive(lst: list) -> bool:
        """Validate all items are positive."""
        return all(x > 0 for x in lst)

    # Valid list
    result = gen_list(
        lambda: gen_integer(min_value=1, max_value=100),
        size=5,
        validator=all_positive,
        default=[1, 2, 3],
    )
    assert len(result) == 5
    assert all(x > 0 for x in result)

    # Invalid list (always generates negatives)
    result = gen_list(
        lambda: -1,
        size=3,
        validator=all_positive,
        default=[1, 2, 3],
        tries=2,
    )
    assert result == [1, 2, 3]


def test_gen_list_validation_requires_default():
    """Test that providing validator without default raises ValueError."""
    with pytest.raises(ValueError, match=r"default.*must not be None"):
        gen_list(
            gen_alpha,
            size=3,
            validator=lambda lst: len(lst) > 0,
        )


def test_gen_list_complex_mixed_types():
    """Test generating list with complex mixed-type items."""
    result = gen_list(
        {
            "id": gen_uuid,
            "data": {
                "name": gen_alpha,
                "scores": [lambda: gen_integer(min_value=0, max_value=100)],
            },
            "active": gen_boolean,
            "tags": ["read", "write"],  # Literal list
        },
        size=2,
    )

    assert len(result) == 2
    for item in result:
        assert isinstance(item["id"], str)
        assert isinstance(item["data"]["name"], str)
        assert isinstance(item["data"]["scores"], list)
        assert len(item["data"]["scores"]) == 3  # Default size
        assert isinstance(item["active"], bool)
        assert item["tags"] == ["read", "write"]


def test_gen_list_large_size():
    """Test generating large list."""
    result = gen_list(gen_alpha, size=100)

    assert isinstance(result, list)
    assert len(result) == 100
    for item in result:
        assert isinstance(item, str)


def test_gen_list_multiple_generator_types():
    """Test using different generator types in separate calls."""
    strings = gen_list(gen_alpha, size=5)
    emails = gen_list(gen_email, size=5)
    booleans = gen_list(gen_boolean, size=5)
    uuids = gen_list(gen_uuid, size=5)

    assert all(isinstance(x, str) for x in strings)
    assert all("@" in x for x in emails)
    assert all(isinstance(x, bool) for x in booleans)
    assert all(isinstance(x, str) and len(x) == 36 for x in uuids)
