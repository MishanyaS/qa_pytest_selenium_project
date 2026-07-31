from __future__ import annotations

import allure
import pytest

from pages.alerts_frames_page import AlertsFramesPage
from pages.home_page import HomePage
from pages.accordion_page import AccordionPage

@allure.epic("DemoQA UI")
@allure.feature("Widgets")
@pytest.mark.ui
@pytest.mark.regression
class TestAlerts:
    @allure.story("Accordion navigation")
    @allure.title("Accordion page opens successfully")
    @allure.description("Verifies that the Accordion page can be opened successfully from the Widgets section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_accordion(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        accordion_page = AccordionPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Widgets section"):
            home_page.open_widgets()

        with allure.step("Open Accordion page"):
            alerts_frames_page.open_accordion()

        with allure.step("Verify Accordion page URL"):
            assert accordion_page.current_url.endswith("/accordian")

    @allure.story("Accordion page")
    @allure.title("Accordion section headers are visible")
    @allure.description("Verifies that all three Accordion section headers are displayed on the Accordion page.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_accordion_sections_visible(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = AccordionPage(driver)

        with allure.step("Open Accordion page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_accordion()

        with allure.step("Verify Section 1 header is visible"):
            assert page.section_1_visible()

        with allure.step("Verify Section 2 header is visible"):
            assert page.section_2_visible()

        with allure.step("Verify Section 3 header is visible"):
            assert page.section_3_visible()

    @allure.story("Accordion Section 1")
    @allure.title("Section 1 opens and contains content")
    @allure.description("Verifies that the first Accordion section can be opened and contains non-empty content.")
    @pytest.mark.positive
    def test_open_section_1(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = AccordionPage(driver)

        with allure.step("Open Accordion page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_accordion()

        with allure.step("Open Section 1"):
            page.open_section_1()

        with allure.step("Verify Section 1 is expanded"):
            assert page.section_1_expanded()

        with allure.step("Verify Section 1 content is visible"):
            assert page.section_1_content_visible()

        with allure.step("Verify Section 1 content is not empty"):
            assert page.section_1_content()

    @allure.story("Accordion Section 2")
    @allure.title("Section 2 opens and contains content")
    @allure.description("Verifies that the second Accordion section can be opened and contains non-empty content.")
    @pytest.mark.positive
    def test_open_section_2(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = AccordionPage(driver)

        with allure.step("Open Accordion page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_accordion()

        with allure.step("Open Section 2"):
            page.open_section_2()

        with allure.step("Verify Section 2 is expanded"):
            assert page.section_2_expanded()

        with allure.step("Verify Section 2 content is visible"):
            assert page.section_2_content_visible()

        with allure.step("Verify Section 2 content is not empty"):
            assert page.section_2_content()

    @allure.story("Accordion Section 3")
    @allure.title("Section 3 opens and contains content")
    @allure.description("Verifies that the third Accordion section can be opened and contains non-empty content.")
    @pytest.mark.positive
    def test_open_section_3(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = AccordionPage(driver)

        with allure.step("Open Accordion page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_accordion()

        with allure.step("Open Section 3"):
            page.open_section_3()

        with allure.step("Verify Section 3 is expanded"):
            assert page.section_3_expanded()

        with allure.step("Verify Section 3 content is visible"):
            assert page.section_3_content_visible()

        with allure.step("Verify Section 3 content is not empty"):
            assert page.section_3_content()

    @allure.story("Accordion content")
    @allure.title("All Accordion sections contain content")
    @allure.description("Verifies that each Accordion section provides non-empty content.")
    @pytest.mark.positive
    def test_all_sections_contain_content(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = AccordionPage(driver)

        with allure.step("Open Accordion page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_accordion()

        with allure.step("Get Section 1 content"):
            section_1_content = page.open_section_1_get_content()

        with allure.step("Get Section 2 content"):
            section_2_content = page.open_section_2_get_content()

        with allure.step("Get Section 3 content"):
            section_3_content = page.open_section_3_get_content()

        with allure.step("Verify Section 1 content is not empty"):
            assert section_1_content

        with allure.step("Verify Section 2 content is not empty"):
            assert section_2_content

        with allure.step("Verify Section 3 content is not empty"):
            assert section_3_content

    @allure.story("Accordion content")
    @allure.title("Accordion sections contain different content")
    @allure.description("Verifies that the three Accordion sections provide different content.")
    @pytest.mark.positive
    def test_sections_contain_different_content(self, driver):
        home_page = HomePage(driver)
        alerts_frames_page = AlertsFramesPage(driver)
        page = AccordionPage(driver)

        with allure.step("Open Accordion page"):
            home_page.open()
            home_page.open_widgets()
            alerts_frames_page.open_accordion()

        with allure.step("Get Section 1 content"):
            section_1_content = page.open_section_1_get_content()

        with allure.step("Get Section 2 content"):
            section_2_content = page.open_section_2_get_content()

        with allure.step("Get Section 3 content"):
            section_3_content = page.open_section_3_get_content()

        with allure.step("Verify all sections contain content"):
            assert section_1_content
            assert section_2_content
            assert section_3_content

        with allure.step("Verify Section 1 differs from Section 2"):
            assert section_1_content != section_2_content
        
        with allure.step("Verify Section 1 differs from Section 3"):
            assert section_1_content != section_3_content

        with allure.step("Verify Section 2 differs from Section 3"):
            assert section_2_content != section_3_content
