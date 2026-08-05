from __future__ import annotations

import allure
import pytest

from pages.buttons_page import ButtonsPage
from pages.elements_page import ElementsPage
from pages.home_page import HomePage


@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestButtons:
    @allure.story("Buttons navigation")
    @allure.title("Buttons page opens successfully")
    @allure.description(
        "Verifies that the Buttons page can be opened from the Elements section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_buttons(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        buttons_page = ButtonsPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Buttons page"):
            elements_page.open_buttons()

        with allure.step("Verify Buttons page URL"):
            assert buttons_page.current_url.endswith("/buttons")

    @allure.story("Buttons page")
    @allure.title("Buttons are visible")
    @allure.description(
        "Verifies that all buttons and their corresponding result message elements are available on the Buttons page."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_buttons_are_visible(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = ButtonsPage(driver)

        with allure.step("Open Buttons page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_buttons()

        with allure.step("Verify Double Click button"):
            assert page.is_visible(page.DOUBLE_CLICK_BUTTON)

        with allure.step("Verify Right Click button"):
            assert page.is_visible(page.RIGHT_CLICK_BUTTON)

        with allure.step("Verify Click Me button"):
            assert page.is_visible(page.CLICK_ME_BUTTON)

        with allure.step("Verify Double Click message is initially hidden"):
            assert page.double_click_message_visible() is False

        with allure.step("Verify Right Click message is initially hidden"):
            assert page.right_click_message_visible() is False

        with allure.step("Verify Dynamic Click message is initially hidden"):
            assert page.click_message_visible() is False

    @allure.story("Double Click")
    @allure.title("Double Click action displays success message")
    @allure.description(
        "Verifies that performing a double click on the Double Click button displays the corresponding success message."
    )
    @pytest.mark.positive
    def test_double_click(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = ButtonsPage(driver)

        with allure.step("Open Buttons page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_buttons()

        with allure.step("Perform double click"):
            page.double_click()

        with allure.step("Verify Double Click message is visible"):
            assert page.double_click_message_visible() is True

        with allure.step("Verify Double Click message text"):
            assert page.double_click_message() == "You have done a double click"

    @allure.story("Right Click")
    @allure.title("Right Click action displays success message")
    @allure.description(
        "Verifies that performing a right click on the Right Click button displays the corresponding success message."
    )
    @pytest.mark.positive
    def test_right_click(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = ButtonsPage(driver)

        with allure.step("Open Buttons page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_buttons()

        with allure.step("Perform right click"):
            page.right_click()

        with allure.step("Verify Right Click message is visible"):
            assert page.right_click_message_visible() is True

        with allure.step("Verify Right Click message text"):
            assert page.right_click_message() == "You have done a right click"

    @allure.story("Dynamic Click")
    @allure.title("Dynamic Click action displays success message")
    @allure.description(
        "Verifies that clicking the dynamically located Click Me button displays the corresponding success message."
    )
    @pytest.mark.positive
    def test_dynamic_click(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = ButtonsPage(driver)

        with allure.step("Open Buttons page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_buttons()

        with allure.step("Perform dynamic click"):
            page.click()

        with allure.step("Verify Dynamic Click message is visible"):
            assert page.click_message_visible() is True

        with allure.step("Verify Dynamic Click message text"):
            assert page.click_message() == "You have done a dynamic click"

    @allure.story("Buttons actions")
    @allure.title("All button actions display corresponding messages")
    @allure.description(
        "Verifies that double click, right click, and dynamic click actions each produce the expected success message."
    )
    @pytest.mark.positive
    def test_all_button_actions(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = ButtonsPage(driver)

        with allure.step("Open Buttons page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_buttons()

        with allure.step("Perform double click"):
            page.double_click()

        with allure.step("Verify Double Click result"):
            assert page.double_click_message_visible() is True
            assert page.double_click_message() == "You have done a double click"

        with allure.step("Perform right click"):
            page.right_click()

        with allure.step("Verify Right Click result"):
            assert page.right_click_message_visible() is True
            assert page.right_click_message() == "You have done a right click"

        with allure.step("Perform dynamic click"):
            page.click()

        with allure.step("Verify Dynamic Click result"):
            assert page.click_message_visible() is True
            assert page.click_message() == "You have done a dynamic click"
