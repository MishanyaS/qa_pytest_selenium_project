from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.alerts_frames_page import AlertsFramesPage
from pages.home_page import HomePage
from pages.nested_frames_page import NestedFramesPage


@allure.epic("DemoQA UI")
@allure.feature("Alerts, Frame & Windows")
@pytest.mark.ui
@pytest.mark.regression
class TestNestedFrames:
    @allure.story("Nested Frames navigation")
    @allure.title("Nested Frames page opens successfully")
    @allure.description(
        "Verifies that the Nested Frames page can be opened successfully from the Alerts, Frame & Windows section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_nested_frames(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        nested_frames_page = NestedFramesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Alerts, Frame & Windows section"):
            home_page.open_alerts_frame_windows()

        with allure.step("Open Nested Frames page"):
            alerts_frames_page.open_nested_frames()

        with allure.step("Verify Nested Frames page URL"):
            assert nested_frames_page.current_url.endswith("/nestedframes")

    @allure.story("Nested Frames page")
    @allure.title("Parent Frame is visible")
    @allure.description(
        "Verifies that the parent frame is displayed on the Nested Frames page."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_parent_frame_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        nested_frames_page = NestedFramesPage(driver)

        with allure.step("Open Nested Frames page"):
            home_page.open_home_page()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_nested_frames()

        with allure.step("Verify parent frame is visible"):
            assert nested_frames_page.parent_frame_visible()

    @allure.story("Parent frame")
    @allure.title("Parent frame contains expected text")
    @allure.description("Verifies that the parent frame contains the expected text.")
    @pytest.mark.positive
    def test_parent_frame_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        nested_frames_page = NestedFramesPage(driver)

        with allure.step("Open Nested Frames page"):
            home_page.open_home_page()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_nested_frames()

        with allure.step("Get parent frame text"):
            parent_text = nested_frames_page.get_parent_frame_text()

        with allure.step("Verify parent frame text"):
            assert "Parent frame" in parent_text

    @allure.story("Child frame")
    @allure.title("Child frame contains expected text")
    @allure.description(
        "Verifies that the nested child frame can be accessed and contains the expected text."
    )
    @pytest.mark.positive
    def test_child_frame_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        nested_frames_page = NestedFramesPage(driver)

        with allure.step("Open Nested Frames page"):
            home_page.open_home_page()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_nested_frames()

        with allure.step("Switch to child frame and get text"):
            child_text = nested_frames_page.get_child_frame_text()

        with allure.step("Verify child frame text"):
            assert "Child Iframe" in child_text

    @allure.story("Nested frame")
    @allure.title("Parent and child frames contain different content")
    @allure.description(
        "Verifies that the parent and child nested frames contain their respective content."
    )
    @pytest.mark.positive
    def test_parent_and_child_frame_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        nested_frames_page = NestedFramesPage(driver)

        with allure.step("Open Nested Frames page"):
            home_page.open_home_page()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_nested_frames()

        with allure.step("Get parent frame text"):
            parent_text = nested_frames_page.get_parent_frame_text()

        with allure.step("Get child frame text"):
            child_text = nested_frames_page.get_child_frame_text()

        with allure.step("Verify parent frame content"):
            assert "Parent frame" in parent_text

        with allure.step("Verify child frame content"):
            assert "Child Iframe" in child_text

        with allure.step("Verify frame contents are different"):
            assert parent_text != child_text
