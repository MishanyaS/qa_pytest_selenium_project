import allure
import pytest
import requests
from unittest.mock import MagicMock

from utils.api_client import ApiClient

@allure.epic("Unit")
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
    @allure.description("Verifies that the client stores the provided session object.")
    @pytest.mark.positive
    def test_session_saved(self, client: ApiClient, session: MagicMock):
        assert client.session is session

    @allure.story("Constructor")
    @allure.title("Client stores timeout")
    @allure.description("Verifies that the client stores the configured timeout value.")
    @pytest.mark.positive
    def test_timeout_saved(self, client: ApiClient):
        assert client.timeout == 15

    @allure.story("Constructor")
    @allure.title("Base url trailing slash removed")
    @allure.description("Verifies that a trailing slash is removed from the base URL.")
    @pytest.mark.positive
    def test_base_url_strip(self, session: MagicMock):
        client = ApiClient(session=session, base_url="https://dummyjson.com/")

        assert client.base_url == "https://dummyjson.com"

    @allure.story("Constructor")
    @allure.title("Custom timeout is used")
    @allure.description("Verifies that the client accepts and stores custom timeout values.")
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
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_custom_timeout(self, session: MagicMock, timeout: int):
        client = ApiClient(session=session, base_url="https://dummyjson.com/", timeout=timeout)

        assert client.timeout == timeout

    @allure.story("Constructor")
    @allure.title("Different base urls")
    @allure.description("Verifies that different base URL formats are normalized correctly.")
    @pytest.mark.parametrize(
        ("base_url", "expected"),
        [
            ("https://dummyjson.com", "https://dummyjson.com"),
            ("https://dummyjson.com/", "https://dummyjson.com"),
            ("https://localhost:8000/", "https://localhost:8000"),
            ("https://127.0.0.1:5000/", "https://127.0.0.1:5000"),
        ]
    )
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_base_url_normalization(self, session: MagicMock, base_url: str, expected: str):
        client = ApiClient(session=session, base_url=base_url)

        assert client.base_url == expected

    @allure.story("URL")
    @allure.title("Endpoint without slash")
    @allure.description("Verifies that an endpoint without a leading slash is converted into a valid URL.")
    @pytest.mark.positive
    def test_url_without_slash(self, client: ApiClient):
        assert client._url("users") == "https://dummyjson.com/users"

    @allure.story("URL")
    @allure.title("Endpoint with slash")
    @allure.description("Verifies that an endpoint with a leading slash is converted into a valid URL.")
    @pytest.mark.positive
    def test_url_with_slash(self, client: ApiClient):
        assert client._url("/users") == "https://dummyjson.com/users"
    
    @allure.story("URL")
    @allure.title("Nested endpoint")
    @allure.description("Verifies that nested endpoints are converted into valid URLs.")
    @pytest.mark.positive
    def test_nested_endpoint(self, client: ApiClient):
        assert client._url("/users/1") == "https://dummyjson.com/users/1"

    @allure.story("URL")
    @allure.title("Empty endpoint")
    @allure.description("Verifies that an empty endpoint resolves to the base URL.")
    @pytest.mark.positive
    def test_empty_endpoint(self, client: ApiClient):
        assert client._url("") == "https://dummyjson.com/"

    @allure.story("URL")
    @allure.title("Several leading slashes are removed")
    @allure.description("Verifies that multiple leading slashes are removed from the endpoint.")
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
    @pytest.mark.positive
    @pytest.mark.boundary
    def test_url_multiple_leading_slashes(self, client: ApiClient, endpoint: str, expected: str):
        assert client._url(endpoint) == expected

    @allure.story("GET")
    @allure.title("Calls session.get")
    @allure.description("Verifies that the GET request is delegated to session.get().")
    @pytest.mark.positive
    def test_get_called(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        result = client.get("/users")

        assert result is response

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15)

    @allure.story("GET")
    @allure.title("Pass params")
    @allure.description("Verifies that query parameters are passed to session.get().")
    @pytest.mark.positive
    def test_get_params(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        client.get("/users", params={"limit": 10})

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, params={"limit": 10})

    @allure.story("GET")
    @allure.title("Pass headers")
    @allure.description("Verifies that request headers are passed to session.get().")
    @pytest.mark.positive
    def test_get_headers(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        headers = {"Authorization": "Bearer token"}

        client.get("/users", headers=headers)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, headers=headers)

    @allure.story("GET")
    @allure.title("Pass cookies")
    @allure.description("Verifies that cookies are passed to session.get().")
    @pytest.mark.positive
    def test_get_cookies(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        cookies = {"session": "123"}

        client.get("/users", cookies=cookies)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, cookies=cookies)

    @allure.story("GET")
    @allure.title("Pass auth")
    @allure.description("Verifies that authentication credentials are passed to session.get().")
    @pytest.mark.positive
    def test_get_auth(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        auth = {"admin": "password"}

        client.get("/users", auth=auth)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, auth=auth)

    @allure.story("GET")
    @allure.title("Pass stream option")
    @allure.description("Verifies that the stream option is passed to session.get().")
    @pytest.mark.positive
    def test_get_stream(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        client.get("/users", stream=True)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, stream=True)

    @allure.story("GET")
    @allure.title("Pass allow_redirects option")
    @allure.description("Verifies that the allow_redirects option is passed to session.get().")
    @pytest.mark.positive
    def test_get_allow_redirects(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.get.return_value = response

        client.get("/users", allow_redirects=False)

        session.get.assert_called_once_with("https://dummyjson.com/users", timeout=15, allow_redirects=False)

    @allure.story("GET")
    @allure.title("Pass multiple kwargs")
    @allure.description("Verifies that multiple keyword arguments are passed to session.get().")
    @pytest.mark.positive
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
    @allure.description("Verifies that the client returns a requests.Response object.")
    @pytest.mark.positive
    def test_returns_response_instance(self, client: ApiClient, session: MagicMock):
        response = MagicMock(spec=requests.Response)

        session.get.return_value = response

        result = client.get("/users")

        assert isinstance(result, requests.Response)

    @allure.story("POST")
    @allure.title("Calls session.post")
    @allure.description("Verifies that the POST request is delegated to session.post().")
    @pytest.mark.positive
    def test_post_called(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.post.return_value = response

        payload = {"name": "John"}

        result = client.post("/users", json=payload)

        assert result is response

        session.post.assert_called_once_with("https://dummyjson.com/users", timeout=15, json=payload)

    @allure.story("POST")
    @allure.title("Post with params")
    @allure.description("Verifies that POST requests are executed successfully with JSON payload.")
    @pytest.mark.positive
    def test_post_params(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.post.return_value = response

        client.post("/users", json={"debug": 1})

        session.post.assert_called_once()

    @allure.story("POST")
    @allure.title("Pass from data")
    @allure.description("Verifies that form data is passed to session.post().")
    @pytest.mark.positive
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
    @allure.description("Verifies that uploaded files are passed to session.post().")
    @pytest.mark.positive
    def test_post_files(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.post.return_value = response

        files = {
            "file": b"dummy content",
        }

        client.post("/upload", files=files)

        session.post.assert_called_once_with("https://dummyjson.com/upload", timeout=15, files=files)

    @allure.story("PUT")
    @allure.title("Calls session.put")
    @allure.description("Verifies that the PUT request is delegated to session.put().")
    @pytest.mark.positive
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
    @allure.description("Verifies that the PATCH request is delegated to session.patch().")
    @pytest.mark.positive
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
    @allure.description("Verifies that the DELETE request is delegated to session.delete().")
    @pytest.mark.positive
    def test_delete_called(self, client: ApiClient, session: MagicMock, response: requests.Response):
        session.delete.return_value = response

        result = client.delete("/users/1")

        assert result is response
        
        session.delete.assert_called_once_with("https://dummyjson.com/users/1", timeout=15)

    @allure.story("Timeout")
    @allure.title("Every request uses timeout")
    @allure.description("Verifies that every HTTP request uses the configured timeout.")
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
    @pytest.mark.positive
    def test_timeout_used(self, client: ApiClient, session: MagicMock, response: requests.Response, method: str, attribute: str):
        mocked = getattr(session, attribute)

        mocked.return_value = response

        getattr(client, method)("/users")

        assert mocked.call_args.kwargs["timeout"] == 15

    @allure.story("Exceptions")
    @allure.title("GET propagates exception")
    @allure.description("Verifies that GET request exceptions are propagated to the caller.")
    @pytest.mark.negative
    def test_get_exception(self, client: ApiClient, session: MagicMock):
        session.get.side_effect = requests.Timeout

        with pytest.raises(requests.Timeout):
            client.get("/users")

    @allure.story("Exceptions")
    @allure.title("POST propagates exception")
    @allure.description("Verifies that POST request exceptions are propagated to the caller.")
    @pytest.mark.negative
    def test_post_exception(self, client: ApiClient, session: MagicMock):
        session.post.side_effect = requests.ConnectionError

        with pytest.raises(requests.ConnectionError):
            client.post("/users")

    @allure.story("Exceptions")
    @allure.title("PUT propagates exception")
    @allure.description("Verifies that PUT request exceptions are propagated to the caller.")
    @pytest.mark.negative
    def test_put_exception(self, client: ApiClient, session: MagicMock):
        session.put.side_effect = requests.RequestException

        with pytest.raises(requests.RequestException):
            client.put("/users")

    @allure.story("Exceptions")
    @allure.title("PATCH propagates exception")
    @allure.description("Verifies that PATCH request exceptions are propagated to the caller.")
    @pytest.mark.negative
    def test_patch_exception(self, client: ApiClient, session: MagicMock):
        session.patch.side_effect = requests.HTTPError

        with pytest.raises(requests.HTTPError):
            client.patch("/users")

    @allure.story("Exceptions")
    @allure.title("DELETE propagates exception")
    @allure.description("Verifies that DELETE request exceptions are propagated to the caller.")
    @pytest.mark.negative
    def test_delete_exception(self, client: ApiClient, session: MagicMock):
        session.delete.side_effect = requests.Timeout

        with pytest.raises(requests.Timeout):
            client.delete("/users")
