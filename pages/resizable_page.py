from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ResizablePage(BasePage):
    RESIZABLE = (By.ID, "resizable")

    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "#resizable .react-resizable-handle-se")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def resizable_visible(self) -> bool:
        return self.is_visible(self.RESIZABLE)

    def resizable_handle_visible(self) -> bool:
        return self.is_visible(self.RESIZABLE_HANDLE)

    def resizable_size(self) -> tuple[int, int]:
        element = self.wait_visible(self.RESIZABLE)

        return (
            element.size["width"],
            element.size["height"],
        )

    def resizable_width(self) -> int:
        return int(self.wait_visible(self.RESIZABLE).size["width"])

    def resizable_height(self) -> int:
        return int(self.wait_visible(self.RESIZABLE).size["height"])

    def resize_element(self, x_offset: int, y_offset: int) -> None:
        self.drag_by_offset(self.RESIZABLE_HANDLE, x_offset, y_offset)
