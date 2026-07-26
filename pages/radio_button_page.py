from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class RadioButtonPage(BasePage):
    YES_RADIO = (
        By.XPATH,
        "//label[@for='yesRadio']",
    )

    IMPRESSIVE_RADIO = (
        By.XPATH,
        "//label[@for='impressiveRadio']",
    )

    NO_RADIO = (
        By.XPATH,
        "//label[@for='noRadio']",
    )

    RESULT_SECTION = (
        By.CLASS_NAME,
        "text-success",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def select_yes(self) -> None:
        self.click(self.YES_RADIO)

    def select_impressive(self) -> None:
        self.click(self.IMPRESSIVE_RADIO)

    def select_no(self) -> None:
        self.click(self.NO_RADIO)

    def result_visible(self) -> bool:
        return self.is_visible(self.RESULT_SECTION)

    def result_text(self) -> str:
        return self.text(self.RESULT_SECTION)

    def yes_selected(self) -> bool:
        return self.is_selected((
            By.ID,
            "yesRadio",
        ))

    def impressive_selected(self) -> bool:
        return self.is_selected((
            By.ID,
            "impressiveRadio",
        ))

    def no_selected(self) -> bool:
        return self.is_selected((
            By.ID,
            "noRadio",
        ))
