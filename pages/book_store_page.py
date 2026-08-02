from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class BookStorePage(BasePage):
    SEARCH_BOX = (
        By.ID,
        "searchBox"
    )

    BOOK_ROWS = (
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    BOOK_TITLE = (
        By.XPATH,
        "//div[@id='title-wrapper']//div[2]/label"
    )

    BOOK_TITLES = (
        By.CSS_SELECTOR,
        "table tbody tr td:nth-child(2) a"
    )

    FIRST_BOOK = (
        By.CSS_SELECTOR,
        "table tbody tr:first-child td:nth-child(2) a"
    )

    LOGIN_BUTTON = (
        By.ID,
        "login"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def search_box_visible(self) -> bool:
        return self.is_visible(self.SEARCH_BOX)

    def books_visible(self) -> bool:
        return self.is_visible(self.BOOK_ROWS)

    def books_count(self) -> int:
        return len(self.find_all(self.BOOK_ROWS))

    def book_title_visible(self, title: str) -> bool:
        return self.text(self.BOOK_TITLE) == title

    def book_titles(self) -> list[str]:
        return [
            book.text
            for book in self.find_all(self.BOOK_TITLES)
            if book.text
        ]

    def book_title(self, index: int) -> str:
        locator = (
            By.CSS_SELECTOR,
            f"table tbody tr:nth-child({index}) td:nth-child(2) a"
        )

        return self.text(locator)

    def book_visible(self, index: int) -> bool:
        locator = (
            By.CSS_SELECTOR,
            f"table tbody tr:nth-child({index}) td:nth-child(2) a"
        )

        return self.is_visible(locator)

    def search(self, text: str) -> None:
        self.type(self.SEARCH_BOX, text)

    def clear_search(self) -> None:
        self.clear(self.SEARCH_BOX)

    def search_value(self) -> str:
        return self.attribute(self.SEARCH_BOX, "value")

    def open_first_book(self) -> None:
        self.click(self.FIRST_BOOK)

    def open_book(self, index: int) -> None:
        locator = (
            By.CSS_SELECTOR,
            f"table tbody tr:nth-child({index}) td:nth-child(2) a"
        )

        self.click(locator)

    def login_button_visible(self) -> bool:
        return self.is_visible(self.LOGIN_BUTTON)

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)
