import allure
import pytest
from jsonschema import ValidationError, validate

from schemas.user_schema import USER_SCHEMA

@allure.epic("Unit")
@allure.feature("User Schema")
@pytest.mark.unit
class TestUserSchema:
    @pytest.fixture(scope="function")
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
    @allure.description("Verifies that the schema root type is object.")
    @pytest.mark.positive
    def test_schema_type(self):
        assert USER_SCHEMA["type"] == "object"

    @allure.story("Schema")
    @allure.title("Schema contains required section")
    @allure.description("Verifies that the schema defines required fields.")
    @pytest.mark.positive
    def test_required_exists(self):
        assert "required" in USER_SCHEMA

    @allure.story("Schema")
    @allure.title("Schema contains properties section")
    @allure.description("Verifies that the schema defines properties.")
    @pytest.mark.positive
    def test_properties_exists(self):
        assert "properties" in USER_SCHEMA

    @allure.story("Schema")
    @allure.title("Required fields count")
    @allure.description("Verifies that the schema contains six required fields.")
    @pytest.mark.positive
    def test_required_fields_count(self):
        assert len(USER_SCHEMA["required"]) == 6

    @allure.story("Schema")
    @allure.title("Required fields match expected")
    @allure.description("Verifies that the required fields match the expected list.")
    @pytest.mark.positive
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
    @allure.description("Verifies that the schema defines six properties.")
    @pytest.mark.positive
    def test_properties_count(self):
        assert len(USER_SCHEMA["properties"]) == 6

    @allure.story("Schema")
    @allure.title("Id type")
    @allure.description("Verifies that the id property is an integer.")
    @pytest.mark.positive
    def test_id_type(self):
        assert USER_SCHEMA["properties"]["id"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("First name type")
    @allure.description("Verifies that the firstName property is a string.")
    @pytest.mark.positive
    def test_first_name_type(self):
        assert USER_SCHEMA["properties"]["firstName"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Last name type")
    @allure.description("Verifies that the lastName property is a string.")
    @pytest.mark.positive
    def test_last_name_type(self):
        assert USER_SCHEMA["properties"]["lastName"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Email type")
    @allure.description("Verifies that the email property is a string.")
    @pytest.mark.positive
    def test_email_type(self):
        assert USER_SCHEMA["properties"]["email"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Email format")
    @allure.description("Verifies that the email property uses the email format.")
    @pytest.mark.positive
    def test_email_format(self):
        assert USER_SCHEMA["properties"]["email"]["format"] == "email"

    @allure.story("Schema")
    @allure.title("Age type")
    @allure.description("Verifies that the age property is an integer.")
    @pytest.mark.positive
    def test_age_type(self):
        assert USER_SCHEMA["properties"]["age"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Age minimum")
    @allure.description("Verifies that the minimum allowed value for age is zero.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_age_minimum(self):
        assert USER_SCHEMA["properties"]["age"]["minimum"] == 0

    @allure.story("Schema")
    @allure.title("Gender type")
    @allure.description("Verifies that the gender property is a string.")
    @pytest.mark.positive
    def test_gender_type(self):
        assert USER_SCHEMA["properties"]["gender"]["type"] == "string"

    @allure.story("Validation")
    @allure.title("Valid user passes validation")
    @allure.description("Verifies that a valid user passes schema validation.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_valid_user(self, valid_user: dict):
        validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Additional properties are allowed")
    @allure.description("Verifies that additional properties are accepted.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_additional_properties(self, valid_user: dict):
        valid_user["country"] = "USA"

        validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing id")
    @allure.description("Verifies that validation fails when id is missing.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_missing_id(self, valid_user: dict):
        valid_user.pop("id")

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing firstName")
    @allure.description("Verifies that validation fails when firstName is missing.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_missing_first_name(self, valid_user: dict):
        valid_user.pop("firstName")

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing email")
    @allure.description("Verifies that validation fails when email is missing.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_missing_email(self, valid_user: dict):
        valid_user.pop("email")

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Negative age")
    @allure.description("Verifies that negative age values are rejected.")
    @pytest.mark.schema
    @pytest.mark.negative
    @pytest.mark.boundary
    def test_negative_age(self, valid_user: dict):
        valid_user["age"] = -1

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Id must be integer")
    @allure.description("Verifies that id must be an integer.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_id_type(self, valid_user: dict):
        valid_user["id"] = "1"

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Age must be integer")
    @allure.description("Verifies that age must be an integer.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_age_type(self, valid_user: dict):
        valid_user["age"] = "18"

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Email must be string")
    @allure.description("Verifies that email must be a string.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_email_type(self, valid_user: dict):
        valid_user["email"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("firstName must be string")
    @allure.description("Verifies that firstName must be a string.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_first_name_type(self, valid_user: dict):
        valid_user["firstName"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("lastName must be string")
    @allure.description("Verifies that lastName must be a string.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_last_name_type(self, valid_user: dict):
        valid_user["lastName"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_user, schema=USER_SCHEMA)

    @allure.story("Validation")
    @allure.title("Gender must be string")
    @allure.description("Verifies that gender must be a string.")
    @pytest.mark.schema
    @pytest.mark.negative
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
    @allure.description("Verifies that different valid age values pass validation.")
    @pytest.mark.schema
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_valid_ages(self, valid_user: dict, age: int):
        valid_user["age"] = age

        validate(instance=valid_user, schema=USER_SCHEMA)
