from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class MenuPage(BasePage):
    HOME_ITEM = (
        By.XPATH,
        "//ul[@id='nav']/li[1]/a"
    )

    MAIN_ITEM_2 = (
        By.XPATH,
        "//ul[@id='nav']/li[2]/a"
    )

    MAIN_ITEM_3 = (
        By.XPATH,
        "//ul[@id='nav']/li[3]/a"
    )

    SUB_SUB_LIST = (
        By.XPATH,
        "//ul[@id='nav']//a[normalize-space()='SUB SUB LIST »']"
    )

    SUB_SUB_ITEM_1 = (
        By.XPATH,
        "//a[normalize-space()='Sub Sub Item 1']"
    )

    SUB_SUB_ITEM_2 = (
        By.XPATH,
        "//a[normalize-space()='Sub Sub Item 2']"
    )

    MENU = (
        By.ID,
        "nav"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
                                
    def menu_visible(self) -> bool:
        return self.is_visible(self.MENU)

    def home_item_visible(self) -> bool:
        return self.is_visible(self.HOME_ITEM)

    def main_item_2_visible(self) -> bool:
        return self.is_visible(self.MAIN_ITEM_2)

    def main_item_3_visible(self) -> bool:
        return self.is_visible(self.MAIN_ITEM_3)

    def sub_sub_list_visible(self) -> bool:
        return self.is_visible(self.SUB_SUB_LIST)

    def sub_sub_item_1_visible(self) -> bool:
        return self.is_visible(self.SUB_SUB_ITEM_1)

    def sub_sub_item_2_visible(self) -> bool:
        return self.is_visible(self.SUB_SUB_ITEM_2)

    def hover_main_item_2(self) -> None:
        self.hover(self.MAIN_ITEM_2)

    def hover_sub_sub_list(self) -> None:
        self.hover(self.SUB_SUB_LIST)

    def click_home(self) -> None:
        self.click(self.HOME_ITEM)

    def click_main_item_2(self) -> None:
        self.click(self.MAIN_ITEM_2)

    def click_main_item_3(self) -> None:
        self.click(self.MAIN_ITEM_3)

    def click_sub_sub_list(self) -> None:
        self.click(self.SUB_SUB_LIST)

    def click_sub_sub_item_1(self) -> None:
        self.click(self.SUB_SUB_ITEM_1)

    def click_sub_sub_item_2(self) -> None:
        self.click(self.SUB_SUB_ITEM_2)

    def home_item_text(self) -> str:
        return self.text(self.HOME_ITEM)

    def main_item_2_text(self) -> str:
        return self.text(self.MAIN_ITEM_2)

    def main_item_3_text(self) -> str:
        return self.text(self.MAIN_ITEM_3)

    def sub_sub_list_text(self) -> str:
        return self.text(self.SUB_SUB_LIST).replace(" »", "").replace("»", "").strip()

    def sub_sub_item_1_text(self) -> str:
        return self.text(self.SUB_SUB_ITEM_1)

    def sub_sub_item_2_text(self) -> str:
        return self.text(self.SUB_SUB_ITEM_2)
