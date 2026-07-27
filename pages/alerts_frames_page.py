from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class AlertsFramesPage(BasePage):
    SIMPLE_ALERT_BUTTON = (
        By.ID,
        "alertButton",
    )

    TIMER_ALLERT_BUTTON = (
        By.ID,
        "timerAlertButton",
    )

    CONFIRM_ALLERT_BUTTON = (
        By.ID,
        "confirmButton",
    )

    PROMPT_ALLERT_BUTTON = (
        By.ID,
        "promptButton",
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

    def open_simple_alert(self) -> None:
        self.click(self.SIMPLE_ALERT_BUTTON)

    def open_timer_alert(self) -> None:
        self.click(self.TIMER_ALLERT_BUTTON)

    def open_confirm_alert(self) -> None:
        self.click(self.CONFIRM_ALLERT_BUTTON)

    def open_prompt_alert(self) -> None:
        self.click(self.PROMPT_ALLERT_BUTTON)

    def simple_alert_visible(self) -> bool:
        return self.is_visible(self.SIMPLE_ALERT_BUTTON)

    def timer_alert_visible(self) -> bool:
        return self.is_visible(self.TIMER_ALLERT_BUTTON)

    def confirm_alert_visible(self) -> bool:
        return self.is_visible(self.CONFIRM_ALLERT_BUTTON)

    def prompt_alert_visible(self) -> bool:
        return self.is_visible(self.PROMPT_ALLERT_BUTTON)

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
