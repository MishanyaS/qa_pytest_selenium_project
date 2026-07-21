import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.post_schema import CREATE_POST_SCHEMA
from utils.api_client import ApiClient

@allure.epic("API")
@allure.feature("Create Posts")
@pytest.mark.api
@pytest.mark.regression
class TestCreatePosts:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)
    
    @pytest.fixture()
    def post_payload(self, faker: Faker) -> dict[str, str | int]:
        return {
            "title": faker.sentence(nb_words=5),
            "body": faker.paragraph(nb_sentences=5),
            "userId": faker.random_int(min=1, max=100),
        }
    
    @allure.story("Create post")
    @allure.title("POST /posts/add returns 201")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_create_post_status_code(self, client: ApiClient, post_payload: dict[str, Any]):
        response = client.post("/posts/add", json=post_payload)

        assert response.status_code == 201
    
    @allure.story("Create post")
    @allure.title("Created post matches schema")
    @pytest.mark.schema
    def test_created_post_schema(self, client: ApiClient, post_payload: dict):
        response = client.post("/posts/add", json=post_payload)

        validate(instance=response.json(), schema=CREATE_POST_SCHEMA)
    
    @allure.story("Create post")
    @allure.title("Returned title equals sent title")
    @pytest.mark.positive
    def test_created_title(self, client: ApiClient, post_payload: dict):
        response = client.post("/posts/add", json=post_payload)

        assert response.json()["title"] == post_payload["title"]
    
    @allure.story("Create post")
    @allure.title("Returned body equals sent body")
    @pytest.mark.positive
    def test_created_body(self, client: ApiClient, post_payload: dict):
        response = client.post("/posts/add", json=post_payload)

        assert response.json()["body"] == post_payload["body"]
    
    @allure.story("Create post")
    @allure.title("Returned userId equals sent userId")
    @pytest.mark.positive
    def test_created_user_id(self, client: ApiClient, post_payload: dict):
        response = client.post("/posts/add", json=post_payload)

        assert response.json()["userId"] == post_payload["userId"]
    
    @allure.story("Create post")
    @allure.title("Returned id is integer")
    @pytest.mark.positive
    def test_created_id_type(self, client: ApiClient, post_payload: dict):
        response = client.post("/posts/add", json=post_payload)

        assert isinstance(response.json()["id"], int)
    
    @allure.story("Validation")
    @allure.title("Create posts with different user ids")
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
    def test_create_with_various_user_ids(self, client: ApiClient, faker: Faker, user_id: int):
        payload = {
            "title": faker.sentence(),
            "body": faker.text(),
            "userId": user_id,
        }

        response = client.post("/posts/add", json=payload)

        assert response.status_code == 201
        assert response.json()["userId"] == user_id
    
    @allure.story("Negative")
    @allure.title("Create post without title")
    @pytest.mark.negative
    def test_create_post_without_title(self, client: ApiClient, faker: Faker):
        payload = {
            "body": faker.text(),
            "userId": 1,
        }

        response = client.post("/posts/add", json=payload)

        assert response.status_code in (200, 201, 400)
    
    @allure.story("Negative")
    @allure.title("Create post without body")
    @pytest.mark.negative
    def test_create_post_without_body(self, client: ApiClient, faker: Faker):
        payload = {
            "title": faker.sentence(),
            "userId": 1,
        }

        response = client.post("/posts/add", json=payload)

        assert response.status_code in (200, 201, 400)
    
    @allure.story("Negative")
    @allure.title("Empty JSON")
    @pytest.mark.negative
    def test_create_post_with_empty_json(self, client: ApiClient):
        response = client.post("/posts/add", json={})

        assert response.status_code in (200, 201, 400)
    
    @allure.story("Negative")
    @allure.title("Invalid endpoint")
    @pytest.mark.negative
    def test_invalid_endpoint(self, client: ApiClient, post_payload: dict):
        response = client.post("/posts/add123", json=post_payload)

        assert response.status_code == 404
    
    @allure.step("Create new post")
    def create_post(self, client: ApiClient, post_payload: dict[str, Any]):
        return client.post("/posts/add", json=post_payload)
    
    @allure.story("Step by step")
    @allure.title("Create several posts")
    @pytest.mark.parametrize(
        "index",
        [
            1,
            2,
            3,
            4,
            5,
        ],
    )
    def test_create_multiple_posts(self, client: ApiClient, faker: Faker, index: int):
        payload = {
            "title": f"Title {index}",
            "body": faker.text(),
            "userId": index,
        }

        response = self.create_post(client, payload)

        assert response.status_code == 201
        assert response.json()["title"] == payload["title"]
        assert response.json()["body"] == payload["body"]
        assert response.json()["userId"] == payload["userId"]

    @allure.story("Performance")
    @allure.title("Create post response time")
    @pytest.mark.slow
    def test_create_response_time(self, client: ApiClient, post_payload: dict):
        response = client.post("/posts/add", json=post_payload)

        assert response.elapsed.total_seconds() < 2
