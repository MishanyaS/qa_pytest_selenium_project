import allure
import pytest
import requests
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.user_schema import USER_SCHEMA
from utils.api_client import ApiClient

@allure.epic("API")
@allure.feature("Update Users")
@pytest.mark.api
@pytest.mark.regression
class TestUpdateUsers:
    @pytest.fixture(scope="function")
    def user_payload(self, faker: Faker) -> dict[str, str | int]:
        return {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": faker.random_int(min=18, max=80),
            "gender": faker.random_element(["male", "female"]),
            "email": faker.email(),
        }

    @allure.step("Put user")
    def _put_user(self, client: ApiClient, user_id: int, user_payload: dict[str, Any]) -> requests.Response:
        return client.put(f"/users/{user_id}", json=user_payload)
    
    @allure.story("Update user")
    @allure.title("PUT /users/1 returns 200")
    @allure.description("Verifies that updating a user returns HTTP 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_updated_user_status_code(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert response.status_code == 200
    
    @allure.story("Update user")
    @allure.title("Update user matches schema")
    @allure.description("Verifies that the updated user matches the JSON schema.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_updated_user_schema(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        validate(instance=response.json(), schema=USER_SCHEMA)
    
    @allure.story("Update user")
    @allure.title("Returned firstName equals sent firstName")
    @allure.description("Verifies that the returned firstName matches the updated value.")
    @pytest.mark.positive
    def test_updated_first_name(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert response.json()["firstName"] == user_payload["firstName"]

    @allure.story("Update user")
    @allure.title("Returned lastName equals sent lastName")
    @allure.description("Verifies that the returned lastName matches the updated value.")
    @pytest.mark.positive
    def test_updated_last_name(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert response.json()["lastName"] == user_payload["lastName"]

    @allure.story("Update user")
    @allure.title("Returned email equals sent email")
    @allure.description("Verifies that the returned email matches the updated value.")
    @pytest.mark.positive
    def test_updated_email(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert response.json()["email"] == user_payload["email"]

    @allure.story("Update user")
    @allure.title("Returned age equals sent age")
    @allure.description("Verifies that the returned age matches the updated value.")
    @pytest.mark.positive
    def test_updated_age(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert response.json()["age"] == user_payload["age"]

    @allure.story("Validation")
    @allure.title("Response contains required fields")
    @allure.description("Verifies that all required fields are present in the response.")
    @pytest.mark.positive
    def test_required_fields_exist(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        data = response.json()

        assert "id" in data
        assert "firstName" in data
        assert "lastName" in data
        assert "email" in data
        assert "age" in data
        assert "gender" in data

    @allure.story("Validation")
    @allure.title("Returned id is positive")
    @allure.description("Verifies that the returned user ID is positive.")
    @pytest.mark.positive
    def test_user_id_positive(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert response.json()["id"] > 0

    @allure.story("Validation")
    @allure.title("Returned field types are correct")
    @allure.description("Verifies that all returned field types are correct.")
    @pytest.mark.positive
    def test_returned_field_types(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["firstName"], str)
        assert isinstance(data["lastName"], str)
        assert isinstance(data["email"], str)
        assert isinstance(data["age"], int)
        assert isinstance(data["gender"], str)

    @allure.story("Validation")
    @allure.title("Update user with different ages")
    @allure.description("Verifies that users can be updated with different ages.")
    @pytest.mark.parametrize(
        "age",
        [
            18,
            25,
            35,
            50,
            65,
            80,
        ]
    )
    @pytest.mark.positive
    def test_update_user_with_various_ages(self, client: ApiClient, faker: Faker, age: int):
        payload = {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": age,
            "gender": "male",
            "email": faker.email(),
        }

        response = self._put_user(client, 1, payload)

        assert response.status_code == 200
        assert response.json()["age"] == age

    @allure.story("Validation")
    @allure.title("Update user with different genders")
    @allure.description("Verifies that users can be updated with different genders.")
    @pytest.mark.parametrize(
        "gender",
        [
            "male",
            "female",
        ]
    )
    @pytest.mark.positive
    def test_update_user_gender(self, client: ApiClient, faker: Faker, gender: str):
        payload = {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": 30,
            "gender": gender,
            "email": faker.email(),
        }

        response = self._put_user(client, 1, payload)

        assert response.status_code == 200
        assert response.json()["gender"] == gender

    @allure.story("Negative")
    @allure.title("Update user without firstName")
    @allure.description("Verifies the behavior when firstName is missing.")
    @pytest.mark.negative
    def test_update_without_first_name(self, client: ApiClient, faker: Faker):
        payload = {
            "lastName": faker.last_name(),
            "age": 30,
            "gender": "male",
            "email": faker.email(),
        }

        response = self._put_user(client, 1, payload)

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Update user without email")
    @allure.description("Verifies the behavior when email is missing.")
    @pytest.mark.negative
    def test_update_without_email(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": 30,
            "gender": "female",
        }

        response = self._put_user(client, 1, payload)

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Update empty payload")
    @allure.description("Verifies the behavior when an empty payload is sent.")
    @pytest.mark.negative
    def test_update_empty_payload(self, client: ApiClient):
        response = self._put_user(client, 1, {})

        assert response.status_code in (200, 400)

    @allure.story("Boundary")
    @allure.title("Update user with minimum age")
    @allure.description("Verifies that a user can be updated with the minimum age value.")
    @pytest.mark.boundary
    @pytest.mark.positive
    def test_update_minimum_age(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": 0,
            "gender": "male",
            "email": faker.email(),
        }

        response = self._put_user(client, 1, payload)

        assert response.status_code == 200

    @allure.story("Headers")
    @allure.title("Response content type is JSON")
    @allure.description("Verifies that the response content type is JSON.")
    @pytest.mark.positive
    def test_response_content_type(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert "application/json" in response.headers["Content-Type"]

    @allure.story("Performance")
    @allure.title("User update response time")
    @allure.description("Verifies that the user update response time is within the acceptable limit.")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient, user_payload: dict[str, Any]):
        response = self._put_user(client, 1, user_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Step by step")
    @allure.title("Update user step by step")
    @allure.description("Verifies the complete user update workflow step by step.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_update_user_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = self._put_user(client, 1, user_payload)
            data = response.json()

        with allure.step("Verifies status code"):
            assert response.status_code == 200

        with allure.step("Verifies schema"):
            validate(instance=data, schema=USER_SCHEMA)

        with allure.step("Verifies firstName"):
            assert data["firstName"] == user_payload["firstName"]

        with allure.step("Verifies lastName"):
            assert data["lastName"] == user_payload["lastName"]

        with allure.step("Verifies email"):
            assert data["email"] == user_payload["email"]

        with allure.step("Verifies age"):
            assert data["age"] == user_payload["age"]

    @allure.story("Step by step")
    @allure.title("Verifies response headers")
    @allure.description("Verifies the response headers step by step.")
    @pytest.mark.positive
    def test_headers_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = self._put_user(client, 1, user_payload)

        with allure.step("Verifies Content-Type"):
            assert "application/json" in response.headers["Content-Type"]

    @allure.story("Step by step")
    @allure.title("Verifies response time")
    @allure.description("Verifies the response time step by step.")
    @pytest.mark.slow
    def test_response_time_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = self._put_user(client, 1, user_payload)

        with allure.step("Verifies response time"):
            assert response.elapsed.total_seconds() < 2
