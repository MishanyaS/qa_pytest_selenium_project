from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    PROGRESS_BAR = (By.ID, "progressBar")

    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "#progressBar .progress-bar")

    START_STOP_BUTTON = (By.ID, "startStopButton")

    RESET_BUTTON = (By.ID, "resetButton")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def progress_bar_visible(self) -> bool:
        return self.is_visible(self.PROGRESS_BAR)

    def progress_bar_value_visible(self) -> bool:
        return self.is_visible(self.PROGRESS_BAR_VALUE)

    def start_stop_button_visible(self) -> bool:
        return self.is_visible(self.START_STOP_BUTTON)

    def reset_button_visible(self) -> bool:
        return self.is_visible(self.RESET_BUTTON)

    def progress_bar_value(self) -> str | None:
        return self.wait_present(self.PROGRESS_BAR_VALUE).get_attribute("aria-valuenow")

    def progress_bar_max_value(self) -> str | None:
        return self.wait_present(self.PROGRESS_BAR_VALUE).get_attribute("aria-valuemax")

    def progress_bar_min_value(self) -> str | None:
        return self.wait_present(self.PROGRESS_BAR_VALUE).get_attribute("aria-valuemin")

    def progress_bar_text(self) -> str:
        return self.text(self.PROGRESS_BAR_VALUE)

    def start_progress(self) -> None:
        self.click(self.START_STOP_BUTTON)

    def stop_progress(self) -> None:
        self.click(self.START_STOP_BUTTON)

    def reset_progress(self) -> None:
        self.click(self.RESET_BUTTON)

    def start_stop_button_text(self) -> str:
        return self.text(self.START_STOP_BUTTON)

    def reset_button_enabled(self) -> bool:
        return self.is_enabled(self.RESET_BUTTON)

    def progress_started(self) -> bool:
        value = self.progress_bar_value()

        return value is not None and int(value) > 0

    def progress_completed(self) -> bool:
        value = self.progress_bar_value()
        maximum = self.progress_bar_max_value()

        if value is None or maximum is None:
            return False

        return int(value) >= int(maximum)

    def progress_reset(self) -> bool:
        value = self.progress_bar_value()

        return value == "0"

    def wait_for_progress_value(self, value: int) -> bool:
        return self.wait_text(self.PROGRESS_BAR_VALUE, f"{value}%")

    def wait_for_progress_completion(self) -> bool:
        return self.wait_text(self.PROGRESS_BAR_VALUE, "100%")
