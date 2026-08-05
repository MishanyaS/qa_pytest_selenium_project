import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.post_schema import CREATE_POST_SCHEMA
from utils.api_client import ApiClient

@allure.epic("API")
@allure.feature("Update Posts")
@pytest.mark.api
@pytest.mark.regression
class TestUpdatePosts:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)
    
    @pytest.fixture()
    def post_payload(self, faker: Faker) -> dict[str, str | int]:
        return {
            "title":faker.sentence(nb_words=5),
            "body": faker.paragraph(nb_sentences=5),
            "userId": faker.random_int(min=1, max=100),
        }
    
    @allure.story("Update post")
    @allure.title("PUT /posts/1 returns 200")
    @allure.description("Verifies that updating a post returns HTTP 200 status code.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_update_post_status_code(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert response.status_code == 200
    
    @allure.story("Update post")
    @allure.title("Update post matches schema")
    @allure.description("Verifies that the updated post matches the expected JSON schema.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_update_post_schema(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        validate(instance=response.json(), schema=CREATE_POST_SCHEMA)
    
    @allure.story("Update post")
    @allure.title("Response is JSON")
    @allure.description("Verifies that the response content type is JSON.")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert response.headers["Content-Type"].startswith("application/json")
    
    @allure.story("Update post")
    @allure.title("Title updated")
    @allure.description("Verifies that the returned title matches the submitted title.")
    @pytest.mark.positive
    def test_title_updated(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert response.json()["title"] == post_payload["title"]
    
    @allure.story("Update post")
    @allure.title("Body updated")
    @allure.description("Verifies that the returned body matches the submitted body.")
    @pytest.mark.positive
    def test_body_updated(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert response.json()["body"] == post_payload["body"]

    @allure.story("Update post")
    @allure.title("UserId updated")
    @allure.description("Verifies that the returned userId matches the submitted userId.")
    @pytest.mark.positive
    def test_user_id_updated(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert response.json()["userId"] == post_payload["userId"]

    @allure.story("Validation")
    @allure.title("Id remains unchanged")
    @allure.description("Verifies that the post identifier remains unchanged after update.")
    @pytest.mark.positive
    def test_id_not_changed(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert response.json()["id"] == 1

    @allure.story("Validation")
    @allure.title("All required fields exist")
    @allure.description("Verifies that all required fields are present in the response.")
    @pytest.mark.positive
    def test_required_fields_exist(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        data = response.json()

        for field in ("id", "title", "body", "userId"):
            assert field in data

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @allure.description("Verifies that the update request is completed within the expected time.")
    @pytest.mark.slow
    @pytest.mark.positive
    def test_response_time(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Update post")
    @allure.title("Update different post ids")
    @allure.description("Verifies that different posts can be updated successfully.")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            2,
            3,
            10,
            50,
        ],
    )
    @pytest.mark.positive
    def test_update_various_posts(self, client: ApiClient, faker: Faker, post_id: int):
        payload = {
            "title": faker.sentence(),
            "body": faker.text(),
            "userId": 1,
        }

        response = client.put(f"/posts/{post_id}", json=payload)

        assert response.status_code == 200
        assert response.json()["id"] == post_id

    @allure.story("Update post")
    @allure.title("Update posts with different user ids")
    @allure.description("Verifies that posts can be updated with different user IDs.")
    @pytest.mark.parametrize(
        "user_id",
        [
            1,
            5,
            10,
            50,
            100,
        ],
    )
    @pytest.mark.positive
    def test_update_with_various_post_ids(self, client: ApiClient, faker: Faker, user_id: int):
        payload = {
            "title": faker.sentence(),
            "body": faker.text(),
            "userId": user_id,
        }

        response = client.put("/posts/1", json=payload)

        assert response.status_code == 200
        assert response.json()["userId"] == user_id

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @allure.description("Verifies that an invalid endpoint returns HTTP 404.")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts123/1", json=post_payload)

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown post id")
    @allure.description("Verifies API behavior when updating a non-existent post.")
    @pytest.mark.negative
    def test_unknown_post_id(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/999999", json=post_payload)

        assert response.status_code in (200, 404)

    @allure.story("Negative")
    @allure.title("Only title")
    @allure.description("Verifies API behavior when only the title is provided.")
    @pytest.mark.negative
    def test_only_title(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Only title",})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Only body")
    @allure.description("Verifies API behavior when only the body is provided.")
    @pytest.mark.negative
    def test_only_body(self, client: ApiClient):
        response = client.put("/posts/1", json={"body": "Only body",})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Only userId")
    @allure.description("Verifies API behavior when only the userId is provided.")
    @pytest.mark.negative
    def test_only_user_id(self, client: ApiClient):
        response = client.put("/posts/1", json={"userId": 1,})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Invalid userId type")
    @allure.description("Verifies API behavior when an invalid userId data type is provided.")
    @pytest.mark.negative
    def test_only_user_id_type(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Title", "body": "Body", "userId": "abc"})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Negative userId")
    @allure.description("Verifies API behavior with a negative userId value.")
    @pytest.mark.negative
    def test_negative_user_id(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Title", "body": "Body", "userId": -1})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Empty title")
    @allure.description("Verifies API behavior when the title is empty.")
    @pytest.mark.negative
    def test_empty_title(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "", "body": "Body", "userId": 1})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Empty body")
    @allure.description("Verifies API behavior when the body is empty.")
    @pytest.mark.negative
    def test_empty_body(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Title", "body": "", "userId": 1})

        assert response.status_code in (200, 400)

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @allure.description("Verifies that the returned id is an integer.")
    @pytest.mark.positive
    def test_id_type(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned title is string")
    @allure.description("Verifies that the returned title is a string.")
    @pytest.mark.positive
    def test_title_type(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert isinstance(response.json()["title"], str)

    @allure.story("Validation")
    @allure.title("Returned body is string")
    @allure.description("Verifies that the returned body is a string.")
    @pytest.mark.positive
    def test_body_type(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert isinstance(response.json()["body"], str)

    @allure.story("Validation")
    @allure.title("Returned userId is integer")
    @allure.description("Verifies that the returned userId is an integer.")
    @pytest.mark.positive
    def test_user_id_type(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.put("/posts/1", json=post_payload)

        assert isinstance(response.json()["userId"], int)

    @allure.step("Update post")
    def update_post(self, client: ApiClient, post_id: int, post_payload: dict[str, Any]):
        return client.put(f"/posts/{post_id}", json=post_payload)

    @allure.story("Step by step")
    @allure.title("Update several posts")
    @allure.description("Verifies that multiple posts can be updated successfully.")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            2,
            3,
            5,
            10,
        ],
    )
    @pytest.mark.positive
    def test_update_multiple_posts(self, client: ApiClient, faker: Faker, post_id: int):
        payload = {
            "title": faker.sentence(),
            "body": faker.text(),
            "userId": post_id,
        }

        response = self.update_post(client, post_id, payload)

        assert response.status_code == 200
        assert response.json()["id"] == post_id
        assert response.json()["title"] == payload["title"]
        assert response.json()["body"] ==payload["body"]
        assert response.json()["userId"] == payload["userId"]
