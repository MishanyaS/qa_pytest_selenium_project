from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.tabs_page import TabsPage
from pages.widgets_page import WidgetsPage


@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestTabs:
    @allure.story("Tabs navigation")
    @allure.title("Tabs page opens successfully")
    @allure.description(
        "Verifies that the Tabs page can be opened successfully from the Widgets section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_tabs(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        tabs_page = TabsPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Tabs page"):
            widgets_page.open_tabs()

        with allure.step("Verify Tabs page URL"):
            assert tabs_page.current_url.endswith("/tabs")

    @allure.story("Tabs page")
    @allure.title("Tabs are displayed")
    @allure.description("Verifies that all available tabs are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_tabs_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = TabsPage(driver)

        with allure.step("Open Tabs page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_tabs()

        with allure.step("Wait until page is loaded"):
            assert page.what_tab_visible()

        with allure.step("Verify What tab is visible"):
            assert page.what_tab_visible()

        with allure.step("Verify Origin tab is visible"):
            assert page.origin_tab_visible()

        with allure.step("Verify Use tab is visible"):
            assert page.use_tab_visible()

        with allure.step("Verify More tab is visible"):
            assert page.more_tab_visible()

    @allure.story("Tabs")
    @allure.title("What tab is active by default")
    @allure.description("Verifies that the What tab is avtive after opening the page.")
    @pytest.mark.positive
    def test_default_active_tab(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = TabsPage(driver)

        with allure.step("Open Tabs page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_tabs()

        with allure.step("Wait until What panel is visible"):
            assert page.what_panel_visible()

        with allure.step("Verify active tab is What"):
            assert page.active_tab() == "What"

        with allure.step("Verify active tab id is demo-tab-what"):
            assert page.active_tab_id() == "demo-tab-what"

    @allure.story("Tabs")
    @allure.title("What tab content is displayed")
    @allure.description("Verifies that the What tab displays its content.")
    @pytest.mark.positive
    def test_what_tab_content(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = TabsPage(driver)

        with allure.step("Open Tabs page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_tabs()

        with allure.step("Open What tab"):
            page.open_what_tab()

        with allure.step("Wait until What panel is visible"):
            assert page.what_panel_visible()

        with allure.step("Verify content of What panel contains 'Lorem Ipsum'"):
            assert "Lorem Ipsum" in page.what_panel_text()

    @allure.story("Tabs")
    @allure.title("Origin tab content is displayed")
    @allure.description("Verifies that the Origin tab displays its content.")
    @pytest.mark.positive
    def test_origin_tab_content(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = TabsPage(driver)

        with allure.step("Open Tabs page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_tabs()

        with allure.step("Open Origin tab"):
            page.open_origin_tab()

        with allure.step("Wait until Origin panel is visible"):
            assert page.origin_panel_visible()

        with allure.step("Verify active tab is Origin"):
            assert page.active_tab() == "Origin"

        with allure.step(
            "Verify content of Origin panel contains 'Contrary to popular belief'"
        ):
            assert "Contrary to popular belief" in page.origin_panel_text()

    @allure.story("Tabs")
    @allure.title("Use tab content is displayed")
    @allure.description("Verifies that the Use tab displays its content.")
    @pytest.mark.positive
    def test_use_tab_content(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = TabsPage(driver)

        with allure.step("Open Tabs page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_tabs()

        with allure.step("Open Use tab"):
            page.open_use_tab()

        with allure.step("Wait until Use panel is visible"):
            assert page.use_panel_visible()

        with allure.step("Verify active tab is Use"):
            assert page.active_tab() == "Use"

        with allure.step(
            "Verify content of Use panel contains 'long established fact'"
        ):
            assert "long established fact" in page.use_panel_text()

    @allure.story("Tabs")
    @allure.title("More tab content is disabled")
    @allure.description("Verifies that the More tab is disabled.")
    @pytest.mark.positive
    def test_more_tab_disabled(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = TabsPage(driver)

        with allure.step("Open Tabs page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_tabs()

        with allure.step("Verify More tab is visible"):
            assert page.more_tab_visible()

        with allure.step("Verify More tab is disabled"):
            assert not page.is_enabled(page.MORE_TAB)

    @allure.story("Tabs")
    @allure.title("Tab switching works correctly")
    @allure.description("Verifies that switching between tabs changes the active tab.")
    @pytest.mark.positive
    def test_switch_tabs(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = TabsPage(driver)

        with allure.step("Open Tabs page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_tabs()

        with allure.step("Open Origin tab"):
            page.open_origin_tab()

        with allure.step("Wait until Origin panel is visible"):
            assert page.origin_panel_visible()

        with allure.step("Verify Origin tab is active"):
            assert page.active_tab() == "Origin"

        with allure.step("Open Use tab"):
            page.open_use_tab()

        with allure.step("Wait until Use panel is visible"):
            assert page.use_panel_visible()

        with allure.step("Verify Use tab is active"):
            assert page.active_tab() == "Use"
