import re
import string

import allure
import pytest

from utils.helpers import is_positive, random_email, random_string, remove_none


@allure.epic("Unit")
@allure.feature("Helpers")
@pytest.mark.unit
class TestHelpers:
    @allure.story("random_string")
    @allure.title("Returns string")
    @allure.description("Verifies that random_string() returns a string.")
    @pytest.mark.positive
    def test_random_string_type(self) -> None:
        assert isinstance(random_string(), str)

    @allure.story("random_string")
    @allure.title("Default length is 10")
    @allure.description("Verifies that the default string length is 10 characters.")
    @pytest.mark.positive
    def test_random_string_default_length(self) -> None:
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
        ],
    )
    @allure.description(
        "Verifies that random_string() returns strings of the requested length."
    )
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_random_string_custom_length(self, length: int) -> None:
        assert len(random_string(length)) == length

    @allure.story("random_string")
    @allure.title("Contains only letters and digits")
    @allure.description(
        "Verifies that the generated string contains only letters and digits."
    )
    @pytest.mark.positive
    def test_random_string_characters(self) -> None:
        result = random_string(100)

        alphabet = set(string.ascii_letters + string.digits)

        assert set(result).issubset(alphabet)

    @allure.story("random_string")
    @allure.title("Returns different values")
    @allure.description("Verifies that consecutive generated strings are different.")
    @pytest.mark.positive
    def test_random_string_unique(self) -> None:
        first = random_string()
        second = random_string()

        assert first != second

    @allure.story("random_string")
    @allure.title("Empty string for zero length")
    @allure.description("Verifies that a zero length returns an empty string.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_random_string_zero_length(self) -> None:
        assert random_string(0) == ""

    @allure.story("random_email")
    @allure.title("Returns string")
    @allure.description("Verifies that random_email() returns a string.")
    @pytest.mark.positive
    def test_random_email_type(self) -> None:
        assert isinstance(random_email(), str)

    @allure.story("random_email")
    @allure.title("Contains at sign")
    @allure.description("Verifies that the generated email contains the at sign.")
    @pytest.mark.positive
    def test_random_email_contains_at(self) -> None:
        assert "@" in random_email()

    @allure.story("random_email")
    @allure.title("Uses example.com domain")
    @allure.description(
        "Verifies that the generated email uses the example.com domain."
    )
    @pytest.mark.positive
    def test_random_email_domain(self) -> None:
        assert random_email().endswith("@example.com")

    @allure.story("random_email")
    @allure.title("Local part length is 12")
    @allure.description("Verifies that the email local part contains 12 characters.")
    @pytest.mark.positive
    def test_random_email_local_part_length(self) -> None:
        local = random_email().split("@")[0]

        assert len(local) == 12

    @allure.story("random_email")
    @allure.title("Matches email pattern")
    @allure.description(
        "Verifies that the generated email matches the expected pattern."
    )
    @pytest.mark.positive
    def test_random_email_pattern(self) -> None:
        email = random_email()

        assert re.fullmatch(r"[A-Za-z0-9]{12}@example\.com", email)

    @allure.story("random_email")
    @allure.title("Generated emails are different")
    @allure.description("Verifies that consecutive generated emails are different.")
    @pytest.mark.positive
    def test_random_email_unique(self) -> None:
        first = random_email()
        second = random_email()

        assert first != second

    @allure.story("is_positive")
    @allure.title("Positive integer")
    @allure.description("Verifies that a positive integer is recognized as positive.")
    @pytest.mark.positive
    def test_positive_integer(self) -> None:
        assert is_positive(5) is True

    @allure.story("is_positive")
    @allure.title("Positive float")
    @allure.description("Verifies that a positive float is recognized as positive.")
    @pytest.mark.positive
    def test_positive_float(self) -> None:
        assert is_positive(3.14) is True

    @allure.story("is_positive")
    @allure.title("Zero is not positive")
    @allure.description("Verifies that zero is not treated as a positive value.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_zero(self) -> None:
        assert is_positive(0) is False

    @allure.story("is_positive")
    @allure.title("Negative integer")
    @allure.description(
        "Verifies that a negative integer is not recognized as positive."
    )
    @pytest.mark.negative
    def test_negative_integer(self) -> None:
        assert is_positive(-5) is False

    @allure.story("is_positive")
    @allure.title("Negative float")
    @allure.description("Verifies that a negative float is not recognized as positive.")
    @pytest.mark.negative
    def test_negative_float(self) -> None:
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
        ],
    )
    @allure.description(
        "Verifies that is_positive() returns the expected result for multiple values."
    )
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_is_positive_parametrize(self, value: int | float, expected: bool) -> None:
        assert is_positive(value) is expected

    @allure.story("remove_none")
    @allure.title("Removes None values")
    @allure.description("Verifies that None values are removed from a dictionary.")
    @pytest.mark.positive
    def test_remove_none(self) -> None:
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
    @allure.description(
        "Verifies that dictionaries without None values remain unchanged."
    )
    @pytest.mark.positive
    def test_remove_none_without_none(self) -> None:
        data = {
            "a": 1,
            "b": 2,
        }

        assert remove_none(data) == data

    @allure.story("remove_none")
    @allure.title("All all values removed")
    @allure.description("Verifies that all None values are removed from a dictionary.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_remove_all_none(self) -> None:
        data = {
            "a": None,
            "b": None,
        }

        assert remove_none(data) == {}

    @allure.story("remove_none")
    @allure.title("Empty dictionary")
    @allure.description("Verifies that an empty dictionary is handled correctly.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_remove_none_empty(self) -> None:
        assert remove_none({}) == {}

    @allure.story("remove_none")
    @allure.title("False values are preserved")
    @allure.description("Verifies that false-like values except None are preserved.")
    @pytest.mark.positive
    def test_false_values_preserved(self) -> None:
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
    @allure.description("Verifies that the original dictionary is not modified.")
    @pytest.mark.positive
    def test_original_dictionary_not_modified(self) -> None:
        data = {
            "a": 1,
            "b": None,
        }

        original = data.copy()

        remove_none(data)

        assert data == original

    @allure.story("remove_none")
    @allure.title("Returns new dictionary")
    @allure.description("Verifies that remove_none() returns a new dictionary.")
    @pytest.mark.positive
    def test_returns_new_dictionary(self) -> None:
        data = {
            "a": 1,
        }

        result = remove_none(data)

        assert result is not data

    @allure.story("remove_none")
    @allure.title("Return type is dict")
    @allure.description("Verifies that remove_none() returns a dictionary.")
    @pytest.mark.positive
    def test_return_type(self) -> None:
        assert isinstance(
            remove_none(
                {
                    "a": 1,
                }
            ),
            dict,
        )
