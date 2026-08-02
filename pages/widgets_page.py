from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class WidgetsPage(BasePage):
    ACCORDION_SECTION = (
        By.XPATH,
        "//span[text()='Accordian']"
    )

    AUTO_COMPLETE_SECTION = (
        By.XPATH,
        "//span[text()='Auto Complete']"
    )

    DATE_PICKER_SECTION = (
        By.XPATH,
        "//span[text()='Date Picker']"
    )

    SLIDER_SECTION = (
        By.XPATH,
        "//span[text()='Slider']"
    )

    PROGRESS_BAR_SECTION = (
        By.XPATH,
        "//span[text()='Progress Bar']"
    )

    TABS_SECTION = (
        By.XPATH,
        "//span[text()='Tabs']"
    )

    TOOL_TIPS_SECTION = (
        By.XPATH,
        "//span[text()='Tool Tips']"
    )

    MENU_SECTION = (
        By.XPATH,
        "//span[text()='Menu']"
    )

    SELECT_MENU_SECTION = (
        By.XPATH,
        "//span[text()='Select Menu']"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
                
    def open_accordion(self) -> None:
        self.scroll_to(self.ACCORDION_SECTION)
        self.click_with_fallback(self.ACCORDION_SECTION)

    def open_auto_complete(self) -> None:
        self.scroll_to(self.AUTO_COMPLETE_SECTION)
        self.click_with_fallback(self.AUTO_COMPLETE_SECTION)

    def open_date_picker(self) -> None:
        self.scroll_to(self.DATE_PICKER_SECTION)
        self.click_with_fallback(self.DATE_PICKER_SECTION)

    def open_slider(self) -> None:
        self.scroll_to(self.SLIDER_SECTION)
        self.click_with_fallback(self.SLIDER_SECTION)

    def open_progress_bar(self) -> None:
        self.scroll_to(self.PROGRESS_BAR_SECTION)
        self.click_with_fallback(self.PROGRESS_BAR_SECTION)

    def open_tabs(self) -> None:
        self.scroll_to(self.TABS_SECTION)
        self.click_with_fallback(self.TABS_SECTION)

    def open_tool_tips(self) -> None:
        self.scroll_to(self.TOOL_TIPS_SECTION)
        self.click_with_fallback(self.TOOL_TIPS_SECTION)

    def open_menu(self) -> None:
        self.scroll_to(self.MENU_SECTION)
        self.click_with_fallback(self.MENU_SECTION)

    def open_select_menu(self) -> None:
        self.scroll_to(self.SELECT_MENU_SECTION)
        self.click_with_fallback(self.SELECT_MENU_SECTION)

    def accordion_visible(self) -> bool:
        return self.is_visible(self.ACCORDION_ITEM)

    def auto_complete_visible(self) -> bool:
        return self.is_visible(self.AUTO_COMPLETE_ITEM)

    def date_picker_visible(self) -> bool:
        return self.is_visible(self.DATE_PICKER_ITEM)

    def slider_visible(self) -> bool:
        return self.is_visible(self.SLIDER_ITEM)

    def progress_bar_visible(self) -> bool:
        return self.is_visible(self.PROGRESS_BAR_ITEM)

    def tabs_visible(self) -> bool:
        return self.is_visible(self.TABS_ITEM)

    def tool_tips_visible(self) -> bool:
        return self.is_visible(self.TOOL_TIPS_SECTION)

    def menu_visible(self) -> bool:
        return self.is_visible(self.MENU_SECTION)

    def select_menu_visible(self) -> bool:
        return self.is_visible(self.SELECT_MENU_SECTION)

