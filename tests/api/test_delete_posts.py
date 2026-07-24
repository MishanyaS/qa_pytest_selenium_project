import allure
import pytest

from utils.api_client import ApiClient

allure.epic("API")
@allure.feature("Delete Posts")
@pytest.mark.api
@pytest.mark.regression
class TestDeletePosts:
    @pytest.fixture(scope="class")
    def client(self, api_session):
        return ApiClient(api_session)

    @allure.story("Delete post")
    @allure.title("DELETE /posts/1 returns 200")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_delete_post_status_code(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.status_code == 200

    @allure.story("Delete post")
    @allure.title("Response is JSON")
    @pytest.mark.positive
    def test_response_is_json(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.headers["Content-Type"].startswith("application/json")

    @allure.story("Delete post")
    @allure.title("Deleted post contains id")
    @pytest.mark.positive
    def test_deleted_post_has_id(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert "id" in response.json()

    @allure.story("Delete post")
    @allure.title("Deleted id equals requested id")
    @pytest.mark.positive
    def test_deleted_id_matches(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.json()["id"] == 1

    @allure.story("Delete post")
    @allure.title("Deleted flag exists")
    @pytest.mark.positive
    def test_deleted_flag_exists(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert "isDeleted" in response.json()

    @allure.story("Delete post")
    @allure.title("Deleted is True")
    @pytest.mark.positive
    def test_deleted_flag_true(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.json()["isDeleted"] is True

    @allure.story("Validation")
    @allure.title("Returned id is integer")
    @pytest.mark.positive
    def test_deleted_id_type(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert isinstance(response.json()["id"], int)

    @allure.story("Delete post")
    @allure.title("Delete different post ids")
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
    @pytest.mark.regression
    def test_delete_various_posts(self, client: ApiClient, post_id: int):
        response = client.delete(f"/posts/{post_id}")

        assert response.status_code == 200
        assert response.json()["id"] == post_id
        assert response.json()["isDeleted"] is True

    @allure.story("Negative")
    @allure.title("Unknown endpoint returns 404")
    @pytest.mark.negative
    def test_unknown_endpoint(self, client: ApiClient):
        response = client.delete("/posts123/1")

        assert response.status_code == 404

    @allure.story("Negative")
    @allure.title("Unknown post id")
    @pytest.mark.negative
    def test_unknown_post_id(self, client: ApiClient):
        response = client.delete("/posts/999999")

        assert response.status_code in (200, 404)

    @allure.story("Performane")
    @allure.title("Response time is acceptable")
    @pytest.mark.slow
    def test_response_time(self, client: ApiClient):
        response = client.delete("/posts/1")

        assert response.elapsed.total_seconds() < 2

    @allure.step("Delete post")
    def delete_post(self, client: ApiClient, post_id: int):
        return client.delete(f"/posts/{post_id}")

    @allure.story("Step by step")
    @allure.title("Delete several posts")
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
    def test_delete_multiple_posts(self, client: ApiClient, post_id: int):
        response = self.delete_post(client, post_id)

        assert response.status_code == 200
        assert response.json()["id"] == post_id
        assert response.json()["isDeleted"] is True
