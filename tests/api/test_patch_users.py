import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.user_schema import USER_SCHEMA
from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Patch Users")
@pytest.mark.api
@pytest.mark.regression
class TestPatchUsers:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)

    @pytest.fixture()
    def user_payload(self, faker: Faker) -> dict[str, Any]:
        return {
            "firstName":faker.first_name(),
        }

    @allure.story("Patch user")
    @allure.title("PATCH /users/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_patch_user_status_code(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/1", json=user_payload)

        assert response.status_code == 200

    @allure.story("Patch user")
    @allure.title("Patched user matches schema")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_patch_schema(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/1", json=user_payload)

        validate(instance=response.json(), schema=USER_SCHEMA)

    @allure.story("Patch user")
    @allure.title("Returned firstName equals sent firstName")
    @pytest.mark.positive
    def test_patch_first_name(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/1", json=user_payload)

        assert response.json()["firstName"] == user_payload["firstName"]

    @allure.story("Validation")
    @allure.title("Returned id is positive")
    @pytest.mark.positive
    def test_user_id_positive(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/1", json=user_payload)

        assert response.json()["id"] > 0

    @allure.story("Validation")
    @allure.title("Returned field types are correct")
    @pytest.mark.positive
    def test_returned_field_types(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/1", json=user_payload)

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["firstName"], str)
        assert isinstance(data["lastName"], str)
        assert isinstance(data["email"], str)
        assert isinstance(data["age"], int)
        assert isinstance(data["gender"], str)

    @allure.story("Validation")
    @allure.title("Patch user with different first names")
    @pytest.mark.parametrize(
        "first_name",
        [
            "John",
            "Alice",
            "Michael",
            "Kate",
            "Robert",
        ]
    )
    @pytest.mark.positive
    def test_patch_various_first_names(self, client: ApiClient, first_name: str):
        payload = {
            "firstName": first_name,
        }

        response = client.patch("/users/1", json=payload)


        assert response.status_code == 200
        assert response.json()["firstName"] == first_name

    @allure.story("Validation")
    @allure.title("Patch several users")
    @pytest.mark.parametrize(
        "user_id",
        [
            1,
            2,
            3,
            5,
            10,
        ]
    )
    @pytest.mark.positive
    def test_patch_multiple_users(self, client: ApiClient, faker: Faker, user_id: int):
        payload = {
            "firstName": faker.first_name(),
        }

        response = client.patch(f"/users/{user_id}", json=payload)


        assert response.status_code == 200
        assert response.json()["id"] == user_id
        assert response.json()["firstName"] == payload["firstName"]

    @allure.story("Validation")
    @allure.title("Patch age")
    @pytest.mark.parametrize(
        "age",
        [
            18,
            30,
            45,
            65,
            80,
        ],
    )
    def test_patch_age(self, client: ApiClient, age: int):
        payload = {
            "age": age,
        }

        response = client.patch("/users/1", json=payload)

        assert response.status_code == 200
        assert response.json()["age"] == age

    @allure.story("Validation")
    @allure.title("Patch gender")
    @pytest.mark.parametrize(
        "gender",
        [
            "male",
            "female"
        ],
    )
    def test_patch_gender(self, client: ApiClient, gender: int):
        payload = {
            "gender": gender,
        }

        response = client.patch("/users/1", json=payload)

        assert response.status_code == 200
        assert response.json()["gender"] == gender

    @allure.story("Negative")
    @allure.title("Patch empty payload")
    @pytest.mark.negative
    def test_patch_empty_payload(self, client: ApiClient):
        response = client.patch("/users/1", json={})

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Patch invalid id")
    @pytest.mark.negative
    def test_patch_invalid_id(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/999999", json=user_payload)

        assert response.status_code in (200, 404)

    @allure.story("Boundary")
    @allure.title("Patch minimum age")
    @pytest.mark.boundary
    def test_patch_minimum_age(self, client: ApiClient):
        payload = {
            "age": 0,
        }

        response = client.patch("/users/1", json=payload)

        assert response.status_code == 200

    @allure.story("Headers")
    @allure.title("Response content type")
    def test_content_type(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/1", json=user_payload)

        assert "application/json" in response.headers["Content-Type"]

    @allure.story("Performane")
    @allure.title("Patch response time")
    @pytest.mark.slow
    def test_patch_response_time(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.patch("/users/1", json=user_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.step("Patch post")
    def patch_user(self, client: ApiClient, user_id: int, user_payload: dict[str, Any]):
        return client.patch(f"/users/{user_id}", json=user_payload)

    @allure.story("Step by step")
    @allure.title("Patch several users")
    @pytest.mark.parametrize(
        "user_id",
        [
            1,
            2,
            3,
            5,
            10,
        ],
    )
    def test_patch_multiple_posts(self, client: ApiClient, faker: Faker, user_id: int):
        payload = {
            "firstName": faker.first_name(),
        }

        response = self.patch_user(client, user_id, payload)

        assert response.status_code == 200
        assert response.json()["id"] == user_id
        assert response.json()["firstName"] == payload["firstName"]

    @allure.story("Step by step")
    @allure.title("Patch user step by step")
    @pytest.mark.smoke
    def test_update_user_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PATCH request"):
            response = self.patch_user(client, 1, user_payload)

        with allure.step("Verify status code"):
            assert response.status_code == 200

        with allure.step("Verify schema"):
            validate(instance=response.json(), schema=USER_SCHEMA)

        with allure.step("Verify firstName"):
            assert response.json()["firstName"] == user_payload["firstName"]

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    def test_headers_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PATCH request"):
            response = self.patch_user(client, 1, user_payload)

        with allure.step("Verify Content-Type"):
            assert "application/json" in response.headers["Content-Type"]

    @allure.story("Step by step")
    @allure.title("Verify response time")
    @pytest.mark.slow
    def test_response_time_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PATCH request"):
            response = self.patch_user(client, 1, user_payload)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
