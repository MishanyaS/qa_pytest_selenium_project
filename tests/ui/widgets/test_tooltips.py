from __future__ import annotations

import allure
import pytest

from pages.widgets_page import WidgetsPage
from pages.home_page import HomePage
from pages.tool_tips_page import ToolTipsPage

@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestToolTips:
    @allure.story("Tool Tips navigation")
    @allure.title("Tool Tips page opens successfully")
    @allure.description("Verifies that the Tool Tips page can be opened successfully from the Widgets section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_tabs(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        tool_tips_page = ToolTipsPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Tool Tips page"):
            widgets_page.open_tabs()

        with allure.step("Verify Tabs page URL"):
            assert tool_tips_page.current_url.endswith("/tabs")

    @allure.story("Tool Tips page")
    @allure.title("Tool Tips elements are visible")
    @allure.description("Verifies that the tooltip button and text field are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_tooltips_elements_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = ToolTipsPage(driver)

        with allure.step("Open Tool Tips page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_tool_tips()

        with allure.step("Verify tooltip button is visible"):
            assert page.tooltip_button_visible()

        with allure.step("Verify tooltip text field is visible"):
            assert page.tooltip_text_field_visible()

    @allure.story("Tool Tips")
    @allure.title("Button tooltip is displayed")
    @allure.description("Verifies that hovering over the button displays the tooltip.")
    @pytest.mark.positive
    def test_button_tooltip(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = ToolTipsPage(driver)

        with allure.step("Open Tool Tips page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_tool_tips()

        with allure.step("Hover over button"):
            page.hover_over_button()

        with allure.step("Verify tooltip is visible"):
            assert page.tooltip_visible()

        with allure.step("Verify tooltip text"):
            assert page.tooltip_text() == "You hovered over the Button"

    @allure.story("Tool Tips")
    @allure.title("Text field tooltip is displayed")
    @allure.description("Verifies that hovering over the text field displays the tooltip.")
    @pytest.mark.positive
    def test_text_field_tooltip(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = ToolTipsPage(driver)

        with allure.step("Open Tool Tips page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_tool_tips()

        with allure.step("Hover over text field"):
            page.hover_over_text_field()

        with allure.step("Verify tooltip is visible"):
            assert page.tooltip_visible()

        with allure.step("Verify tooltip text"):
            assert page.tooltip_text() == "You hovered over the text field"

    @allure.story("Tool Tips")
    @allure.title("Tooltip button text is correct")
    @allure.description("Verifies that the tooltip button has the expected label.")
    @pytest.mark.positive
    def test_tooltip_button_text(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = ToolTipsPage(driver)

        with allure.step("Open Tool Tips page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_tool_tips()

        with allure.step("Verify button text"):
            assert page.tooltip_button_text() == "Hover me to see"

    @allure.story("Tool Tips")
    @allure.title("Text field is initially empty")
    @allure.description("Verifies that the tooltip text field has no value initially.")
    @pytest.mark.positive
    def test_tooltip_text_field_initial_value(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = ToolTipsPage(driver)

        with allure.step("Open Tool Tips page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_tool_tips()

        with allure.step("Verify text field is empty"):
            assert page.tooltip_text_field_value() == ""

    @allure.story("Tool Tips")
    @allure.title("Hover helper returns button tooltip")
    @allure.description("Verifies that the helper method returns the tooltip text for the button.")
    @pytest.mark.positive
    def test_hover_button_get_tooltip(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = ToolTipsPage(driver)

        with allure.step("Open Tool Tips page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_tool_tips()

        with allure.step("Get tooltip text"):
            tooltip = page.hover_button_get_tooltip()

        with allure.step("Verify tooltip text"):
            assert tooltip == "You hovered over the Button"

    @allure.story("Tool Tips")
    @allure.title("Hover helper returns text field tooltip")
    @allure.description("Verifies that the helper method returns the tooltip text for the text field.")
    @pytest.mark.positive
    def test_hover_text_field_get_tooltip(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = ToolTipsPage(driver)

        with allure.step("Open Tool Tips page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_tool_tips()

        with allure.step("Get tooltip text"):
            tooltip = page.hover_text_field_get_tooltip()

        with allure.step("Verify tooltip text"):
            assert tooltip == "You hovered over the text field"
