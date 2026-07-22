import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.post_schema import CREATE_POST_SCHEMA
from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Update Posts")
@pytest.mark.api
@pytest.mark.regression
class TestUpdatePosts:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)
    
    @pytest.fixture()
    def update_payload(self, faker: Faker) -> dict[str, str | int]:
        return {
            "title":faker.sentence(nb_words=5),
            "body": faker.paragraph(nb_sentences=5),
            "userId": faker.random_int(min=1, max=100),
        }
    
    @allure.story("Update post")
    @allure.title("PUT /posts/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_update_post_status_code(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert response.status_code == 200
    
    @allure.story("Update post")
    @allure.title("Update post matches schema")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_update_post_schema(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        validate(instance=response.json(), schema=CREATE_POST_SCHEMA)
    
    @allure.story("Update post")
    @allure.title("Response is JSON")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert response.headers["Content-Type"].startswith("application/json")
    
    @allure.story("Update post")
    @allure.title("Title updated")
    @pytest.mark.positive
    def test_title_updated(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert response.json()["title"] == update_payload["title"]
    
    @allure.story("Update post")
    @allure.title("Body updated")
    @pytest.mark.positive
    def test_body_updated(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert response.json()["body"] == update_payload["body"]

    @allure.story("Update post")
    @allure.title("UserId updated")
    @pytest.mark.positive
    def test_user_id_updated(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert response.json()["userId"] == update_payload["userId"]

    @allure.story("Validation")
    @allure.title("Id remains unchanged")
    @pytest.mark.positive
    def test_id_not_changed(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert response.json()["id"] == 1

    @allure.story("Validation")
    @allure.title("All required fields exist")
    @pytest.mark.positive
    def test_required_fields_exist(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        data = response.json()

        for field in ("id", "title", "body", "userId"):
            assert field in data

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Update post")
    @allure.title("Update different post ids")
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
    @pytest.mark.regression
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
    @allure.title("Update with different user ids")
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
    def test_update_various_posts(self, client: ApiClient, faker: Faker, user_id: int):
        payload = {
            "title": faker.sentence(),
            "body": faker.text(),
            "userId": user_id,
        }

        response = client.put("/posts/1", json=payload)

        assert response.status_code == 200
        assert response.json()["userId"] == user_id

    @allure.story("Negative")
    @allure.title("Unknown endpoint retutns 404")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts123/1", json=update_payload)

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown post id")
    @pytest.mark.negative
    def test_unknown_post_id(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/999999", json=update_payload)

        assert response.status_code in (200, 404)

    @allure.story("Negative")
    @allure.title("Only title")
    @pytest.mark.negative
    def test_only_title(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Only title",})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Only body")
    @pytest.mark.negative
    def test_only_body(self, client: ApiClient):
        response = client.put("/posts/1", json={"body": "Only body",})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Only userId")
    @pytest.mark.negative
    def test_only_user_id(self, client: ApiClient):
        response = client.put("/posts/1", json={"userId": 1,})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Invalid userId type")
    @pytest.mark.negative
    def test_only_user_id_type(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Title", "body": "Body", "userId": "abc"})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Negative userId")
    @pytest.mark.negative
    def test_negative_user_id(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Title", "body": "Body", "userId": -1})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Empty title")
    @pytest.mark.negative
    def test_empty_title(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "", "body": "Body", "userId": 1})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Empty body")
    @pytest.mark.negative
    def test_empty_body(self, client: ApiClient):
        response = client.put("/posts/1", json={"title": "Title", "body": "", "userId": 1})

        assert response.status_code in (200, 400)

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @pytest.mark.positive
    def test_id_type(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned title is string")
    @pytest.mark.positive
    def test_title_type(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert isinstance(response.json()["title"], str)

    @allure.story("Validation")
    @allure.title("Returned body is string")
    @pytest.mark.positive
    def test_body_type(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert isinstance(response.json()["body"], str)

    @allure.story("Validation")
    @allure.title("Returned userId is integer")
    @pytest.mark.positive
    def test_user_id_type(self, client: ApiClient, update_payload: dict[str, Any]):
        response = client.put("/posts/1", json=update_payload)

        assert isinstance(response.json()["userId"], int)

    @allure.step("Update post")
    @pytest.mark.positive
    def update_post(self, client: ApiClient, post_id: int, update_payload: dict[str, Any]):
        return client.put(f"/posts/{post_id}", json=update_payload)

    @allure.story("Step by step")
    @allure.title("Update several posts")
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
