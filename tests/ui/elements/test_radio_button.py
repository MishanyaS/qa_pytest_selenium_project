from __future__ import annotations

import allure
import pytest
from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.radio_button_page import RadioButtonPage


@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestRadioButton:
    @allure.story("Radio Button navigation")
    @allure.title("Radio Button page opens successfully")
    @allure.description(
        "Verifies that the Radio Button page can be opened from the Elements section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_radio_button(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        radio_button_page = RadioButtonPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Radio Button page"):
            elements_page.open_radio_button()

        with allure.step("Verify Text Box page URL"):
            assert radio_button_page.current_url.endswith("/radio-button")

    @allure.story("Radio Button page")
    @allure.title("Radio Button elements are visible")
    @allure.description(
        "Verifies that the main Radio Button elements are displayed when the page is opened."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_radio_button_elements_visible(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Verify Yes radio button is visible"):
            assert page.is_visible(page.YES_RADIO)

        with allure.step("Verify Impressive radio button is visible"):
            assert page.is_visible(page.IMPRESSIVE_RADIO)

        with allure.step("Verify No radio button is visible"):
            assert page.is_visible(page.NO_RADIO)

    @allure.story("Radio Button initial state")
    @allure.title("No radio button is selected initially")
    @allure.description(
        "Verifies that no radio button is selected when the Radio Button page is opened."
    )
    @pytest.mark.positive
    def test_no_radio_button_selected_initially(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Verify Yes radio button is not selected"):
            assert page.yes_selected() is False

        with allure.step("Verify Impressive radio button is not selected"):
            assert page.impressive_selected() is False

        with allure.step("Verify No radio button is not selected"):
            assert page.no_selected() is False

        with allure.step("Verify result is not visible"):
            assert page.result_visible() is False

    @allure.story("Radio Button initial state")
    @allure.title("No radio button is disabled")
    @allure.description(
        "Verifies that the No radio button is disabled and cannot be selected."
    )
    @pytest.mark.positive
    def test_no_radio_button_is_disabled(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Verify No radio button is disabled"):
            no_radio = page.wait_present((By.ID, "noRadio"))

            assert no_radio.is_enabled() is False

    @allure.story("Radio Button selection")
    @allure.title("Yes radio button can be selected")
    @allure.description(
        "Verifies that the Yes radio button can be selected and the correct result is displayed."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_select_yes(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Select Yes radio button"):
            page.select_yes()

        with allure.step("Verify Yes radio button is selected"):
            assert page.yes_selected() is True

        with allure.step("Verify Impressive radio button is not selected"):
            assert page.impressive_selected() is False

        with allure.step("Verify result is visible"):
            assert page.result_visible() is True

        with allure.step("Verify result text"):
            assert page.result_text() == "Yes"

    @allure.story("Radio Button selection")
    @allure.title("Impressive radio button can be selected")
    @allure.description(
        "Verifies that the Impressive radio button can be selected and the correct result is displayed."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_select_impressive(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Select Impressive radio button"):
            page.select_impressive()

        with allure.step("Verify Impressive radio button is selected"):
            assert page.impressive_selected() is True

        with allure.step("Verify Yes radio button is not selected"):
            assert page.yes_selected() is False

        with allure.step("Verify result is visible"):
            assert page.result_visible() is True

        with allure.step("Verify result text"):
            assert page.result_text() == "Impressive"

    @allure.story("Radio Button selection")
    @allure.title("Selecting Impressive deselects Yes")
    @allure.description(
        "Verifies the mutual exclusivity of radio buttons by selecting Yes first and then Impressive."
    )
    @pytest.mark.positive
    def test_switch_from_yes_to_impressive(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Select Yes radio button"):
            page.select_yes()

        with allure.step("Verify Yes radio button is selected"):
            assert page.yes_selected() is True

        with allure.step("Select Impressive radio button"):
            page.select_impressive()

        with allure.step("Verify Yes is deselected"):
            assert page.yes_selected() is False

        with allure.step("Verify Impressive is selected"):
            assert page.impressive_selected() is True

        with allure.step("Verify result text"):
            assert page.result_text() == "Impressive"

    @allure.story("Radio Button selection")
    @allure.title("Selecting Yes deselects Impressive")
    @allure.description(
        "Verifies the mutual exclusivity of radio buttons by selecting Impressive first and then Yes."
    )
    @pytest.mark.positive
    def test_switch_from_impressive_to_yes(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Select Impressive radio button"):
            page.select_impressive()

        with allure.step("Verify Impressive is selected"):
            assert page.impressive_selected() is True

        with allure.step("Select Yes radio button"):
            page.select_yes()

        with allure.step("Verify Impressive is deselected"):
            assert page.impressive_selected() is False

        with allure.step("Verify Yes is selected"):
            assert page.yes_selected() is True

        with allure.step("Verify result text"):
            assert page.result_text() == "Yes"

    @allure.story("Radio Button selection")
    @allure.title("No radio button cannot be selected")
    @allure.description(
        "Verifies that the disabled No radio button cannot be selected."
    )
    @pytest.mark.negative
    def test_select_no_radio_button(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Verify No radio button is disabled"):
            no_radio = page.wait_present((By.ID, "noRadio"))

            assert no_radio.is_enabled() is False

        with allure.step("Verify No radio button is not disabled"):
            assert page.no_selected() is False

        with allure.step("Verify result is not visible"):
            assert page.result_visible() is False

    @allure.story("Radio Button result")
    @allure.title("Result changes when selected radio button changes")
    @allure.description(
        "Verifies that the displayed result corresponds to the currently selected radio button."
    )
    @pytest.mark.positive
    def test_result_changes_after_switching_radio_buttons(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = RadioButtonPage(driver)

        with allure.step("Open Radio Button page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_radio_button()

        with allure.step("Select Yes radio button"):
            page.select_yes()

        with allure.step("Verify Yes result"):
            assert page.result_text() == "Yes"

        with allure.step("Select Impressive radio button"):
            page.select_impressive()

        with allure.step("Verify Impressive result"):
            assert page.result_text() == "Impressive"

        with allure.step("Verify only Impressive is selected"):
            assert page.impressive_selected() is True
            assert page.yes_selected() is False
