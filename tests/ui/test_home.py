from __future__ import annotations

import allure
import pytest

from config import BASE_UI_URL
from pages.home_page import HomePage

@allure.epic("DemoQA UI")
@allure.feature("Home Page")
@pytest.mark.ui
@pytest.mark.smoke
class TestHomePage:
    @allure.story("Home Page")
    @allure.title("Home page opens successfully")
    @allure.description("Verifies that the DemoQA home page is opened successfully and the expected URL is displayed")
    @pytest.mark.positive
    def test_home_page_opens(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Verify current URL"):
            assert page.current_url == BASE_UI_URL

    @allure.story("Home Page cards")
    @allure.title("All main category cards are visible")
    @allure.description("Verifies that all six main DemoQA category cards are displayed on the home page.")
    @pytest.mark.positive
    def test_all_category_cards_visible(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Verify Element card"):
            assert page.elements_visible()

        with allure.step("Verify Forms card"):
            assert page.forms_visible()

        with allure.step("Verify Alerts, Frame & Windows card"):
            assert page.alerts_frame_windows_visible()

        with allure.step("Verify Widgets card"):
            assert page.widgets_visible()

        with allure.step("Verify Interactions card"):
            assert page.interactions_visible()

        with allure.step("Verify Book Store Application card"):
            assert page.interactions_visible()

    @allure.story("Elements navigation")
    @allure.title("Elements card opens Elements section")
    @allure.description("Verifies navigation from the Home page to the Elements section.")
    @pytest.mark.positive
    def test_open_elements(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Click Elements card"):
            page.open_elements()

        with allure.step("Verify Elements URL"):
            assert page.current_url.endswith("/elements")

    @allure.story("Forms navigation")
    @allure.title("Forms card opens Forms section")
    @allure.description("Verifies navigation from the Home page to the Forms section.")
    @pytest.mark.positive
    def test_open_forms(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Click Forms card"):
            page.open_forms()

        with allure.step("Verify Forms URL"):
            assert page.current_url.endswith("/forms")

    @allure.story("Alerts navigation")
    @allure.title("Alerts, Frame & Windows card opens corresponding section")
    @allure.description("Verifies navigation from the Home page to the Alerts, Frame & Windows section.")
    @pytest.mark.positive
    def test_open_alerts(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Click Alerts, Frame & Windows card"):
            page.open_alerts_frame_windows()

        with allure.step("Verify Alerts, Frame & Window URL"):
            assert page.current_url.endswith("/alertsWindows")

    @allure.story("Widgets navigation")
    @allure.title("Widgets card opens Widgets section")
    @allure.description("Verifies navigation from the Home page to the Widgets section.")
    @pytest.mark.positive
    def test_open_widgets(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Click Widgets card"):
            page.open_widgets()

        with allure.step("Verify Widgets URL"):
            assert page.current_url.endswith("/widgets")

    @allure.story("Interactions navigation")
    @allure.title("Interactions card opens Interactions section")
    @allure.description("Verifies navigation from the Home page to the Interactions section.")
    @pytest.mark.positive
    def test_open_interactions(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Click Interactions card"):
            page.open_interactions()

        with allure.step("Verify Interactions URL"):
            assert page.current_url.endswith("/interaction")

    @allure.story("Book Store navigation")
    @allure.title("Book Store Application card opens Book Store section")
    @allure.description("Verifies navigation from the Home page to the Book Store Application section.")
    @pytest.mark.positive
    def test_open_book_store(self, driver):
        page = HomePage(driver)

        with allure.step("Open DemoQA home page"):
            page.open()

        with allure.step("Click Book Store Application card"):
            page.open_book_store()

        with allure.step("Verify Book Store URL"):
            assert page.wait_url_contains("/books")
