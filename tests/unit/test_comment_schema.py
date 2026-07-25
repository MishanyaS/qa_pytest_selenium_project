import allure
import pytest
from jsonschema import ValidationError, validate

from schemas.comment_schema import COMMENT_SCHEMA

allure.epic("Unit")
@allure.feature("Comment Schema")
@pytest.mark.unit
class TestCommentSchema:
    @pytest.fixture()
    def valid_comment(self) -> dict:
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
    def test_schema_type(self):
        assert COMMENT_SCHEMA["type"] == "object"

    @allure.story("Schema")
    @allure.title("Schema contains required section")
    def test_required_exists(self):
        assert "required" in COMMENT_SCHEMA

    @allure.story("Schema")
    @allure.title("Schema contains properties section")
    def test_properties_exists(self):
        assert "properties" in COMMENT_SCHEMA

    @allure.story("Schema")
    @allure.title("Required fields count")
    def test_required_fields_count(self):
        assert len(COMMENT_SCHEMA["required"]) == 5

    @allure.story("Schema")
    @allure.title("Required fields match expected")
    def test_required_fields(self):
        assert COMMENT_SCHEMA["required"] == [
            "id",
            "body",
            "postId",
            "likes",
            "user",
        ]

    @allure.story("Schema")
    @allure.title("Properties count")
    def test_properties_count(self):
        assert len(COMMENT_SCHEMA["properties"]) == 5

    @allure.story("Schema")
    @allure.title("Id type")
    def test_id_type(self):
        assert COMMENT_SCHEMA["properties"]["id"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Body type")
    def test_title_type(self):
        assert COMMENT_SCHEMA["properties"]["body"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("postId type")
    def test_post_id_type(self):
        assert COMMENT_SCHEMA["properties"]["postId"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Likes type")
    def test_likes_type(self):
        assert COMMENT_SCHEMA["properties"]["likes"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Likes minimum")
    def test_likes_minimum(self):
        assert COMMENT_SCHEMA["properties"]["likes"]["minimum"] == 0

    @allure.story("Schema")
    @allure.title("User type")
    def test_user_type(self):
        assert COMMENT_SCHEMA["properties"]["user"]["type"] == "object"

    @allure.story("Schema")
    @allure.title("User required fields")
    def test_user_required_fields(self):
        assert COMMENT_SCHEMA["properties"]["user"]["required"] == [
            "id",
            "username",
        ]

    @allure.story("Schema")
    @allure.title("User id type")
    def test_user_id_type(self):
        assert COMMENT_SCHEMA["properties"]["user"]["properties"]["id"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Username type")
    def test_username_type(self):
        assert COMMENT_SCHEMA["properties"]["user"]["properties"]["username"]["type"] == "string"

    @allure.story("Validation")
    @allure.title("Valid comment passes validation")
    def test_valid_comment(self, valid_comment: dict):
        validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Additional properties are allowed")
    def test_additional_properties(self, valid_comment: dict):
        valid_comment["createdAt"] = "2026-07-25"

        validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing id")
    def test_missing_id(self, valid_comment: dict):
        valid_comment.pop("id")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing body")
    def test_missing_body(self, valid_comment: dict):
        valid_comment.pop("body")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing user")
    def test_missing_user(self, valid_comment: dict):
        valid_comment.pop("user")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing username")
    def test_missing_username(self, valid_comment: dict):
        valid_comment["user"].pop("username")

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Negative likes")
    def test_negative_likes(self, valid_comment: dict):
        valid_comment["likes"] = -1

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Id must be integer")
    def test_invalid_id_type(self, valid_comment: dict):
        valid_comment["id"] = "1"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Body must be string")
    def test_invalid_body_type(self, valid_comment: dict):
        valid_comment["body"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("postId must be integer")
    def test_invalid_post_id_type(self, valid_comment: dict):
        valid_comment["postId"] = "10"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Likes must be integer")
    def test_invalid_likes_type(self, valid_comment: dict):
        valid_comment["likes"] = "5"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("User must be object")
    def test_invalid_user_type(self, valid_comment: dict):
        valid_comment["user"] = []

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("User id must be integer")
    def test_invalid_user_id_type(self, valid_comment: dict):
        valid_comment["user"]["id"] = "3"

        with pytest.raises(ValidationError):
            validate(instance=valid_comment, schema=COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Username must be string")
    def test_invalid_username_type(self, valid_comment: dict):
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
        ]
    )
    def test_valid_likes(self, valid_comment: dict, likes: int):
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
        ]
    )
    def test_valid_post_ids(self, valid_comment: dict, post_id: int):
        valid_comment["postId"] = post_id

        validate(instance=valid_comment, schema=COMMENT_SCHEMA)
