import allure
import pytest

from utils.api_client import ApiClient

@allure.epic("API")
@allure.feature("Delete Posts")
@pytest.mark.api
@pytest.mark.regression
class TestDeletePosts:
    @allure.story("Delete post")
    @allure.title("DELETE /posts/1 returns 200")
    @allure.description("Verifies that deleting an existing post returns HTTP 200.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_delete_post_status_code(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.status_code == 200

    @allure.story("Delete post")
    @allure.title("Response is JSON")
    @allure.description("Verifies that the DELETE response is returned in JSON format.")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Delete post")
    @allure.title("Deleted post contains id")
    @allure.description("Verifies that the deleted post response contains the id field.")
    @pytest.mark.positive
    def test_deleted_post_has_id(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert "id" in response.json()

    @allure.story("Delete post")
    @allure.title("Deleted id equals requested id")
    @allure.description("Verifies that the returned post id matches the requested id.")
    @pytest.mark.positive
    def test_deleted_id_matches(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.json()["id"] == 1

    @allure.story("Delete post")
    @allure.title("Deleted flag exists")
    @allure.description("Verifies that the response contains the deletion flag.")
    @pytest.mark.positive
    def test_deleted_flag_exists(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert "isDeleted" in response.json()

    @allure.story("Delete post")
    @allure.title("Deleted is True")
    @allure.description("Verifies that the deleted flag is set to True.")
    @pytest.mark.positive
    def test_deleted_flag_true(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.json()["isDeleted"] is True

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @allure.description("Verifies that the returned post id has integer type.")
    @pytest.mark.positive
    def test_deleted_id_type(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert isinstance(response.json()["id"], int)

    @allure.story("Delete post")
    @allure.title("Delete different post ids")
    @allure.description("Verifies that different existing posts can be deleted successfully.")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            2,
            3,
            10,
            50,
        ],
    )
    @pytest.mark.positive
    def test_delete_various_posts(self, client: ApiClient, post_id: int):
        response = client.delete(f"/posts/{post_id}")

        assert response.status_code == 200
        assert response.json()["id"] == post_id
        assert response.json()["isDeleted"] is True

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @allure.description("Verifies that an unknown endpoint returns HTTP 404.")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.delete("/posts123/1")

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown post id")
    @allure.description("Verifies the API behavior when deleting a non-existent post.")
    @pytest.mark.negative
    def test_unknown_post_id(self, client: ApiClient):
        response = client.delete("/posts/999999")

        assert response.status_code in (200, 404)

    @allure.story("Performance")
    @allure.title("Response time is acceptable")
    @allure.description("Verifies that the DELETE request completes within the expected time.")
    @pytest.mark.slow
    @pytest.mark.positive
    def test_response_time(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.elapsed.total_seconds() < 2

    @allure.step("Delete post")
    def delete_post(self, client: ApiClient, post_id: int):
        return client.delete(f"/posts/{post_id}")

    @allure.story("Step by step")
    @allure.title("Delete several posts")
    @allure.description("Verifies successful deletion of multiple posts using different ids.")
    @pytest.mark.parametrize(
        "post_id",
        [
            1,
            2,
            3,
            5,
            10,
        ],
    )
    @pytest.mark.positive
    def test_delete_multiple_posts(self, client: ApiClient, post_id: int):
        response = self.delete_post(client, post_id)

        assert response.status_code == 200
        assert response.json()["id"] == post_id
        assert response.json()["isDeleted"] is True
