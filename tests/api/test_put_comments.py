import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.comment_schema import COMMENT_SCHEMA
from utils.api_client import ApiClient

@allure.epic("API")
@allure.feature("Update Comments")
@pytest.mark.api
@pytest.mark.regression
class TestUpdatePComments:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)
    
    @pytest.fixture()
    def comment_payload(self, faker: Faker) -> dict[str, str | int]:
        return {
            "body":faker.sentence(nb_words=200),
            "postId": faker.random_int(min=1, max=200),
            "userId": faker.random_int(min=1, max=200),
        }

    @allure.story("Update comment")
    @allure.title("PUT /comments/1 returns 200")
    @allure.description("Verifies that PUT /comments/{id} returns HTTP 200.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_updated_comment_status_code(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        assert response.status_code == 200

    @allure.story("Update comment")
    @allure.title("Update comment matches schema")
    @allure.description("Verifies that the updated comment matches the JSON schema.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_updated_comment_schema(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        validate(instance=response.json(), schema=COMMENT_SCHEMA)

    @allure.story("Update comment")
    @allure.title("Returned body equals sent body")
    @allure.description("Verifies that the returned body matches the submitted value.")
    @pytest.mark.positive
    def test_updated_body(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        assert response.json()["body"] == comment_payload["body"]

    @allure.story("Update comment")
    @allure.title("Returned postId equals sent postId")
    @allure.description("Verifies that the returned postId matches the submitted value.")
    @pytest.mark.positive
    def test_updated_post_id(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        assert response.json()["postId"] == comment_payload["postId"]

    @allure.story("Validation")
    @allure.title("Response contains required fields")
    @allure.description("Verifies that the response contains all required fields.")
    @pytest.mark.positive
    def test_required_fields_exist(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        data = response.json()

        assert "id" in data
        assert "body" in data
        assert "postId" in data

    @allure.story("Validation")
    @allure.title("Returned id is positive")
    @allure.description("Verifies that the returned comment ID is positive.")
    @pytest.mark.positive
    def test_comment_id_positive(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        assert response.json()["id"] > 0

    @allure.story("Validation")
    @allure.title("Returned field types are correct")
    @allure.description("Verifies that the returned fields have the expected data types.")
    @pytest.mark.positive
    def test_returned_field_types(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["body"], str)
        assert isinstance(data["postId"], int)

    @allure.story("Validation")
    @allure.title("Update comment with different post ids")
    @allure.description("Verifies that comments can be updated with different postId values.")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            10,
            25,
            50,
            100,
            200,
        ]
    )
    @pytest.mark.regression
    @pytest.mark.positive
    def test_update_comment_with_various_post_ids(self, client: ApiClient, faker: Faker, post_id: int):
        payload = {
            "body": faker.sentence(nb_words=50),
            "postId": post_id,
            "userId": 1,
        }

        response = client.put("/comments/1", json=payload)

        assert response.status_code == 200
        assert response.json()["postId"] == post_id

    @allure.story("Validation")
    @allure.title("Update comment with different body lengths")
    @allure.description("Verifies that comments can be updated with different body lengths.")
    @pytest.mark.parametrize(
        "lengths",
        [
            1,
            10,
            50,
            100,
            200,
        ]
    )
    @pytest.mark.regression
    @pytest.mark.positive
    def test_update_comment_body_lengths(self, client: ApiClient, faker: Faker, lengths: int):
        payload = {
            "body": faker.sentence(nb_words=lengths),
            "postId": 1,
            "userId": 1,
        }

        response = client.put("/comments/1", json=payload)

        assert response.status_code == 200

    @allure.story("Negative")
    @allure.title("Update comment without body")
    @allure.description("Verifies the API behabior when body is missing.")
    @pytest.mark.negative
    def test_update_without_body(self, client: ApiClient):
        payload = {
            "postId": 1,
            "userId": 1,
        }

        response = client.put("/comments/1", json=payload)

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Update comment without postId")
    @allure.description("Verifies the API behabior when postId is missing.")
    @pytest.mark.negative
    def test_update_without_post_id(self, client: ApiClient, faker: Faker):
        payload = {
            "body": faker.sentence(),
            "userId": 1,
        }

        response = client.put("/comments/1", json=payload)

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Update comment without userId")
    @allure.description("Verifies the API behabior when userId is missing.")
    @pytest.mark.negative
    def test_update_without_user_id(self, client: ApiClient, faker: Faker):
        payload = {
            "body": faker.sentence(),
            "postId": 1,
        }

        response = client.put("/comments/1", json=payload)

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Update empty payload")
    @allure.description("Verifies the API behabior when an empty payload is submitted.")
    @pytest.mark.negative
    def test_update_empty_payload(self, client: ApiClient):
        response = client.put("/comments/1", json={})

        assert response.status_code in (200, 400)

    @allure.story("Boundary")
    @allure.title("Update comment with minimum body")
    @allure.description("Verifies that a comment can be updated with the minimum body length.")
    @pytest.mark.boundary
    @pytest.mark.positive
    def test_update_minimum_body(self, client: ApiClient):
        payload = {
            "body": "A",
            "post_id": 1,
            "userId": 1,
        }
        response = client.put("/comments/1", json=payload)

        assert response.status_code == 200

    @allure.story("Headers")
    @allure.title("Response content type is JSON")
    @allure.description("Verifies that the response content type is JSON.")
    @pytest.mark.positive
    def test_response_content_type(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        assert "application/json" in response.headers["Content-Type"]

    @allure.story("Performance")
    @allure.title("Comment update response time")
    @allure.description("Verifies that the comment update response time is acceptable.")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.put("/comments/1", json=comment_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Step by step")
    @allure.title("Update comment step by step")
    @allure.description("Verifies the comment update workflow step by step.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_update_comment_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = client.put("/comments/1", json=comment_payload)

        with allure.step("Verify status code"):
            assert response.status_code == 200

        with allure.step("Verify schema"):
            validate(instance=response.json(), schema=COMMENT_SCHEMA)

        with allure.step("Verify body"):
            assert response.json()["body"] == comment_payload["body"]

        with allure.step("Verify postId"):
            assert response.json()["postId"] == comment_payload["postId"]

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    @allure.description("Verifies the response headers step by step.")
    @pytest.mark.positive
    def test_headers_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = client.put("/comments/1", json=comment_payload)

        with allure.step("Verify Content-Type"):
            assert "application/json" in response.headers["Content-Type"]

    @allure.story("Step by step")
    @allure.title("Verify response time")
    @allure.description("Verifies the response time step by step.")
    @pytest.mark.slow
    def test_response_time_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = client.put("/comments/1", json=comment_payload)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
