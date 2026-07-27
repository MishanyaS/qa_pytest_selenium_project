from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class InteractionsPage(BasePage):
    SELECTABLE_ITEM_1 = (
        By.CSS_SELECTOR,
        "#selectable li:nth-child(1)"
    )

    SELECTABLE_ITEM_2 = (
        By.CSS_SELECTOR,
        "#selectable li:nth-child(2)"
    )

    SELECTABLE_ITEM_3 = (
        By.CSS_SELECTOR,
        "#selectable li:nth-child(3)"
    )

    SELECTABLE_ITEM_4 = (
        By.CSS_SELECTOR,
        "#selectable li:nth-child(4)"
    )

    SELECTABLE_ITEM_5 = (
        By.CSS_SELECTOR,
        "#selectable li:nth-child(5)"
    )

    SELECTABLE_ITEMS = (
        By.CSS_SELECTOR,
        "#selectable li"
    )

    SELECTABLE_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        "#selectable li.ui-selected"
    )

    SORTABLE_ITEMS = (
        By.CSS_SELECTOR,
        "#sortable li"
    )

    SORTABLE_ITEM_1 = (
        By.CSS_SELECTOR,
        "#sortable li:nth-child(1)"
    )

    SORTABLE_ITEM_2 = (
        By.CSS_SELECTOR,
        "#sortable li:nth-child(2)"
    )

    SORTABLE_ITEM_3 = (
        By.CSS_SELECTOR,
        "#sortable li:nth-child(3)"
    )

    SORTABLE_ITEM_4 = (
        By.CSS_SELECTOR,
        "#sortable li:nth-child(4)"
    )

    SORTABLE_ITEM_5 = (
        By.CSS_SELECTOR,
        "#sortable li:nth-child(5)"
    )

    SORTABLE_ITEM_6 = (
        By.CSS_SELECTOR,
        "#sortable li:nth-child(6)"
    )

    DROPPABLE = (
        By.ID,
        "droppable"
    )

    DRAGGABLE = (
        By.ID,
        "draggable"
    )

    RESIZABLE = (
        By.ID,
        "resizable"
    )

    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR,
        "#resizable .ui-resizable-se"
    )

    TOOLTIP = (
        By.CSS_SELECTOR,
        ".ui-tooltip"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def selectable_visible(self) -> bool:
        return self.is_visible(self.SELECTABLE_ITEMS)

    def selectable_items(self) -> list[str]:
        return [
            item.text
            for item in self.find_all(self.SELECTABLE_ITEMS)
        ]

    def selectable_items_count(self) -> int:
        return len(self.find_all(self.SELECTABLE_ITEMS))

    def selectable_item_visible(self, index: int) -> bool:
        item = (
            By.CSS_SELECTOR,
            f"#selectable li:nth-child({index})",
        )

        return self.is_visible(item)

    def select_item(self, index: int) -> None:
        item = (
            By.CSS_SELECTOR,
            f"#selectable li:nth-child({index})",
        )

        self.click(item)

    def selected_items(self) -> list[str]:
        return [
            item.text
            for item in self.find_all(self.SELECTABLE_ITEM_ACTIVE)
        ]

    def selected_items_count(self) -> int:
        return len(self.find_all(self.SELECTABLE_ITEM_ACTIVE))

    def item_selected(self, index: int) -> bool:
        item = (
            By.CSS_SELECTOR,
            f"#selectable li:nth-child({index}).ui-selected",
        )

        return self.exists(item)

    def sortable_visible(self) -> bool:
        return self.is_visible(self.SORTABLE_ITEMS)

    def sortable_items(self) -> list[str]:
        return [
            item.text
            for item in self.find_all(self.SORTABLE_ITEMS)
        ]

    def sortable_items_count(self) -> int:
        return len(self.find_all(self.SORTABLE_ITEMS))

    def sortable_item_visible(self, index: int) -> bool:
        item = (
            By.CSS_SELECTOR,
            f"#sortable li:nth-child({index})",
        )

        return self.is_visible(item)

    def sortable_item_text(self, index: int) -> str:
        item = (
            By.CSS_SELECTOR,
            f"#sortable li:nth-child({index})",
        )

        return self.text(item)

    def drag_sortable_item(self, source_index: int, target_index: int) -> None:
        source = (
            By.CSS_SELECTOR,
            f"#sortable li:nth-child({source_index})"
        )

        target = (
            By.CSS_SELECTOR,
            f"#sortable li:nth-child({target_index})"
        )

        self.drag_and_drop(source, target)

    def drag_sortable_item_by_locator(self, source: tuple[str, str], target: tuple[str, str]) -> None:
        self.drag_and_drop(source, target)

    def draggable_visible(self) -> bool:
        return self.is_visible(self.DRAGGABLE)

    def droppable_visible(self) -> bool:
        return self.is_visible(self.DROPPABLE)

    def drag_draggable_to_droppable(self) -> None:
        self.drag_and_drop(self.DRAGGABLE, self.DROPPABLE)

    def droppable_text(self) -> str:
        return self.text(self.DROPPABLE)

    def resizable_visible(self) -> bool:
        return self.is_visible(self.RESIZABLE)

    def resizable_size(self) -> tuple[int, int]:
        element = self.wait_visible(self.RESIZABLE)

        return (
            element.size["width"],
            element.size["height"],
        )

    def resize_element(self, x_offset: int, y_offset: int) -> None:
        self.drag_by_offset(self.RESIZABLE_HANDLE, x_offset, y_offset)

    def element_text(self, locator: tuple[str, str]) -> str:
        return self.text(locator)

    def element_visible(self, locator: tuple[str, str]) -> bool:
        return self.is_visible(locator)
