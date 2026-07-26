from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class BrokenLinksPage(BasePage):
    VALID_LINK = (
        By.XPATH,
        "//a[text()='Click Here for Valid Link']"
    )

    BROKEN_LINK = (
        By.XPATH,
        "//a[text()='Click Here for Broken Link']"
    )

    VALID_IMAGE = (
        By.XPATH,
        "//p[text()='Valid image']/following-sibling::img",
    )

    BROKEN_IMAGE = (
        By.XPATH,
        "//p[text()='Broken image']/following-sibling::img",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def click_valid_link(self) -> None:
        self.click(self.VALID_LINK)

    def click_broken_link(self) -> None:
        self.click(self.BROKEN_LINK)

    def valid_link_visible(self) -> bool:
        return self.is_visible(self.VALID_LINK)

    def broken_link_visible(self) -> bool:
        return self.is_visible(self.BROKEN_LINK)

    def valid_image_visible(self) -> bool:
        return self.is_visible(self.VALID_IMAGE)

    def broken_image_visible(self) -> bool:
        return self.is_visible(self.BROKEN_IMAGE)

    def valid_image_loaded(self) -> bool:
        return self.attribute(self.VALID_IMAGE, "naturalWidth") != "0"

    def broken_image_loaded(self) -> bool:
        return self.attribute(self.BROKEN_IMAGE, "naturalWidth") != "0"

    def valid_link_href(self) -> str | None:
        return self.attribute(self.VALID_LINK, "href")

    def broken_link_href(self) -> str | None:
        return self.attribute(self.BROKEN_LINK, "href")
