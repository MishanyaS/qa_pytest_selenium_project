from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class DynamicPropertiesPage(BasePage):
    ENABLE_AFTER_BUTTON = (
        By.ID,
        "enableAfter",
    )

    COLOR_CHANGE_BUTTON = (
        By.ID,
        "colorChange",
    )

    VISIBLE_AFTER_BUTTON = (
        By.ID,
        "visibleAfter",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def enable_after_visible(self) -> bool:
        return self.is_visible(self.ENABLE_AFTER_BUTTON)

    def color_change_visible(self) -> bool:
        return self.is_visible(self.COLOR_CHANGE_BUTTON)

    def visible_after_visible(self) -> bool:
        return self.is_visible(self.VISIBLE_AFTER_BUTTON)

    def enable_after_enable(self) -> bool:
        return self.is_enabled(self.ENABLE_AFTER_BUTTON)

    def color_change_attribute(self, name: str) -> str | None:
        return self.attribute(self.COLOR_CHANGE_BUTTON, name)

    def visible_after_enable(self) -> bool:
        return self.is_enabled(self.VISIBLE_AFTER_BUTTON)

    def wait_enable_after_enabled(self) -> bool:
        return self.wait.until(
            lambda driver: driver.find_element(
                *self.ENABLE_AFTER_BUTTON
            ).is_enabled()
        )

    def wait_visible_after_visible(self) -> bool:
        return self.wait.until(
            lambda driver: driver.find_element(
                *self.VISIBLE_AFTER_BUTTON
            ).is_displayed()
        )
