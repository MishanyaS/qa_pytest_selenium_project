from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class SelectMenuPage(BasePage):
    SELECT_VALUE = (
        By.ID,
        "withOptGroup"
    )

    SELECT_ONE = (
        By.ID,
        "selectOne"
    )

    OLD_STYLE_SELECT = (
        By.ID,
        "oldSelectMenu"
    )

    MULTI_SELECT = (
        By.ID,
        "cars"
    )

    REACT_SELECT_INPUT = (
        By.CSS_SELECTOR,
        "#selectMenuContainer .react-select__input"
    )

    REACT_SELECT_SINGLE = (
        By.ID,
        "react-select-2-input"
    )

    REACT_SELECT_MULTI = (
        By.ID,
        "react-select-3-input"
    )

    REACT_SELECT_OPTIONS = (
        By.CSS_SELECTOR,
        ".react-select__option"
    )

    SELECTED_OPTION = (
        By.CSS_SELECTOR,
        ".react-select__single-value"
    )

    SELECTED_OPTIONS = (
        By.CSS_SELECTOR,
        ".react-select__multi-value__label"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def select_value_visible(self) -> bool:
        return self.is_visible(self.SELECT_VALUE)

    def select_one_visible(self) -> bool:
        return self.is_visible(self.SELECT_ONE)

    def old_style_select_visible(self) -> bool:
        return self.is_visible(self.OLD_STYLE_SELECT)

    def multi_select_visible(self) -> bool:
        return self.is_visible(self.MULTI_SELECT)

    def react_select_input_visible(self) -> bool:
        return self.is_visible(self.REACT_SELECT_INPUT)

    def select_value_by_text(self, text: str) -> None:
        self.select_by_text(self.SELECT_VALUE, text)

    def select_value_by_value(self, value: str) -> None:
        self.select_by_value(self.SELECT_VALUE, value)

    def select_value_by_index(self, index: int) -> None:
        self.select_by_index(self.SELECT_VALUE, index)

    def select_value(self, text: str) -> None:
        self.select_value_by_text(text)

    def select_one_by_text(self, text: str) -> None:
        self.select_by_text(self.SELECT_ONE, text)

    def select_one_by_value(self, value: str) -> None:
        self.select_by_value(self.SELECT_ONE, value)

    def select_one_by_index(self, index: int) -> None:
        self.select_by_index(self.SELECT_ONE, index)

    def select_one(self, text: str) -> None:
        self.select_one_by_text(text)

    def select_old_style_by_text(self, text: str) -> None:
        self.select_by_text(self.OLD_STYLE_SELECT, text)

    def select_old_style_by_value(self, value: str) -> None:
        self.select_by_value(self.OLD_STYLE_SELECT, value)

    def select_old_style_by_index(self, index: int) -> None:
        self.select_by_index(self.OLD_STYLE_SELECT, index)

    def select_old_style(self, text: str) -> None:
        self.select_old_style_by_text(text)

    def select_multiple_by_text(self, text: str) -> None:
        self.select_by_text(self.MULTI_SELECT, text)

    def select_multiple_by_value(self, value: str) -> None:
        self.select_by_value(self.MULTI_SELECT, value)

    def select_multiple_by_index(self, index: int) -> None:
        self.select_by_index(self.MULTI_SELECT, index)

    def select_multiple(self, text: str) -> None:
        self.select_multiple_by_text(text)

    def open_react_select(self) -> None:
        self.click(self.REACT_SELECT_INPUT)

    def react_options_visible(self) -> bool:
        return self.exists(self.REACT_SELECT_OPTIONS)

    def react_options(self) -> list[str]:
        return [
            option.text
            for option in self.find_all(self.REACT_SELECT_OPTIONS)
        ]

    def select_react_option(self, value: str) -> None:
        options = (
            By.XPATH,
            "//div[contains(@class, 'react-select__option' "
            f"and normalize-space()='{value}']",
        )

        self.click(options)

    def select_react_option_by_text(self, value: str) -> None:
        self.open_react_select()
        self.select_react_option(value)

    def selected_react_option(self) -> str:
        return self.text(self.SELECTED_OPTION)

    def selected_react_options(self) -> list[str]:
        return [
            option.text
            for option in self.find_all(self.SELECTED_OPTIONS)
        ]

    def selected_react_option_visible(self) -> bool:
        return self.is_visible(self.SELECTED_OPTION)

    def selected_react_options_visible(self) -> bool:
        return self.exists(self.SELECTED_OPTIONS)

    def selected_value(self, locator: tuple[str, str]) -> str | None:
        return self.attribute(locator, "value")

    def clear_multi_select(self) -> None:
        self.clear(self.MULTI_SELECT)
