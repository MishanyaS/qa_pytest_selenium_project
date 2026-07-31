from __future__ import annotations

import allure
import pytest

from pages.alerts_frames_page import AlertsFramesPage
from pages.home_page import HomePage
from pages.browser_windows_page import BrowserWindowsPage

@allure.epic("DemoQA UI")
@allure.feature("Alerts, Frame & Windows")
@pytest.mark.ui
@pytest.mark.regression
class TestBrowserWindows:
    @allure.story("Browser Windows navigation")
    @allure.title("Browser Windows page opens successfully")
    @allure.description("Verifies that the Browser Windows page page can be opened successfully.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_browser_windows(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        browser_windows_page = BrowserWindowsPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Alerts, Frame & Windows section"):
            home_page.open_alerts()

        with allure.step("Open Browser Windows page"):
            alerts_frames_page.open_browser_windows()

        with allure.step("Verify Browser Windows page URL"):
            assert browser_windows_page.current_url.endswith("/browser-windows")

    @allure.story("Browser Windows page")
    @allure.title("Browser Windows page elements are visible")
    @allure.description("Verifies that all Browser Windows controls are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_browser_windows_elements_visible(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Verify New Tab button is visible"):
            assert page.new_tab_visible()

        with allure.step("Verify New Window button is visible"):
            assert page.new_window_visible()

        with allure.step("Verify New Window Message button is visible"):
            assert page.new_window_message_visible()


    @allure.story("Browser Windows page")
    @allure.title("Opening a new tab creates a new browser window handle")
    @allure.description("Verifies that clicking the New Tab button opens a new browser tab without closing the original browser window.")
    @pytest.mark.positive
    def test_open_new_tab_creates_new_window_handle(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Store initial window handle"):
            original_handle = page.current_window_handle()

        with allure.step("Store initial window count"):
            initial_window_count = page.window_count()

        with allure.step("Open new tab"):
            page.open_new_tab()

        with allure.step("Verify new tab was opened"):
            assert page.window_count() == initial_window_count + 1

        with allure.step("Verify original window handle still exists"):
            assert original_handle in page.window_handles()

    @allure.story("Browser Windows")
    @allure.title("New Tab displays the sample page")
    @allure.description("Verifies that the new tab opened by the New Tab button displays the expected DemoQA simple page.")
    @pytest.mark.positive
    def test_new_tab_contains_sample_heading(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Open new tab"):
            page.open_new_tab()

        with allure.step("Switch to new tab"):
            page.switch_to_last_window()

        with allure.step("Verify sample heading is visible"):
            assert page.sample_heading_visible()

        with allure.step("Verify sample heading text"):
            assert page.sample_heading_text() == "This is a sample page"

    @allure.story("Browser Windows")
    @allure.title("Opening a new window creates a new browser window handle")
    @allure.description("Verifies that clicking the New Window button opens a new browser window without closing the original browser window.")
    @pytest.mark.positive
    def test_open_new_window_creates_new_window_handle(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Store initial window handle"):
            original_handle = page.current_window_handle()

        with allure.step("Store initial window count"):
            initial_window_count = page.window_count()

        with allure.step("Open new window"):
            page.open_new_window()

        with allure.step("Verify new window was opened"):
            assert page.window_count() == initial_window_count + 1

        with allure.step("Verify original window handle still exists"):
            assert original_handle in page.window_handles()

    @allure.story("Browser Windows")
    @allure.title("New window displays the sample page")
    @allure.description("Verifies that the new browser window opened by the New Window button displays the expected DemoQA sample page.")
    @pytest.mark.positive
    def test_new_window_contains_sample_heading(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Open new window"):
            page.open_new_window()

        with allure.step("Switch to new window"):
            page.switch_to_last_window()

        with allure.step("Verify sample heading is visible"):
            assert page.sample_heading_visible()

        with allure.step("Verify sample heading text"):
            assert page.sample_heading_text() == "This is a sample page"

    @allure.story("Browser Windows")
    @allure.title("Opening a new tab changes the current window handle")
    @allure.description("Verifies that the browser switches to the newly opened tab after the New Tab button is clicked.")
    @pytest.mark.positive
    def test_new_tab_becomes_current_window(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Store original window handle"):
            original_handle = page.current_window_handle()

        with allure.step("Open new tab"):
            page.open_new_tab()

        with allure.step("Switch to new tab"):
            page.switch_to_last_window()

        with allure.step("Verify current window is different from original"):
            assert page.current_window_handle() != original_handle

        with allure.step("Verify sample page is displayed"):
            assert page.sample_heading_text() == "This is a sample page"

    @allure.story("Browser Windows")
    @allure.title("User can switch back to the original browser window")
    @allure.description("Verifies that the user can return from the newly opened tab to the original Browser Windows page.")
    @pytest.mark.positive
    def test_switch_back_to_original_window(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Store original window handle"):
            original_handle = page.current_window_handle()

        with allure.step("Open new tab"):
            page.open_new_tab()

        with allure.step("Switch to new tab"):
            page.switch_to_last_window()

        with allure.step("Verify sample page is displayed"):
            assert page.sample_heading_visible()

        with allure.step("Switch back to original window"):
            page.switch_to_window(0)

        with allure.step("Verify original window is active"):
            assert page.current_window_handle() == original_handle

        with allure.step("Verify Browser Windows page is displayed"):
            assert page.new_tab_visible()
            assert page.new_window_visible()
            assert page.new_window_message_visible()

    @allure.story("Browser Windows")
    @allure.title("User can close the newly opened browser window")
    @allure.description("Verifies that the newly opened browser window can be closed and that the original browser window remains available.")
    @pytest.mark.positive
    def test_close_new_window(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = BrowserWindowsPage(driver)

        with allure.step("Open Browser Windows page"):
            home_page.open()
            home_page.open_alerts()
            alerts_frames_page.open_browser_windows()

        with allure.step("Store original window handle"):
            original_handle = page.current_window_handle()

        with allure.step("Store initial window count"):
            initial_window_count = page.window_count()

        with allure.step("Open new window"):
            page.open_new_window()

        with allure.step("Verify new window was opened"):
            assert page.window_count() == initial_window_count + 1

        with allure.step("Switch to new tab"):
            page.switch_to_last_window()

        with allure.step("Close current window"):
            page.close_current_window()

        with allure.step("Switch back to original window"):
            page.switch_to_window(0)

        with allure.step("Verify original window is active"):
            assert page.current_window_handle() == original_handle

        with allure.step("Verify window count returned to initial value"):
            assert page.window_count() == initial_window_count
