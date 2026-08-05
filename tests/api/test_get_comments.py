import allure
import pytest
import requests
from jsonschema import validate
from typing import Any

from schemas.comment_schema import COMMENT_SCHEMA
from utils.api_client import ApiClient
from utils.validators import validate_status_code

@allure.epic("API")
@allure.feature("Comments")
@pytest.mark.api
@pytest.mark.regression
class TestGetComments:
    @allure.step("Get comment")
    def _get_comment(self, client: ApiClient, comment_id: int) -> requests.Response:
        return client.get(f"/comments/{comment_id}")

    @allure.step("Get comments")
    def _get_comments(self, client: ApiClient, **kwargs: Any) -> requests.Response:
        return client.get("/comments", **kwargs)

    @allure.story("Get comments list")
    @allure.title("GET /comments returns 200")
    @allure.description("Verifies that the comments list endpoint returns HTTP 200.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_get_comments_status_code(self, client: ApiClient):
        response = self._get_comments(client)

        assert validate_status_code(response.status_code, 200)

    @allure.story("Get comments list")
    @allure.title("Response is JSON")
    @allure.description("Verifies that the comments list response is returned in JSON format.")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient):
        response = self._get_comments(client)

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Get comments list")
    @allure.title("Response contains comments")
    @allure.description("Verifies that the response contains the comments field.")
    @pytest.mark.positive
    def test_comments_key_exists(self, client: ApiClient):
        response = self._get_comments(client)

        data = response.json()

        assert "comments" in data

    @allure.story("Get comments list")
    @allure.title("Comments is list")
    @allure.description("Verifies that the comments field is a list.")
    @pytest.mark.positive
    def test_comments_is_list(self, client: ApiClient):
        response = self._get_comments(client)

        data = response.json()

        assert isinstance(data["comments"], list)

    @allure.story("Get comments list")
    @allure.title("Comments list is not empty")
    @allure.description("Verifies that the comments list is not empty.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_comments_is_not_empty(self, client: ApiClient):
        response = self._get_comments(client)

        data = response.json()

        assert len(data["comments"]) > 0

    @allure.story("Schema check")
    @allure.title("First comment matches schema")
    @allure.description("Verifies that the first comment matches the JSON schema.")
    @pytest.mark.schema
    def test_first_comment_schema(self, client: ApiClient):
        response = self._get_comments(client)

        first_comment = response.json()["comments"][0]

        validate(instance=first_comment, schema=COMMENT_SCHEMA)

    @allure.story("Get comments list")
    @allure.title("Comments total count is bigger than 0")
    @allure.description("Verifies that the total number of comments is greater than zero.")
    @pytest.mark.positive
    def test_total_positive(self, client: ApiClient):
        response = self._get_comments(client)

        data = response.json()

        assert data["total"] > 0

    @allure.story("Get comments list")
    @allure.title("limit is bigger than 0")
    @allure.description("Verifies that the limit value is greater than zero.")
    @pytest.mark.positive
    def test_limit_positive(self, client: ApiClient):
        response = self._get_comments(client)

        data = response.json()

        assert data["limit"] > 0

    @allure.story("Get comments list")
    @allure.title("skip is not negative")
    @allure.description("Verifies that the skip value is not negative.")
    @pytest.mark.positive
    def test_skip_not_negative(self, client: ApiClient):
        response = self._get_comments(client)

        data = response.json()

        assert data["skip"] >= 0

    @allure.story("Get comments list")
    @allure.title("First comment contains id")
    @allure.description("Verifies that the first comment contains the id field.")
    @pytest.mark.positive
    def test_first_comment_has_id(self, client: ApiClient):
        response = self._get_comments(client)

        first_comment = response.json()["comments"][0]

        assert "id" in first_comment

    @allure.story("Get comments list")
    @allure.title("First comment contains body")
    @allure.description("Verifies that the first comment contains the body field.")
    @pytest.mark.positive
    def test_first_comment_has_body(self, client: ApiClient):
        response = self._get_comments(client)

        first_comment = response.json()["comments"][0]

        assert "body" in first_comment

    @allure.story("Get comments list")
    @allure.title("First comment contains likes")
    @allure.description("Verifies that the first comment contains the likes field.")
    @pytest.mark.positive
    def test_first_comment_has_likes(self, client: ApiClient):
        response = self._get_comments(client)

        first_comment = response.json()["comments"][0]

        assert "likes" in first_comment

    @allure.story("Get comments list")
    @allure.title("First comment contains user")
    @allure.description("Verifies that the first comment contains the user field.")
    @pytest.mark.positive
    def test_first_comment_has_user(self, client: ApiClient):
        response = self._get_comments(client)

        first_comment = response.json()["comments"][0]

        assert "user" in first_comment

    @allure.story("Get single comment")
    @allure.title("GET /comments/1 returns 200")
    @allure.description("Verifies that retrieving a single comment returns HTTP 200.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_get_single_comment_status_code(self, client: ApiClient):
        response = self._get_comment(client, 1)

        assert response.status_code == 200

    @allure.story("Get single comment")
    @allure.title("Single comment matches schema")
    @allure.description("Verifies that the returned comment matches the JSON schema.")
    @pytest.mark.schema
    def test_single_comment_schema(self, client: ApiClient):
        response = self._get_comment(client, 1)

        validate(instance=response.json(), schema=COMMENT_SCHEMA)

    @allure.story("Get single comment")
    @allure.title("Returned id matches requested")
    @allure.description("Verifies that the returned comment id matches the requested id.")
    @pytest.mark.positive
    def test_comment_id_matches(self, client: ApiClient):
        response = self._get_comment(client, 1)

        assert response.json()["id"] == 1

    @allure.story("Pagination")
    @allure.title("Limit parameter works")
    @allure.description("Verifies that the limit parameter restricts the number of returned comments.")
    @pytest.mark.parametrize(
        "limit",
        [
            1,
            3,
            5,
            10,
            20,
        ],
    )
    @pytest.mark.positive
    def test_limit_parameter(self, client: ApiClient, limit: int):
        response = self._get_comments(client, params={"limit": limit})

        comments = response.json()["comments"]

        assert len(comments) == limit

    @allure.story("Pagination")
    @allure.title("Skip parameter works")
    @allure.description("Verifies that the skip parameter offsets the returned comments.")
    @pytest.mark.parametrize(
        "skip",
        [
            0,
            1,
            5,
            10,
            20,
        ],
    )
    @pytest.mark.positive
    def test_skip_parameter(self, client: ApiClient, skip: int):
        response = self._get_comments(client, params={"skip": skip})

        assert response.json()["skip"] == skip

    @allure.story("Pagination")
    @allure.title("Limit and skip together")
    @allure.description("Verifies that limit and skip parameters work together correctly.")
    @pytest.mark.parametrize(
        "limit, skip",
        [
            (5, 0),
            (5, 5),
            (10, 10),
            (15, 15),
        ],
    )
    @pytest.mark.regression
    @pytest.mark.positive
    def test_limit_skip(self, client: ApiClient, limit: int, skip: int):
        response = self._get_comments(client, params={"limit": limit, "skip": skip})

        data = response.json()

        assert len(data["comments"]) == limit
        assert data["skip"] == skip

    @allure.story("Get comments by post")
    @allure.title("GET /comments/post/{post_id} returns 200")
    @allure.description("Verifies that comments can be retrieved for a specific post.")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            2,
            3,
            10,
            20,
        ],
    )
    @pytest.mark.positive
    def test_comment_by_post_status_code(self, client: ApiClient, post_id: int):
        response = client.get(f"/comments/post/{post_id}")

        assert response.status_code == 200

    @allure.story("Get comments by post")
    @allure.title("Returned comments belong to requested post")
    @allure.description("Verifies that all returned comments belong to the requested post.")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            2,
            3,
            10,
            20,
        ],
    )
    @pytest.mark.regression
    @pytest.mark.positive
    def test_comments_belong_to_post(self, client: ApiClient, post_id: int):
        response = client.get(f"/comments/post/{post_id}")

        comments = response.json()["comments"]

        assert all(
            comment["postId"] == post_id
            for comment in comments
        )

    @allure.story("Validation")
    @allure.title("Every comment has unique id")
    @allure.description("Verifies that all returned comments have unique ids.")
    @pytest.mark.regression
    def test_unique_comment_ids(self, client: ApiClient):
        response = self._get_comments(client)

        data = response.json()

        ids = [
            comment["id"]
            for comment in data["comments"]
        ]

        assert len(ids) == len(set(ids))

    @allure.story("Validation")
    @allure.title("Every comment has body")
    @allure.description("Verifies that every returned comment has a non-empty body.")
    @pytest.mark.regression
    def test_comment_bodies_not_empty(self, client: ApiClient):
        response = self._get_comments(client)

        comments = response.json()["comments"]

        assert all(
            len(comment["body"].strip()) > 0
            for comment in comments
        )

    @allure.story("Validation")
    @allure.title("Likes are not negative")
    @allure.description("Verifies that comment likes are never negative.")
    @pytest.mark.regression
    def test_likes_not_negative(self, client: ApiClient):
        response = self._get_comments(client)

        comments = response.json()["comments"]

        assert all(
            comment["likes"] >= 0
            for comment in comments
        )

    @allure.story("Validation")
    @allure.title("Every comment has user id")
    @allure.description("Verifies that every comment contains a user id.")
    @pytest.mark.regression
    def test_every_comment_has_user_id(self, client: ApiClient):
        response = self._get_comments(client)

        comments = response.json()["comments"]

        assert all(
            "id" in comment["user"]
            for comment in comments
        )

    @allure.story("Validation")
    @allure.title("Every comment has username")
    @allure.description("Verifies that every comment contains a username.")
    @pytest.mark.regression
    def test_every_comment_has_username(self, client: ApiClient):
        response = self._get_comments(client)

        comments = response.json()["comments"]

        assert all(
            "username" in comment["user"]
            for comment in comments
        )

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @allure.description("Verifies that the response time is within the expected limit.")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient):
        response = self._get_comments(client)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @allure.description("Verifies that an unknown endpoint returns HTTP 404.")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.get("/comments123456")

        assert response.status_code == 404

    @allure.story("Step by step")
    @allure.title("Several comments are successfully loaded")
    @allure.description("Verifies successful retrieval of multiple comments using different ids.")
    @pytest.mark.parametrize(
        "comment_id",
        [
            1,
            2,
            3,
            10,
            20,
        ],
    )
    @pytest.mark.regression
    @pytest.mark.positive
    def test_multiple_comments(self, client: ApiClient, comment_id: int):
        response = self._get_comment(client, comment_id)

        assert response.status_code == 200
        assert response.json()["id"] == comment_id
