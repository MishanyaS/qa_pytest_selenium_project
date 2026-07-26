from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class CheckBoxPage(BasePage):
    HOME_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Home']",
    )

    DESKTOP_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Desktop']",
    )

    DOCUMENTS_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Documents']",
    )

    DOWNLOADS_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Downloads']",
    )

    NOTES_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Notes']",
    )

    COMMANDS_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Commands']",
    )

    WORKSPACE_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='WorkSpace']",
    )

    REACT_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='React']",
    )

    ANGULAR_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Angular']",
    )

    VEU_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Veu']",
    )

    GENERAL_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='General']",
    )

    WORD_FILE_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Word File.doc']",
    )

    EXCEL_FILE_CHECKBOX = (
        By.XPATH,
        "//span[@class='rct-title' and text()='Excel File.doc']",
    )

    EXPAND_ALL_BUTTON = (
        By.XPATH,
        "//button[@title='Expand all']",
    )

    COLLAPSE_ALL_BUTTON = (
        By.XPATH,
        "//button[@title='Collapse all']",
    )

    RESULT_SECTION = (
        By.ID,
        "result",
    )

    SELECTED_ITEMS = (
        By.CSS_SELECTOR,
        "#result .text-success",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def select_home(self) -> None:
        self.click(self.HOME_CHECKBOX)

    def select_desktop(self) -> None:
        self.click(self.DESKTOP_CHECKBOX)

    def select_documents(self) -> None:
        self.click(self.DOCUMENTS_CHECKBOX)

    def select_downloads(self) -> None:
        self.click(self.DOWNLOADS_CHECKBOX)

    def select_notes(self) -> None:
        self.click(self.NOTES_CHECKBOX)

    def select_commands(self) -> None:
        self.click(self.COMMANDS_CHECKBOX)

    def select_workspace(self) -> None:
        self.click(self.WORKSPACE_CHECKBOX)

    def select_react(self) -> None:
        self.click(self.REACT_CHECKBOX)

    def select_angular(self) -> None:
        self.click(self.ANGULAR_CHECKBOX)

    def select_veu(self) -> None:
        self.click(self.VEU_CHECKBOX)

    def select_general(self) -> None:
        self.click(self.GENERAL_CHECKBOX)

    def select_word_file(self) -> None:
        self.click(self.WORD_FILE_CHECKBOX)

    def select_excel_file(self) -> None:
        self.click(self.EXCEL_FILE_CHECKBOX)

    def expand_all(self) -> None:
        self.click(self.EXPAND_ALL_BUTTON)

    def collapse_all(self) -> None:
        self.click(self.COLLAPSE_ALL_BUTTON)

    def result_visible(self) -> bool:
        return self.is_visible(self.RESULT_SECTION)

    def selected_items(self) -> list[str]:
        elements = self.wait_all_present(self.SELECTED_ITEMS)

        return [element.text for element in elements]

    def selected_items_text(self) -> str:
        return self.text(self.RESULT_SECTION)
