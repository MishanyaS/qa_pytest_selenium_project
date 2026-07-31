from __future__ import annotations

import allure
import pytest

from pages.alerts_frames_page import AlertsFramesPage
from pages.home_page import HomePage
from pages.alerts_page import AlertsPage

@allure.epic("DemoQA UI")
@allure.feature("Alerts, Frame & Windows")
@pytest.mark.ui
@pytest.mark.regression
class TestAlerts:
    @allure.story("Alerts navigation")
    @allure.title("Alerts page opens successfully")
    @allure.description("Verifies that the Alerts page can be opens successfully from the Alerts, Frame & Windows section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_alerts(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        alerts_page = AlertsPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Alerts, Frame & Windows section"):
            home_page.open_alerts_frame_windows()

        with allure.step("Open Alerts page"):
            alerts_frames_page.open_alerts()

        with allure.step("Verify Alerts page URL"):
            assert alerts_page.current_url.endswith("/alerts")

    @allure.story("Alerts page")
    @allure.title("Alerts controls are visible")
    @allure.description("Verifies that all alert controls are displayed on the Alerts page.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_alert_controls_visible(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Verify Simple Alert button is visible"):
            assert page.simple_alert_visible()

        with allure.step("Verify Timer Alert button is visible"):
            assert page.timer_alert_visible()

        with allure.step("Verify Confirm Alert button is visible"):
            assert page.confirm_alert_visible()

        with allure.step("Verify Prompt Alert button is visible"):
            assert page.prompt_alert_visible()

    @allure.story("Simple Alert")
    @allure.title("Simple alert opens with expected message")
    @allure.description("Verifies that clicking the Simple Alert button opens a browser alert containing the expected message.")
    @pytest.mark.positive
    def test_simple_alert_text(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Simple Alert"):
            page.open_simple_alert()

        with allure.step("Get Simple Alert text"):
            alert_text = page.current_alert_text()

        with allure.step("Verify Simple Alert text"):
            assert alert_text == "You clicked a button"

        with allure.step("Accept Simple Alert"):
            page.accept_current_alert()

    @allure.story("Simple Alert")
    @allure.title("Simple alert can be accepted")
    @allure.description("Verifies that the Simple Alert can be successfully accepted.")
    @pytest.mark.positive
    def test_accept_simple_alert(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Simple Alert"):
            page.open_simple_alert()

        with allure.step("Accept Simple Alert"):
            page.accept_current_alert()

        with allure.step("Verify Alerts page remains available"):
            assert page.simple_alert_visible()

    @allure.story("Timer Alert")
    @allure.title("Timer Alert appears with expected message")
    @allure.description("Verifies that the Timer Alert appears after the configured delay and contains the expected message.")
    @pytest.mark.positive
    def test_timer_alert_text(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Timer Alert"):
            page.open_timer_alert()

        with allure.step("Open Timer Alert text"):
            alert_text = page.current_alert_text()

        with allure.step("Verify Timer Alert text"):
            assert alert_text == "This alert appeared after 5 seconds"

        with allure.step("Accept Timer Alert"):
            page.accept_current_alert()

    @allure.story("Confirm Alert")
    @allure.title("Confirm Alert opens with expected message")
    @allure.description("Verifies that the Confirm Alert opens with the expected message.")
    @pytest.mark.positive
    def test_confirm_alert_text(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Confirm Alert"):
            page.open_confirm_alert()

        with allure.step("Open Confirm Alert text"):
            alert_text = page.current_alert_text()

        with allure.step("Verify Confirm Alert text"):
            assert alert_text == "Do you confirm action?"

        with allure.step("Accept Confirm Alert"):
            page.accept_current_alert()

    @allure.story("Confirm Alert")
    @allure.title("Accepting confirm alert displays success result")
    @allure.description("Verifies that accepting the Confirm Alert displays the expected confirmation result.")
    @pytest.mark.positive
    def test_accept_confirm_alert(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Confirm Alert"):
            page.open_confirm_alert()
        
        with allure.step("Accept Confirm Alert"):
            page.accept_current_alert()

        with allure.step("Verify confirmation result is visible"):
            assert page.confirm_result_visible()

        with allure.step("Verify confirmation result text"):
            assert page.confirm_result_text() == "You selected Ok"

    @allure.story("Confirm Alert")
    @allure.title("Dismissing confirm alert displays cancellation result")
    @allure.description("Verifies that dismissing the Confirm Alert displays the expected cancellation result.")
    @pytest.mark.positive
    def test_dismiss_confirm_alert(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Confirm Alert"):
            page.open_confirm_alert()

        with allure.step("Dismiss Confirm Alert"):
            page.dismiss_current_alert()

        with allure.step("Verify confirmation result is visible"):
            assert page.confirm_result_visible()

        with allure.step("Verify cancellation result text"):
            assert page.confirm_result_text() == "You selected Cancel"

    @allure.story("Prompt Alert")
    @allure.title("Prompt alert opens with expected message")
    @allure.description("Verifies that the Prompt Alert opens with the expected message.")
    @pytest.mark.positive
    def test_prompt_alert_text(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Prompt Alert"):
            page.open_prompt_alert()

        with allure.step("Get Prompt Alert text"):
            alert_text = page.current_alert_text()

        with allure.step("Verify Prompt Alert text"):
            assert alert_text == "Please enter your name"

        with allure.step("Accept Prompt Alert"):
            page.accept_current_alert()

    @allure.story("Prompt Alert")
    @allure.title("Prompt alert can be dismissed")
    @allure.description("Verifies that the Prompt Alert can be dismissed successfully.")
    @pytest.mark.positive
    def test_dismiss_prompt_alert(self, driver):
        home_page = HomePage(driver)
        alerts_page = AlertsPage(driver)
        page = AlertsFramesPage(driver)

        with allure.step("Open Alerts page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_page.open_alerts()

        with allure.step("Open Prompt Alert"):
            page.open_prompt_alert()

        with allure.step("Dismiss Prompt Alert"):
            page.dismiss_current_alert()

        with allure.step("Verify Prompt Alert result is not displayed"):
            assert page.prompt_result_visible() is False
        