from __future__ import annotations

from urllib.parse import urlparse

import allure
import pytest

from pages.broken_links_page import BrokenLinksPage
from pages.elements_page import ElementsPage
from pages.home_page import HomePage


@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestButtons:
    @allure.story("Broken Links navigation")
    @allure.title("Broken Links page opens successfully")
    @allure.description(
        "Verifies that the Broken Links page can be opened from the Elements section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_broken_links(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        broken_links_page = BrokenLinksPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Broken Links page"):
            elements_page.open_broken_links_images()

        with allure.step("Verify Buttons page URL"):
            assert broken_links_page.current_url.endswith("/broken")

    @allure.story("Broken Links page")
    @allure.title("Broken Links page elements are visible")
    @allure.description(
        "Verifies that both valid and broken links and images are displayed on the Broken Links - Images page."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_broken_links_elements_visible(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Verify valid link is visible"):
            assert page.valid_link_visible()

        with allure.step("Verify broken link is visible"):
            assert page.broken_link_visible()

        with allure.step("Verify valid image is visible"):
            assert page.valid_image_visible()

        with allure.step("Verify broken image is visible"):
            assert page.broken_image_visible()

    @allure.story("Links")
    @allure.title("Valid link has a valid href")
    @allure.description("Verifies that the valid link contains an HTTP(S) destination.")
    @pytest.mark.positive
    def test_valid_link_href(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Get valid link href"):
            href = page.valid_link_href()

        with allure.step("Verify broken link is visible"):
            assert href
            assert href.startswith(("http://", "https://"))

    @allure.story("Links")
    @allure.title("Broken Link has a valid href")
    @allure.description(
        "Verifies that the broken link contains an HTTP(S) destination even though the destination itself is expected to be unavailable."
    )
    @pytest.mark.positive
    def test_broken_link_href(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Get broken link href"):
            href = page.broken_link_href()

        with allure.step("Verify broken link href"):
            assert href
            assert href.startswith(("http://", "https://"))

    @allure.story("Links")
    @allure.title("Valid link opens successfully")
    @allure.description(
        "Verifies that clicking the valid link navigates to the expected DemoQA page."
    )
    @pytest.mark.positive
    def test_click_valid_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Click valid link"):
            page.click_valid_link()

        with allure.step("Verify navigation to DemoQA home page"):
            assert driver.current_url.rstrip("/") == "https://demoqa.com"

    @allure.story("Links")
    @allure.title("Broken Link leads to an unavailable page")
    @allure.description(
        "Verifies that clicking the broken link navigates to its configured broken destination."
    )
    @pytest.mark.negative
    def test_click_broken_link(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Get broken link href before clicking"):
            href = page.broken_link_href()

        with allure.step("Click broken link"):
            page.click_broken_link()

        with allure.step("Verify browser navigated to broken link destination"):
            assert href

            expected = urlparse(href)
            actual = urlparse(driver.current_url)

            assert actual.netloc == expected.netloc
            assert actual.path == expected.path
            assert actual.query == expected.query

    @allure.story("Images")
    @allure.title("Valid image element is displayed")
    @allure.description(
        "Verifies that the valid image element is displayed and contains a configured image source."
    )
    @pytest.mark.positive
    def test_valid_image_loaded(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Verify valid image is visible"):
            assert page.valid_image_visible()

        with allure.step("Get valid image source"):
            image = page.find(page.VALID_IMAGE)

            src = page.execute_script("return arguments[0].getAttribute('src');", image)

        with allure.step("Verify valid image source is configured"):
            assert src
            assert src.endswith("Toolsqa.jpg")

    @allure.story("Images")
    @allure.title("Broken image is not loaded")
    @allure.description(
        "Verifies that the broken image is present on the page but its naturalWidth is zero."
    )
    @pytest.mark.negative
    def test_broken_image_not_loaded(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Verify broken image element is visible"):
            assert page.broken_image_visible()

        with allure.step("Verify broken image is not loaded"):
            assert page.broken_image_loaded() is False

    @allure.story("Images")
    @allure.title("Valid and broken image elements have different sources")
    @allure.description(
        "Verifies that the valid and broken image elements are displayed and reference different image resources."
    )
    @pytest.mark.regression
    @pytest.mark.positive
    def test_images_load_states(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Get valid image source"):
            valid_image = page.find(page.VALID_IMAGE)

            valid_src = page.execute_script(
                "return arguments[0].getAttribute('src');", valid_image
            )

        with allure.step("Get broken image source"):
            broken_image = page.find(page.BROKEN_IMAGE)

            broken_src = page.execute_script(
                "return arguments[0].getAttribute('src');", broken_image
            )

        with allure.step("Verify valid image source"):
            assert valid_src
            assert valid_src.endswith("Toolsqa.jpg")

        with allure.step("Verify broken image source"):
            assert broken_src
            assert broken_src.endswith("Toolsqa_1.jpg")

        with allure.step("Verify image sources are different"):
            assert valid_src != broken_src

    @allure.story("Links")
    @allure.title("Both links have different destinations")
    @allure.description(
        "Verifies that the valid and broken links point to different URLs."
    )
    @pytest.mark.positive
    def test_links_have_different_destinations(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = BrokenLinksPage(driver)

        with allure.step("Open Broken Links page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_broken_links_images()

        with allure.step("Get valid link href"):
            valid_href = page.valid_link_href()

        with allure.step("Get broken link href"):
            broken_href = page.broken_link_href()

        with allure.step("Verify both href values exist"):
            assert valid_href
            assert broken_href

        with allure.step("Verify link destinations are different"):
            assert valid_href != broken_href
