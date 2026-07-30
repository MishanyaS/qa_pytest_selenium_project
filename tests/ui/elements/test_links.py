from __future__ import annotations

import allure
import pytest

from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.links_page import LinkPage

@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestLinks:
    @allure.story("Links navigation")
    @allure.title("Links page opens successfully")
    @allure.description("Verifies that the Links page can be opened from the Elements section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_links(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        links_page = LinkPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Links page"):
            elements_page.open_links()

        with allure.step("Verify Links page URL"):
            assert links_page.current_url.endswith("/links")

    @allure.story("Links page")
    @allure.title("All required links are visible")
    @allure.description("Verifies that navigation links and response links are displayed on the links page.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_links_are_visible(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Verify Home Link"):
            assert page.is_visible(page.HOME_LINK)

        with allure.step("Verify Dynamic Home Link"):
            assert page.is_visible(page.HOME_LINK_DYNAMIC)

        with allure.step("Verify Created Link"):
            assert page.is_visible(page.CREATED_LINK)

        with allure.step("Verify No Content Link"):
            assert page.is_visible(page.NO_CONTENT_LINK)

        with allure.step("Verify Moved Link"):
            assert page.is_visible(page.MOVED_LINK)

        with allure.step("Verify Bad Request Link"):
            assert page.is_visible(page.BAD_REQUEST_LINK)

        with allure.step("Verify Unauthorized Link"):
            assert page.is_visible(page.UNAUTHORIZED_LINK)

        with allure.step("Verify Forbidden Link"):
            assert page.is_visible(page.FORBIDDEN_LINK)

        with allure.step("Verify Not Found Link"):
            assert page.is_visible(page.NOT_FOUND_LINK)

    @allure.story("Home link")
    @allure.title("Home link opens DemoQA home page")
    @allure.description("Verifies that clicking the Home link opens the DemoQA home page in a new browser tab.")
    @pytest.mark.positive
    def test_home_links(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        original_window = driver.current_window_handle
        original_windows = driver.window_handles

        with allure.step("Click Home link"):
            page.click_home()

        with allure.step("Wait for new browser tab"):
            page.wait.until(
                lambda driver: len(driver.window_handles) > len(original_windows)
            )

        with allure.step("Switch to new browser tab"):
            new_window = next(
                window
                for window in driver.window_handles
                if window != original_window
            )
            driver.switch_to.window(new_window)

        with allure.step("Verify DemoQA home page URL"):
            assert driver.current_url == "https://demoqa.com/"

    @allure.story("Dynamic Home link")
    @allure.title("Dynamic Home link opens DemoQA home page")
    @allure.description("Verifies that clicking the dynamically generated Home link opens the DemoQA home page in a new browser tab.")
    @pytest.mark.positive
    def test_dynamic_home_links(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        original_window = driver.current_window_handle
        original_windows = driver.window_handles

        with allure.step("Click Dynamic Home link"):
            page.click_dynamic_home()

        with allure.step("Wait for new browser tab"):
            page.wait.until(
                lambda driver: len(driver.window_handles) > len(original_windows)
            )

        with allure.step("Switch to new browser tab"):
            new_window = next(
                window
                for window in driver.window_handles
                if window != original_window
            )
            driver.switch_to.window(new_window)

        with allure.step("Verify DemoQA home page URL"):
            assert driver.current_url == "https://demoqa.com/"

    @allure.story("Link responses")
    @allure.title("Created link returns 201 response")
    @allure.description("Verifies that clicking the Created link displays a successful HTTP 201 Created response.")
    @pytest.mark.positive
    def test_created_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Click Created link"):
            page.click_created()

        with allure.step("Verify response is visible"):
            assert page.response_visible()

        with allure.step("Verify response status"):
            assert "201" in page.response_text()

    @allure.story("Link responses")
    @allure.title("No Content link returns 204 response")
    @allure.description("Verifies that clicking the No Content link displays an HTTP 204 No Content response.")
    @pytest.mark.positive
    def test_no_content_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Click No Content link"):
            page.click_no_content()

        with allure.step("Verify response is visible"):
            assert page.response_visible()

        with allure.step("Verify response status"):
            assert "204" in page.response_text()

    @allure.story("Link responses")
    @allure.title("Moved link returns 301 response")
    @allure.description("Verifies that clicking the No Moved link displays an HTTP 301 Moved response.")
    @pytest.mark.positive
    def test_moved_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Click Moved link"):
            page.click_moved()

        with allure.step("Verify response is visible"):
            assert page.response_visible()

        with allure.step("Verify response status"):
            assert "301" in page.response_text()

    @allure.story("Link responses")
    @allure.title("Bad Request link returns 400 response")
    @allure.description("Verifies that clicking the Bad Request link displays an HTTP 400 Bad Request response.")
    @pytest.mark.positive
    def test_bad_request_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Click Bad Request link"):
            page.click_bad_request()

        with allure.step("Verify response is visible"):
            assert page.response_visible()

        with allure.step("Verify response status"):
            assert "400" in page.response_text()

    @allure.story("Link responses")
    @allure.title("Unauthorized link returns 401 response")
    @allure.description("Verifies that clicking the Unauthorized link displays an HTTP 401 Unauthorized response.")
    @pytest.mark.positive
    def test_unauthorized_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Click Unauthorized link"):
            page.click_unauthorized()

        with allure.step("Verify response is visible"):
            assert page.response_visible()

        with allure.step("Verify response status"):
            assert "401" in page.response_text()

    @allure.story("Link responses")
    @allure.title("Forbidden link returns 403 response")
    @allure.description("Verifies that clicking the Forbidden link displays an HTTP 403 Forbidden response.")
    @pytest.mark.positive
    def test_forbidden_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Click Forbidden link"):
            page.click_forbidden()

        with allure.step("Verify response is visible"):
            assert page.response_visible()

        with allure.step("Verify response status"):
            assert "403" in page.response_text()

    @allure.story("Link responses")
    @allure.title("Not Found link returns 404 response")
    @allure.description("Verifies that clicking the Not Found link displays an HTTP 404 Not Found response.")
    @pytest.mark.positive
    def test_not_found_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        with allure.step("Click Not Found link"):
            page.click_not_found()

        with allure.step("Verify response is visible"):
            assert page.response_visible()

        with allure.step("Verify response status"):
            assert "404" in page.response_text()

    @allure.story("Link responses")
    @allure.title("All response links return expected status codes")
    @allure.description("Verifies that all HTTP response links display their expected HTTP status code.")
    @pytest.mark.positive
    def test_all_response_links(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = LinkPage(driver)

        with allure.step("Open Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_links()

        response_links = (
            ("Created", page.click_created, "201"),
            ("No Content", page.click_no_content, "204"),
            ("Moved", page.click_moved, "301"),
            ("Bad Request", page.click_bad_request, "400"),
            ("Unauthorized", page.click_unauthorized, "401"),
            ("Forbidden", page.click_forbidden, "403"),
            ("Not Found", page.click_not_found, "404"),
        )

        for link_name, click_action, expected_status in response_links:
            with allure.step(f"Click {link_name} link"):
                click_action()

            with allure.step(f"Verify {link_name} response status is {expected_status}"):
                page.wait_for_response_status(expected_status)
                assert page.response_visible()
                assert expected_status in page.response_text()
