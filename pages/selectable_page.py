from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class SelectablePage(BasePage):
    SELECTABLE = (
        By.ID,
        "selectable"
    )

    SELECTABLE_ITEMS = (
        By.CSS_SELECTOR,
        "#selectable li"
    )

    SELECTED_ITEMS = (
        By.CSS_SELECTOR,
        "#selectable li.ui-selected"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def selectable_visible(self) -> bool:
        return self.is_visible(self.SELECTABLE)

    def selectable_items_visible(self) -> bool:
        return self.is_visible(self.SELECTABLE_ITEMS)

    def selectable_items_count(self) -> int:
        return len(self.find_all(self.SELECTABLE_ITEMS))

    def selectable_items(self) -> list[str]:
        return [
            item.text
            for item in self.find_all(self.SELECTABLE_ITEMS)
        ]

    def selectable_item_visible(self, index: int) -> bool:
        item = (
            By.CSS_SELECTOR,
            f"#selectable li:nth-child({index})"
        )

        return self.is_visible(item)

    def selectable_item_text(self, index: int) -> str:
        item = (
            By.CSS_SELECTOR,
            f"#selectable li:nth-child({index})"
        )

        return self.text(item)

    def select_item(self, index: int) -> None:
        item = (
            By.CSS_SELECTOR,
            f"#selectable li:nth-child({index})"
        )

        self.click(item)

    def selected_items(self) -> list[str]:
        return [
            item.text
            for item in self.find_all(self.SELECTED_ITEMS)
        ]

    def selected_items_count(self) -> int:
        return len(self.find_all(self.SELECTED_ITEMS))

    def item_selected(self, index: int) -> bool:
        item = (
            By.CSS_SELECTOR,
            f"#selectable li:nth-child({index}).ui-selected"
        )

        return self.exists(item)

    def clear_selection(self) -> None:
        selected_items = self.find_all(self.SELECTED_ITEMS)

        for item in selected_items:
            item.click()
