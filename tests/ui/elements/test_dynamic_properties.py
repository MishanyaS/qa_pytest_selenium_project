from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.elements_page import ElementsPage
from pages.home_page import HomePage


@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestDynamicProperties:
    @allure.story("Dynamic Properties navigation")
    @allure.title("Dynamic Properties page opens successfully")
    @allure.description(
        "Verifies that the Dynamic Properties page can be opened from the Elements section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_dynamic_properties(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        dynamic_properties_page = DynamicPropertiesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Dynamic Properties page"):
            elements_page.open_dynamic_properties()

        with allure.step("Verify Dynamic Properties page URL"):
            assert dynamic_properties_page.current_url.endswith("/dynamic-properties")

    @allure.story("Dynamic Properties page")
    @allure.title("Dynamic Properties elements are visible")
    @allure.description(
        "Verifies that all dynamic property controls are visible on the page."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_dynamic_properties_elements_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = DynamicPropertiesPage(driver)

        with allure.step("Open Dynamic Properties page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_dynamic_properties()

        with allure.step("Verify Enable After button is visible"):
            assert page.enable_after_visible()

        with allure.step("Verify Color Change button is visible"):
            assert page.color_change_visible()

        with allure.step("Verify Visible After button is visible"):
            assert page.visible_after_visible()

    @allure.story("Enable After dynamic property")
    @allure.title("Enable After button is initially disabled")
    @allure.description(
        "Verifies that the Enable After button is displayed but disabled immediately after opening the Dynamic Properties page."
    )
    @pytest.mark.positive
    def test_enable_after_button_initially_disabled(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = DynamicPropertiesPage(driver)

        with allure.step("Open Dynamic Properties page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_dynamic_properties()

        with allure.step("Verify Enable After button is visible"):
            assert page.enable_after_visible()

        with allure.step("Verify Enable After button is disabled"):
            assert page.enable_after_enable() is False

    @allure.story("Enable After dynamic property")
    @allure.title("Enable After button becomes enabled")
    @allure.description(
        "Verifies that the Enable After button becomes enabled automatically after the configured delay."
    )
    @pytest.mark.positive
    def test_enable_after_button_becomes_enabled(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = DynamicPropertiesPage(driver)

        with allure.step("Open Dynamic Properties page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_dynamic_properties()

        with allure.step("Verify button is initially disabled"):
            assert page.enable_after_enable() is False

        with allure.step("Wait until Enable After button becomes enabled"):
            assert page.wait_enable_after_enabled() is True

        with allure.step("Verify Enable After button is enabled"):
            assert page.enable_after_enable() is True

    @allure.story("Visible After dynamic property")
    @allure.title("Visible After button is visible")
    @allure.description(
        "Verifies that the Visible After button becomes visible after the configured delay."
    )
    @pytest.mark.positive
    def test_visible_after_button_appears(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = DynamicPropertiesPage(driver)

        with allure.step("Open Dynamic Properties page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_dynamic_properties()

        with allure.step("Verify Visible After button is visible"):
            assert page.visible_after_visible() is True

        with allure.step("Wait until Visible After button is visible"):
            assert page.wait_visible_after_visible() is True

        with allure.step("Verify Visible After button remains visible"):
            assert page.visible_after_visible() is True

    @allure.story("Color Change dynamic property")
    @allure.title("Color Change button has initial primary color")
    @allure.description(
        "Verifies that the Color Change button initially has the primary Bootstrap button class."
    )
    @pytest.mark.positive
    def test_color_change_initial_color(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = DynamicPropertiesPage(driver)

        with allure.step("Open Dynamic Properties page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_dynamic_properties()

        with allure.step("Get initial Color Change button class"):
            class_attribute = page.color_change_attribute("class")

        with allure.step("Verify initial color class"):
            assert class_attribute is not None
            assert "btn-primary" in class_attribute
            assert "btn-success" not in class_attribute

    @allure.story("Color Change dynamic property")
    @allure.title("Color Change button changes color after delay")
    @allure.description(
        "Verifies that the Color Change button changes its computed text color after the configured delay."
    )
    @pytest.mark.positive
    def test_color_change_button_changes_color(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = DynamicPropertiesPage(driver)

        with allure.step("Open Dynamic Properties page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_dynamic_properties()

        with allure.step("Wait for Color Change button to be present"):
            color_change_button = driver.find_element(*page.COLOR_CHANGE_BUTTON)

        with allure.step("Get initial computed color"):
            initial_color = driver.execute_script(
                """
                return window.getComputedStyle(arguments[0]).color;
                """,
                color_change_button,
            )

        with allure.step("Verify initial computed color is available"):
            assert initial_color

        with allure.step("Wait until Color Change button changes color"):
            WebDriverWait(driver, 15).until(
                lambda _driver: (
                    _driver.execute_script(
                        """
                        return window.getComputedStyle(arguments[0]).color;
                        """,
                        color_change_button,
                    )
                    != initial_color
                )
            )

        with allure.step("Get updated computed color"):
            updated_color = driver.execute_script(
                """
                return window.getComputedStyle(arguments[0]).color;
                """,
                color_change_button,
            )

        with allure.step("Verify color has changed"):
            assert updated_color
            assert updated_color != initial_color

    @allure.story("Dynamic Properties state transitions")
    @allure.title("All dynamic properties reach expected final states")
    @allure.description(
        "Verifies that all dynamic properties reach their expected final states: Enable After becomes enabled, Visible After remains visible, and "
        "Color Change changes its computed color."
    )
    @pytest.mark.positive
    def test_dynamic_properties_final_states(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = DynamicPropertiesPage(driver)

        with allure.step("Open Dynamic Properties page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_dynamic_properties()

        with allure.step("Verify initial Enable After state"):
            assert page.enable_after_enable() is False

        with allure.step("Verify initial Visible After state"):
            assert page.visible_after_visible() is True

        with allure.step("Get initial Color Change computed color"):
            color_change_button = driver.find_element(*page.COLOR_CHANGE_BUTTON)

            initial_color = driver.execute_script(
                """
                return window.getComputedStyle(arguments[0]).color;
                """,
                color_change_button,
            )

        with allure.step("Verify initial Color Change color"):
            assert initial_color

        with allure.step("Wait until Enable After bitton is enabled"):
            assert page.wait_enable_after_enabled() is True

        with allure.step("Wait until Visible After bitton is visible"):
            assert page.wait_visible_after_visible() is True

        with allure.step("Wait until Color Change button changes color"):
            WebDriverWait(driver, 15).until(
                lambda _driver: (
                    _driver.execute_script(
                        """
                        return window.getComputedStyle(arguments[0]).color;
                        """,
                        color_change_button,
                    )
                    != initial_color
                )
            )

        with allure.step("Verify Enable After final state"):
            assert page.enable_after_enable() is True

        with allure.step("Verify Visible After final state"):
            assert page.visible_after_visible() is True

        with allure.step("Verify Color Change final state"):
            final_color = driver.execute_script(
                """
                return window.getComputedStyle(arguments[0]).color;
                """,
                color_change_button,
            )

            assert final_color
            assert final_color != initial_color
