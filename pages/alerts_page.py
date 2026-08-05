from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AlertsPage(BasePage):
    BROWSER_WINDOWS_ITEM = (By.XPATH, "//span[text()='Browser Windows']")

    ALERTS_ITEM = (By.XPATH, "//span[text()='Alerts']")

    FRAMES_ITEM = (By.XPATH, "//span[text()='Frames']")

    NESTED_FRAMES_ITEM = (By.XPATH, "//span[text()='Nested Frames']")

    MODAL_DIALOGS_ITEM = (By.XPATH, "//span[text()='Modal Dialogs']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_browser_windows(self) -> None:
        self.click(self.BROWSER_WINDOWS_ITEM)

    def open_alerts(self) -> None:
        self.click(self.ALERTS_ITEM)

    def open_frames(self) -> None:
        self.click(self.FRAMES_ITEM)

    def open_nested_frames(self) -> None:
        self.click(self.NESTED_FRAMES_ITEM)

    def open_modal_dialogs(self) -> None:
        self.click(self.MODAL_DIALOGS_ITEM)

    def browser_windows_visible(self) -> bool:
        return self.is_visible(self.BROWSER_WINDOWS_ITEM)

    def alerts_visible(self) -> bool:
        return self.is_visible(self.ALERTS_ITEM)

    def frames_visible(self) -> bool:
        return self.is_visible(self.FRAMES_ITEM)

    def nested_frames_visible(self) -> bool:
        return self.is_visible(self.NESTED_FRAMES_ITEM)

    def modal_dialogs_visible(self) -> bool:
        return self.is_visible(self.MODAL_DIALOGS_ITEM)
