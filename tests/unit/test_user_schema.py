import allure
import pytest
from jsonschema import ValidationError, validate

from schemas.user_schema import USER_SCHEMA

allure.epic("Unit")
@allure.feature("User Schema")
@pytest.mark.unit
class TestUserSchema:
    @pytest.fixture()
    def valid_user(self) -> dict:
        return {
            "id": 1,
            "firstName": "John",
            "lastName": "Smith",
            "email": "john@example.com",
            "age": 25,
            "gender": "male",
        }

    @allure.story("Schema")
    @allure.title("Schema is object")
    def test_schema_type(self):
        assert USER_SCHEMA["type"] == "object"

    @allure.story("Schema")
    @allure.title("Schema contains required section")
    def test_required_exists(self):
        assert "required" in USER_SCHEMA

    @allure.story("Schema")
    @allure.title("Schema contains properties section")
    def test_properties_exists(self):
        assert "properties" in USER_SCHEMA

    @allure.story("Schema")
    @allure.title("Required fields count")
    def test_required_fields_count(self):
        assert len(USER_SCHEMA["required"]) == 6

    @allure.story("Schema")
    @allure.title("Required fields match expected")
    def test_required_fields(self):
        assert USER_SCHEMA["required"] == [
            "id",
            "firstName",
            "lastName",
            "email",
            "age",
            "gender",
        ]

    @allure.story("Schema")
    @allure.title("Properties count")
    def test_properties_count(self):
        assert len(USER_SCHEMA["properties"]) == 6

    @allure.story("Schema")
    @allure.title("Id type")
    def test_id_type(self):
        assert USER_SCHEMA["properties"]["id"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("First name type")
    def test_first_name_type(self):
        assert USER_SCHEMA["properties"]["firstName"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Last name type")
    def test_last_name_type(self):
        assert USER_SCHEMA["properties"]["lastName"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Email type")
    def test_email_type(self):
        assert USER_SCHEMA["properties"]["email"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Email format")
    def test_email_format(self):
        assert USER_SCHEMA["properties"]["email"]["format"] == "email"

    @allure.story("Schema")
    @allure.title("Age type")
    def test_age_type(self):
        assert USER_SCHEMA["properties"]["age"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Age minimum")
    def test_age_minimum(self):
        assert USER_SCHEMA["properties"]["age"]["minimum"] == 0

    @allure.story("Schema")
    @allure.title("Gender type")
    def test_gender_type(self):
        assert USER_SCHEMA["properties"]["gender"]["type"] == "string"

    @allure.story("Validation")
    @allure.title("Valid user passes validation")
    def test_valid_user(self, valid_user: dict):
        validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Additional properties are allowed")
    def test_additional_properties(self, valid_user: dict):
        valid_user["country"] = "USA"

        validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing id")
    def test_missing_id(self, valid_user: dict):
        valid_user.pop("id")

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing firstName")
    def test_missing_first_name(self, valid_user: dict):
        valid_user.pop("firstName")

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing email")
    def test_missing_email(self, valid_user: dict):
        valid_user.pop("email")

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Negative age")
    def test_negative_age(self, valid_user: dict):
        valid_user["age"] = -1

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Id must be integer")
    def test_invalid_id_type(self, valid_user: dict):
        valid_user["id"] = "1"

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Age must be integer")
    def test_invalid_age_type(self, valid_user: dict):
        valid_user["age"] = "18"

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Email must be string")
    def test_invalid_email_type(self, valid_user: dict):
        valid_user["email"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("firstName must be string")
    def test_invalid_first_name_type(self, valid_user: dict):
        valid_user["firstName"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("lastName must be string")
    def test_invalid_last_name_type(self, valid_user: dict):
        valid_user["lastName"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Gender must be string")
    def test_invalid_gender_type(self, valid_user: dict):
        valid_user["gender"] = 1

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Validate several ages")
    @pytest.mark.parametrize(
        "age",
        [
            0,
            1,
            18,
            50,
            100,
        ]
    )
    def test_valid_ages(self, valid_user: dict, age: int):
        valid_user["age"] = age

        validate(instance=valid_user, schema=USER_SCHEMA)
