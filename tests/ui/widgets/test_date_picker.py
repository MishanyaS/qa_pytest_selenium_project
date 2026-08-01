from __future__ import annotations

import allure
import pytest

from pages.widgets_page import WidgetsPage
from pages.home_page import HomePage
from pages.date_picker_page import DatePickerPage

@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestDatePicker:
    @allure.story("Date Picker navigation")
    @allure.title("Date Picker page opens successfully")
    @allure.description("Verifies that the Date Picker page can be opened successfully from the Widgets section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_date_picker(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        date_picker_page = DatePickerPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Date Picker page"):
            widgets_page.open_date_picker()

        with allure.step("Verify Date Picker page URL"):
            assert date_picker_page.current_url.endswith("/date-picker")

    @allure.story("Date Picker page")
    @allure.title("Date Picker inputs are visible")
    @allure.description("Verifies that Date Picker input fields are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_date_picker_inputs_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = DatePickerPage(driver)

        with allure.step("Open Date Picker page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_date_picker()

        with allure.step("Verify Select Date input is visible"):
            assert page.date_input_visible()

        with allure.step("Verify Date and Time input is visible"):
            assert page.date_and_time_input_visible()

    @allure.story("Date Picker")
    @allure.title("Date Picker popup opens")
    @allure.description("Verifies that the standard Date Picker popup opens.")
    @pytest.mark.positive
    def test_open_date_picker_popup(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = DatePickerPage(driver)

        with allure.step("Open Date Picker page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_date_picker()

        with allure.step("Open Date Picker popup"):
            page.open_date_picker()

        with allure.step("Verify popup is visible"):
            assert page.date_picker_visible()

    @allure.story("Date Picker")
    @allure.title("Date and Time Picker popup opens")
    @allure.description("Verifies that the standard Date Picker popup opens.")
    @pytest.mark.positive
    def test_open_date_and_time_picker_popup(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = DatePickerPage(driver)

        with allure.step("Open Date Picker page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_date_picker()

        with allure.step("Open Date and Time Picker popup"):
            page.open_date_and_time_picker()

        with allure.step("Verify popup is visible"):
            assert page.date_and_time_picker_visible()

    @allure.story("Date selection")
    @allure.title("User can select a date")
    @allure.description("Verifies that a date can be selected successfully.")
    @pytest.mark.positive
    def test_select_date(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = DatePickerPage(driver)

        with allure.step("Open Date Picker page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_date_picker()

        with allure.step("Select date"):
            page.select_date_by_month_year(month="July", year="2025", day="15")

        with allure.step("Verify selected date exists"):
            assert page.date_input_value()

    @allure.story("Date and Time selection")
    @allure.title("User can select date and time")
    @allure.description("Verifies that a date and time can be selected successfully.")
    @pytest.mark.positive
    def test_select_date_and_time(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = DatePickerPage(driver)

        with allure.step("Open Date Picker page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_date_picker()

        with allure.step("Select date and time"):
            page.select_date_and_time(month="July", year="2025", day="15", time="12:00")

        with allure.step("Verify date and time were selected"):
            assert page.date_and_time_input_value()

    @allure.story("Time selection")
    @allure.title("Time options are displayed")
    @allure.description("Verifies that time options are available in the picker.")
    @pytest.mark.positive
    def test_time_options_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = DatePickerPage(driver)

        with allure.step("Open Date Picker page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_date_picker()

        with allure.step("Select Date and Time Picker"):
            page.open_date_and_time_picker()

        with allure.step("Verify time options are visible"):
            assert page.time_options_visible()

        with allure.step("Verify time options list is not empty"):
            assert page.time_options()
        