from __future__ import annotations

from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class DraggablePage(BasePage):
    DRAGGABLE = (By.ID, "dragBox")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def draggable_visible(self) -> bool:
        return self.is_visible(self.DRAGGABLE)

    def draggable_enabled(self) -> bool:
        return self.is_enabled(self.DRAGGABLE)

    def draggable_text(self) -> str:
        return self.text(self.DRAGGABLE)

    def draggable_position(self) -> tuple[int, int]:
        self.wait_visible(self.DRAGGABLE)

        return (
            self.execute_script(
                "return window.getComputedStyle(arguments[0]).left;",
                self.wait_visible(self.DRAGGABLE),
            ),
            self.execute_script(
                "return window.getComputedStyle(arguments[0]).top;",
                self.wait_visible(self.DRAGGABLE),
            ),
        )

    def draggable_x(self) -> Any:
        return self.execute_script(
            "return window.getComputedStyle(arguments[0]).left;",
            self.wait_visible(self.DRAGGABLE),
        )

    def draggable_y(self) -> Any:
        return self.execute_script(
            "return window.getComputedStyle(arguments[0]).top;",
            self.wait_visible(self.DRAGGABLE),
        )

    def drag(self, x_offset: int, y_offset: int) -> None:
        self.drag_by_offset(self.DRAGGABLE, x_offset, y_offset)
