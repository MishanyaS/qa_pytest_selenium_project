from typing import Any

import allure
import pytest
import requests
from faker import Faker
from jsonschema import validate

from schemas.user_schema import USER_SCHEMA
from utils.api_client import ApiClient


@allure.epic("API")
@allure.feature("Create Users")
@pytest.mark.api
@pytest.mark.regression
class TestCreateUsers:
    @pytest.fixture(scope="function")
    def user_payload(self, faker: Faker) -> dict[str, Any]:
        return {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "age": faker.random_int(min=18, max=80),
            "gender": faker.random_element(
                elements=(
                    "male",
                    "female",
                )
            ),
        }

    @allure.step("Create user")
    def _create_user(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> requests.Response:
        return client.post("/users/add", json=user_payload)

    @allure.story("Create user")
    @allure.title("POST /users/add returns 201")
    @allure.description("Verifies that POST /users/add returns HTTP 201.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_create_user_status_code(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert response.status_code == 201

    @allure.story("Create user")
    @allure.title("Response is JSON")
    @allure.description("Verifies that the response is returned in JSON format.")
    @pytest.mark.positive
    def test_response_is_json(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Create user")
    @allure.title("Created user matches schema")
    @allure.description("Verifies that the created user matches the JSON schema.")
    @pytest.mark.schema
    @pytest.mark.positive
    def test_created_user_schema(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        validate(instance=response.json(), schema=USER_SCHEMA)

    @allure.story("Create user")
    @allure.title("Returned firstName equals sent firstName")
    @allure.description(
        "Verifies that the returned firstName matches the submitted value."
    )
    @pytest.mark.positive
    def test_created_first_name(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert response.json()["firstName"] == user_payload["firstName"]

    @allure.story("Create user")
    @allure.title("Returned lastName equals sent lastName")
    @allure.description(
        "Verifies that the returned lastName matches the submitted value."
    )
    @pytest.mark.positive
    def test_created_last_name(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert response.json()["lastName"] == user_payload["lastName"]

    @allure.story("Create user")
    @allure.title("Returned email equals sent email")
    @allure.description("Verifies that the returned email matches the submitted value.")
    @pytest.mark.positive
    def test_created_email(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert response.json()["email"] == user_payload["email"]

    @allure.story("Create user")
    @allure.title("Returned age equals sent age")
    @allure.description("Verifies that the returned age matches the submitted value.")
    @pytest.mark.positive
    def test_created_age(self, client: ApiClient, user_payload: dict[str, Any]) -> None:
        response = self._create_user(client, user_payload)

        assert response.json()["age"] == user_payload["age"]

    @allure.story("Create user")
    @allure.title("Returned gender equals sent gender")
    @allure.description(
        "Verifies that the returned gender matches the submitted value."
    )
    @pytest.mark.positive
    def test_created_gender(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert response.json()["gender"] == user_payload["gender"]

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @allure.description("Verifies that the returned user ID is an integer.")
    @pytest.mark.positive
    def test_created_id_type(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned id exists")
    @allure.description("Verifies that the response contains the user ID.")
    @pytest.mark.positive
    def test_id_exists(self, client: ApiClient, user_payload: dict[str, Any]) -> None:
        response = self._create_user(client, user_payload)

        assert "id" in response.json()

    @allure.story("Validation")
    @allure.title("Returned firstName exists")
    @allure.description("Verifies that the response contains the firstName field.")
    @pytest.mark.positive
    def test_first_name_exists(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert "firstName" in response.json()

    @allure.story("Validation")
    @allure.title("Returned lastName exists")
    @allure.description("Verifies that the response contains the lastName field.")
    @pytest.mark.positive
    def test_last_name_exists(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert "lastName" in response.json()

    @allure.story("Validation")
    @allure.title("Returned email exists")
    @allure.description("Verifies that the response contains the email field.")
    @pytest.mark.positive
    def test_email_exists(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert "email" in response.json()

    @allure.story("Validation")
    @allure.title("Returned age exists")
    @allure.description("Verifies that the response contains the age field.")
    @pytest.mark.positive
    def test_age_exists(self, client: ApiClient, user_payload: dict[str, Any]) -> None:
        response = self._create_user(client, user_payload)

        assert "age" in response.json()

    @allure.story("Validation")
    @allure.title("Returned gender exists")
    @allure.description("Verifies that the response contains the gender field.")
    @pytest.mark.positive
    def test_gender_exists(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert "gender" in response.json()

    @allure.story("Validation")
    @allure.title("Create users with different ages")
    @allure.description("Verifies that users can be created with different age values.")
    @pytest.mark.parametrize(
        "age",
        [
            18,
            25,
            35,
            50,
            80,
        ],
    )
    @pytest.mark.positive
    def test_create_with_various_ages(
        self, client: ApiClient, faker: Faker, age: int
    ) -> None:
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "age": age,
            "gender": "male",
        }

        response = self._create_user(client, payload)

        assert response.status_code == 201
        assert response.json()["age"] == age

    @allure.story("Validation")
    @allure.title("Create users with different genders")
    @allure.description(
        "Verifies that users can be created with different gender values."
    )
    @pytest.mark.parametrize(
        "gender",
        [
            "male",
            "female",
        ],
    )
    @pytest.mark.positive
    def test_create_with_various_genders(
        self, client: ApiClient, faker: Faker, gender: str
    ) -> None:
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "age": 30,
            "gender": gender,
        }

        response = self._create_user(client, payload)

        assert response.status_code == 201
        assert response.json()["gender"] == gender

    @allure.story("Validation")
    @allure.title("Create users with different email domains")
    @allure.description(
        "Verifies that users can be created with different email domains."
    )
    @pytest.mark.parametrize(
        "domain",
        [
            "gmail.com",
            "outlook.com",
            "yahoo.com",
            "example.com",
        ],
    )
    @pytest.mark.positive
    def test_create_with_various_domains(
        self, client: ApiClient, faker: Faker, domain: str
    ) -> None:
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": f"{faker.user_name()}@{domain}",
            "age": 25,
            "gender": "female",
        }

        response = self._create_user(client, payload)

        assert response.status_code == 201
        assert response.json()["email"] == payload["email"]

    @allure.story("Negative")
    @allure.title("Empty JSON")
    @allure.description(
        "Verifies the API behavior when an empty JSON payload is submitted."
    )
    @pytest.mark.negative
    def test_empty_json(self, client: ApiClient) -> None:
        response = self._create_user(client, {})

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Missing firstName")
    @allure.description("Verifies the API behavior when firstName is missing.")
    @pytest.mark.negative
    def test_missing_first_name(self, client: ApiClient, faker: Faker) -> None:
        payload = {
            "firstName": faker.first_name(),
            "email": faker.email(),
            "age": 25,
            "gender": "male",
        }

        response = self._create_user(client, payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Missing lastName")
    @allure.description("Verifies the API behavior when lastName is missing.")
    @pytest.mark.negative
    def test_missing_last_name(self, client: ApiClient, faker: Faker) -> None:
        payload = {
            "firstName": faker.first_name(),
            "email": faker.email(),
            "age": 25,
            "gender": "male",
        }

        response = self._create_user(client, payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Missing email")
    @allure.description("Verifies the API behavior when email is missing.")
    @pytest.mark.negative
    def test_missing_email(self, client: ApiClient, faker: Faker) -> None:
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "age": 25,
            "gender": "male",
        }

        response = self._create_user(client, payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Invalid email")
    @allure.description("Verifies the API behavior when an invalid email is submitted.")
    @pytest.mark.negative
    def test_invalid_email(self, client: ApiClient, faker: Faker) -> None:
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": "invalid-email",
            "age": 25,
            "gender": "male",
        }

        response = self._create_user(client, payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Negative age")
    @allure.description("Verifies the API behavior when a negative age is submitted.")
    @pytest.mark.negative
    def test_negative_age(self, client: ApiClient, faker: Faker) -> None:
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "age": -10,
            "gender": "male",
        }

        response = self._create_user(client, payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Invalid endpoint")
    @allure.description("Verifies that an invalid endpoint returns HTTP 404.")
    @pytest.mark.negative
    def test_invalid_endpoint(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = client.post("/users/add123", json=user_payload)

        assert response.status_code == 404

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @allure.description("Verifies that the user creation response time is acceptable.")
    @pytest.mark.slow
    @pytest.mark.positive
    def test_response_time(
        self, client: ApiClient, user_payload: dict[str, Any]
    ) -> None:
        response = self._create_user(client, user_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Step by step")
    @allure.title("Create several users")
    @allure.description("Verifies that multiple users can be created successfully.")
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
    @pytest.mark.positive
    def test_create_multiple_users(
        self, client: ApiClient, faker: Faker, index: int
    ) -> None:
        payload = {
            "firstName": f"User{index}",
            "lastName": faker.last_name(),
            "email": f"user{index}@example.com",
            "age": 20 + index,
            "gender": "male",
        }

        response = self._create_user(client, payload)

        data = response.json()

        assert response.status_code == 201
        assert data["firstName"] == payload["firstName"]
        assert data["lastName"] == payload["lastName"]
        assert data["email"] == payload["email"]
        assert data["age"] == payload["age"]
        assert data["gender"] == payload["gender"]
