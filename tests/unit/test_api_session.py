import allure
import pytest
import requests

@allure.epic("Unit")
@allure.feature("API Session")
@pytest.mark.unit
class TestApiSession:
    @allure.story("Session")
    @allure.title("Fixture returns request.Session")
    @allure.description("Verifies that the fixture returns a requests.Session instance.")
    @pytest.mark.positive
    def test_session_instance(self, api_session):
        assert isinstance(api_session, requests.Session)

    @allure.story("Headers")
    @allure.title("Content-Type header is application/json")
    @allure.description("Verifies that the Content-Type header is set to application/json.")
    @pytest.mark.positive
    def test_content_type_header(self, api_session):
        assert api_session.headers["Content-Type"] == "application/json"

    @allure.story("Headers")
    @allure.title("Accept header is application/json")
    @allure.description("Verifies that the Accept header is set to application/json.")
    @pytest.mark.positive
    def test_accept_header(self, api_session):
        assert api_session.headers["Accept"] == "application/json"

    @allure.story("Headers")
    @allure.title("Session contains required headers")
    @allure.description("Verifies that the session contains the required default headers.")
    @pytest.mark.positive
    def test_required_headers_exist(self, api_session):
        assert "Content-Type" in api_session.headers
        assert "Accept" in api_session.headers

    @allure.story("Headers")
    @allure.title("Headers are strings")
    @allure.description("Verifies that the default header values are strings.")
    @pytest.mark.positive
    def test_header_types(self, api_session):
        assert isinstance(api_session.headers["Content-Type"], str)
        assert isinstance(api_session.headers["Accept"], str)

    @allure.story("Session")
    @allure.title("Session headers object exists")
    @allure.description("Verifies that the session headers object is initialized.")
    @pytest.mark.positive
    def test_headers_object_exists(self, api_session):
        assert api_session.headers is not None

    @allure.story("Session")
    @allure.title("Session cookies object exists")
    @allure.description("Verifies that the session cookies object is initialized.")
    @pytest.mark.positive
    def test_cookies_object_exists(self, api_session):
        assert api_session.cookies is not None

    @allure.story("Session")
    @allure.title("Session adapters exist")
    @allure.description("Verifies that the session contains HTTP and HTTPS adapters.")
    @pytest.mark.positive
    def test_adapters_exist(self, api_session):
        assert "http://" in api_session.adapters
        assert "https://" in api_session.adapters

    @allure.story("Session")
    @allure.title("Verify session can prepare request")
    @allure.description("Verifies that the session prepares a request correctly.")
    @pytest.mark.positive
    def test_prepare_request(self, api_session):
        request = requests.Request("GET", "https://dummyjson.com/users")

        prepared = api_session.prepare_request(request)

        assert prepared.method == "GET"
        assert prepared.url == "https://dummyjson.com/users"

    @allure.story("Session")
    @allure.title("Headers are included into prepared request")
    @allure.description("Verifies that session headers are included in a prepared requests.")
    @pytest.mark.positive
    def test_headers_in_prepared_request(self, api_session):
        request = requests.Request("GET", "https://dummyjson.com/users")

        prepared = api_session.prepare_request(request)

        assert prepared.headers["Content-Type"] == "application/json"
        assert prepared.headers["Accept"] == "application/json"

    @allure.story("Session")
    @allure.title("Session stores custom header")
    @allure.description("Verifies that a custom header can be added to the session.")
    @pytest.mark.positive
    def test_add_custom_header(self, api_session):
        api_session.headers["Authorization"] = "Bearer token"

        assert api_session.headers["Authorization"] == "Bearer token"

    @allure.story("Session")
    @allure.title("Session stores cookie")
    @allure.description("Verifies that a cookie can be added to the session.")
    @pytest.mark.positive
    def test_add_cookie(self, api_session):
        api_session.cookies.set("session", "123")

        assert api_session.cookies.get("session") == "123"

    @allure.story("Session")
    @allure.title("Session verify flag exists")
    @allure.description("Verifies that the session has the verify attribute.")
    @pytest.mark.positive
    def test_verify_attribute(self, api_session):
        assert hasattr(api_session, "verify")

    @allure.story("Session")
    @allure.title("Session cert attribute exists")
    @allure.description("Verifies that the session has the cert attribute.")
    @pytest.mark.positive
    def test_cert_attribute(self, api_session):
        assert hasattr(api_session, "cert")

    @allure.story("Session")
    @allure.title("Session auth attribute exists")
    @allure.description("Verifies that the session has the auth attribute.")
    @pytest.mark.positive
    def test_auth_attribute(self, api_session):
        assert hasattr(api_session, "auth")

    @allure.story("Session")
    @allure.title("Session proxies attribute exists")
    @allure.description("Verifies that the session has the proxies attribute.")
    @pytest.mark.positive
    def test_proxies_attribute(self, api_session):
        assert hasattr(api_session, "proxies")
