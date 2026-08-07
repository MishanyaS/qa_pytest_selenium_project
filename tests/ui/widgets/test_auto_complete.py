from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.auto_complete_page import AutoCompletePage
from pages.home_page import HomePage
from pages.widgets_page import WidgetsPage


@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestAutoComplete:
    @allure.story("Auto Complete navigation")
    @allure.title("Auto Complete page opens successfully")
    @allure.description(
        "Verifies that the Auto Complete page can be opened successfully from the Widgets section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_auto_complete(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        auto_complete_page = AutoCompletePage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Auto Complete page"):
            widgets_page.open_auto_complete()

        with allure.step("Verify Auto Complete page URL"):
            assert auto_complete_page.current_url.endswith("/auto-complete")

    @allure.story("Auto Complete page")
    @allure.title("Auto Complete input fields are visible")
    @allure.description(
        "Verifies that both Single Value and Multiple Values Auto Complete input fields are displayed."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_auto_complete_input_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Verify Single Value input is visible"):
            assert page.single_value_input_visible()

        with allure.step("Verify Multiple Values input is visible"):
            assert page.multiple_value_input_visible()

    @allure.story("Single Value Auto Complete")
    @allure.title("Single Value input accepts text")
    @allure.description(
        "Verifies that text can be entered into the Single Value Auto Complete input."
    )
    @pytest.mark.positive
    def test_enter_single_value(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        value = "Red"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Enter value into Single Value input"):
            page.enter_single_value(value)

        with allure.step("Verify entered value"):
            assert page.single_value_input_value() == value

    @allure.story("Multiple Value Auto Complete")
    @allure.title("Multiple Values input accepts text")
    @allure.description(
        "Verifies that text can be entered into the Multiple Values Auto Complete input."
    )
    @pytest.mark.positive
    def test_enter_multiple_value(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        value = "Red"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Enter value into Multiple Value input"):
            page.enter_multiple_value(value)

        with allure.step("Verify entered value"):
            assert page.multiple_value_input_value() == value

    @allure.story("Auto Complete suggestions")
    @allure.title("Suggestions are displayed after entering a value")
    @allure.description(
        "Verifies that Auto Complete suggestions are displayed after entering a color value."
    )
    @pytest.mark.positive
    def test_options_are_displayed(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        value = "Red"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Enter value into Single Value input"):
            page.enter_single_value(value)

        with allure.step("Verify suggestions are displayed"):
            assert page.options_visible()

        with allure.step("Verify matching option is displayed"):
            assert value in page.options()

    @allure.story("Single Value Auto Complete")
    @allure.title("Single Value can be selected")
    @allure.description(
        "Verifies that a color can be selected from the Single Value Auto Complete suggestions."
    )
    @pytest.mark.positive
    def test_select_single_value(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        value = "Red"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Select Single Value"):
            page.select_single_value(value)

        with allure.step("Verify selected value is visible"):
            assert page.selected_single_value_visible()

        with allure.step("Verify selected value"):
            assert page.selected_single_value() == value

    @allure.story("Multiple Values Auto Complete")
    @allure.title("Multiple values can be selected")
    @allure.description(
        "Verifies that a color can be selected from the Multiple Values Auto Complete suggestions."
    )
    @pytest.mark.positive
    def test_select_multiple_values(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        first_value = "Red"
        second_value = "Blue"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Select first value"):
            page.select_multiple_value(first_value)

        with allure.step("Select second value"):
            page.select_multiple_value(second_value)

        with allure.step("Verify selected values are visible"):
            assert page.selected_multiple_value_visible()

        with allure.step("Verify selected values"):
            selected_values = page.selected_multiple_value()

            assert first_value in selected_values
            assert second_value in selected_values

    @allure.story("Multiple Values Auto Complete")
    @allure.title("Selected multiple value can be removed")
    @allure.description(
        "Verifies that a selected color can be removed from the Multiple Values Auto Complete field."
    )
    @pytest.mark.positive
    def test_remove_multiple_value(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        first_value = "Red"
        second_value = "Blue"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Select first value"):
            page.select_multiple_value(first_value)

        with allure.step("Select second value"):
            page.select_multiple_value(second_value)

        with allure.step("Remove first selected value"):
            page.remove_multiple_value(first_value)

        with allure.step("Verify removed value is absent"):
            selected_values = page.selected_multiple_value()

            assert first_value not in selected_values

        with allure.step("Verify second value remains selected"):
            assert second_value in selected_values

    @allure.story("Single Value Auto Complete")
    @allure.title("Single Value input can be cleared")
    @allure.description(
        "Verifies that the Single Value Auto Complete input can be cleared."
    )
    @pytest.mark.positive
    def test_clear_single_value(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        value = "Red"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Enter value"):
            page.enter_single_value(value)

        with allure.step("Clear Single Value input"):
            page.clear_single_value()

        with allure.step("Verify input is empty"):
            assert page.single_value_input_value() == ""

    @allure.story("Multiple Values Auto Complete")
    @allure.title("Multiple Values input can be cleared")
    @allure.description(
        "Verifies that the Multiple Values Auto Complete input can be cleared."
    )
    @pytest.mark.positive
    def test_clear_multiple_value_input(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = AutoCompletePage(driver)

        value = "Red"

        with allure.step("Open Auto Complete page"):
            home_page.open_home_page()
            home_page.open_widgets()
            widgets_page.open_auto_complete()

        with allure.step("Enter value"):
            page.enter_multiple_value(value)

        with allure.step("Clear Multiple Values input"):
            page.clear_multiple_value_input()

        with allure.step("Verify input is empty"):
            assert page.multiple_value_input_value() == ""
