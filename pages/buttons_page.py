from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ButtonsPage(BasePage):
    DOUBLE_CLICK_BUTTON = (
        By.ID,
        "doubleClickBtn",
    )

    RIGHT_CLICK_BUTTON = (
        By.ID,
        "rightClickBtn",
    )

    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    DOUBLE_CLICK_MESSAGE = (
        By.ID,
        "doubleClickMessage",
    )

    RIGHT_CLICK_MESSAGE = (
        By.ID,
        "rightClickMessage",
    )

    DYNAMIC_CLICK_MESSAGE = (
        By.ID,
        "dynamicClickMessage",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def double_click_button(self) -> None:
        super().double_click(self.DOUBLE_CLICK_BUTTON)

    def right_click_button(self) -> None:
        super().right_click(self.RIGHT_CLICK_BUTTON)

    def click_button(self) -> None:
        super().click(self.CLICK_ME_BUTTON)

    def double_click_message_visible(self) -> bool:
        return self.is_visible(self.DOUBLE_CLICK_MESSAGE)

    def right_click_message_visible(self) -> bool:
        return self.is_visible(self.RIGHT_CLICK_MESSAGE)

    def click_message_visible(self) -> bool:
        return self.is_visible(self.DYNAMIC_CLICK_MESSAGE)

    def double_click_message(self) -> str:
        return self.text(self.DOUBLE_CLICK_MESSAGE)

    def right_click_message(self) -> str:
        return self.text(self.RIGHT_CLICK_MESSAGE)

    def click_message(self) -> str:
        return self.text(self.DYNAMIC_CLICK_MESSAGE)
