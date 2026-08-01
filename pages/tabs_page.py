from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class TabsPage(BasePage):
    WHAT_TAB = (
        By.ID,
        "demo-tab-what"
    )

    ORIGIN_TAB = (
        By.ID,
        "demo-tab-origin"
    )

    USE_TAB = (
        By.ID,
        "demo-tab-use"
    )

    MORE_TAB = (
        By.ID,
        "demo-tab-more"
    )

    WHAT_PANEL = (
        By.ID,
        "demo-tabpane-what"
    )

    ORIGIN_PANEL = (
        By.ID,
        "demo-tabpane-origin"
    )

    USE_PANEL = (
        By.ID,
        "demo-tabpane-use"
    )

    MORE_PANEL = (
        By.ID,
        "demo-tabpane-more"
    )

    ACTIVE_TAB = (
        By.CSS_SELECTOR,
        ".nav-link.active"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
                                
    def open_what_tab(self) -> None:
        self.scroll_to(self.WHAT_TAB)
        self.click_with_fallback(self.WHAT_TAB)

    def open_origin_tab(self) -> None:
        self.scroll_to(self.ORIGIN_TAB)
        self.click_with_fallback(self.ORIGIN_TAB)

    def open_use_tab(self) -> None:
        self.scroll_to(self.USE_TAB)
        self.click_with_fallback(self.USE_TAB)

    def open_more_tab(self) -> None:
        self.scroll_to(self.MORE_TAB)
        self.click_with_fallback(self.MORE_TAB)

    def what_tab_visible(self) -> bool:
        return self.is_visible(self.WHAT_TAB)

    def origin_tab_visible(self) -> bool:
        return self.is_visible(self.ORIGIN_TAB)

    def use_tab_visible(self) -> bool:
        return self.is_visible(self.USE_TAB)

    def more_tab_visible(self) -> bool:
        return self.is_visible(self.MORE_TAB)

    def what_panel_visible(self) -> bool:
        return self.is_visible(self.WHAT_PANEL)

    def origin_panel_visible(self) -> bool:
        return self.is_visible(self.ORIGIN_PANEL)

    def use_panel_visible(self) -> bool:
        return self.is_visible(self.USE_PANEL)

    def more_panel_visible(self) -> bool:
        return self.is_visible(self.MORE_PANEL)

    def what_panel_text(self) -> str:
        return self.text(self.WHAT_PANEL)

    def origin_panel_text(self) -> str:
        return self.text(self.ORIGIN_PANEL)

    def use_panel_text(self) -> str:
        return self.text(self.USE_PANEL)

    def more_panel_text(self) -> str:
        return self.text(self.MORE_PANEL)

    def active_tab(self) -> str:
        return self.text(self.ACTIVE_TAB)

    def active_tab_id(self) -> str | None:
        return self.attribute(self.ACTIVE_TAB, "id")

    def open_what_tab_get_content(self) -> str:
        self.open_what_tab()
        return self.what_panel_text()

    def open_origin_tab_get_content(self) -> str:
        self.open_origin_tab()
        return self.origin_panel_text()

    def open_use_tab_get_content(self) -> str:
        self.open_use_tab()
        return self.use_panel_text()

    def open_more_tab_get_content(self) -> str:
        self.open_more_tab()
        return self.more_panel_text()
