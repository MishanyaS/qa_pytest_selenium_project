from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class DraggablePage(BasePage):
    DRAGGABLE = (
        By.ID,
        "draggable"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def draggable_visible(self) -> bool:
        return self.is_visible(self.DRAGGABLE)

    def draggable_enabled(self) -> bool:
        return self.is_enabled(self.DRAGGABLE)

    def draggable_text(self) -> bool:
        return self.text(self.DRAGGABLE)

    def draggable_position(self) -> tuple[int, int]:
        element = self.wait_visible(self.DRAGGABLE)

        return (
            element.location["x"],
            element.location["y"],
        )

    def draggable_x(self) -> int:
        return self.wait_visible(self.DRAGGABLE).location["x"]

    def draggable_y(self) -> int:
        return self.wait_visible(self.DRAGGABLE).location["y"]

    def drag(self, x_offset: int, y_offset: int) -> int:
        self.drag_by_offset(self.DRAGGABLE, x_offset, y_offset)
