from __future__ import annotations

import allure
import pytest

from pages.home_page import HomePage
from pages.slider_page import SliderPage
from pages.widgets_page import WidgetsPage


@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestSlider:
    @allure.story("Slider navigation")
    @allure.title("Slider page opens successfully")
    @allure.description(
        "Verifies that the Slider page can be opened successfully from the Widgets section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_slider(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        slider_page = SliderPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Slider page"):
            widgets_page.open_slider()

        with allure.step("Verify Slider page URL"):
            assert slider_page.current_url.endswith("/slider")

    @allure.story("Slider page")
    @allure.title("Slider is visible")
    @allure.description("Verifies that the Slider and its value field are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_slider_visible(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SliderPage(driver)

        with allure.step("Open Slider page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_slider()

        with allure.step("Verify Slider is visibile"):
            assert page.slider_visible()

        with allure.step("Verify Slider value field is visible"):
            assert page.slider_value_visible()

    @allure.story("Slider properties")
    @allure.title("Slider has valid range and step")
    @allure.description(
        "Verifies that the Slider has valid minimum, maximum and step values."
    )
    @pytest.mark.positive
    def test_slider_properties(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SliderPage(driver)

        with allure.step("Open Slider page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_slider()

        with allure.step("Verify minimum value exists"):
            assert page.slider_min()

        with allure.step("Verify maximum value exists"):
            assert page.slider_max()

        with allure.step("Verify step value exists"):
            assert page.slider_value_attribute()

    @allure.story("Slider interaction")
    @allure.title("Slider value can be changed")
    @allure.description(
        "Verifies that the Slider value can be changed programmatically."
    )
    @pytest.mark.positive
    def test_set_slider_value(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SliderPage(driver)

        with allure.step("Open Slider page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_slider()

        with allure.step("Set Slider value to 75"):
            page.set_slider_value(75)

        with allure.step("Verify Slider value"):
            assert page.slider_value() == "75"

    @allure.story("Slider interaction")
    @allure.title("Slider value increases")
    @allure.description(
        "Verifies that the Slider value increases using keyboard controls."
    )
    @pytest.mark.positive
    def test_increase_slider(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SliderPage(driver)

        with allure.step("Open Slider page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_slider()

        with allure.step("Store initial value"):
            initial = int(page.slider_value())

        with allure.step("Increase Slider"):
            page.increase_slider()

        with allure.step("Verify Slider value increased"):
            assert int(page.slider_value()) > initial

    @allure.story("Slider interaction")
    @allure.title("Slider value decreases")
    @allure.description(
        "Verifies that the Slider value decreases using keyboard controls."
    )
    @pytest.mark.positive
    def test_decrease_slider(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SliderPage(driver)

        with allure.step("Open Slider page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_slider()

        with allure.step("Move Slider to maximum"):
            page.set_slider_to_max()

        with allure.step("Store initial value"):
            initial = int(page.slider_value())

        with allure.step("Decrease Slider"):
            page.decrease_slider()

        with allure.step("Verify Slider value decreased"):
            assert int(page.slider_value()) < initial

    @allure.story("Slider interaction")
    @allure.title("Slider can be set to minimum and maximum values")
    @allure.description(
        "Verifies that the Slider can be moved to its minimum and maximum values."
    )
    @pytest.mark.positive
    def test_slider_min_and_max(self, driver):
        home_page = HomePage(driver)
        widgets_page = WidgetsPage(driver)
        page = SliderPage(driver)

        with allure.step("Open Slider page"):
            home_page.open()
            home_page.open_widgets()
            widgets_page.open_slider()

        with allure.step("Set Slider to minimum"):
            page.set_slider_to_min()

        with allure.step("Verify minimum value"):
            assert page.slider_value() == page.slider_min()

        with allure.step("Set Slider to maximum"):
            page.set_slider_to_max()

        with allure.step("Verify maximum value"):
            assert page.slider_value() == page.slider_max()
