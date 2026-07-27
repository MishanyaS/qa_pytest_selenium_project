from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class WidgetsPage(BasePage):
    ACCORDION_ITEM = (
        By.XPATH,
        "//span[text()='Accordion']"
    )

    AUTO_COMPLETE_ITEM = (
        By.XPATH,
        "//span[text()='Auto Complete']"
    )

    DATE_PICKER_ITEM = (
        By.XPATH,
        "//span[text()='Date Picker']"
    )

    SLIDER_ITEM = (
        By.XPATH,
        "//span[text()='Slider']"
    )

    PROGRESS_BAR_ITEM = (
        By.XPATH,
        "//span[text()='Progress Bar']"
    )

    TABS_ITEM = (
        By.XPATH,
        "//span[text()='Tabs']"
    )

    TOOL_TIPS_ITEM = (
        By.XPATH,
        "//span[text()='Tool Tips']"
    )

    MENU_ITEM = (
        By.XPATH,
        "//span[text()='Menu']"
    )

    SELECT_MENU_ITEM = (
        By.XPATH,
        "//span[text()='Select Menu']"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
                
    def open_accordion(self) -> None:
        self.click(self.ACCORDION_ITEM)

    def open_auto_complete(self) -> None:
        self.click(self.AUTO_COMPLETE_ITEM)

    def open_date_picker(self) -> None:
        self.click(self.DATE_PICKER_ITEM)

    def open_slider(self) -> None:
        self.click(self.SLIDER_ITEM)

    def open_progress_bar(self) -> None:
        self.click(self.PROGRESS_BAR_ITEM)

    def open_tabs(self) -> None:
        self.click(self.TABS_ITEM)

    def open_tool_tips(self) -> None:
        self.click(self.TOOL_TIPS_ITEM)

    def open_menu(self) -> None:
        self.click(self.MENU_ITEM)

    def open_select_menu(self) -> None:
        self.click(self.SELECT_MENU_ITEM)

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
        return self.is_visible(self.TOOL_TIPS_ITEM)

    def menu_visible(self) -> bool:
        return self.is_visible(self.MENU_ITEM)

    def select_menu_visible(self) -> bool:
        return self.is_visible(self.SELECT_MENU_ITEM)
