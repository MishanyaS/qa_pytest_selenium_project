import allure
import pytest

from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Delete Users")
@pytest.mark.api
@pytest.mark.regression
class TestDeleteUsers:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)

    @allure.story("Delete user")
    @allure.title("DELETE /users/1 returns 200")
    @allure.description("Verifies that deleting an existing user returns HTTP 200.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_delete_user_status_code(self, client: ApiClient):
        response = client.delete("/users/1")

        assert response.status_code == 200

    @allure.story("Delete user")
    @allure.title("Response is JSON")
    @allure.description("Verifies that the DELETE response is returned in JSON format.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_response_is_json(self, client: ApiClient):
        response = client.delete("/users/1")

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Delete user")
    @allure.title("Deleted user contains id")
    @allure.description("Verifies that the deleted user response contains the id field.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_user_has_id(self, client: ApiClient):
        response = client.delete("/users/1")

        assert "id" in response.json()

    @allure.story("Delete user")
    @allure.title("Deleted id equals requested id")
    @allure.description("Verifies that the returned user id matches re requested id.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_id_matches(self, client: ApiClient):
        response = client.delete("/users/1")

        assert response.json()["id"] == 1

    @allure.story("Delete user")
    @allure.title("Deleted flag exists")
    @allure.description("Verifies that the response contains the deletion flag.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_flag_exists(self, client: ApiClient):
        response = client.delete("/users/1")

        assert "isDeleted" in response.json()

    @allure.story("Delete user")
    @allure.title("Deleted flag is True")
    @allure.description("Verifies that the deleted flag is set to True.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_flag_true(self, client: ApiClient):
        response = client.delete("/users/1")

        assert response.json()["isDeleted"] is True

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @allure.description("Verifies that the returned user id has integer type.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_id_type(self, client: ApiClient):
        response = client.delete("/users/1")

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned firstName is string")
    @allure.description("Verifies that the returned firstName has string type.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_first_name_type(self, client: ApiClient):
        response = client.delete("/users/1")

        assert isinstance(response.json()["firstName"], str)

    @allure.story("Validation")
    @allure.title("Returned lastName is string")
    @allure.description("Verifies that the returned lastName has string type.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_last_name_type(self, client: ApiClient):
        response = client.delete("/users/1")

        assert isinstance(response.json()["lastName"], str)

    @allure.story("Validation")
    @allure.title("Returned email is string")
    @allure.description("Verifies that the returned email has string type.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_email_type(self, client: ApiClient):
        response = client.delete("/users/1")

        assert isinstance(response.json()["email"], str)

    @allure.story("Validation")
    @allure.title("Returned age is integer")
    @allure.description("Verifies that the returned age has integer type.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_age_type(self, client: ApiClient):
        response = client.delete("/users/1")

        assert isinstance(response.json()["age"], int)

    @allure.story("Validation")
    @allure.title("Returned gender is string")
    @pytest.mark.positive
    @allure.description("Verifies that the returned gender has integer type.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_deleted_gender_type(self, client: ApiClient):
        response = client.delete("/users/1")

        assert isinstance(response.json()["gender"], str)

    @allure.story("Delete user")
    @allure.title("Delete different user ids")
    @allure.description("Verifies that different existing users can be deleted successfully.")
    @pytest.mark.parametrize(
        "user_id",
        [
            1,
            2,
            3,
            10,
            50,
        ],
    )
    @pytest.mark.regression
    @pytest.mark.positive
    def test_delete_various_users(self, client: ApiClient, user_id: int):
        response = client.delete(f"/users/{user_id}")

        assert response.status_code == 200
        assert response.json()["id"] == user_id
        assert response.json()["isDeleted"] is True

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @allure.description("Verifies that an unknown endpoint returns HTTP 404.")
    @pytest.mark.negative
    @pytest.mark.api
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.delete("/users123/1")

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown user id")
    @allure.description("Verifies the API behavior when deleting a non-existent user.")
    @pytest.mark.negative
    @pytest.mark.api
    def test_unknown_user_id(self, client: ApiClient):
        response = client.delete("/users/999999")

        assert response.status_code in (200, 404)

    @allure.story("Performane")
    @allure.title("Response time is acceptable")
    @allure.description("Verifies that the DELETE request completes within the expected time.")
    @pytest.mark.slow
    @pytest.mark.api
    def test_response_time(self, client: ApiClient):
        response = client.delete("/users/1")

        assert response.elapsed.total_seconds() < 2

    @allure.step("Delete user")
    def delete_user(self, client: ApiClient, user_id: int):
        return client.delete(f"/users/{user_id}")

    @allure.story("Step by step")
    @allure.title("Delete several users")
    @allure.description("Verifies successful deletion of multiple users using different ids.")
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
    @pytest.mark.regression
    @pytest.mark.positive
    def test_delete_multiple_users(self, client: ApiClient, user_id: int):
        response = self.delete_user(client, user_id)

        assert response.status_code == 200
        assert response.json()["id"] == user_id
        assert response.json()["isDeleted"] is True

    @allure.story("Step by step")
    @allure.title("Delete user step by step")
    @allure.description("Verifies user deletion step by step.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_delete_user_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self.delete_user(client, 1)

        with allure.step("Verify status code"):
            assert response.status_code == 200

        with allure.step("Verify id"):
            assert response.json()["id"] == 1

        with allure.step("Verify deleted flag"):
            assert response.json()["isDeleted"] is True

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    @allure.description("Verifies response headers after deleting a user.")
    @pytest.mark.positive
    @pytest.mark.api
    def test_headers_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self.delete_user(client, 1)

        with allure.step("Verify Content-Type"):
            assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Step by step")
    @allure.title("Verify response time")
    @allure.description("Verifies response time after deleting a user.")
    @pytest.mark.slow
    @pytest.mark.api
    def test_response_time_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self.delete_user(client, 1)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
