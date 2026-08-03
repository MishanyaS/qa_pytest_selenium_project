import allure
import pytest
from jsonschema import ValidationError, validate

from schemas.post_schema import POST_SCHEMA

@allure.epic("Unit")
@allure.feature("Post Schema")
@pytest.mark.unit
class TestPostSchema:
    @pytest.fixture()
    def valid_post(self) -> dict:
        return {
            "id": 1,
            "title": "Test title",
            "body": "Test body",
            "userId": 5,
            "tags": [
                "python",
                "pytest",
            ],
            "reactions": {
                "likes": 15,
                "dislikes": 2,
            },
            "views": 150,
        }

    @allure.story("Schema")
    @allure.title("Schema is object")
    @allure.description("Verifies that the schema root type is object.")
    @pytest.mark.positive
    def test_schema_type(self):
        assert POST_SCHEMA["type"] == "object"

    @allure.story("Schema")
    @allure.title("Schema contains required section")
    @allure.description("Verifies that the schema defines required fields.")
    @pytest.mark.positive
    def test_required_exists(self):
        assert "required" in POST_SCHEMA

    @allure.story("Schema")
    @allure.title("Schema contains properties section")
    @allure.description("Verifies that the schema defines properties.")
    @pytest.mark.positive
    def test_properties_exists(self):
        assert "properties" in POST_SCHEMA

    @allure.story("Schema")
    @allure.title("Required fields count")
    @allure.description("Verifies that the schema contains seven required fields.")
    @pytest.mark.positive
    def test_required_fields_count(self):
        assert len(POST_SCHEMA["required"]) == 7

    @allure.story("Schema")
    @allure.title("Required fields match expected")
    @allure.description("Verifies that required fields match the expected list.")
    @pytest.mark.positive
    def test_required_fields(self):
        assert POST_SCHEMA["required"] == [
            "id",
            "title",
            "body",
            "userId",
            "tags",
            "reactions",
            "views",
        ]

    @allure.story("Schema")
    @allure.title("Properties count")
    @allure.description("Verifies that the schema defines seven properties.")
    @pytest.mark.positive
    def test_properties_count(self):
        assert len(POST_SCHEMA["properties"]) == 7

    @allure.story("Schema")
    @allure.title("Id type")
    @allure.description("Verifies that the id property is an integer.")
    @pytest.mark.positive
    def test_id_type(self):
        assert POST_SCHEMA["properties"]["id"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Title type")
    @allure.description("Verifies that the title property is a string.")
    @pytest.mark.positive
    def test_title_type(self):
        assert POST_SCHEMA["properties"]["title"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Body type")
    @allure.description("Verifies that the body property is a string.")
    @pytest.mark.positive
    def test_body_type(self):
        assert POST_SCHEMA["properties"]["body"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("userId type")
    @allure.description("Verifies that the userId property is an integer.")
    @pytest.mark.positive
    def test_user_id_type(self):
        assert POST_SCHEMA["properties"]["userId"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Tags type")
    @allure.description("Verifies that the tags property is an array.")
    @pytest.mark.positive
    def test_tags_format(self):
        assert POST_SCHEMA["properties"]["tags"]["type"] == "array"

    @allure.story("Schema")
    @allure.title("Tags item type")
    @allure.description("Verifies that tag items are strings.")
    @pytest.mark.positive
    def test_tags_item_type(self):
        assert POST_SCHEMA["properties"]["tags"]["items"]["type"] == "string"

    @allure.story("Schema")
    @allure.title("Reactions type")
    @allure.description("Verifies that the reactions property is an object.")
    @pytest.mark.positive
    def test_reactions_type(self):
        assert POST_SCHEMA["properties"]["reactions"]["type"] == "object"

    @allure.story("Schema")
    @allure.title("Views type")
    @allure.description("Verifies that the views property is an integer.")
    @pytest.mark.positive
    def test_views_type(self):
        assert POST_SCHEMA["properties"]["views"]["type"] == "integer"

    @allure.story("Schema")
    @allure.title("Views minimum")
    @allure.description("Verifies that the minimum allowed value foe views is zero.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_views_minimum(self):
        assert POST_SCHEMA["properties"]["views"]["minimum"] == 0

    @allure.story("Schema")
    @allure.title("Likes minimum")
    @allure.description("Verifies that the minimum allowed value foe likes is zero.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_likes_minimum(self):
        assert POST_SCHEMA["properties"]["reactions"]["properties"]["likes"]["minimum"] == 0

    @allure.story("Schema")
    @allure.title("Dislikes minimum")
    @allure.description("Verifies that the minimum allowed value foe dislikes is zero.")
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_dislikes_minimum(self):
        assert POST_SCHEMA["properties"]["reactions"]["properties"]["dislikes"]["minimum"] == 0

    @allure.story("Validation")
    @allure.title("Valid post passes validation")
    @allure.description("Verifies that a valid post passes schema validation.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_valid_post(self, valid_post: dict):
        validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Additional properties are allowed")
    @allure.description("Verifies that additional properties are accepted.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_additional_properties(self, valid_post: dict):
        valid_post["country"] = "2026-07-25"

        validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing id")
    @allure.description("Verifies that validation fails when id is missing.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_missing_id(self, valid_post: dict):
        valid_post.pop("id")

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing title")
    @allure.description("Verifies that validation fails when title is missing.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_missing_title(self, valid_post: dict):
        valid_post.pop("title")

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Missing reactions")
    @allure.description("Verifies that validation fails when reactions are missing.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_missing_reactions(self, valid_post: dict):
        valid_post.pop("reactions")

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Negative views")
    @allure.description("Verifies that negative views are rejected.")
    @pytest.mark.schema
    @pytest.mark.negative
    @pytest.mark.boundary
    def test_negative_views(self, valid_post: dict):
        valid_post["views"] = -1

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Negative likes")
    @allure.description("Verifies that negative likes are rejected.")
    @pytest.mark.schema
    @pytest.mark.negative
    @pytest.mark.boundary
    def test_negative_likes(self, valid_post: dict):
        valid_post["reactions"]["likes"] = -1

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Negative dislikes")
    @allure.description("Verifies that negative dislikes are rejected.")
    @pytest.mark.schema
    @pytest.mark.negative
    @pytest.mark.boundary
    def test_negative_dislikes(self, valid_post: dict):
        valid_post["reactions"]["dislikes"] = -1

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Id must be integer")
    @allure.description("Verifies that id must be an integer.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_id_type(self, valid_post: dict):
        valid_post["id"] = "1"

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Title must be string")
    @allure.description("Verifies that title must be a string.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_title_type(self, valid_post: dict):
        valid_post["title"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Body must be string")
    @allure.description("Verifies that body must be a string.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_body_type(self, valid_post: dict):
        valid_post["body"] = 123

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Tags must be array")
    @allure.description("Verifies that tags must be an array.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_tags_type(self, valid_post: dict):
        valid_post["tags"] = "python"

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Reactions must be object")
    @allure.description("Verifies that reactions must be an object.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_reactions_type(self, valid_post: dict):
        valid_post["reactions"] = []

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Views must be integer")
    @allure.description("Verifies that views must be an integer.")
    @pytest.mark.schema
    @pytest.mark.negative
    def test_invalid_views_type(self, valid_post: dict):
        valid_post["views"] = "100"

        with pytest.raises(ValidationError):
            validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Validate several view values")
    @pytest.mark.parametrize(
        "views",
        [
            0,
            1,
            100,
            1000,
            100000,
        ]
    )
    @allure.description("Verifies that different valid views values pass validation.")
    @pytest.mark.schema
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_valid_views(self, valid_post: dict, views: int):
        valid_post["views"] = views

        validate(instance=valid_post, schema=POST_SCHEMA)

    @allure.story("Validation")
    @allure.title("Validate several tag counts")
    @pytest.mark.parametrize(
        "tags",
        [
            [],
            ["python"],
            ["python", "pytest"],
            ["api", "json", "schema"],
        ]
    )
    @allure.description("Verifies that different valid tag collections pass validation.")
    @pytest.mark.schema
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_valid_tags(self, valid_post: dict, tags: list[str]):
        valid_post["tags"] = tags

        validate(instance=valid_post, schema=POST_SCHEMA)
