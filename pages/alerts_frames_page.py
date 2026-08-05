from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AlertsFramesPage(BasePage):
    BROWSER_WINDOWS_SECTION = (By.XPATH, "//span[text()='Browser Windows']")

    ALERTS_SECTION = (By.XPATH, "//span[text()='Alerts']")

    FRAMES_SECTION = (By.XPATH, "//span[text()='Frames']")

    NESTED_FRAMES_SECTION = (By.XPATH, "//span[text()='Nested Frames']")

    MODAL_DIALOGS_SECTION = (By.XPATH, "//span[text()='Modal Dialogs']")

    SIMPLE_ALERT_BUTTON = (
        By.ID,
        "alertButton",
    )

    TIMER_ALERT_BUTTON = (
        By.ID,
        "timerAlertButton",
    )

    CONFIRM_ALERT_BUTTON = (
        By.ID,
        "confirmButton",
    )

    PROMPT_ALERT_BUTTON = (
        By.ID,
        "promtButton",
    )

    CONFIRM_RESULT = (
        By.ID,
        "confirmResult",
    )

    PROMPT_RESULT = (
        By.ID,
        "promptResult",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_browser_windows(self) -> None:
        self.scroll_to(self.BROWSER_WINDOWS_SECTION)
        self.click_with_fallback(self.BROWSER_WINDOWS_SECTION)

    def open_alerts(self) -> None:
        self.scroll_to(self.ALERTS_SECTION)
        self.click_with_fallback(self.ALERTS_SECTION)

    def open_frames(self) -> None:
        self.scroll_to(self.FRAMES_SECTION)
        self.click_with_fallback(self.FRAMES_SECTION)

    def open_nested_frames(self) -> None:
        self.scroll_to(self.NESTED_FRAMES_SECTION)
        self.click_with_fallback(self.NESTED_FRAMES_SECTION)

    def open_modal_dialogs(self) -> None:
        self.scroll_to(self.MODAL_DIALOGS_SECTION)
        self.click_with_fallback(self.MODAL_DIALOGS_SECTION)

    def open_simple_alert(self) -> None:
        self.click(self.SIMPLE_ALERT_BUTTON)

    def open_timer_alert(self) -> None:
        self.click(self.TIMER_ALERT_BUTTON)

    def open_confirm_alert(self) -> None:
        self.click(self.CONFIRM_ALERT_BUTTON)

    def open_prompt_alert(self) -> None:
        self.click(self.PROMPT_ALERT_BUTTON)

    def simple_alert_visible(self) -> bool:
        return self.is_visible(self.SIMPLE_ALERT_BUTTON)

    def timer_alert_visible(self) -> bool:
        return self.is_visible(self.TIMER_ALERT_BUTTON)

    def confirm_alert_visible(self) -> bool:
        return self.is_visible(self.CONFIRM_ALERT_BUTTON)

    def prompt_alert_visible(self) -> bool:
        return self.is_visible(self.PROMPT_ALERT_BUTTON)

    def accept_current_alert(self) -> None:
        self.accept_alert()

    def dismiss_current_alert(self) -> None:
        self.dismiss_alert()

    def current_alert_text(self) -> str:
        return self.alert_text()

    def confirm_result_visible(self) -> bool:
        return self.is_visible(self.CONFIRM_RESULT)

    def confirm_result_text(self) -> str:
        return self.text(self.CONFIRM_RESULT)

    def prompt_result_visible(self) -> bool:
        return self.is_visible(self.PROMPT_RESULT)

    def prompt_result_text(self) -> str:
        return self.text(self.PROMPT_RESULT)
