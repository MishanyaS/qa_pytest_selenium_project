from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class AutoCompletePage(BasePage):
    SINGLE_VALUE_INPUT = (
        By.ID,
        "autoCompleteSingleInput"
    )

    MULTIPLE_VALUE_INPUT = (
        By.ID,
        "autoCompleteMultipleInput"
    )

    SELECTED_SINGLE_VALUE = (
        By.CSS_SELECTOR,
        ".auto-complete__single-value"
    )

    SELECTED_MULTIPLE_VALUES = (
        By.CSS_SELECTOR,
        ".auto-complete__multi-value__label"
    )

    OPTIONS = (
        By.CSS_SELECTOR,
        ".auto-complete__option"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
                        
    def enter_single_value(self, value: str) -> None:
        self.type(self.SINGLE_VALUE_INPUT, value)

    def enter_multiple_value(self, value: str) -> None:
        self.type(self.MULTIPLE_VALUE_INPUT, value)

    def single_value_input_visible(self) -> bool:
        return self.is_visible(self.SINGLE_VALUE_INPUT)

    def multiple_value_input_visible(self) -> bool:
        return self.is_visible(self.MULTIPLE_VALUE_INPUT)

    def single_value_input_value(self) -> str | None:
        return self.attribute(self.SINGLE_VALUE_INPUT, "value")

    def multiple_value_input_value(self) -> str | None:
        return self.attribute(self.MULTIPLE_VALUE_INPUT, "value")

    def options_visible(self) -> bool:
        return self.exists(self.OPTIONS)

    def options(self) -> list[str]:
        return [
            option.text
            for option in self.find_all(self.OPTIONS)
        ]

    def select_option(self, value: str) -> None:
        option = (
            By.XPATH,
            f"//div[contains(@class, 'auto-complete__option') "
            f"and normalize-space()='{value}']"
        )

        self.click(option)

    def select_single_value(self, value: str) -> None:
        self.enter_single_value(value)
        self.select_option(value)

    def select_multiple_value(self, value: str) -> None:
        self.enter_multiple_value(value)
        self.select_option(value)

    def selected_single_value(self) -> str:
        return self.text(self.SELECTED_SINGLE_VALUE)

    def selected_multiple_value(self) -> list[str]:
        return [
            element.text
            for element in self.find_all(self.SELECTED_MULTIPLE_VALUES)
        ]

    def selected_single_value_visible(self) -> bool:
        return self.is_visible(self.SELECTED_SINGLE_VALUE)

    def selected_multiple_value_visible(self) -> bool:
        return self.exists(self.SELECTED_MULTIPLE_VALUES)

    def remove_multiple_value(self, value: str) -> None:
        remove_button = (
            By.XPATH,
            f"//div[contains(@class, 'auto-complete__multi-value') "
            f"and .//div[contains(@class, 'auto-complete__multi-value__label') "
            f"and normalize-space()='{value}']]"
            f"//div[contains(@class, 'auto-complete__multi-value__remove')]",
        )

        self.click(remove_button)

    def clear_single_value(self) -> None:
        self.clear(self.SINGLE_VALUE_INPUT)

    def clear_multiple_value_input(self) -> None:
        self.clear(self.MULTIPLE_VALUE_INPUT)
