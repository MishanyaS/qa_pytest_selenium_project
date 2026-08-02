from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class DroppablePage(BasePage):
    DRAGGABLE = (
        By.ID,
        "draggable"
    )

    DROPPABLE = (
        By.ID,
        "droppable"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def draggable_visible(self) -> bool:
        return self.is_visible(self.DRAGGABLE)

    def droppable_visible(self) -> bool:
        return self.is_visible(self.DROPPABLE)

    def draggable_enabled(self) -> bool:
        return self.is_enabled(self.DRAGGABLE)

    def droppable_enabled(self) -> bool:
        return self.is_enabled(self.DROPPABLE)

    def drag_to_drop(self) -> None:
        self.drag_and_drop(self.DRAGGABLE, self.DROPPABLE)

    def droppable_text(self) -> str:
        return self.text(self.DROPPABLE)

    def draggable_text(self) -> str:
        return self.text(self.DRAGGABLE)

    def dropped(self) -> bool:
        return self.droppable_text() == "Dropped!"
    