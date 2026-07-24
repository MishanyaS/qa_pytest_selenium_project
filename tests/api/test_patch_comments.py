import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.comment_schema import COMMENT_SCHEMA
from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Patch Comments")
@pytest.mark.api
@pytest.mark.regression
class TestPatchComments:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)

    @pytest.fixture()
    def comment_payload(self, faker: Faker) -> dict[str, Any]:
        return {
            "body":faker.sentence(nb_words=50),
        }

    @allure.story("Patch comment")
    @allure.title("PATCH /comments/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_patch_comment_status_code(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        assert response.status_code == 200

    @allure.story("Patch comment")
    @allure.title("Patched user matches schema")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_patch_schema(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        validate(instance=response.json(), schema=COMMENT_SCHEMA)

    @allure.story("Patch comment")
    @allure.title("Returned body equals sent body")
    @pytest.mark.positive
    def test_patch_body(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        assert response.json()["body"] == comment_payload["body"]

    @allure.story("Validation")
    @allure.title("Returned id is positive")
    @pytest.mark.positive
    def test_comment_id_positive(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        assert response.json()["id"] > 0

    @allure.story("Validation")
    @allure.title("Returned field types are correct")
    @pytest.mark.positive
    def test_returned_field_types(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["body"], str)
        assert isinstance(data["postId"], int)
        assert isinstance(data["likes"], int)
        assert isinstance(data["user"], dict)

    @allure.story("Validation")
    @allure.title("Nested user object contains required fields")
    @pytest.mark.positive
    def test_nested_user_fields(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        user = response.json()["user"]

        assert "id" in user
        assert "username" in user

    @allure.story("Validation")
    @allure.title("Patch comment with different body values")
    @pytest.mark.parametrize(
        "body",
        [
            "Updated",
            "Hello world",
            "Very long updated comment",
            "QA Automation",
            "Python",
        ]
    )
    @pytest.mark.positive
    def test_patch_various_bodies(self, client: ApiClient, body: str):
        payload = {
            "body": body,
        }

        response = client.patch("/comments/1", json=payload)


        assert response.status_code == 200
        assert response.json()["body"] == body

    @allure.story("Validation")
    @allure.title("Patch several comments")
    @pytest.mark.parametrize(
        "comment_id",
        [
            1,
            2,
            3,
            5,
            10,
        ]
    )
    @pytest.mark.positive
    def test_patch_multiple_comments(self, client: ApiClient, faker: Faker, comment_id: int):
        payload = {
            "body": faker.sentence(),
        }

        response = client.patch(f"/comments/{comment_id}", json=payload)


        assert response.status_code == 200
        assert response.json()["id"] == comment_id
        assert response.json()["body"] == payload["body"]

    @allure.story("Validation")
    @allure.title("Patch postId")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            10,
            25,
            50,
            100,
        ]
    )
    @pytest.mark.positive
    def test_patch_post_id(self, client: ApiClient, post_id: int):
        payload = {
            "postId": post_id,
        }

        response = client.patch("/comments/1", json=payload)

        assert response.status_code == 200
        assert response.json()["postId"] == post_id

    @allure.story("Negative")
    @allure.title("Patch empty payload")
    @pytest.mark.negative
    def test_patch_empty_payload(self, client: ApiClient):
        response = client.patch("/comments/1", json={})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Patch invalid id")
    @pytest.mark.negative
    def test_patch_invalid_id(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/999999", json=comment_payload)

        assert response.status_code in (200, 404)

    @allure.story("Boundary")
    @allure.title("Patch minimum body")
    @pytest.mark.boundary
    def test_patch_minimum_body(self, client: ApiClient):
        payload = {
            "body": "A",
        }

        response = client.patch("/comments/1", json=payload)

        assert response.status_code == 200

    @allure.story("Headers")
    @allure.title("Response content type")
    @pytest.mark.positive
    def test_content_type(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        assert "application/json" in response.headers["Content-Type"]

    @allure.story("Performane")
    @allure.title("Patch response time")
    @pytest.mark.slow
    def test_patch_response_time(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.patch("/comments/1", json=comment_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.step("Patch comment")
    def patch_comment(self, client: ApiClient, comment_id: int, comment_payload: dict[str, Any]):
        return client.patch(f"/comments/{comment_id}", json=comment_payload)

    @allure.story("Step by step")
    @allure.title("Patch several comments")
    @pytest.mark.parametrize(
        "comment_id",
        [
            1,
            2,
            3,
            5,
            10,
        ],
    )
    def test_patch_multiple_comments(self, client: ApiClient, faker: Faker, comment_id: int):
        payload = {
            "body": faker.sentence(),
        }

        response = self.patch_comment(client, comment_id, payload)

        assert response.status_code == 200
        assert response.json()["id"] == comment_id
        assert response.json()["body"] == payload["body"]

    @allure.story("Step by step")
    @allure.title("Patch comment step by step")
    @pytest.mark.smoke
    def test_update_comment_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send PATCH request"):
            response = self.patch_comment(client, 1, comment_payload)

        with allure.step("Verify status code"):
            assert response.status_code == 200

        with allure.step("Verify schema"):
            validate(instance=response.json(), schema=COMMENT_SCHEMA)

        with allure.step("Verify body"):
            assert response.json()["body"] == comment_payload["body"]

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    def test_headers_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send PATCH request"):
            response = self.patch_comment(client, 1, comment_payload)

        with allure.step("Verify Content-Type"):
            assert "application/json" in response.headers["Content-Type"]

    @allure.story("Step by step")
    @allure.title("Verify response time")
    @pytest.mark.slow
    def test_response_time_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send PATCH request"):
            response = self.patch_comment(client, 1, comment_payload)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
