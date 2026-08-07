from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.droppable_page import DroppablePage
from pages.home_page import HomePage
from pages.interactions_page import InteractionsPage


@allure.epic("DemoQA UI")
@allure.feature("Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestDroppable:
    @allure.story("Droppable navigation")
    @allure.title("Droppable page opens successfully")
    @allure.description(
        "Verifies that the Droppable page can be opened successfully from the Interactions section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_droppable(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        droppable_page = DroppablePage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Interactions section"):
            home_page.open_interactions()

        with allure.step("Open Droppable page"):
            interactions_page.open_droppable()

        with allure.step("Verify Droppable page URL"):
            assert droppable_page.current_url.endswith("/droppable")

    @allure.story("Draggable element")
    @allure.title("Draggable element is displayed")
    @allure.description("Verifies that the draggable element is visible.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_draggable_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DroppablePage(driver)

        with allure.step("Open Droppable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_droppable()

        with allure.step("Verify draggable is visible"):
            assert page.draggable_visible()

    @allure.story("Droppable area")
    @allure.title("Droppable area is displayed")
    @allure.description("Verifies that the droppable area is visible.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_droppable_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DroppablePage(driver)

        with allure.step("Open Droppable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_droppable()

        with allure.step("Verify droppable is visible"):
            assert page.droppable_visible()

    @allure.story("Draggable element")
    @allure.title("Draggable element is enabled")
    @allure.description("Verifies that the draggable element is enabled.")
    @pytest.mark.positive
    def test_draggable_enabled(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DroppablePage(driver)

        with allure.step("Open Droppable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_droppable()

        with allure.step("Verify draggable is enabled"):
            assert page.draggable_enabled()

    @allure.story("Droppable area")
    @allure.title("Droppable area is enabled")
    @allure.description("Verifies that the droppable area is enabled.")
    @pytest.mark.positive
    def test_droppable_enabled(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DroppablePage(driver)

        with allure.step("Open Droppable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_droppable()

        with allure.step("Verify droppable is enabled"):
            assert page.droppable_enabled()

    @allure.story("Drag and Drop")
    @allure.title("Element can be dropped")
    @allure.description("Verifies that dragging the element to the drop area succeeds.")
    @pytest.mark.positive
    def test_drag_and_drop(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DroppablePage(driver)

        with allure.step("Open Droppable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_droppable()

        with allure.step("Drag element into drop area"):
            page.drag_to_drop()

        with allure.step("Verify drop completed"):
            assert page.dropped()

    @allure.story("Drag and Drop")
    @allure.title("Droppable text changes after drop")
    @allure.description(
        "Verifies that the drop area text changes after a successful drop."
    )
    @pytest.mark.positive
    def test_droppable_text_after_drop(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DroppablePage(driver)

        with allure.step("Open Droppable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_droppable()

        with allure.step("Drag element into drop area"):
            page.drag_to_drop()

        with allure.step("Verify droppable text"):
            assert page.droppable_text() == "Dropped!"

    @allure.story("Drag and Drop")
    @allure.title("Droppable text is correct")
    @allure.description(
        "Verifies that the draggable element displays the expected text before dragging."
    )
    @pytest.mark.positive
    def test_draggable_text(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DroppablePage(driver)

        with allure.step("Open Droppable page"):
            home_page.open_home_page()
            home_page.open_interactions()
            interactions_page.open_droppable()

        with allure.step("Verify draggable text"):
            assert page.draggable_text() == "Drag Me"
