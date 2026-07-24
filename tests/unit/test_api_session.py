import allure
import pytest
import requests

allure.epic("Unit")
@allure.feature("API Session")
@pytest.mark.unit
class TestApiSession:
    @allure.story("Session")
    @allure.title("Fixture returns request.Session")
    def test_session_instance(self, api_session):
        assert isinstance(api_session, requests.Session)

    @allure.story("Headers")
    @allure.title("Content-Type header is application/json")
    def test_content_type_header(self, api_session):
        assert api_session.headers["Content-Type"] == "application/json"

    @allure.story("Headers")
    @allure.title("Accept header is application/json")
    def test_accept_header(self, api_session):
        assert api_session.headers["Accept"] == "application/json"

    @allure.story("Headers")
    @allure.title("Session contains required headers")
    def test_required_headers_exist(self, api_session):
        assert "Content-Type" in api_session.headers
        assert "Accept" in api_session.headers

    @allure.story("Headers")
    @allure.title("Headers are strings")
    def test_header_types(self, api_session):
        assert isinstance(api_session.headers["Content-Type"], str)
        assert isinstance(api_session.headers["Accept"], str)

    @allure.story("Session")
    @allure.title("Session headers object exists")
    def test_headers_object_exists(self, api_session):
        assert api_session.headers is not None

    @allure.story("Session")
    @allure.title("Session cookies object exists")
    def test_cookies_object_exists(self, api_session):
        assert api_session.cookies is not None

    @allure.story("Session")
    @allure.title("Session adapters exist")
    def test_adapters_exist(self, api_session):
        assert "http://" in api_session.adapters
        assert "https://" in api_session.adapters

    @allure.story("Session")
    @allure.title("Verify session can prepare request")
    def test_prepare_request(self, api_session):
        request = requests.Request("GET", "https://dummyjson.com/users")

        prepared = api_session.prepare_request(request)

        assert prepared.method == "GET"
        assert prepared.url == "https://dummyjson.com/users"

    @allure.story("Session")
    @allure.title("Headers are included into prepared request")
    def test_headers_in_prepared_request(self, api_session):
        request = requests.Request("GET", "https://dummyjson.com/users")

        prepared = api_session.prepare_request(request)

        assert prepared.headers["Content-Type"] == "application/json"
        assert prepared.headers["Accept"] == "application/json"

    @allure.story("Session")
    @allure.title("Session stores custom header")
    def test_add_custom_header(self, api_session):
        api_session.headers["Authorization"] = "Bearer token"

        assert api_session.headers["Authorization"] == "Bearer token"

    @allure.story("Session")
    @allure.title("Session stores cookie")
    def test_add_cookie(self, api_session):
        api_session.cookies.set("session", "123")

        assert api_session.cookies.get("session") == "123"

    @allure.story("Session")
    @allure.title("Session verify flag exists")
    def test_verify_attribute(self, api_session):
        assert hasattr(api_session, "verify")

    @allure.story("Session")
    @allure.title("Session cert atribute exists")
    def test_cert_attribute(self, api_session):
        assert hasattr(api_session, "cert")

    @allure.story("Session")
    @allure.title("Session auth ttribute exists")
    def test_auth_attribute(self, api_session):
        assert hasattr(api_session, "auth")

    @allure.story("Session")
    @allure.title("Session proxies attribute exists")
    def test_proxies_attribute(self, api_session):
        assert hasattr(api_session, "proxies")
