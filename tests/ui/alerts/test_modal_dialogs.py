from __future__ import annotations

import allure
import pytest

from selenium.webdriver.support.ui import WebDriverWait

from pages.alerts_frames_page import AlertsFramesPage
from pages.home_page import HomePage
from pages.modal_dialogs_page import ModalDialogsPage

@allure.epic("DemoQA UI")
@allure.feature("Alerts, Frame & Windows")
@pytest.mark.ui
@pytest.mark.regression
class TestModalDialogs:
    @allure.story("Modal Dialogs navigation")
    @allure.title("Modal Dialogs page opens successfully")
    @allure.description("Verifies that the Modal Dialogs page can be opened successfully from the Alerts, Frame & Windows section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_frames(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        modal_dialogs_page = ModalDialogsPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Alerts, Frame & Windows section"):
            home_page.open_alerts_frame_windows()

        with allure.step("Open Modal Dialogs page"):
            alerts_frames_page.open_modal_dialogs()

        with allure.step("Verify Modal Dialogs page URL"):
            assert modal_dialogs_page.current_url.endswith("/modal-dialogs")

    @allure.story("Modal Dialogs page")
    @allure.title("Modal dialog controls are visible")
    @allure.description("Verifies that both Small Modal and Large Modal buttons are displayed on the Modal Dialogs page.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_modal_dialog_controls_visible(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ModalDialogsPage(driver)

        with allure.step("Open Modal Dialogs page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_modal_dialogs()

        with allure.step("Verify Small Modal button is visible"):
            assert page.small_modal_button_visible()

        with allure.step("Verify Large Modal button is visible"):
            assert page.large_modal_button_visible()

    @allure.story("Small Modal")
    @allure.title("Small Modal opens successfully")
    @allure.description("Verifies that clicking the Small Modal button opens the modal dialog.")
    @pytest.mark.positive
    def test_open_small_modal(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ModalDialogsPage(driver)

        with allure.step("Open Modal Dialogs page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_modal_dialogs()

        with allure.step("Open Small Modal"):
            page.open_small_modal()

        with allure.step("Verify modal is visible"):
            assert page.modal_visible()

        with allure.step("Close Small Modal"):
            page.close_modal()

        with allure.step("Verify modal is closed"):
            WebDriverWait(driver, 10).until(
                lambda _: page.modal_closed()
            )

    @allure.story("Small Modal")
    @allure.title("Small Modal contains expected title and body")
    @allure.description("Verifies that the Small Modal contains the expected title and non-empty body content.")
    @pytest.mark.positive
    def test_small_modal_content(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ModalDialogsPage(driver)

        with allure.step("Open Modal Dialogs page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_modal_dialogs()

        with allure.step("Open Small Modal"):
            page.open_small_modal()

        try:
            with allure.step("Get Small Modal title"):
                title = page.modal_title()

            with allure.step("Get Small Modal body"):
                body = page.modal_body()

            with allure.step("Verify Small Modal title"):
                assert title == "Small Modal"

            with allure.step("Verify Small Modal body is not empty"):
                assert body
        finally:
            with allure.step("Close Small Modal"):
                page.close_modal()

    @allure.story("Large Modal")
    @allure.title("Large Modal opens successfully")
    @allure.description("Verifies that clicking the Large Modal button opens the modal dialog.")
    @pytest.mark.positive
    def test_open_large_modal(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ModalDialogsPage(driver)

        with allure.step("Open Modal Dialogs page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_modal_dialogs()

        with allure.step("Open Large Modal"):
            page.open_large_modal()

        with allure.step("Verify modal is visible"):
            assert page.modal_visible()

        with allure.step("Close Large Modal"):
            page.close_modal()

        with allure.step("Verify modal is closed"):
            WebDriverWait(driver, 10).until(
                lambda _: page.modal_closed()
            )

    @allure.story("Large Modal")
    @allure.title("Large Modal contains expected title and body")
    @allure.description("Verifies that the Large Modal contains the expected title and non-empty body content.")
    @pytest.mark.positive
    def test_large_modal_content(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ModalDialogsPage(driver)

        with allure.step("Open Modal Dialogs page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_modal_dialogs()

        with allure.step("Open Large Modal"):
            page.open_large_modal()

        try:
            with allure.step("Get Large Modal title"):
                title = page.modal_title()

            with allure.step("Get Large Modal body"):
                body = page.modal_body()

            with allure.step("Verify Large Modal title"):
                assert title == "Large Modal"

            with allure.step("Verify Large Modal body is not empty"):
                assert body
        finally:
            with allure.step("Close Large Modal"):
                page.close_modal()

    @allure.story("Modal Dialogs")
    @allure.title("Small and Large Modals contain different content")
    @allure.description("Verifies that the Small Modal and Large Modal provide different dialog content.")
    @pytest.mark.positive
    def test_small_and_large_modal_content_is_different(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = ModalDialogsPage(driver)

        with allure.step("Open Modal Dialogs page"):
            home_page.open()
            home_page.open_alerts_frame_windows()
            alerts_frames_page.open_modal_dialogs()

        with allure.step("Get Small Modal text"):
            small_modal_text = page.open_small_modal_and_get_text()

        with allure.step("Get Large Modal text"):
            large_modal_text = page.open_large_modal_and_get_text()

        with allure.step("Verify modal contents are different"):
            assert small_modal_text
            assert large_modal_text
            assert small_modal_text != large_modal_text
