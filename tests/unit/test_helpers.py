import re
import string

import allure
import pytest

from utils.helpers import is_positive, random_email, random_string, remove_none

allure.epic("Unit")
@allure.feature("Helpers")
@pytest.mark.unit
class TestHelpers:
    @allure.story("random_string")
    @allure.title("Returns string")
    def test_random_string_type(self):
        assert isinstance(random_string(), str)

    @allure.story("random_string")
    @allure.title("Default length is 10")
    def test_random_string_default_length(self):
        assert len(random_string()) == 10

    @allure.story("random_string")
    @allure.title("Custom length")
    @pytest.mark.parametrize(
        "length",
        [
            0,
            1,
            5,
            10,
            25,
            100,
        ]
    )
    def test_random_string_custom_length(self, length: int):
        assert len(random_string(length)) == length

    @allure.story("random_string")
    @allure.title("Contains only letters and digits")
    def test_random_string_characters(self):
        result = random_string(100)

        alphabet = set(string.ascii_letters + string.digits)

        assert set(result).issubset(alphabet)

    @allure.story("random_string")
    @allure.title("Returns different values")
    def test_random_string_unique(self):
        first = random_string()
        second = random_string()

        assert first != second

    @allure.story("random_string")
    @allure.title("Empty string for zero length")
    def test_random_string_zero_length(self):
        assert random_string(0) == ""

    @allure.story("random_email")
    @allure.title("Returns string")
    def test_random_email_type(self):
        assert isinstance(random_email(), str)

    @allure.story("random_email")
    @allure.title("Contains at sign")
    def test_random_email_contains_at(self):
        assert "@" in random_email()

    @allure.story("random_email")
    @allure.title("Uses example.com domain")
    def test_random_email_domain(self):
        assert random_email().endswith("@example.com")

    @allure.story("random_email")
    @allure.title("Local part length is 12")
    def test_random_email_local_part_length(self):
        local = random_email().split("@")[0]

        assert len(local) == 12

    @allure.story("random_email")
    @allure.title("Patches email pattern")
    def test_random_email_pattern(self):
        email = random_email()

        assert re.fullmatch(r"[A-Za-z0-9]{12}@example\.com", email)

    @allure.story("random_email")
    @allure.title("Generated emails are different")
    def test_random_email_unique(self):
        first = random_email()
        second = random_email()

        assert first != second

    @allure.story("is_positive")
    @allure.title("Positive integer")
    def test_positive_integer(self):
        assert is_positive(5) is True

    @allure.story("is_positive")
    @allure.title("Positive float")
    def test_positive_float(self):
        assert is_positive(3.14) is True

    @allure.story("is_positive")
    @allure.title("Zero is not positive")
    def test_zero(self):
        assert is_positive(0) is False

    @allure.story("is_positive")
    @allure.title("Negative integer")
    def test_negative_integer(self):
        assert is_positive(-5) is False

    @allure.story("is_positive")
    @allure.title("Negative float")
    def test_negative_float(self):
        assert is_positive(-0.1) is False

    @allure.story("is_positive")
    @allure.title("Several values")
    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (100, True),
            (1, True),
            (0.1, True),
            (0, False),
            (-1, False),
            (-100.5, False),
        ]
    )
    def test_is_positive_parametrize(self, value: int | float, expected: bool):
        assert is_positive(value) is expected

    @allure.story("remove_none")
    @allure.title("Removes None values")
    def test_remove_none(self):
        data = {
            "a": 1,
            "b": None,
            "c": "text",
        }

        assert remove_none(data) == {
            "a": 1,
            "c": "text",
        }

    @allure.story("remove_none")
    @allure.title("Keeps all values if no None")
    def test_remove_none_without_none(self):
        data = {
            "a": 1,
            "b": 2,
        }

        assert remove_none(data) == data

    @allure.story("remove_none")
    @allure.title("All all values removed")
    def test_remove_all_none(self):
        data = {
            "a": None,
            "b": None,
        }

        assert remove_none(data) == {}

    @allure.story("remove_none")
    @allure.title("Empty dictionary")
    def test_remove_none_empty(self):
        assert remove_none({}) == {}

    @allure.story("remove_none")
    @allure.title("False values are preserved")
    def test_false_values_preserved(self):
        data = {
            "zero": 0,
            "false": False,
            "empty": "",
            "list": [],
            "none": None,
        }

        assert remove_none(data) == {
            "zero": 0,
            "false": False,
            "empty": "",
            "list": [],
        }

    @allure.story("remove_none")
    @allure.title("Original dictionary is unchanged")
    def test_original_dictionary_not_modified(self):
        data = {
            "a": 1,
            "b": None,
        }

        original = data.copy()

        remove_none(data)

        assert data == original

    @allure.story("remove_none")
    @allure.title("Returns new dictionary")
    def test_returns_new_dictionary(self):
        data = {
            "a": 1,
        }

        result = remove_none(data)

        assert result is not data

    @allure.story("remove_none")
    @allure.title("Return type is dict")
    def test_return_type(self):
        assert isinstance(remove_none({"a": 1,}), dict)
