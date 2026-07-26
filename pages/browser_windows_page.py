from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):
    NEW_TAB_BUTTON = (
        By.ID,
        "tabButton"
    )

    NEW_WINDOW_BUTTON = (
        By.ID,
        "windowButton"
    )

    NEW_WINDOW_MESSAGE_BUTTON = (
        By.ID,
        "messageWindowButton"
    )

    SAMPLE_HEADING = (
        By.ID,
        "sampleHeading"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_new_tab(self) -> None:
        self.click(self.NEW_TAB_BUTTON)

    def open_new_window(self) -> None:
        self.click(self.NEW_WINDOW_BUTTON)

    def open_new_window_message(self) -> None:
        self.click(self.NEW_WINDOW_MESSAGE_BUTTON)

    def new_tab_visible(self) -> bool:
        return self.is_visible(self.NEW_TAB_BUTTON)

    def new_window_visible(self) -> bool:
        return self.is_visible(self.NEW_WINDOW_BUTTON)

    def new_window_message_visible(self) -> bool:
        return self.is_visible(self.NEW_WINDOW_MESSAGE_BUTTON)

    def window_handles(self) -> list[str]:
        return self.driver.window_handles

    def window_count(self) -> int:
        return len(self.window_handles())

    def current_window_handle(self) -> str:
        return self.driver.current_window_handle

    def switch_to_window(self, index: int) -> None:
        super().switch_to_window(index)

    def switch_to_last_window(self) -> None:
        super().switch_to_window(-1)

    def close_current_window(self) -> None:
        self.close_window()

    def sample_heading_visible(self) -> bool:
        return self.is_visible(self.SAMPLE_HEADING)

    def sample_heading_text(self) -> str:
        return self.text(self.SAMPLE_HEADING)
