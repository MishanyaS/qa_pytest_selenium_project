import allure
import pytest
import requests
from unittest.mock import MagicMock

from utils.api_client import ApiClient

allure.epic("Unit")
@allure.feature("ApiClient")
@pytest.mark.unit
class TestApiClient:
    @pytest.fixture()
    def session(self) -> MagicMock:
        return MagicMock(spec=requests.Session)

    @pytest.fixture()
    def client(self, session: MagicMock) -> ApiClient:
        return ApiClient(session=session, base_url="https://dummyjson.com", timeout=15)

    @pytest.fixture()
    def response(self) -> MagicMock:
        response = MagicMock(spec=requests.Response)
        response.status_code = 200
        return response

    @allure.story("Constructor")
    @allure.title("Client stores session")
    def test_session_saved(self, client: ApiClient, session: MagicMock):
        assert client.session is session

    @allure.story("Constructor")
    @allure.title("Client stores timeout")
    def test_timeout_saved(self, client: ApiClient):
        assert client.timeout == 15

    @allure.story("Constructor")
    @allure.title("Base url trailing slash removed")
    def test_base_url_strip(self, session: MagicMock):
        client = ApiClient(session=session, base_url="https://dummyjson.com/")

        assert client.base_url == "https://dummyjson.com"

    @allure.story("Constructor")
    @allure.title("Custom timeout is used")
    @pytest.mark.parametrize(
        "timeout",
        [
            1,
            5,
            10,
            30,
            60,
        ]
    )
    def test_custom_timeout(self, session: MagicMock, timeout: int):
        client = ApiClient(session=session, base_url="https://dummyjson.com/", timeout=timeout)

        assert client.timeout == timeout

    @allure.story("Constructor")
    @allure.title("Different base urls")
    @pytest.mark.parametrize(
        ("base_url", "expected"),
        [
            ("https://dummyjson.com", "https://dummyjson.com"),
            ("https://dummyjson.com/", "https://dummyjson.com"),
            ("https://localhost:8000/", "https://localhost:8000"),
            ("https://127.0.0.1:5000/", "https://127.0.0.1:5000"),
        ]
    )
    def test_base_url_normalization(self, session: MagicMock, base_url: str, expected: str):
        client = ApiClient(session=session, base_url=base_url)

        assert client.base_url == expected

    @allure.story("URL")
    @allure.title("Endpoint without slash")
    def test_url_without_slash(self, client: ApiClient):
        assert client._url("users") == "https://dummyjson.com/users"

    @allure.story("URL")
    @allure.title("Endpoint with slash")
    def test_url_with_slash(self, client: ApiClient):
        assert client._url("/users") == "https://dummyjson.com/users"
    
    @allure.story("URL")
    @allure.title("Nested endpoint")
    def test_nested_endpoint(self, client: ApiClient):
        assert client._url("/users/1") == "https://dummyjson.com/users/1"

    @allure.story("URL")
    @allure.title("Empty endpoint")
    def test_empty_endpoint(self, client: ApiClient):
        assert client._url("") == "https://dummyjson.com/"

    @allure.story("URL")
    @allure.title("Several leading slashes are removed")
    @pytest.mark.parametrize(
        ("endpoint", "expected"),
        [
            ("users", "https://dummyjson.com/users"),
            ("/users", "https://dummyjson.com/users"),
            ("//users", "https://dummyjson.com/users"),
            ("///users", "https://dummyjson.com/users"),
            ("////users/1", "https://dummyjson.com/users/1"),
        ]
    )
    def test_url_multiple_leading_slashes(self, client: ApiClient, endpoint: str, expected: str):
        assert client._url(endpoint) == expected

    @allure.story("GET")
    @allure.title("Calls session.get")
    def test_get_called(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        result = client.get("/users")

        assert result is response

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15)

    @allure.story("GET")
    @allure.title("Pass params")
    def test_get_params(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        client.get("/users", params={"limit": 10})

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, params={"limit": 10})

    @allure.story("GET")
    @allure.title("Pass headers")
    def test_get_headers(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        headers = {"Authorization": "Bearer token"}

        client.get("/users", headers=headers)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, headers=headers)

    @allure.story("GET")
    @allure.title("Pass cookies")
    def test_get_cookies(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        cookies = {"session": "123"}

        client.get("/users", cookies=cookies)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, cookies=cookies)

    @allure.story("GET")
    @allure.title("Pass auth")
    def test_get_auth(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        auth = {"admin": "password"}

        client.get("/users", auth=auth)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, auth=auth)

    @allure.story("GET")
    @allure.title("Pass stream option")
    def test_get_stream(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        client.get("/users", stream=True)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, stream=True)

    @allure.story("GET")
    @allure.title("Pass allow_redirects option")
    def test_get_allow_redirects(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        client.get("/users", allow_redirects=False)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, allow_redirects=False)

    @allure.story("GET")
    @allure.title("Pass multiple kwargs")
    def test_multiple_kwargs(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        headers = {
            "Authorization": "Bearer token"
        }
        params = {
            "limit": 10,
        }
        cookies = {
            "session": "abc",
        }

        client.get("/users", headers=headers, params=params, cookies=cookies)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, headers=headers, params=params, cookies=cookies)

    @allure.story("Response")
    @allure.title("Returns requests.Response object")
    def test_returns_response_instance(self, client: ApiClient, session: MagicMock):
        response = MagicMock(spec=requests.Response)

        session.get.return_value = response

        result = client.get("/users")

        assert isinstance(result, requests.Response)

    @allure.story("POST")
    @allure.title("Calls session.post")
    def test_get_headers(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.post.return_value = response

        payload = {"name": "John"}

        result = client.post("/users", json=payload)

        assert result is response

        session.post.assert_called_once_with("https://dummyjson.com/users", timeout=15, json=payload)

    @allure.story("POST")
    @allure.title("Post with params")
    def test_post_params(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.post.return_value = response

        client.post("/users", json={"debug": 1})

        session.post.assert_called_once()

    @allure.story("POST")
    @allure.title("Pass from data")
    def test_post_data(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.post.return_value = response

        data = {
            "username": "john",
            "password": "123456",
        }

        client.post("/login", data=data)

        session.post.assert_called_once_with("https://dummyjson.com/login", timeout=15, data=data)

    @allure.story("POST")
    @allure.title("Pass files")
    def test_post_files(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.post.return_value = response

        files = {
            "file": b"dummy content",
        }

        client.post("/upload", files=files)

        session.post.assert_called_once_with("https://dummyjson.com/upload", timeout=15, files=files)

    @allure.story("PUT")
    @allure.title("Calls session.put")
    def test_put_called(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.put.return_value = response

        payload = {
            "firstName": "John",
        }

        result = client.put("/users/1", json=payload)

        assert result is response
        
        session.put.assert_called_once_with("https://dummyjson.com/users/1", timeout=15, json=payload)

    @allure.story("PATCH")
    @allure.title("Calls session.patch")
    def test_patch_called(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.patch.return_value = response

        payload = {
            "age": 50,
        }

        result = client.patch("/users/1", json=payload)

        assert result is response
        
        session.patch.assert_called_once_with("https://dummyjson.com/users/1", timeout=15, json=payload)

    @allure.story("DELETE")
    @allure.title("Calls session.delete")
    def test_delete_called(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.delete.return_value = response

        result = client.delete("/users/1")

        assert result is response
        
        session.delete.assert_called_once_with("https://dummyjson.com/users/1", timeout=15)

    @allure.story("Timeout")
    @allure.title("Every request uses timeout")
    @pytest.mark.parametrize(
        ("method", "attribute"),
        [
            ("get", "get"),
            ("post", "post"),
            ("put", "put"),
            ("patch", "patch"),
            ("delete", "delete"),
        ]
    )
    def test_timeout_used(self, client: ApiClient, session: MagicMock, response: requests.Response, method: str, attribute: str):
        mocked = getattr(session, attribute)

        mocked.return_value = response

        getattr(client, method)("/users")

        assert mocked.call_args.kwargs["timeout"] == 15

    @allure.story("Exceptions")
    @allure.title("GET propagates exception")
    def test_get_exception(self, client: ApiClient, session: MagicMock):
        session.get.side_effect = requests.Timeout

        with pytest.raises(requests.Timeout):
            client.get("/users")

    @allure.story("Exceptions")
    @allure.title("POST propagates exception")
    def test_post_exception(self, client: ApiClient, session: MagicMock):
        session.post.side_effect = requests.ConnectionError

        with pytest.raises(requests.ConnectionError):
            client.post("/users")

    @allure.story("Exceptions")
    @allure.title("PUT propagates exception")
    def test_put_exception(self, client: ApiClient, session: MagicMock):
        session.put.side_effect = requests.RequestException

        with pytest.raises(requests.RequestException):
            client.put("/users")

    @allure.story("Exceptions")
    @allure.title("PATCH propagates exception")
    def test_patch_exception(self, client: ApiClient, session: MagicMock):
        session.patch.side_effect = requests.HTTPError

        with pytest.raises(requests.HTTPError):
            client.patch("/users")

    @allure.story("Exceptions")
    @allure.title("DELETE propagates exception")
    def test_delete_exception(self, client: ApiClient, session: MagicMock):
        session.delete.side_effect = requests.Timeout

        with pytest.raises(requests.Timeout):
            client.delete("/users")
