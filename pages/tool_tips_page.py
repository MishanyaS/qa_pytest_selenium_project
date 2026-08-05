from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    TOOLTIP_BUTTON = (By.ID, "toolTipButton")

    TOOLTIP_TEXT_FIELD = (By.ID, "toolTipTextField")

    TOOLTIP = (By.CSS_SELECTOR, ".tooltip-inner")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def hover_over_button(self) -> None:
        self.hover(self.TOOLTIP_BUTTON)

    def hover_over_text_field(self) -> None:
        self.hover(self.TOOLTIP_TEXT_FIELD)

    def tooltip_button_visible(self) -> bool:
        return self.is_visible(self.TOOLTIP_BUTTON)

    def tooltip_text_field_visible(self) -> bool:
        return self.is_visible(self.TOOLTIP_TEXT_FIELD)

    def tooltip_visible(self) -> bool:
        return self.is_visible(self.TOOLTIP)

    def tooltip_text(self) -> str:
        return self.text(self.TOOLTIP)

    def tooltip_button_text(self) -> str:
        return self.text(self.TOOLTIP_BUTTON)

    def tooltip_text_field_value(self) -> str | None:
        return self.attribute(self.TOOLTIP_TEXT_FIELD, "value")

    def hover_button_get_tooltip(self) -> str:
        self.hover_over_button()
        return self.tooltip_text()

    def hover_text_field_get_tooltip(self) -> str:
        self.hover_over_text_field()
        return self.tooltip_text()
