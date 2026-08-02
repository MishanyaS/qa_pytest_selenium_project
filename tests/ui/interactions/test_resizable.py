from __future__ import annotations

import allure
import pytest

from pages.interactions_page import InteractionsPage
from pages.home_page import HomePage
from pages.resizable_page import ResizablePage

@allure.epic("DemoQA UI")
@allure.feature("Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestResizable:
    @allure.story("Resizable navigation")
    @allure.title("Resizable page opens successfully")
    @allure.description("Verifies that the Resizable page can be opened successfully from the Interactions section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_resizable(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        resizable_page = ResizablePage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Interactions section"):
            home_page.open_interactions()

        with allure.step("Open Resizable page"):
            interactions_page.open_resizable()

        with allure.step("Verify Resizable page URL"):
            assert resizable_page.current_url.endswith("/resizable")

    @allure.story("Resizable page")
    @allure.title("Resizable handle is displayed")
    @allure.description("Verifies that the resize handle is visible.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_resizable_handle_visible(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = ResizablePage(driver)

        with allure.step("Open Resizable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_resizable()

        with allure.step("Verify resize handle is visible"):
            assert page.resizable_handle_visible()

    @allure.story("Resizable element")
    @allure.title("Resizable element has default size")
    @allure.description("Verifies that the resizeable element has the expected default dimension.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_resizable_default_size(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = ResizablePage(driver)

        with allure.step("Open Resizable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_resizable()

        with allure.step("Verify default size"):
            assert page.resizable_size() == (200, 200)

    @allure.story("Resizable element")
    @allure.title("Resizable width has default value")
    @allure.description("Verifies that the resizeable element has the expected default width.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_resizable_default_width(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = ResizablePage(driver)

        with allure.step("Open Resizable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_resizable()

        with allure.step("Verify default width"):
            assert page.resizable_width() == 200

    @allure.story("Resizable element")
    @allure.title("Resizable height has default value")
    @allure.description("Verifies that the resizeable element has the expected default height.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_resizable_default_height(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = ResizablePage(driver)

        with allure.step("Open Resizable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_resizable()

        with allure.step("Verify default height"):
            assert page.resizable_height() == 200

    @allure.story("Resizable element")
    @allure.title("Resizable element size changes after resize")
    @allure.description("Verifies that resizing the element changes its dimensions.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_resize_element(self, driver):
        home_page = HomePage(driver)
        interactions_page = InteractionsPage(driver)
        page = ResizablePage(driver)

        with allure.step("Open Resizable page"):
            home_page.open()
            home_page.open_interactions()
            interactions_page.open_resizable()

        with allure.step("Save initial size"):
            initial_width, initial_height = page.resizable_size()

        with allure.step("Resize element"):
            page.resize_element(100, 50)

        with allure.step("Verify size changed"):
            width, height = page.resizable_size()

            assert width > initial_width
            assert height > initial_height
