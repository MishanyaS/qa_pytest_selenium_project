from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SortablePage(BasePage):
    SORTABLE = (By.ID, "demo-tabpane-list")

    SORTABLE_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def sortable_visible(self) -> bool:
        return self.is_visible(self.SORTABLE)

    def sortable_items_visible(self) -> bool:
        return self.is_visible(self.SORTABLE_ITEMS)

    def sortable_items_count(self) -> int:
        return len(self.find_all(self.SORTABLE_ITEMS))

    def sortable_items(self) -> list[str]:
        return [item.text for item in self.find_all(self.SORTABLE_ITEMS)]

    def sortable_item_visible(self, index: int) -> bool:
        item = (
            By.CSS_SELECTOR,
            f"#demo-tabpane-list .list-group-item:nth-child({index})",
        )

        return self.is_visible(item)

    def sortable_item_text(self, index: int) -> str:
        item = (
            By.CSS_SELECTOR,
            f"#demo-tabpane-list .list-group-item:nth-child({index})",
        )

        return self.text(item)

    def drag_item(self, source_index: int, target_index: int) -> None:
        source = (
            By.CSS_SELECTOR,
            f"#demo-tabpane-list .list-group-item:nth-child({source_index})",
        )

        target = (
            By.CSS_SELECTOR,
            f"#demo-tabpane-list .list-group-item:nth-child({target_index})",
        )

        self.drag_and_drop_by_hold(source, target)

    def drag_item_by_locator(
        self, source: tuple[str, str], target: tuple[str, str]
    ) -> None:
        self.drag_and_drop_by_hold(source, target)
