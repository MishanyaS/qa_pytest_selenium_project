from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    HOME_CHECKBOX = (By.XPATH, "//span[@role='checkbox' and @aria-label='Select Home']")

    DESKTOP_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Desktop']",
    )

    DOCUMENTS_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Documents']",
    )

    DOWNLOADS_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Downloads']",
    )

    NOTES_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Notes']",
    )

    COMMANDS_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Commands']",
    )

    WORKSPACE_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select WorkSpace']",
    )

    REACT_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select React']",
    )

    ANGULAR_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Angular']",
    )

    VEU_CHECKBOX = (By.XPATH, "//span[@role='checkbox' and @aria-label='Select Veu']")

    GENERAL_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select General']",
    )

    WORD_FILE_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Word File.doc']",
    )

    EXCEL_FILE_CHECKBOX = (
        By.XPATH,
        "//span[@role='checkbox' and @aria-label='Select Excel File.doc']",
    )

    RESULT_SECTION = (
        By.ID,
        "result",
    )

    SELECTED_ITEMS = (
        By.CSS_SELECTOR,
        "#result .text-success",
    )

    HOME_SWITCHER = (
        By.XPATH,
        "//div[@role='treeitem'][.//span[@title='Home']]"
        "//span[contains(@class, 'rc-tree-switcher')]",
    )

    DOCUMENTS_SWITCHER = (
        By.XPATH,
        "//div[@role='treeitem'][.//span[@title='Documents']]"
        "//span[contains(@class, 'rc-tree-switcher')]",
    )

    WORKSPACE_SWITCHER = (
        By.XPATH,
        "//div[@role='treeitem'][.//span[@title='WorkSpace']]"
        "//span[contains(@class, 'rc-tree-switcher')]",
    )

    OFFICE_SWITCHER = (
        By.XPATH,
        "//div[@role='treeitem'][.//span[@title='Office']]"
        "//span[contains(@class, 'rc-tree-switcher')]",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def select_home(self) -> None:
        self.click(self.HOME_CHECKBOX)

    def select_desktop(self) -> None:
        self.expand_home()
        self.click(self.DESKTOP_CHECKBOX)

    def select_documents(self) -> None:
        self.expand_home()
        self.click(self.DOCUMENTS_CHECKBOX)

    def select_downloads(self) -> None:
        self.expand_home()
        self.click(self.DOWNLOADS_CHECKBOX)

    def select_notes(self) -> None:
        self.expand_home()
        self.click(self.NOTES_CHECKBOX)

    def select_commands(self) -> None:
        self.expand_home()
        self.click(self.COMMANDS_CHECKBOX)

    def select_workspace(self) -> None:
        self.expand_home()
        self.click(self.WORKSPACE_CHECKBOX)

    def select_react(self) -> None:
        self.expand_home()
        self.click(self.REACT_CHECKBOX)

    def select_angular(self) -> None:
        self.expand_home()
        self.click(self.ANGULAR_CHECKBOX)

    def select_veu(self) -> None:
        self.expand_home()
        self.click(self.VEU_CHECKBOX)

    def select_general(self) -> None:
        self.expand_home()
        self.click(self.GENERAL_CHECKBOX)

    def select_word_file(self) -> None:
        self.expand_home()
        self.click(self.WORD_FILE_CHECKBOX)

    def select_excel_file(self) -> None:
        self.expand_home()
        self.click(self.EXCEL_FILE_CHECKBOX)

    def expand_home(self) -> None:
        switcher = self.find(self.HOME_SWITCHER)

        if "switcher_close" in switcher.get_attribute("class"):
            switcher.click()

    def expand_documents(self) -> None:
        switcher = self.find(self.DOCUMENTS_SWITCHER)

        if "switcher_close" in switcher.get_attribute("class"):
            switcher.click()

    def expand_workspace(self) -> None:
        switcher = self.find(self.WORKSPACE_SWITCHER)

        if "switcher_close" in switcher.get_attribute("class"):
            switcher.click()

    def expand_office(self) -> None:
        switcher = self.find(self.OFFICE_SWITCHER)

        if "switcher_close" in switcher.get_attribute("class"):
            switcher.click()

    def result_visible(self) -> bool:
        return self.is_visible(self.RESULT_SECTION)

    def selected_items(self) -> list[str]:
        elements = self.wait_all_present(self.SELECTED_ITEMS)

        return [element.text for element in elements]

    def selected_items_text(self) -> str:
        return self.text(self.RESULT_SECTION)
