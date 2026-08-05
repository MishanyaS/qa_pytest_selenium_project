from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ElementsPage(BasePage):
    TEXT_BOX_ITEM = (
        By.XPATH,
        "//span[text()='Text Box']",
    )

    CHECK_BOX_ITEM = (
        By.XPATH,
        "//span[text()='Check Box']",
    )

    RADIO_BUTTON_ITEM = (
        By.XPATH,
        "//span[text()='Radio Button']",
    )

    WEB_TABLES_ITEM = (
        By.XPATH,
        "//span[text()='Web Tables']",
    )

    BUTTONS_ITEM = (
        By.XPATH,
        "//span[text()='Buttons']",
    )

    LINKS_ITEM = (
        By.XPATH,
        "//span[text()='Links']",
    )

    BROKEN_LINKS_IMAGES_ITEM = (
        By.XPATH,
        "//span[text()='Broken Links - Images']",
    )

    UPLOAD_DOWNLOAD_ITEM = (
        By.XPATH,
        "//span[text()='Upload and Download']",
    )

    DYNAMIC_PROPERTIES_ITEM = (
        By.XPATH,
        "//span[text()='Dynamic Properties']",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_text_box(self) -> None:
        self.click(self.TEXT_BOX_ITEM)

    def open_check_box(self) -> None:
        self.click(self.CHECK_BOX_ITEM)

    def open_radio_button(self) -> None:
        self.click(self.RADIO_BUTTON_ITEM)

    def open_web_tables(self) -> None:
        self.click(self.WEB_TABLES_ITEM)

    def open_buttons(self) -> None:
        self.click(self.BUTTONS_ITEM)

    def open_links(self) -> None:
        self.click(self.LINKS_ITEM)

    def open_broken_links_images(self) -> None:
        self.click(self.BROKEN_LINKS_IMAGES_ITEM)

    def open_upload_download(self) -> None:
        self.click(self.UPLOAD_DOWNLOAD_ITEM)

    def open_dynamic_properties(self) -> None:
        self.click(self.DYNAMIC_PROPERTIES_ITEM)

    def text_box_visible(self) -> bool:
        return self.is_visible(self.TEXT_BOX_ITEM)

    def check_box_visible(self) -> bool:
        return self.is_visible(self.CHECK_BOX_ITEM)

    def radio_button_visible(self) -> bool:
        return self.is_visible(self.RADIO_BUTTON_ITEM)

    def web_tables_visible(self) -> bool:
        return self.is_visible(self.WEB_TABLES_ITEM)

    def buttons_visible(self) -> bool:
        return self.is_visible(self.BUTTONS_ITEM)

    def links_visible(self) -> bool:
        return self.is_visible(self.LINKS_ITEM)

    def broken_links_images_visible(self) -> bool:
        return self.is_visible(self.BROKEN_LINKS_IMAGES_ITEM)

    def upload_download_visible(self) -> bool:
        return self.is_visible(self.UPLOAD_DOWNLOAD_ITEM)

    def dynamic_properties_visible(self) -> bool:
        return self.is_visible(self.DYNAMIC_PROPERTIES_ITEM)
