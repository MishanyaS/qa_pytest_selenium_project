from __future__ import annotations

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.check_box_page import CheckBoxPage
from pages.elements_page import ElementsPage
from pages.home_page import HomePage


@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestCheckBox:
    @allure.story("Check Box navigation")
    @allure.title("Check Box page opens successfully")
    @allure.description(
        "Verifies that the Check Box page can be opened from the Elements section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_check_box(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        check_box_page = CheckBoxPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Check Box page"):
            elements_page.open_check_box()

        with allure.step("Verify Check Box page URL"):
            assert check_box_page.current_url.endswith("/checkbox")

    @allure.story("Check Box page")
    @allure.title("Check Box elements are visible")
    @allure.description(
        "Verifies that the main Check Box elements are displayed when the page is opened."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_check_box_elements_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Verify Home checkbox is visible"):
            assert page.is_visible(page.HOME_CHECKBOX)

        with allure.step("Verify result section is individually hidden"):
            assert page.result_visible() is False

    @allure.story("Check Box initial state")
    @allure.title("No items are selected initially")
    @allure.description(
        "Verifies that the Check Box tree starts with no selected items."
    )
    @pytest.mark.positive
    def test_no_items_selected_initially(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Verify result section is not visible"):
            assert page.result_visible() is False

    @allure.story("Check Box initial state")
    @allure.title("Home checkbox is initially unchecked")
    @allure.description(
        "Verifies that the Home checkbox has aria-checked=false before selection."
    )
    @pytest.mark.positive
    def test_home_checkbox_initially_unchecked(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Open Home checkbox state"):
            checked_state = page.attribute(page.HOME_CHECKBOX, "aria-checked")

        with allure.step("Verify Home checkbox is unchecked"):
            assert checked_state == "false"

    @allure.story("Check Box selection")
    @allure.title("Home checkbox selects the Home tree")
    @allure.description(
        "Verifies that selecting Home selects Home and its child items."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_select_home(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Select Home checkbox"):
            page.select_home()

        with allure.step("Verify Home checkbox is selected"):
            assert page.attribute(page.HOME_CHECKBOX, "aria-checked") == "true"

        with allure.step("Verify result section is visible"):
            assert page.result_visible() is True

        with allure.step("Get selected items"):
            selected_items = page.selected_items()

        with allure.step("Verify Home tree items are selected"):
            assert "home" in selected_items
            assert "desktop" in selected_items
            assert "documents" in selected_items
            assert "downloads" in selected_items

    @allure.story("Check Box selection")
    @allure.title("Selected Home checkbox can be deselected")
    @allure.description(
        "Verifies that the Home checkbox can be selected and then deselected."
    )
    @pytest.mark.positive
    def test_deselect_home(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Select Home checkbox"):
            page.select_home()

        with allure.step("Verify Home checkbox is selected"):
            assert page.attribute(page.HOME_CHECKBOX, "aria-checked") == "true"

        with allure.step("Deselect Home checkbox"):
            page.select_home()

        with allure.step("Verify Home checkbox is deselected"):
            assert page.attribute(page.HOME_CHECKBOX, "aria-checked") == "false"

        with allure.step("Verify result section is hidden"):
            assert page.result_visible() is False

    @allure.story("Check Box selection")
    @allure.title("Desktop checkbox can be selected")
    @allure.description("Verifies that the Desktop checkbox can be selected.")
    @pytest.mark.positive
    def test_select_desktop(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Select Desktop checkbox"):
            page.select_home()

        with allure.step("Verify Desktop is displayed in results"):
            assert "desktop" in page.selected_items()

    @allure.story("Check Box selection")
    @allure.title("Documents checkbox can be selected")
    @allure.description("Verifies that the Documents checkbox can be selected.")
    @pytest.mark.positive
    def test_select_documents(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Select Documents checkbox"):
            page.select_documents()

        with allure.step("Verify Documents is displayed in results"):
            assert "documents" in page.selected_items()

    @allure.story("Check Box selection")
    @allure.title("Downloads checkbox can be selected")
    @allure.description("Verifies that the Downloads checkbox can be selected.")
    @pytest.mark.positive
    def test_select_downloads(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Select Downloads checkbox"):
            page.select_downloads()

        with allure.step("Verify Downloads is displayed in results"):
            assert "downloads" in page.selected_items()

    @allure.story("Check Box selection")
    @allure.title("Multiple checkboxes can be selected")
    @allure.description(
        "Verifies that multiple independent checkboxes can be selected and all selected items are displayed in the results."
    )
    @pytest.mark.positive
    def test_select_multiple_checkboxes(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = CheckBoxPage(driver)

        with allure.step("Open Check Box page"):
            home_page.open_home_page()
            home_page.open_elements()
            elements_page.open_check_box()

        with allure.step("Select Desktop checkbox"):
            page.select_desktop()

        with allure.step("Select Documents checkbox"):
            page.select_documents()

        with allure.step("Select Downloads checkbox"):
            page.select_downloads()

        with allure.step("Get selected items"):
            selected_items = page.selected_items()

        with allure.step("Verify Downloads is displayed in results"):
            assert "desktop" in selected_items
            assert "documents" in selected_items
            assert "downloads" in selected_items
