import allure
import pytest

from utils.parser import get_value, key_exists, nested_value

@allure.epic("Unit")
@allure.feature("Parser")
@pytest.mark.unit
class TestParser:
    @allure.story("get_value")
    @allure.title("Returns value by key")
    @allure.description("Verifies that get_value() returns the value for an existing key.")
    @pytest.mark.positive
    def test_get_value(self):
        data = {
            "name": "John",
            "age": 25,
        }

        assert get_value(data, "name") == "John"

    @allure.story("get_value")
    @allure.title("Returns integer value")
    @allure.description("Verifies that get_value() returns an integer value.")
    @pytest.mark.positive
    def test_get_integer(self):
        assert get_value({"id": 10}, "id") == 10

    @allure.story("get_value")
    @allure.title("Returns nested object")
    @allure.description("Verifies that get_value() returns a nested object.")
    @pytest.mark.positive
    def test_get_nested_object(self):
        user = {
            "id": 1,
        }

        data = {
            "user": user,
        }

        assert get_value(data, "user") is user

    @allure.story("get_value")
    @allure.title("Returns KeyError for missing key")
    @allure.description("Verifies that get_value() raises KeyError for a missing key.")
    @pytest.mark.negative
    @pytest.mark.boundary
    def test_get_missing_key(self):
        with pytest.raises(KeyError):
            get_value({}, "missing")

    @allure.story("get_value")
    @allure.title("Returns None value")
    @allure.description("Verifies that get_value() returns None for an existing key with a None value.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_get_none_value(self):
        assert get_value({"value": None}, "value") is None

    @allure.story("key_exists")
    @allure.title("Returns True when key exists")
    @allure.description("Verifies that key_exists() returns True for an existing key.")
    @pytest.mark.positive
    def test_key_exists(self):
        assert key_exists({"a": 1}, "a") is True

    @allure.story("key_exists")
    @allure.title("Returns False when key missing")
    @allure.description("Verifies that key_exists() returns False for a missing key.")
    @pytest.mark.positive
    def test_key_exists_false(self):
        assert key_exists({"a": 1}, "b") is False

    @allure.story("key_exists")
    @allure.title("Works with empty dictionary")
    @allure.description("Verifies that key_exists() returns False for an empty dictionary.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_key_exists_empty_dict(self):
        assert key_exists({}, "a") is False

    @allure.story("key_exists")
    @allure.title("None value still means key exists")
    @allure.description("Verifies that a key with a None value is treated as existing.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_key_exists_none_value(self):
        assert key_exists({"a": None}, "a") is True

    @allure.story("key_exists")
    @allure.title("Check several keys")
    @pytest.mark.parametrize(
        ("key", "expected"),
        [
            ("id", True),
            ("name", True),
            ("email", False),
            ("age", False),
        ]
    )
    @allure.description("Verifies that key_exists() returns the expected result for multiple keys.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_key_exists_parametrize(self, key: str, expected: bool):
        data = {
            "id": 1,
            "name": "John",
        }

        assert key_exists(data, key) is expected

    @pytest.fixture()
    def nested_data(self) -> dict:
        return {
            "user": {
                "profile": {
                    "name": "John",
                    "age": 30,
                }
            }
        }

    @allure.story("nested_value")
    @allure.title("Returns nested string")
    @allure.description("Verifies that nested_value() returns a nested string value.")
    @pytest.mark.positive
    def test_nested_string(self, nested_data: dict):
        assert nested_value(nested_data, "user", "profile", "name") == "John"

    @allure.story("nested_value")
    @allure.title("Returns nested integer")
    @allure.description("Verifies that nested_value() returns a nested integer value.")
    @pytest.mark.positive
    def test_nested_integer(self, nested_data: dict):
        assert nested_value(nested_data, "user", "profile", "age") == 30

    @allure.story("nested_value")
    @allure.title("Returns intermidiate dictionary")
    @allure.description("Verifies that nested_value() returns an intermediate dictionary.")
    @pytest.mark.positive
    def test_nested_dictionary(self, nested_data: dict):
        result = nested_value(nested_data, "user")

        assert isinstance(result, dict)

    @allure.story("nested_value")
    @allure.title("Returns original object without keys")
    @allure.description("Verifies that nested_value() returns the original object when no keys are provided.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_nested_without_keys(self, nested_data: dict):
        assert nested_value(nested_data) == nested_data

    @allure.story("nested_value")
    @allure.title("Raises KeyError on first missing key")
    @allure.description("Verifies that nested_value() raises KeyError for a missing first-level key.")
    @pytest.mark.positive
    def test_nested_missing_first_key(self, nested_data: dict):
        with pytest.raises(KeyError):
            nested_value(nested_data, "account")

    @allure.story("nested_value")
    @allure.title("Raises KeyError on nested missing key")
    @allure.description("Verifies that nested_value() raises KeyError for a missing nested key.")
    @pytest.mark.positive
    def test_nested_missing_inner_key(self, nested_data: dict):
        with pytest.raises(KeyError):
            nested_value(nested_data, "user", "address")

    @allure.story("nested_value")
    @allure.title("Raises KeyError on last missing key")
    @allure.description("Verifies that nested_value() raises KeyError for a missing final key.")
    @pytest.mark.positive
    def test_nested_none_value(self, nested_data: dict):
        with pytest.raises(KeyError):
            nested_value(nested_data, "user", "profile", "city")

    @allure.story("nested_value")
    @allure.title("Works with None value")
    @allure.description("Verifies that nested_value() returns None for an existing key with a None value.")
    @pytest.mark.positive
    def test_nested_missing_last_key(self):
        data = {
            "user": {
                "address": None,
            }
        }

        assert nested_value(data, "user", "address") is None

    @allure.story("nested_value")
    @allure.title("Works with boolean value")
    @allure.description("Verifies that nested_value() returns a boolean value.")
    @pytest.mark.positive
    def test_nested_boolean(self):
        data = {
            "settings": {
                "enabled": True,
            }
        }

        assert nested_value(data, "settings", "enabled") is True
