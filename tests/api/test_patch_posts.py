import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.post_schema import CREATE_POST_SCHEMA
from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Patch Posts")
@pytest.mark.api
@pytest.mark.regression
class TestPatchPosts:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)

    @pytest.fixture()
    def patch_payload(self, faker: Faker) -> dict[str, str | int]:
        return {
            "title":faker.sentence(nb_words=5),
            "body": faker.paragraph(nb_sentences=5),
            "userId": faker.random_int(min=1, max=100),
        }

    @allure.story("Patch post")
    @allure.title("PUT /posts/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_patch_post_status_code(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert response.status_code == 200

    @allure.story("Patch post")
    @allure.title("Patched post matches schema")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_patch_schema(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        validate(instance=response.json(), schema=CREATE_POST_SCHEMA)

    @allure.story("Patch post")
    @allure.title("Response is JSON")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Patch post")
    @allure.title("Title patched")
    @pytest.mark.positive
    def test_title_updated(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert response.json()["title"] == patch_payload["title"]

    @allure.story("Patch post")
    @allure.title("Body patched")
    @pytest.mark.positive
    def test_body_updated(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert response.json()["body"] == patch_payload["body"]

    @allure.story("Patch post")
    @allure.title("UserId patched")
    @pytest.mark.positive
    def test_user_id_updated(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert response.json()["userId"] == patch_payload["userId"]

    @allure.story("Validation")
    @allure.title("Id remains unchanged")
    @pytest.mark.positive
    def test_id_not_changed(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert response.json()["id"] == 1

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @pytest.mark.positive
    def test_id_type(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned title is string")
    @pytest.mark.positive
    def test_title_type(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert isinstance(response.json()["title"], str)

    @allure.story("Validation")
    @allure.title("Returned body is string")
    @pytest.mark.positive
    def test_body_type(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert isinstance(response.json()["body"], str)

    @allure.story("Validation")
    @allure.title("Returned userId is integer")
    @pytest.mark.positive
    def test_user_id_type(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert isinstance(response.json()["userId"], int)

    @allure.story("Patch post")
    @allure.title("Patch different posts")
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
    def test_patch_various_posts(self, client: ApiClient, faker: Faker, post_id: int):
        payload = {
            "title": faker.sentence(),
        }

        response = client.patch(f"/posts/{post_id}", json=payload)

        assert response.status_code == 200
        assert response.json()["id"] == post_id
        assert response.json()["title"] == payload["title"]

    @allure.story("Patch post")
    @allure.title("Patch different user ids")
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
    def test_patch_various_user_ids(self, client: ApiClient, user_id: int):
        payload = {
            "userId": user_id,
        }

        response = client.patch("/posts/1", json=payload)

        assert response.status_code == 200
        assert response.json()["userId"] == user_id

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @pytest.mark.negative
    def test_user_id_type(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts123/1", json=patch_payload)

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown post id")
    @pytest.mark.negative
    def test_unknown_post_id(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/999999", json=patch_payload)

        assert response.status_code in (200, 404)

    @allure.story("Negative")
    @allure.title("Empty JSON")
    @pytest.mark.negative
    def test_empty_json(self, client: ApiClient):
        response = client.patch("/posts/1", json={})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Invalid userId type")
    @pytest.mark.negative
    def test_invalid_user_id_type(self, client: ApiClient):
        response = client.patch("/posts/1", json={"userId": "abc"})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Negative userId")
    @pytest.mark.negative
    def test_negative_user_id(self, client: ApiClient):
        response = client.patch("/posts/1", json={"userId": -1})

        assert response.status_code in (200, 400)

    @allure.story("Performane")
    @allure.title("Response time is acceptable")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient, patch_payload: dict[str, Any]):
        response = client.patch("/posts/1", json=patch_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.step("Patch post")
    def patch_post(self, client: ApiClient, post_id: int, patch_payload: dict[str, Any]):
        return client.patch(f"/posts/{post_id}", json=patch_payload)

    @allure.story("Step by step")
    @allure.title("Patch several posts")
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
    def test_patch_multiple_posts(self, client: ApiClient, faker: Faker, post_id: int):
        payload = {
            "title": faker.sentence(),
        }

        response = self.patch_post(client, post_id, payload)

        assert response.status_code == 200
        assert response.json()["id"] == post_id
        assert response.json()["title"] == payload["title"]
