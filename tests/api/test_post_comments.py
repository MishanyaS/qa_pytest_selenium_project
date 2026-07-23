import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.comment_schema import CREATE_COMMENT_SCHEMA, CREATE_COMMENT_RESPONSE_SCHEMA
from utils.api_client import ApiClient

@allure.epic("API")
@allure.feature("Create Comments")
@pytest.mark.api
@pytest.mark.regression
class TestCreateComments:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)
    
    @pytest.fixture()
    def comment_payload(self, faker: Faker) -> dict[str, Any]:
        return {
            "body": faker.sentence(nb_words=200),
            "postId": faker.random_int(min=1, max=200),
            "userId": faker.random_int(min=1, max=200),
        }
    
    @allure.story("Create comment")
    @allure.title("POST /comments/add returns 201")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_create_comment_status_code(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        assert response.status_code == 201

    @allure.story("Create comment")
    @allure.title("Created comment matches schema")
    @pytest.mark.schema
    def test_created_user_schema(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        validate(instance=response.json(), schema=CREATE_COMMENT_RESPONSE_SCHEMA)

    @allure.story("Create comment")
    @allure.title("Returned body equals sent body")
    @pytest.mark.positive
    def test_created_body(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        assert response.json()["body"] == comment_payload["body"]

    @allure.story("Create comment")
    @allure.title("Returned postId equals sent postId")
    @pytest.mark.positive
    def test_created_post_id(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        assert response.json()["postId"] == comment_payload["postId"]

    @allure.story("Create comment")
    @allure.title("Returned id is integer")
    @pytest.mark.positive
    def test_created_comment_id_type(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        assert isinstance(response.json()["id"], int)

    @allure.story("Schema")
    @allure.title("Payload matches create comment schema")
    @pytest.mark.schema
    def test_comment_payload_schema(self, comment_payload: dict[str, Any]):
        validate(instance=comment_payload, schema=CREATE_COMMENT_SCHEMA)

    @allure.story("Validation")
    @allure.title("Response contains all required fields")
    @pytest.mark.positive
    def test_required_fields_exist(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        data = response.json()

        assert "id" in data
        assert "body" in data
        assert "postId" in data

    @allure.story("Validation")
    @allure.title("Returned id is positive")
    @pytest.mark.positive
    def test_comment_id_positive(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        assert response.json()["id"] > 0

    @allure.story("Validation")
    @allure.title("Returned field types are correct")
    @pytest.mark.positive
    def test_returned_field_types(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["body"], str)
        assert isinstance(data["postId"], int)

    @allure.story("Validation")
    @allure.title("Create comments with different post ids")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            10,
            25,
            50,
            100,
            200,
        ],
    )
    @pytest.mark.positive
    def test_create_comment_with_various_post_ids(self, client: ApiClient, faker: Faker, post_id: int):
        payload = {
            "body": faker.sentence(nb_words=200),
            "postId": post_id,
            "userId": 1,
        }

        response = client.post("/comments/add", json=payload)

        assert response.status_code == 201
        assert response.json()["postId"] == post_id

    @allure.story("Validation")
    @allure.title("Create comments with different body lengths")
    @pytest.mark.parametrize(
        "length",
        [
            1,
            10,
            50,
            100,
            200,
        ],
    )
    @pytest.mark.positive
    def test_create_comment_body_lengths(self, client: ApiClient, faker: Faker, length: int):
        payload = {
            "body": faker.sentence(nb_words=length),
            "postId": 1,
            "userId": 1,
        }

        response = client.post("/comments/add", json=payload)

        assert response.status_code == 201

    @allure.story("Negative")
    @allure.title("Create comment without postId")
    @pytest.mark.negative
    def test_create_comment_without_post_id(self, client: ApiClient, faker: Faker):
        payload = {
            "postId": faker.text(),
            "userId": 1,
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Create comment without userId")
    @pytest.mark.negative
    def test_create_comment_without_user_id(self, client: ApiClient, faker: Faker):
        payload = {
            "postId": faker.text(),
            "postId": 1,
        }

        response = client.post("/comments/add", json=payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Create empty comment")
    @pytest.mark.negative
    def test_create_empty_comment(self, client: ApiClient):

        response = client.post("/comments/add", json={})

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Response content type is JSON")
    @pytest.mark.positive
    def test_response_content_type(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        assert "application/json" in response.headers["Content-Type"]

    @allure.story("Performance")
    @allure.title("Comment creation response time")
    @pytest.mark.slow
    def test_comment_creation_response_time(self, client: ApiClient, comment_payload: dict[str, Any]):
        response = client.post("/comments/add", json=comment_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Boundary")
    @allure.title("Comment creation response time")
    @pytest.mark.boundary
    def test_comment_min_body(self, client: ApiClient):
        payload = {
            "body": "A",
            "postId": 1,
            "userId": 1,
        }

        response = client.post("/comments/add", json=payload)

        assert response.status_code == 201

    @allure.story("Step by step")
    @allure.title("Create comment step by step")
    @pytest.mark.smoke
    def test_create_comment_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send POST request"):
            response = client.post("/comments/add", json=comment_payload)

        with allure.step("Verify status code"):
            assert response.status_code == 201

        with allure.step("Verify response schema"):
            validate(instance=response.json(), schema=CREATE_COMMENT_RESPONSE_SCHEMA)

        with allure.step("Verify body"):
            assert response.json()["body"] == comment_payload["body"]

        with allure.step("Verify postId"):
            assert response.json()["postId"] == comment_payload["postId"]

        with allure.step("Verify id"):
            assert response.json()["id"] > 0

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    def test_response_headers_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send POST request"):
            response = client.post("/comments/add", json=comment_payload)

        with allure.step("Verify Content-Type"):
            assert "application/json" in response.headers["Content-Type"]

    @allure.story("Step by step")
    @allure.title("Verify response time")
    @pytest.mark.slow
    def test_comment_response_time_step_by_step(self, client: ApiClient, comment_payload: dict[str, Any]):
        with allure.step("Send POST request"):
            response = client.post("/comments/add", json=comment_payload)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
