from __future__ import annotations

import allure
import pytest

from pages.alerts_frames_page import AlertsFramesPage
from pages.frames_page import FramesPage
from pages.home_page import HomePage


@allure.epic("DemoQA UI")
@allure.feature("Alerts, Frame & Windows")
@pytest.mark.ui
@pytest.mark.regression
class TestFrames:
    @allure.story("Frames navigation")
    @allure.title("Frame page opens successfully")
    @allure.description(
        "Verifies that the Frame page can be opened successfully from the Alerts, Frame & Windows section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_frames(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        frames_page = FramesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Alerts, Frame & Windows section"):
            home_page.open_alerts_frame_windows()

        with allure.step("Open Frames page"):
            alerts_frames_page.open_frames()

        with allure.step("Verify Frames page URL"):
            assert frames_page.current_url.endswith("/frames")

    @allure.story("Frames page")
    @allure.title("Frames are visible")
    @allure.description("Verifies that both frames are displayed on the Frames page.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_frames_visible(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        frames_page = FramesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_frames()

        with allure.step("Verify Frame 1 is visible"):
            assert frames_page.frame_1_visible()

        with allure.step("Verify Frame 2 is visible"):
            assert frames_page.frame_2_visible()

    @allure.story("Frame 1")
    @allure.title("Frame 1 contains expected heading")
    @allure.description(
        "Verifies that Frame 1 can be accessed and contains the expected sample heading."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_frame_1_heading(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        frames_page = FramesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_frames()

        with allure.step("Switch to Frame 1"):
            heading = frames_page.frame_1_heading()

        with allure.step("Verify Frame 1 heading"):
            assert heading == "This is a sample page"

    @allure.story("Frame 2")
    @allure.title("Frame 2 contains expected heading")
    @allure.description(
        "Verifies that Frame 2 can be accessed and contains the expected sample heading."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_frame_2_heading(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        frames_page = FramesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_frames()

        with allure.step("Switch to Frame 2"):
            heading = frames_page.frame_2_heading()

        with allure.step("Verify Frame 2 heading"):
            assert heading == "This is a sample page"
