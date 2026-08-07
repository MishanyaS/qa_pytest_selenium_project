from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.interactions_page import InteractionsPage
from pages.selectable_page import SelectablePage


@allure.epic("DemoQA UI")
@allure.feature("Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestSelectable:
    @allure.story("Selectable navigation")
    @allure.title("Selectable page opens successfully")
    @allure.description(
        "Verifies that the Selectable page can be opened successfully from the Interactions section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_selectable(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        selectable_page = SelectablePage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Interactions section"):
            home_page.open_interactions()

        with allure.step("Open Selectable page"):
            interactions_page.open_selectable()

        with allure.step("Verify Selectable page URL"):
            assert selectable_page.current_url.endswith("/selectable")

    @allure.story("Selectable page")
    @allure.title("Selectable items are displayed")
    @allure.description("Verifies that all selectable items are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_selectable_items_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SelectablePage(driver)

        with allure.step("Open Selectable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_selectable()

        with allure.step("Verify items are visible"):
            assert page.selectable_items_visible()

        with allure.step("Verify items count"):
            assert page.selectable_items_count() == 4

    @allure.story("Selectable items")
    @allure.title("Selectable items have correct names")
    @allure.description("Verifies that selectable items contain expected text.")
    @pytest.mark.positive
    def test_selectable_items_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SelectablePage(driver)

        expected = [
            "Cras justo odio",
            "Dapibus ac facilisis in",
            "Morbi leo risus",
            "Porta ac consectetur ac",
        ]

        with allure.step("Open Selectable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_selectable()

        with allure.step("Verify items text"):
            assert page.selectable_items() == expected

    @allure.story("Selectable items")
    @allure.title("Selectable item can be selected")
    @allure.description("Verifies that a selectable item can be selected.")
    @pytest.mark.positive
    def test_select_item(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SelectablePage(driver)

        with allure.step("Open Selectable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_selectable()

        with allure.step("Select third item"):
            page.select_item(3)

        with allure.step("Verify third item selected"):
            assert page.item_selected(3)

    @allure.story("Selectable items")
    @allure.title("Selectable item count is correct")
    @allure.description("Verifies that one selected item is reported.")
    @pytest.mark.positive
    def test_selected_items_count(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SelectablePage(driver)

        with allure.step("Open Selectable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_selectable()

        with allure.step("Select first item"):
            page.select_item(1)

        with allure.step("Verify selected count"):
            assert page.selected_items_count() == 1

    @allure.story("Selectable items")
    @allure.title("Selectable item text correct")
    @allure.description("Verifies that the selected item text is returned.")
    @pytest.mark.positive
    def test_selected_items_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SelectablePage(driver)

        with allure.step("Open Selectable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_selectable()

        with allure.step("Select second item"):
            page.select_item(2)

        with allure.step("Verify selected text"):
            assert page.selected_items() == ["Dapibus ac facilisis in"]

    @allure.story("Selectable items")
    @allure.title("Selection can be cleared")
    @allure.description("Verifies that selected items can be unselected.")
    @pytest.mark.positive
    def test_clear_selection(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SelectablePage(driver)

        with allure.step("Open Selectable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_selectable()

        with allure.step("Select first item"):
            page.select_item(1)

        with allure.step("Clear selection"):
            page.clear_selection()

        with allure.step("Verify no selected items"):
            assert page.selected_items_count() == 0
