from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.interactions_page import InteractionsPage
from pages.sortable_page import SortablePage


@allure.epic("DemoQA UI")
@allure.feature("Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestSortable:
    @allure.story("Sortable navigation")
    @allure.title("Sortable page opens successfully")
    @allure.description(
        "Verifies that the Sortable page can be opened successfully from the Interactions section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_sortable(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        sortable_page = SortablePage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Interactions section"):
            home_page.open_interactions()

        with allure.step("Open Sortable page"):
            interactions_page.open_sortable()

        with allure.step("Verify Sortable page URL"):
            assert sortable_page.current_url.endswith("/sortable")

    @allure.story("Sortable page")
    @allure.title("Sortable items are displayed")
    @allure.description("Verifies that all sortable items are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_sortable_items_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SortablePage(driver)

        with allure.step("Open Sortable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_sortable()

        with allure.step("Verify items are visible"):
            assert page.sortable_items_visible()

        with allure.step("Verify items count"):
            assert page.sortable_items_count() == 6

    @allure.story("Sortable items")
    @allure.title("Sortable items have correct names")
    @allure.description("Verifies that sortable items contain expected text.")
    @pytest.mark.positive
    def test_sortable_items_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SortablePage(driver)

        expected = ["One", "Two", "Three", "Four", "Five", "Six"]

        with allure.step("Open Sortable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_sortable()

        with allure.step("Verify items text"):
            assert page.sortable_items() == expected

    @allure.story("Sortable items")
    @allure.title("Sortable item text is correct")
    @allure.description(
        "Verifies that the specified sortable item contains the expected text."
    )
    @pytest.mark.positive
    def test_sortable_item_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SortablePage(driver)

        with allure.step("Open Sortable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_sortable()

        with allure.step("Verify third item text"):
            assert page.sortable_item_text(3) == "Three"

    @allure.story("Sortable items")
    @allure.title("Sortable item can be reordered")
    @allure.description(
        "Verifies that dragging one sortable item onto another changes the order."
    )
    @pytest.mark.positive
    def test_drag_sortable_item(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SortablePage(driver)

        with allure.step("Open Sortable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_sortable()

        with allure.step("Drag first item to third position"):
            page.drag_item(1, 3)

        with allure.step("Verify third item text"):
            assert page.sortable_items() != [
                "One",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
            ]

    @allure.story("Sortable items")
    @allure.title("Sortable items can be reordered using locators")
    @allure.description(
        "Verifies that sortable items can be reordered using locator arguments."
    )
    @pytest.mark.positive
    def test_drag_sortable_item_by_locator(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = SortablePage(driver)

        with allure.step("Open Sortable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_sortable()

        with allure.step("Drag first item to sixth position"):
            page.drag_item_by_locator(
                interactions_page.SORTABLE_ITEM_1, interactions_page.SORTABLE_ITEM_6
            )

        with allure.step("Verify order changed"):
            assert page.sortable_items() != [
                "One",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
            ]
