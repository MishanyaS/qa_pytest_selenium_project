from __future__ import annotations

import allure
import pytest

from pages.interactions_page import InteractionsPage
from pages.home_page import HomePage
from pages.draggable_page import DraggablePage

@allure.epic("DemoQA UI")
@allure.feature("Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestDraggable:
    @allure.story("Draggable navigation")
    @allure.title("Draggable page opens successfully")
    @allure.description("Verifies that the Draggable page can be opened successfully from the Interactions section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_draggable(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        draggable_page = DraggablePage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Interactions section"):
            home_page.open_interactions()

        with allure.step("Open Draggable page"):
            interactions_page.open_draggable()

        with allure.step("Verify Draggable page URL"):
            assert draggable_page.current_url.endswith("/dragabble")

    @allure.story("Draggable element")
    @allure.title("Draggable element is displayed")
    @allure.description("Verifies that the draggable element is visible.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_draggable_visible(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DraggablePage(driver)

        with allure.step("Open Draggable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_draggable()

        with allure.step("Verify draggable is visible"):
            assert page.draggable_visible()

    @allure.story("Draggable element")
    @allure.title("Draggable element is enabled")
    @allure.description("Verifies that the draggable element is enabled.")
    @pytest.mark.positive
    def test_draggable_enabled(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DraggablePage(driver)

        with allure.step("Open Draggable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_draggable()

        with allure.step("Verify draggable is enabled"):
            assert page.draggable_enabled()

    @allure.story("Draggable element")
    @allure.title("Draggable text is correct")
    @allure.description("Verifies that the draggable element contains the expected text.")
    @pytest.mark.positive
    def test_draggable_text(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DraggablePage(driver)

        with allure.step("Open Draggable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_draggable()

        with allure.step("Verify draggable text"):
            assert page.draggable_text() == "Drag me"

    @allure.story("Drag")
    @allure.title("Draggable position changes after dragging")
    @allure.description("Verifies that the draggable element changes its position after being dragged.")
    @pytest.mark.positive
    def test_drag_changes_position(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DraggablePage(driver)

        with allure.step("Open Draggable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_draggable()

        with allure.step("Remember initial position"):
            initial_position = page.draggable_position()

        with allure.step("Drag element"):
            page.drag(120, 80)

        with allure.step("Verify position changed"):
            assert page.draggable_position() != initial_position

    @allure.story("Drag")
    @allure.title("Draggable X coordinate changes")
    @allure.description("Verifies that the X coordinate changes after dragging.")
    @pytest.mark.positive
    def test_drag_changes_x(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DraggablePage(driver)

        with allure.step("Open Draggable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_draggable()

        with allure.step("Remember initial X"):
            initial_x = page.draggable_x()

        with allure.step("Drag element horizontally"):
            page.drag(100, 0)

        with allure.step("Verify X changed"):
            assert page.draggable_x() != initial_x

    @allure.story("Drag")
    @allure.title("Draggable Y coordinate changes")
    @allure.description("Verifies that the Y coordinate changes after dragging.")
    @pytest.mark.positive
    def test_drag_changes_y(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = DraggablePage(driver)

        with allure.step("Open Draggable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_draggable()

        with allure.step("Remember initial Y"):
            initial_y = page.draggable_y()

        with allure.step("Drag element vertically"):
            page.drag(0, 100)

        with allure.step("Verify Y changed"):
            assert page.draggable_y() != initial_y
