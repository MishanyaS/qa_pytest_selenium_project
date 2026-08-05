from typing import Any

import allure
import pytest
import requests
from jsonschema import validate

from schemas.post_schema import POST_SCHEMA
from utils.api_client import ApiClient
from utils.validators import validate_status_code


@allure.epic("API")
@allure.feature("Posts")
@pytest.mark.api
@pytest.mark.regression
class TestGetPosts:
    @allure.step("Get post")
    def _get_post(self, client: ApiClient, post_id: int) -> requests.Response:
        return client.get(f"/posts/{post_id}")

    @allure.step("Get posts")
    def _get_posts(self, client: ApiClient, **kwargs: Any) -> requests.Response:
        return client.get("/posts", **kwargs)

    @allure.story("Get posts list")
    @allure.title("GET /posts returns 200")
    @allure.description("Verifies that GET /posts returns HTTP 200 status code.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_get_posts_status_code(self, client: ApiClient):
        response = self._get_posts(client)

        assert validate_status_code(response.status_code, 200)

    @allure.story("Get posts list")
    @allure.title("Response is JSON")
    @allure.description("Verifies that the response Content-Type is JSON.")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient):
        response = self._get_posts(client)

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Get posts list")
    @allure.title("Response contains posts")
    @allure.description("Verifies that the response contains the 'posts' field.")
    @pytest.mark.positive
    def test_posts_key_exists(self, client: ApiClient):
        response = self._get_posts(client)

        data = response.json()

        assert "posts" in data

    @allure.story("Get posts list")
    @allure.title("posts is list")
    @allure.description("Verifies that the 'posts' field is returned as a list.")
    @pytest.mark.positive
    def test_posts_is_list(self, client: ApiClient):
        response = self._get_posts(client)

        data = response.json()

        assert isinstance(data["posts"], list)

    @allure.story("Get posts list")
    @allure.title("Posts list is not empty")
    @allure.description("Verifies that the posts list is not empty.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_posts_is_not_empty(self, client: ApiClient):
        response = self._get_posts(client)

        data = response.json()

        assert len(data["posts"]) > 0

    @allure.story("Schema check")
    @allure.title("First post matches schema")
    @allure.description("Verifies that the first post matches the JSON schema.")
    @pytest.mark.schema
    def test_first_post_schema(self, client: ApiClient):
        response = self._get_posts(client)

        first_post = response.json()["posts"][0]

        validate(instance=first_post, schema=POST_SCHEMA)

    @allure.story("Get posts list")
    @allure.title("Posts total count is bigger than 0")
    @allure.description("Verifies that the total number of posts is greater than zero.")
    @pytest.mark.positive
    def test_total_positive(self, client: ApiClient):
        response = self._get_posts(client)

        data = response.json()

        assert data["total"] > 0

    @allure.story("Get posts list")
    @allure.title("limit is bigger than 0")
    @allure.description("Verifies that the limit value is greater than zero.")
    @pytest.mark.positive
    def test_limit_positive(self, client: ApiClient):
        response = self._get_posts(client)

        data = response.json()

        assert data["limit"] > 0

    @allure.story("Get posts list")
    @allure.title("skip is not negative")
    @allure.description("Verifies that the skip value is not negative.")
    @pytest.mark.positive
    def test_skip_not_negative(self, client: ApiClient):
        response = self._get_posts(client)

        data = response.json()

        assert data["skip"] >= 0

    @allure.story("Get posts list")
    @allure.title("First post contains id")
    @allure.description("Verifies that the first post contains the 'id' field.")
    @pytest.mark.positive
    def test_first_post_has_id(self, client: ApiClient):
        response = self._get_posts(client)

        first_post = response.json()["posts"][0]

        assert "id" in first_post

    @allure.story("Get posts list")
    @allure.title("First post contains title")
    @allure.description("Verifies that the first post contains the 'title' field.")
    @pytest.mark.positive
    def test_first_post_has_title(self, client: ApiClient):
        response = self._get_posts(client)

        first_post = response.json()["posts"][0]

        assert "title" in first_post

    @allure.story("Get posts list")
    @allure.title("First post contains body")
    @allure.description("Verifies that the first post contains the 'body' field.")
    @pytest.mark.positive
    def test_first_post_has_body(self, client: ApiClient):
        response = self._get_posts(client)

        first_post = response.json()["posts"][0]

        assert "body" in first_post

    @allure.story("Get single post")
    @allure.title("GET /posts/1 returns 200")
    @allure.description("Verifies that GET /posts/{id} returns HTTP 200 status code.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_get_single_post_status_code(self, client: ApiClient):
        response = self._get_post(client, 1)

        assert response.status_code == 200

    @allure.story("Get single post")
    @allure.title("Single post matches schema")
    @allure.description("Verifies that the returned post matches the JSON schema.")
    @pytest.mark.schema
    def test_single_post_schema(self, client: ApiClient):
        response = self._get_post(client, 1)

        validate(instance=response.json(), schema=POST_SCHEMA)

    @allure.story("Get single post")
    @allure.title("Post id equals requested id")
    @allure.description("Verifies that the returned post ID matches the requested ID.")
    @pytest.mark.positive
    def test_post_id_matches_requested(self, client: ApiClient):
        response = self._get_post(client, 1)

        assert response.json()["id"] == 1

    @allure.story("Pagination")
    @allure.title("Limit parameter works")
    @allure.description(
        "Verifies that the limit query parameter limits the number of returned posts."
    )
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
    @pytest.mark.boundary
    def test_limit_parameter(self, client: ApiClient, limit: int):
        response = self._get_posts(client, params={"limit": limit})

        posts = response.json()["posts"]

        assert len(posts) == limit

    @allure.story("Pagination")
    @allure.title("Skip parameter works")
    @allure.description(
        "Verifies that the skip query parameter skips the expected number of posts."
    )
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
    @pytest.mark.boundary
    def test_skip_parameter(self, client: ApiClient, skip: int):
        response = self._get_posts(client, params={"skip": skip})

        assert response.json()["skip"] == skip

    @allure.story("Pagination")
    @allure.title("Limit and skip together")
    @allure.description(
        "Verifies that limit and skip parameters work correctly together."
    )
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
    @pytest.mark.boundary
    def test_limit_skip(self, client: ApiClient, limit: int, skip: int):
        response = self._get_posts(client, params={"limit": limit, "skip": skip})

        data = response.json()

        assert len(data["posts"]) == limit
        assert data["skip"] == skip

    @allure.story("Search")
    @allure.title("Search returns 200")
    @allure.description(
        "Verifies that the search endpoint returns HTTP 200 status code."
    )
    @pytest.mark.positive
    def test_search_status_code(self, client: ApiClient):
        response = client.get("/posts/search", params={"q": "love"})

        assert response.status_code == 200

    @allure.story("Search")
    @allure.title("Search result contains query")
    @allure.description("Verifies that search results contain the requested query.")
    @pytest.mark.positive
    def test_search_contains_query(self, client: ApiClient):
        response = client.get("/posts/search", params={"q": "love"})

        posts = response.json()["posts"]

        assert any(
            "love" in post["title"].lower() or "love" in post["body"].lower()
            for post in posts
        )

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @allure.description("Verifies that the response time is less than two seconds.")
    @pytest.mark.slow
    @pytest.mark.positive
    def test_response_time(self, client: ApiClient):
        response = self._get_posts(client)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @allure.description(
        "Verifies that an unknown endpoint returns HTTP 404 status code."
    )
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.get("/posts123456")

        assert response.status_code == 404

    @allure.story("Validation")
    @allure.title("All returned ids are unique")
    @allure.description("Verifies that all returned post IDs are unique.")
    @pytest.mark.regression
    @pytest.mark.positive
    def test_all_post_ids_unique(self, client: ApiClient):
        response = self._get_posts(client)

        ids = [post["id"] for post in response.json()["posts"]]

        assert len(ids) == len(set(ids))

    @allure.story("Validation")
    @allure.title("Every post has non-empty title")
    @allure.description("Verifies that every returned post has a non-empty title.")
    @pytest.mark.regression
    @pytest.mark.positive
    def test_every_post_has_title(self, client: ApiClient):
        response = self._get_posts(client)

        posts = response.json()["posts"]

        assert all(len(post["title"].strip()) > 0 for post in posts)

    @allure.story("Validation")
    @allure.title("Every post has non-empty body")
    @allure.description("Verifies that every returned post has a non-empty body.")
    @pytest.mark.regression
    @pytest.mark.positive
    def test_every_post_has_body(self, client: ApiClient):
        response = self._get_posts(client)

        posts = response.json()["posts"]

        assert all(len(post["body"].strip()) > 0 for post in posts)

    @allure.story("Step by step")
    @allure.title("Several posts are successfully loaded")
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
    @allure.description("Verifies that multiple posts can be retrieved successfully.")
    @pytest.mark.regression
    @pytest.mark.positive
    def test_multiple_posts(self, client: ApiClient, post_id: int):
        response = self._get_post(client, post_id)

        assert response.status_code == 200
        assert response.json()["id"] == post_id
