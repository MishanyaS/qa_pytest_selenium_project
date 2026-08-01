from __future__ import annotations

import allure
import pytest
import time

from pages.alerts_frames_page import AlertsFramesPage
from pages.home_page import HomePage
from pages.progress_bar_page import ProgressBarPage

@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestProgressBar:
    @allure.story("Progress Bar navigation")
    @allure.title("Progress Bar page opens successfully")
    @allure.description("Verifies that the Progress Bar page can be opened successfully from the Widgets section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_progress_bar(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        progress_bar_page = ProgressBarPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Progress Bar page"):
            alerts_frames_page.open_progress_bar()

        with allure.step("Verify Progress Bar page URL"):
            assert progress_bar_page.current_url.endswith("/progress-bar")

    @allure.story("Progress Bar page")
    @allure.title("Progress Bar elements are visible")
    @allure.description("Verifies that the progress bar and control buttons are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_progress_bar_elements_visible(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ProgressBarPage(driver)

        with allure.step("Open Progress Bar page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_progress_bar()

        with allure.step("Verify progress bar is visible"):
            assert page.progress_bar_visible()

        with allure.step("Verify initial progress bar value is 0"):
            assert page.progress_bar_value() == "0"

        with allure.step("Verify Start button is visible"):
            assert page.start_stop_button_visible()

    @allure.story("Progress")
    @allure.title("Progress starts successfully")
    @allure.description("Verifies that clicking Start begins progress.")
    @pytest.mark.positive
    def test_start_progress(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ProgressBarPage(driver)

        with allure.step("Open Progress Bar page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_progress_bar()

        with allure.step("Start progress"):
            page.start_progress()

        with allure.step("Wait for progress to begin"):
            time.sleep(1)

        with allure.step("Verify progress started"):
            assert page.progress_started()

    @allure.story("Progress")
    @allure.title("Progress can be stopped")
    @allure.description("Verifies that the running progress can be stopped.")
    @pytest.mark.positive
    def test_stop_progress(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ProgressBarPage(driver)

        with allure.step("Open Progress Bar page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_progress_bar()

        with allure.step("Start progress"):
            page.start_progress()

        with allure.step("Wait until progress increases"):
            time.sleep(1)

        with allure.step("Stop progress"):
            page.stop_progress()

        with allure.step("Verify button changed back to Start"):
            assert page.start_stop_button_text() == "Start"

    @allure.story("Progress")
    @allure.title("Progress reaches 100 percent")
    @allure.description("Verifies that the progress bar reaches 100 percent.")
    @pytest.mark.positive
    def test_progress_completion(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ProgressBarPage(driver)

        with allure.step("Open Progress Bar page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_progress_bar()

        with allure.step("Start progress"):
            page.start_progress()

        with allure.step("Wait for completion"):
            assert page.wait_for_progress_completion()

        with allure.step("Verify progress is complete"):
            assert page.progress_completed()

    @allure.story("Progress")
    @allure.title("Progress can be reset")
    @allure.description("Verifies that the Reset button restores the progress bar.")
    @pytest.mark.positive
    def test_reset_progress(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ProgressBarPage(driver)

        with allure.step("Open Progress Bar page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_progress_bar()

        with allure.step("Start progress"):
            page.start_progress()

        with allure.step("Wait for completion"):
            assert page.wait_for_progress_completion()

        with allure.step("Verify Reset button is enabled"):
            assert page.reset_button_enabled()

        with allure.step("Reset progress"):
            page.reset_progress()

        with allure.step("Verify progress reset"):
            assert page.progress_reset()

    @allure.story("Progress")
    @allure.title("Progress bar has valid limits")
    @allure.description("Verifies that minimum and maximum values are configured correctly.")
    @pytest.mark.positive
    def test_progress_bar_limits(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ProgressBarPage(driver)

        with allure.step("Open Progress Bar page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_progress_bar()

        with allure.step("Verify minimum value"):
            assert page.progress_bar_min_value() == "0"

        with allure.step("Verify maximum value"):
            assert page.progress_bar_max_value() == "100"
