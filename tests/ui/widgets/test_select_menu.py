from __future__ import annotations

import allure
import pytest

from pages.widgets_page import WidgetsPage
from pages.home_page import HomePage
from pages.select_menu_page import SelectMenuPage

@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestSelectMenu:
    @allure.story("Select Menu navigation")
    @allure.title("Select Menu page opens successfully")
    @allure.description("Verifies that the Select Menu page can be opened successfully from the Widgets section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_select_menu(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        select_menu_page = SelectMenuPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Select Menu page"):
            widgets_page.open_select_menu()

        with allure.step("Verify Select Menu page URL"):
            assert select_menu_page.current_url.endswith("/select-menu")

    @allure.story("Select Menu page")
    @allure.title("All select controls are displayed")
    @allure.description("Verifies that all select controls are displayed on the page.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_select_controls_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Verify Select Value is visible"):
            assert page.select_value_visible()

        with allure.step("Verify Select One is visible"):
            assert page.select_one_visible()

        with allure.step("Verify Old Style Select Menu is visible"):
            assert page.old_style_select_visible()

        with allure.step("Verify Multi Select is visible"):
            assert page.multi_select_visible()

    @allure.story("Select Menu")
    @allure.title("Old Style Select Menu selection works")
    @allure.description("Verifies that an option can be selected from the old style select menu.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_old_style_select(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Select Purple"):
            page.select_old_style("Purple")

        with allure.step("Verify selected value"):
            assert page.selected_value(page.OLD_STYLE_SELECT) == "4"

    @allure.story("Select Menu")
    @allure.title("Old Style Select Menu selection by value works")
    @allure.description("Verifies that an option can be selected by value.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_old_style_select_by_value(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Select Blue by value"):
            page.select_old_style_by_value("1")

        with allure.step("Verify selected value"):
            assert page.selected_value(page.OLD_STYLE_SELECT) == "1"

    @allure.story("Select Menu")
    @allure.title("Old Style Select Menu selection by index works")
    @allure.description("Verifies that an option can be selected by index.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_old_style_select_by_index(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Select Blue by index"):
            page.select_old_style_by_index(4)

        with allure.step("Verify selected index"):
            assert page.selected_value(page.OLD_STYLE_SELECT) == "4"

    @allure.story("React Select")
    @allure.title("React Select options are displayed")
    @allure.description("Verifies that opening the React Select displays available options.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_react_select_options_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Open React Select"):
            page.open_react_select()

        with allure.step("Verify options are visible"):
            assert page.react_options_visible()

    @allure.story("React Select")
    @allure.title("React Select option can be selected")
    @allure.description("Verifies that an option can be selected from React Select.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_react_select_option(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Select Group 1, option 1"):
            page.select_react_option_by_text("Group 1, option 1")

        with allure.step("Verify selected option"):
            assert page.selected_react_option() == "Group 1, option 1"

    @allure.story("React Select")
    @allure.title("React Select option can be selected")
    @allure.description("Verifies that the selected React option is visible.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_react_select_option_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Select Group 2, option 1"):
            page.select_react_option_by_text("Group 2, option 1")

        with allure.step("Verify selected option is visible"):
            assert page.selected_react_option_visible()

    @allure.story("Multi Select")
    @allure.title("Standard multi select works")
    @allure.description("Verifies that an option can be selected in the standard multi select.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_multi_select_option(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SelectMenuPage(driver)

        with allure.step("Open Select Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_select_menu()

        with allure.step("Select Volvo"):
            page.select_multiple("Volvo")

        with allure.step("Verify selected value"):
            assert page.selected_value(page.MULTI_SELECT) == "volvo"
        