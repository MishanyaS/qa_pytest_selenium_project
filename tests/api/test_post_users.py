import allure
import pytest
from faker import Faker
from jsonschema import validate
from typing import Any

from schemas.user_schema import USER_SCHEMA
from utils.api_client import ApiClient
from utils.validators import validate_email

@allure.epic("API")
@allure.feature("Create Users")
@pytest.mark.api
@pytest.mark.regression
class TestCreateUsers:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)
    
    @pytest.fixture()
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
    
    @allure.story("Create user")
    @allure.title("POST /users/add returns 201")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_create_user_status_code(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.status_code == 201
    
    @allure.story("Create user")
    @allure.title("Response is JSON")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.headers["Content-Type"].startswith("application/json")
    
    @allure.story("Create user")
    @allure.title("Created user matches schema")
    @pytest.mark.schema
    def test_created_user_schema(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        validate(instance=response.json(), schema=USER_SCHEMA)
    
    @allure.story("Create user")
    @allure.title("Returned firstName equals sent firstName")
    @pytest.mark.positive
    def test_created_first_name(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.json()["firstName"] == user_payload["firstName"]
    
    @allure.story("Create user")
    @allure.title("Returned lastName equals sent lastName")
    @pytest.mark.positive
    def test_created_last_name(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.json()["lastName"] == user_payload["lastName"]

    @allure.story("Create user")
    @allure.title("Returned email equals sent email")
    @pytest.mark.positive
    def test_created_email(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.json()["email"] == user_payload["email"]

    @allure.story("Create user")
    @allure.title("Returned age equals sent age")
    @pytest.mark.positive
    def test_created_age(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.json()["age"] == user_payload["age"]

    @allure.story("Create user")
    @allure.title("Returned gender equals sent gender")
    @pytest.mark.positive
    def test_created_gender(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.json()["gender"] == user_payload["gender"]
    
    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @pytest.mark.positive
    def test_created_id_type(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned id exists")
    @pytest.mark.positive
    def test_id_exists(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert "id" in response.json()

    @allure.story("Validation")
    @allure.title("Returned firstName exists")
    @pytest.mark.positive
    def test_first_name_exists(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert "firstName" in response.json()

    @allure.story("Validation")
    @allure.title("Returned lastName exists")
    @pytest.mark.positive
    def test_last_name_exists(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert "lastName" in response.json()

    @allure.story("Validation")
    @allure.title("Returned email exists")
    @pytest.mark.positive
    def test_email_exists(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert "email" in response.json()

    @allure.story("Validation")
    @allure.title("Returned age exists")
    @pytest.mark.positive
    def test_age_exists(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert "age" in response.json()

    @allure.story("Validation")
    @allure.title("Returned gender exists")
    @pytest.mark.positive
    def test_gender_exists(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert "gender" in response.json()
    
    @allure.story("Validation")
    @allure.title("Create users with different ages")
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
    def test_create_with_various_ages(self, client: ApiClient, faker: Faker, age: int):
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "age": age,
            "gender": "male",
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code == 201
        assert response.json()["age"] == age

    @allure.story("Validation")
    @allure.title("Create users with different genders")
    @pytest.mark.parametrize(
        "gender",
        [
            "male",
            "female",
        ],
    )
    @pytest.mark.positive
    def test_create_with_various_genders(self, client: ApiClient, faker: Faker, gender: str):
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "age": 30,
            "gender": gender,
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code == 201
        assert response.json()["gender"] == gender

    @allure.story("Validation")
    @allure.title("Create users with different email domains")
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
    def test_create_with_various_domains(self, client: ApiClient, faker: Faker, domain: str):
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": f"{faker.user_name()}@{domain}",
            "age": 25,
            "gender": "female",
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code == 201
        assert response.json()["email"] == payload["email"]
    
    @allure.story("Negative")
    @allure.title("Empty JSON")
    @pytest.mark.negative
    def test_empty_json(self, client: ApiClient):
        response = client.post("/users/add", json={})

        assert response.status_code in (200, 201, 400)
    
    @allure.story("Negative")
    @allure.title("Missing firstName")
    @pytest.mark.negative
    def test_missing_first_name(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName": faker.first_name(),
            "email": faker.email(),
            "age": 25,
            "gender": "male",
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Missing lastName")
    @pytest.mark.negative
    def test_missing_last_name(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName": faker.first_name(),
            "email": faker.email(),
            "age": 25,
            "gender": "male",
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Missing email")
    @pytest.mark.negative
    def test_missing_email(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "age": 25,
            "gender": "male",
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code in (200, 201, 400)
    
    @allure.story("Negative")
    @allure.title("Invalid email")
    @pytest.mark.negative
    def test_invalid_email(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": "invalid-email",
            "age": 25,
            "gender": "male",
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Negative age")
    @pytest.mark.negative
    def test_negative_age(self, client: ApiClient, faker: Faker):
        payload = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "age": -10,
            "gender": "male",
        }

        response = client.post("/users/add", json=payload)

        assert response.status_code in (200, 201, 400)

    @allure.story("Negative")
    @allure.title("Invalid endpoint")
    @pytest.mark.negative
    def test_invalid_endpoint(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add123", json=user_payload)

        assert response.status_code == 404

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient, user_payload: dict[str, Any]):
        response = client.post("/users/add", json=user_payload)

        assert response.elapsed.total_seconds() < 2

    @allure.step("Create user")
    def create_user(self, client: ApiClient, user_payload: dict[str, Any]):
        return client.post("/users/add", json=user_payload)

    @allure.story("Step by step")
    @allure.title("Create several users")
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
    def test_create_multiple_users(self, client: ApiClient, faker: Faker, index: int):
        payload = {
            "firstName": f"User{index}",
            "lastName": faker.last_name(),
            "email": f"user{index}@example.com",
            "age": 20 + index,
            "gender": "male",
        }

        response = self.create_user(client, payload)

        assert response.status_code == 201
        assert response.json()["firstName"] == payload["firstName"]
        assert response.json()["lastName"] == payload["lastName"]
        assert response.json()["email"] == payload["email"]
        assert response.json()["age"] == payload["age"]
        assert response.json()["gender"] == payload["gender"]
