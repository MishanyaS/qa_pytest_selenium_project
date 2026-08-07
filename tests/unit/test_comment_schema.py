from typing import Any

import allure
import pytest
from jsonschema import ValidationError, validate

from schemas.comment_schema import COMMENT_SCHEMA


@allure.epic("Unit")
@allure.feature("Comment Schema")
@pytest.mark.unit
class TestCommentSchema:
    @pytest.fixture(scope="function")
    def valid_comment(self) -> dict[str, Any]:
        return {
            "id": 1,
            "body": "Test comment",
            "postId": 10,
            "likes": 5,
            "user": {
                "id": 3,
                "username": "johnsmith",
            },
        }

    @allure.story("Schema")
    @allure.title("Schema is object")
    @allure.description("Verifies that the schema root type is object.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_schema_type(self) -> None:
        assert COMMENT_SCHEMA["type"] == "object"

    @allure.story("Schema")
    @allure.title("Schema contains required section")
    @allure.description("Verifies that the schema contains the required section.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_required_exists(self) -> None:
        assert "required" in COMMENT_SCHEMA

    @allure.story("Schema")
    @allure.title("Schema contains properties section")
    @allure.description("Verifies that the schema contains the properties section.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_properties_exists(self) -> None:
        assert "properties" in COMMENT_SCHEMA

    @allure.story("Schema")
    @allure.title("Required fields count")
    @allure.description(
        "Verifies that the schema defines the expected number of required fields."
    )
    @pytest.mark.positive
    @pytest.mark.schema
    def test_required_fields_count(self) -> None:
        assert len(COMMENT_SCHEMA["required"]) == 5

    @allure.story("Schema")
    @allure.title("Required fields match expected")
    @allure.description("Verifies that the required fields match the expected list.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_required_fields(self) -> None:
        assert COMMENT_SCHEMA["required"] == [
            "id",
            "body",
            "postId",
            "likes",
            "user",
        ]

    @allure.story("Schema")
    @allure.title("Properties count")
    @allure.description(
        "Verifies that the schema defines the expected number of properties."
    )
    @pytest.mark.positive
    @pytest.mark.schema
    def test_properties_count(self) -> None:
        assert len(COMMENT_SCHEMA["properties"]) == 5

    @allure.story("Schema")
    @allure.title("Id type")
    @allure.description("Verifies that the id property is defined as an integer.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_id_type(self) -> None:
        assert COMMENT_SCHEMA["properties"]["id"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Body type")
    @allure.description("Verifies that the body property is defined as a string.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_body_type(self) -> None:
        assert COMMENT_SCHEMA["properties"]["body"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("postId type")
    @allure.description("Verifies that the postId property is defined as an integer.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_post_id_type(self) -> None:
        assert COMMENT_SCHEMA["properties"]["postId"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Likes type")
    @allure.description("Verifies that the likes property is defined as an integer.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_likes_type(self) -> None:
        assert COMMENT_SCHEMA["properties"]["likes"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Likes minimum")
    @allure.description("Verifies that the minimum value for likes is zero.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_likes_minimum(self) -> None:
        assert COMMENT_SCHEMA["properties"]["likes"]["minimum"] == 0

    @allure.story("Schema")
    @allure.title("User type")
    @allure.description("Verifies that the user property is defined as an object.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_user_type(self) -> None:
        assert COMMENT_SCHEMA["properties"]["user"]["type"] == "object"

    @allure.story("Schema")
    @allure.title("User required fields")
    @allure.description("Verifies that the user object defines the required fields.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_user_required_fields(self) -> None:
        assert COMMENT_SCHEMA["properties"]["user"]["required"] == [
            "id",
            "username",
        ]

    @allure.story("Schema")
    @allure.title("User id type")
    @allure.description("Verifies that the user id property is defined as an integer.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_user_id_type(self) -> None:
        assert (
            COMMENT_SCHEMA["properties"]["user"]["properties"]["id"]["type"]
            == "integer"
        )

    @allure.story("Schema")
    @allure.title("Username type")
    @allure.description("Verifies that the username property is defined as a string.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_username_type(self) -> None:
        assert (
            COMMENT_SCHEMA["properties"]["user"]["properties"]["username"]["type"]
            == "string"
        )

    @allure.story("Validation")
    @allure.title("Valid comment passes validation")
    @allure.description("Verifies that a valid comment passes schema validation.")
    @pytest.mark.positive
    @pytest.mark.schema
    def test_valid_comment(self, valid_comment: dict[str, Any]) -> None:
        validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Additional properties are allowed")
    @allure.description(
        "Verifies that additional properties are accepted by the schema."
    )
    @pytest.mark.positive
    @pytest.mark.schema
    def test_additional_properties(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["createdAt"] = "2026-07-25"

        validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing id")
    @allure.description("Verifies that validation fails when the id field is missing.")
    @pytest.mark.negative
    @pytest.mark.schema
    def test_missing_id(self, valid_comment: dict[str, Any]) -> None:
        valid_comment.pop("id")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing body")
    @allure.description(
        "Verifies that validation fails when the body field is missing."
    )
    @pytest.mark.negative
    @pytest.mark.schema
    def test_missing_body(self, valid_comment: dict[str, Any]) -> None:
        valid_comment.pop("body")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing user")
    @allure.description(
        "Verifies that validation fails when the user field is missing."
    )
    @pytest.mark.negative
    @pytest.mark.schema
    def test_missing_user(self, valid_comment: dict[str, Any]) -> None:
        valid_comment.pop("user")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing username")
    @allure.description(
        "Verifies that validation fails when the username field is missing."
    )
    @pytest.mark.negative
    @pytest.mark.schema
    def test_missing_username(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["user"].pop("username")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Negative likes")
    @allure.description("Verifies that validation fails for negative likes values.")
    @pytest.mark.negative
    @pytest.mark.schema
    @pytest.mark.boundary
    def test_negative_likes(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["likes"] = -1

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Id must be integer")
    @allure.description("Verifies that validation fails when id is not an integer.")
    @pytest.mark.negative
    @pytest.mark.schema
    def test_invalid_id_type(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["id"] = "1"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Body must be string")
    @allure.description("Verifies that validation fails when body is not a string.")
    @pytest.mark.negative
    @pytest.mark.schema
    def test_invalid_body_type(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["body"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("postId must be integer")
    @allure.description("Verifies that validation fails when postId is not an integer.")
    @pytest.mark.negative
    @pytest.mark.schema
    def test_invalid_post_id_type(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["postId"] = "10"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Likes must be integer")
    @allure.description("Verifies that validation fails when likes is not an integer.")
    @pytest.mark.negative
    @pytest.mark.schema
    def test_invalid_likes_type(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["likes"] = "5"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("User must be object")
    @allure.description("Verifies that validation fails when user is not an object.")
    @pytest.mark.negative
    @pytest.mark.schema
    def test_invalid_user_type(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["user"] = []

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("User id must be integer")
    @allure.description(
        "Verifies that validation fails when user id is not an integer."
    )
    @pytest.mark.negative
    @pytest.mark.schema
    def test_invalid_user_id_type(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["user"]["id"] = "3"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Username must be string")
    @allure.description("Verifies that validation fails when username is not a string.")
    @pytest.mark.negative
    @pytest.mark.schema
    def test_invalid_username_type(self, valid_comment: dict[str, Any]) -> None:
        valid_comment["user"]["username"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Validate several likes values")
    @pytest.mark.parametrize(
        "likes",
        [
            0,
            1,
            10,
            100,
            1000,
        ],
    )
    @allure.description("Verifies that valid likes values pass schema validation.")
    @pytest.mark.positive
    @pytest.mark.schema
    @pytest.mark.boundary
    def test_valid_likes(self, valid_comment: dict[str, Any], likes: int) -> None:
        valid_comment["likes"] = likes

        validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Validate several post ids")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            10,
            100,
            999,
        ],
    )
    @allure.description("Verifies that valid postId values pass schema validation.")
    @pytest.mark.positive
    @pytest.mark.schema
    @pytest.mark.boundary
    def test_valid_post_ids(self, valid_comment: dict[str, Any], post_id: int) -> None:
        valid_comment["postId"] = post_id

        validate(instance=valid_comment, schema=COMMENT_SCHEMA)
