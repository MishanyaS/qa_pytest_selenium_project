import allure
import pytest

from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Delete Comments")
@pytest.mark.api
@pytest.mark.regression
class TestDeleteComments:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)

    @allure.story("Delete user")
    @allure.title("DELETE /comments/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_delete_comment_status_code(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert response.status_code == 200

    @allure.story("Delete comment")
    @allure.title("Response is JSON")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Delete comment")
    @allure.title("Deleted comment contains id")
    @pytest.mark.positive
    def test_deleted_comment_has_id(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert "id" in response.json()

    @allure.story("Delete comment")
    @allure.title("Deleted id equals requested id")
    @pytest.mark.positive
    def test_deleted_id_matches(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert response.json()["id"] == 1

    @allure.story("Delete comment")
    @allure.title("Deleted flag exists")
    @pytest.mark.positive
    def test_deleted_flag_exists(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert "isDeleted" in response.json()

    @allure.story("Delete comment")
    @allure.title("Deleted flag is True")
    @pytest.mark.positive
    def test_deleted_flag_true(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert response.json()["isDeleted"] is True

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @pytest.mark.positive
    def test_deleted_id_type(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert isinstance(response.json()["id"], int)

    @allure.story("Validation")
    @allure.title("Returned body is string")
    @pytest.mark.positive
    def test_deleted_body_type(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert isinstance(response.json()["body"], str)

    @allure.story("Validation")
    @allure.title("Returned postId is integer")
    @pytest.mark.positive
    def test_deleted_post_id_type(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert isinstance(response.json()["postId"], int)

    @allure.story("Validation")
    @allure.title("Returned likes is integer")
    @pytest.mark.positive
    def test_deleted_likes_type(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert isinstance(response.json()["likes"], int)

    @allure.story("Validation")
    @allure.title("Returned user is object")
    @pytest.mark.positive
    def test_deleted_user_type(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert isinstance(response.json()["user"], dict)

    @allure.story("Validation")
    @allure.title("Returned user contains required fields")
    @pytest.mark.positive
    def test_deleted_user_fields(self, client: ApiClient):
        response = client.delete("/comments/1")

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
    @pytest.mark.regression
    def test_delete_various_comments(self, client: ApiClient, comment_id: int):
        response = client.delete(f"/comments/{comment_id}")

        assert response.status_code == 200
        assert response.json()["id"] == comment_id
        assert response.json()["isDeleted"] is True

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.delete("/comments123/1")

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown comment id")
    @pytest.mark.negative
    def test_unknown_comment_id(self, client: ApiClient):
        response = client.delete("/comments/999999")

        assert response.status_code in (200, 404)

    @allure.story("Performane")
    @allure.title("Response time is acceptable")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient):
        response = client.delete("/comments/1")

        assert response.elapsed.total_seconds() < 2

    @allure.step("Delete comment")
    def delete_comment(self, client: ApiClient, comment_id: int):
        return client.delete(f"/comments/{comment_id}")

    @allure.story("Step by step")
    @allure.title("Delete several comments")
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
    def test_delete_multiple_comments(self, client: ApiClient, comment_id: int):
        response = self.delete_comment(client, comment_id)

        assert response.status_code == 200
        assert response.json()["id"] == comment_id
        assert response.json()["isDeleted"] is True

    @allure.story("Step by step")
    @allure.title("Delete commentuser step by step")
    @pytest.mark.smoke
    def test_delete_comment_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self.delete_comment(client, 1)

        with allure.step("Verify status code"):
            assert response.status_code == 200

        with allure.step("Verify id"):
            assert response.json()["id"] == 1

        with allure.step("Verify deleted flag"):
            assert response.json()["isDeleted"] is True

    @allure.story("Step by step")
    @allure.title("Verify response headers")
    def test_headers_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self.delete_comment(client, 1)

        with allure.step("Verify Content-Type"):
            assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Step by step")
    @allure.title("Verify response time")
    def test_response_time_step_by_step(self, client: ApiClient):
        with allure.step("Send DELETE request"):
            response = self.delete_comment(client, 1)

        with allure.step("Verify response time"):
            assert response.elapsed.total_seconds() < 2
