from __future__ import annotations

import allure
import pytest

from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.widgets_page import WidgetsPage


@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestMenu:
    @allure.story("Menu navigation")
    @allure.title("Menu page opens successfully")
    @allure.description(
        "Verifies that the Menu page can be opened successfully from the Widgets section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_menu(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        menu_page = MenuPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Menu page"):
            widgets_page.open_menu()

        with allure.step("Verify Menu page URL"):
            assert menu_page.current_url.endswith("/menu")

    @allure.story("Menu page")
    @allure.title("Main menu items are visible")
    @allure.description("Verifies that all top-level menu items are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_menu_items_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = MenuPage(driver)

        with allure.step("Open Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_menu()

        with allure.step("Verify menu is visible"):
            assert page.menu_visible()

        with allure.step("Verify Main Item 1 is visible"):
            assert page.home_item_visible()

        with allure.step("Verify Main Item 2 is visible"):
            assert page.main_item_2_visible()

        with allure.step("Verify Main Item 3 is visible"):
            assert page.main_item_3_visible()

    @allure.story("Menu")
    @allure.title("Main menu item texts are correct")
    @allure.description("Verifies the text of the top-level menu items.")
    @pytest.mark.positive
    def test_main_menu_item_texts(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = MenuPage(driver)

        with allure.step("Open Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_menu()

        with allure.step("Verify Main Item 1 text"):
            assert page.home_item_text() == "Main Item 1"

        with allure.step("Verify Main Item 2 text"):
            assert page.main_item_2_text() == "Main Item 2"

        with allure.step("Verify Main Item 3 text"):
            assert page.main_item_3_text() == "Main Item 3"

    @allure.story("Menu")
    @allure.title("Sub menu becomes visible")
    @allure.description("Verifies that hovering over Main Item 2 displays its submenu.")
    @pytest.mark.positive
    def test_sub_menu_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = MenuPage(driver)

        with allure.step("Open Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_menu()

        with allure.step("Hover over Main Item 2"):
            page.hover_main_item_2()

        with allure.step("Verify SUB SUB LIST is visible"):
            assert page.sub_sub_list_visible()

    @allure.story("Menu")
    @allure.title("Nested submenu becomes visible")
    @allure.description(
        "Verifies that hovering over SUB SUB LIST displays nested items."
    )
    @pytest.mark.positive
    def test_nested_sub_menu_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = MenuPage(driver)

        with allure.step("Open Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_menu()

        with allure.step("Hover over Main Item 2"):
            page.hover_main_item_2()

        with allure.step("Hover over SUB SUB LIST"):
            page.hover_sub_sub_list()

        with allure.step("Verify Sub Sub Item 1 is visible"):
            assert page.sub_sub_item_1_visible()

        with allure.step("Verify Sub Sub Item 2 is visible"):
            assert page.sub_sub_item_2_visible()

    @allure.story("Menu")
    @allure.title("Nested submenu item texts are correct")
    @allure.description("Verifies the text of nested submenu items.")
    @pytest.mark.positive
    def test_nested_sub_menu_item_texts(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = MenuPage(driver)

        with allure.step("Open Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_menu()

        with allure.step("Hover over Main Item 2"):
            page.hover_main_item_2()

        with allure.step("Hover over SUB SUB LIST"):
            page.hover_sub_sub_list()

        with allure.step("Verify SUB SUB LIST text"):
            assert page.sub_sub_list_text() == "SUB SUB LIST"

        with allure.step("Verify Sub Sub Item 1 text"):
            assert page.sub_sub_item_1_text() == "Sub Sub Item 1"

        with allure.step("Verify Sub Sub Item 2 text"):
            assert page.sub_sub_item_2_text() == "Sub Sub Item 2"

    @allure.story("Menu")
    @allure.title("Main Item 2 is enabled")
    @allure.description("Verifies that Main Item 2 is enabled.")
    @pytest.mark.positive
    def test_main_item_2_enabled(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = MenuPage(driver)

        with allure.step("Open Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_menu()

        with allure.step("Verify Main Item 2 is enabled"):
            assert page.is_enabled(page.MAIN_ITEM_2)

    @allure.story("Menu")
    @allure.title("Sub Sub Item 1 is enabled")
    @allure.description(
        "Verifies that Sub Sub Item 1 is enabled after opening the nested menu."
    )
    @pytest.mark.positive
    def test_sub_sub_item_1_enabled(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = MenuPage(driver)

        with allure.step("Open Menu page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_menu()

        with allure.step("Hover over Main Item 2"):
            page.hover_main_item_2()

        with allure.step("Hover over SUB SUB LIST"):
            page.hover_sub_sub_list()

        with allure.step("Verify Sub Sub Item 1 is enabled"):
            assert page.is_enabled(page.SUB_SUB_ITEM_1)
