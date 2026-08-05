from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class FormsPage(BasePage):
    PRACTICE_FORM_ITEM = (
        By.XPATH,
        "//span[text()='Practice Form']",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_practice_form(self) -> None:
        self.click(self.PRACTICE_FORM_ITEM)

    def practice_form_visible(self) -> bool:
        return self.is_visible(self.PRACTICE_FORM_ITEM)
