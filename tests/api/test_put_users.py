import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.user_schema import USER_SCHEMA
from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Update Users")
@pytest.mark.api
@pytest.mark.regression
class TestUpdateUsers:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)
    
    @pytest.fixture()
    def user_payload(self, faker: Faker) -> dict[str, str | int]:
        return {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": faker.random_int(min=18, max=80),
            "gender": faker.random_element(["male", "female"]),
            "email": faker.email(),
        }
    
    @allure.story("Update user")
    @allure.title("PUT /users/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_updated_user_status_code(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert response.status_code == 200
    
    @allure.story("Update user")
    @allure.title("Update user matches schema")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_updated_user_schema(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        validate(instance=response.json(), schema=USER_SCHEMA)
    
    @allure.story("Update user")
    @allure.title("Returned firstName equals sent firstName")
    @pytest.mark.positive
    def test_updated_first_name(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert response.json()["firstName"] == user_payload["firstName"]

    @allure.story("Update user")
    @allure.title("Returned lastName equals sent lastName")
    @pytest.mark.positive
    def test_updated_last_name(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert response.json()["lastName"] == user_payload["lastName"]

    @allure.story("Update user")
    @allure.title("Returned email equals sent email")
    @pytest.mark.positive
    def test_updated_email(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert response.json()["email"] == user_payload["email"]

    @allure.story("Update user")
    @allure.title("Returned age equals sent age")
    @pytest.mark.positive
    def test_updated_age(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert response.json()["age"] == user_payload["age"]

    @allure.story("Validation")
    @allure.title("Response contains required fields")
    @pytest.mark.positive
    def test_required_fields_exist(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        data = response.json()

        assert "id" in data
        assert "firstName" in data
        assert "lastName" in data
        assert "email" in data
        assert "age" in data
        assert "gender" in data

    @allure.story("Validation")
    @allure.title("Returned id is positive")
    @pytest.mark.positive
    def test_user_id_positive(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert response.json()["id"] > 0

    @allure.story("Validation")
    @allure.title("Returned field types are correct")
    @pytest.mark.positive
    def test_returned_field_types(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["firstName"], str)
        assert isinstance(data["lastName"], str)
        assert isinstance(data["email"], str)
        assert isinstance(data["age"], int)
        assert isinstance(data["gender"], str)

    @allure.story("Validation")
    @allure.title("Update user with different ages")
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

        response = client.put("/users/1", json=payload)

        assert response.status_code == 200
        assert response.json()["age"] == age

    @allure.story("Validation")
    @allure.title("Update user with different genders")
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

        response = client.put("/users/1", json=payload)

        assert response.status_code == 200
        assert response.json()["gender"] == gender

    @allure.story("Negative")
    @allure.title("Update user without firstName")
    @pytest.mark.negative
    def test_update_without_first_name(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": 30,
            "gender": "male",
            "email": faker.email(),
        }

        response = client.put("/users/1", json=payload)

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Update user without email")
    @pytest.mark.negative
    def test_update_without_email(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": 30,
            "gender": "female",
        }

        response = client.put("/users/1", json=payload)

        assert response.status_code in (200, 400)

    @allure.story("Negative")
    @allure.title("Update empty payload")
    @pytest.mark.negative
    def test_update_empty_payload(self, client: ApiClient):
        response = client.put("/users/1", json={})

        assert response.status_code in (200, 400)

    @allure.story("Boundary")
    @allure.title("Update user with minimum age")
    @pytest.mark.boundary
    def test_update_minimum_age(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName":faker.first_name(),
            "lastName": faker.last_name(),
            "age": 0,
            "gender": "male",
            "email": faker.email(),
        }

        response = client.put("/users/1", json=payload)

        assert response.status_code == 200

    @allure.story("Headers")
    @allure.title("Response content type is JSON")
    @pytest.mark.positive
    def test_response_content_type(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert "application/json" in response.headers["Content-Type"]

    @allure.story("Performance")
    @allure.title("User update response time")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.put("/users/1", json=user_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Step by step")
    @allure.title("Update user step by step")
    @pytest.mark.smoke
    def test_update_user_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = client.put("/users/1", json=user_payload)

        with allure.step("Verify status code"):
            assert response.status_code == 200

        with allure.step("Verify schema"):
            validate(instance=response.json(), schema=USER_SCHEMA)

        with allure.step("Verify firstName"):
            assert response.json()["firstName"] == user_payload["firstName"]

        with allure.step("Verify lastName"):
            assert response.json()["lastName"] == user_payload["lastName"]

        with allure.step("Verify email"):
            assert response.json()["email"] == user_payload["email"]

        with allure.step("Verify age"):
            assert response.json()["age"] == user_payload["age"]

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    def test_headers_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = client.put("/users/1", json=user_payload)

        with allure.step("Verify Content-Type"):
            assert "application/json" in response.headers["Content-Type"]

    @allure.story("Step by step")
    @allure.title("Verify response time")
    @pytest.mark.slow
    def test_response_time_step_by_step(self, client: ApiClient, user_payload: dict[str, Any]):
        with allure.step("Send PUT request"):
            response = client.put("/users/1", json=user_payload)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
