import allure
import pytest
from jsonschema import validate

from schemas.user_schema import USER_SCHEMA
from utils.api_client import ApiClient
from utils.validators import validate_status_code, validate_email

@allure.epic("API")
@allure.feature("Users")
@pytest.mark.api
@pytest.mark.regression
class TestGetUsers:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)

    @allure.story("Get users list")
    @allure.title("GET /users returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_get_users_status_code(self, client: ApiClient):
        response = client.get("/users")

        assert validate_status_code(response.status_code, 200)

    @allure.story("Get users list")
    @allure.title("Response is JSON")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient):
        response = client.get("/users")

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Get users list")
    @allure.title("Response contains users")
    @pytest.mark.positive
    def test_users_key_exists(self, client: ApiClient):
        response = client.get("/users")

        data = response.json()

        assert "users" in data

    @allure.story("Get users list")
    @allure.title("Users is list")
    @pytest.mark.positive
    def test_users_is_list(self, client: ApiClient):
        response = client.get("/users")

        data = response.json()

        assert isinstance(data["users"], list)

    @allure.story("Get users list")
    @allure.title("Users list is not empty")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_users_is_not_empty(self, client: ApiClient):
        response = client.get("/users")

        data = response.json()

        assert len(data["users"]) > 0

    @allure.story("Schema check")
    @allure.title("First user matches schema")
    @pytest.mark.schema
    def test_first_user_schema(self, client: ApiClient):
        response = client.get("/users")

        first_post = response.json()["users"][0]

        validate(instance=first_post, schema=USER_SCHEMA)

    @allure.story("Get users list")
    @allure.title("Users total count is bigger than 0")
    @pytest.mark.positive
    def test_total_positive(self, client: ApiClient):
        response = client.get("/users")

        data = response.json()

        assert data["total"] > 0

    @allure.story("Get users list")
    @allure.title("limit is bigger than 0")
    @pytest.mark.positive
    def test_limit_positive(self, client: ApiClient):
        response = client.get("/users")

        data = response.json()

        assert data["limit"] > 0

    @allure.story("Get users list")
    @allure.title("skip is not negative")
    @pytest.mark.positive
    def test_skip_not_negative(self, client: ApiClient):
        response = client.get("/users")

        data = response.json()

        assert data["skip"] >= 0

    @allure.story("Get users list")
    @allure.title("First user contains id")
    @pytest.mark.positive
    def test_first_user_has_id(self, client: ApiClient):
        response = client.get("/users")

        first_user = response.json()["users"][0]

        assert "id" in first_user

    @allure.story("Get users list")
    @allure.title("First user contains firstName")
    @pytest.mark.positive
    def test_first_user_has_first_name(self, client: ApiClient):
        response = client.get("/users")

        first_user = response.json()["users"][0]

        assert "firstName" in first_user

    @allure.story("Get single user")
    @allure.title("GET /users/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_get_single_user_status_code(self, client: ApiClient):
        response = client.get("/users/1")

        assert response.status_code == 200

    @allure.story("Get single user")
    @allure.title("Single user matches schema")
    @pytest.mark.schema
    def test_single_user_schema(self, client: ApiClient):
        response = client.get("/users/1")

        validate(instance=response.json(), schema=USER_SCHEMA)

    @allure.story("Get single user")
    @allure.title("Returned id matches requested")
    @pytest.mark.positive
    def test_user_id_matches(self, client: ApiClient):
        response = client.get("/users/1")

        assert response.json()["id"] == 1

    @allure.story("Pagination")
    @allure.title("Limit parameter works")
    @pytest.mark.parametrize(
        "limit",
        [
            1,
            3,
            5,
            10,
            20,
        ],
    )
    @pytest.mark.positive
    def test_limit_parameter(self, client: ApiClient, limit: int):
        response = client.get("/users", params={"limit": limit})

        users = response.json()["users"]

        assert len(users) == limit

    @allure.story("Pagination")
    @allure.title("Skip parameter works")
    @pytest.mark.parametrize(
        "skip",
        [
            0,
            1,
            5,
            10,
            20,
        ],
    )
    @pytest.mark.positive
    def test_skip_parameter(self, client: ApiClient, skip: int):
        response = client.get("/users", params={"skip": skip})

        assert response.json()["skip"] == skip

    @allure.story("Pagination")
    @allure.title("Limit and skip together")
    @pytest.mark.parametrize(
        "limit, skip",
        [
            (5, 0),
            (5, 5),
            (10, 10),
            (15, 15),
        ],
    )
    @pytest.mark.regression
    def test_limit_skip(self, client: ApiClient, limit: int, skip: int):
        response = client.get("/users", params={"limit": limit, "skip": skip})

        data = response.json()

        assert len(data["users"]) == limit
        assert data["skip"] == skip

    @allure.story("Search")
    @allure.title("Search returns 200")
    @pytest.mark.positive
    def test_search_status_code(self, client: ApiClient):
        response = client.get("/users/search", params={"q": "John",})

        assert response.status_code == 200

    @allure.story("Search")
    @allure.title("Search returns matching users")
    @pytest.mark.positive
    def test_search_contains_query(self, client: ApiClient):
        response = client.get("/users/search", params={"q": "John",})

        users = response.json()["users"]

        assert any(
            "john" in user["firstName"].lower()
            or "john" in user["lastName"].lower()
            for user in users
        )

    @allure.story("Validation")
    @allure.title("Every user has unique id")
    @pytest.mark.regression
    def test_unique_ids(self, client: ApiClient):
        response = client.get("/users")

        ids = [
            user["id"]
            for user in response.json()["users"]
        ]

        assert len(ids) == len(set(ids))

    @allure.story("Validation")
    @allure.title("Every user has first name")
    @pytest.mark.regression
    def test_first_names_not_empty(self, client: ApiClient):
        response = client.get("/users")

        users = response.json()["users"]

        assert all(
            len(user["firstName"].strip()) > 0
            for user in users
        )

    @allure.story("Validation")
    @allure.title("Every user has last name")
    @pytest.mark.regression
    def test_last_names_not_empty(self, client: ApiClient):
        response = client.get("/users")

        users = response.json()["users"]

        assert all(
            len(user["lastName"].strip()) > 0
            for user in users
        )

    @allure.story("Validation")
    @allure.title("Every age is bigger than 0")
    @pytest.mark.regression
    def test_age_positive(self, client: ApiClient):
        response = client.get("/users")

        users = response.json()["users"]

        assert all(
            user["age"] >= 0
            for user in users
        )

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient):
        response = client.get("/users")

        assert response.elapsed.total_seconds() < 2

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.get("/users123456")

        assert response.status_code == 404

    @allure.step("Get user")
    def get_user(self, client: ApiClient, user_id: int):
        return client.get(f"/users/{user_id}")

    @allure.story("Step by step")
    @allure.title("Several users are successfully loaded")
    @pytest.mark.parametrize(
        "user_id",
        [
            1,
            2,
            3,
            10,
            20,
        ],
    )
    def test_multiple_users(self, client: ApiClient, user_id: int):
        response = self.get_user(client, user_id)

        assert response.status_code == 200
        assert response.json()["id"] == user_id
