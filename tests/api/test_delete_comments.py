import allure
import pytest
import requests

from utils.api_client import ApiClient


@allure.epic("API")
@allure.feature("Delete Comments")
@pytest.mark.api
@pytest.mark.regression
class TestDeleteComments:
    @allure.step("Delete comment")
    def _delete_comment(self, client: ApiClient, comment_id: int) -> requests.Response:
        return client.delete(f"/comments/{comment_id}")

    @allure.story("Delete comment")
    @allure.title("DELETE /comments/1 returns 200")
    @allure.description("Verifies that DELETE /comments/1 returns status code 200.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_delete_comment_status_code(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert response.status_code == 200

    @allure.story("Delete comment")
    @allure.title("Response is JSON")
    @allure.description("Verifies that the response content type is JSON.")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Delete comment")
    @allure.title("Deleted comment contains id")
    @allure.description("Verifies that the deleted comment contains an id field.")
    @pytest.mark.positive
    def test_deleted_comment_has_id(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert "id" in response.json()

    @allure.story("Delete comment")
    @allure.title("Deleted id equals requested id")
    @allure.description(
        "Verifies that the returned id matches the requested comment id."
    )
    @pytest.mark.positive
    def test_deleted_id_matches(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert response.json()["id"] == 1

    @allure.story("Delete comment")
    @allure.title("Deleted flag exists")
    @allure.description("Verifies that the response contains the deletion flag.")
    @pytest.mark.positive
    def test_deleted_flag_exists(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert "isDeleted" in response.json()

    @allure.story("Delete comment")
    @allure.title("Deleted flag is True")
    @allure.description("Verifies that the deletion flag is set to True.")
    @pytest.mark.positive
    def test_deleted_flag_true(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert response.json()["isDeleted"] is True

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @allure.description("Verifies that the returned id is an integer.")
    @pytest.mark.positive
    def test_deleted_id_type(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned body is string")
    @allure.description("Verifies that the returned body is a string.")
    @pytest.mark.positive
    def test_deleted_body_type(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert isinstance(response.json()["body"], str)

    @allure.story("Validation")
    @allure.title("Returned postId is integer")
    @allure.description("Verifies that the returned postId is an integer.")
    @pytest.mark.positive
    def test_deleted_post_id_type(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert isinstance(response.json()["postId"], int)

    @allure.story("Validation")
    @allure.title("Returned likes is integer")
    @allure.description("Verifies that the returned likes value is an integer.")
    @pytest.mark.positive
    def test_deleted_likes_type(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert isinstance(response.json()["likes"], int)

    @allure.story("Validation")
    @allure.title("Returned user is object")
    @allure.description("Verifies that the returned user is an object.")
    @pytest.mark.positive
    def test_deleted_user_type(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert isinstance(response.json()["user"], dict)

    @allure.story("Validation")
    @allure.title("Returned user contains required fields")
    @allure.description("Verifies that the returned user contains required fields.")
    @pytest.mark.positive
    def test_deleted_user_fields(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        user = response.json()["user"]

        assert "id" in user
        assert "username" in user

    @allure.story("Delete comment")
    @allure.title("Delete different comment ids")
    @pytest.mark.parametrize(
        "comment_id",
        [
            1,
            2,
            3,
            10,
            50,
        ],
    )
    @allure.description(
        "Verifies that different comment ids can be deleted successfully."
    )
    @pytest.mark.positive
    def test_delete_various_comments(self, client: ApiClient, comment_id: int):
        response = self._delete_comment(client, comment_id)

        data = response.json()

        assert response.status_code == 200
        assert data["id"] == comment_id
        assert data["isDeleted"] is True

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @allure.description("Verifies that an unknown endpoint returns status code 404.")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.delete("/comments123/1")

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown comment id")
    @allure.description("Verifies API behavior for an unknown comment id.")
    @pytest.mark.negative
    def test_unknown_comment_id(self, client: ApiClient):
        response = self._delete_comment(client, 999999)

        assert response.status_code in (200, 404)

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @allure.description("Verifies that the response time is less than two seconds.")
    @pytest.mark.slow
    @pytest.mark.positive
    def test_response_time(self, client: ApiClient):
        response = self._delete_comment(client, 1)

        assert response.elapsed.total_seconds() < 2

    @allure.story("Step by step")
    @allure.title("Delete several comments")
    @allure.description("Verifies deletion of several comments step by step.")
    @pytest.mark.parametrize(
        "comment_id",
        [
            1,
            2,
            3,
            5,
            10,
        ],
    )
    @pytest.mark.positive
    def test_delete_multiple_comments(self, client: ApiClient, comment_id: int):
        response = self._delete_comment(client, comment_id)

        data = response.json()

        assert response.status_code == 200
        assert data["id"] == comment_id
        assert data["isDeleted"] is True

    @allure.story("Step by step")
    @allure.title("Delete comment step by step")
    @allure.description("Verifies successful comment deletion step by step.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_delete_comment_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self._delete_comment(client, 1)
            data = response.json()

        with allure.step("Verify status code"):
            assert response.status_code == 200

        with allure.step("Verify id"):
            assert data["id"] == 1

        with allure.step("Verify deleted flag"):
            assert data["isDeleted"] is True

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    @allure.description("Verifies response headers step by step.")
    @pytest.mark.positive
    def test_headers_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self._delete_comment(client, 1)

        with allure.step("Verify Content-Type"):
            assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Step by step")
    @allure.title("Verify response time")
    @allure.description("Verifies response time step by step.")
    @pytest.mark.slow
    @pytest.mark.positive
    def test_response_time_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self._delete_comment(client, 1)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
