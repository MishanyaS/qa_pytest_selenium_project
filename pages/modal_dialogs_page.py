from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class ModalDialogsPage(BasePage):
    SMALL_MODAL_BUTTON = (
        By.ID,
        "showSmallModal"
    )

    LARGE_MODAL_BUTTON = (
        By.ID,
        "showLargeModal"
    )

    MODAL = (
        By.CLASS_NAME,
        "modal-content"
    )

    MODAL_TITLE = (
        By.CLASS_NAME,
        "modal-title"
    )

    MODAL_BODY = (
        By.CLASS_NAME,
        "modal-body"
    )

    CLOSE_MODAL_BUTTON = (
        By.XPATH,
        "//button[@class='close']"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
            
    def open_small_modal(self) -> None:
        self.click(self.SMALL_MODAL_BUTTON)

    def open_large_modal(self) -> None:
        self.click(self.LARGE_MODAL_BUTTON)

    def small_modal_button_visible(self) -> bool:
        return self.is_visible(self.SMALL_MODAL_BUTTON)

    def large_modal_button_visible(self) -> bool:
        return self.is_visible(self.LARGE_MODAL_BUTTON)

    def modal_visible(self) -> bool:
        return self.is_visible(self.MODAL)

    def modal_title(self) -> str:
        return self.text(self.MODAL_TITLE)

    def modal_body(self) -> str:
        return self.text(self.MODAL_BODY)

    def modal_text(self) -> str:
        return self.text(self.MODAL)

    def close_modal(self) -> None:
        self.click(self.CLOSE_MODAL_BUTTON)

    def modal_closed(self) -> bool:
        return not self.is_visible(self.MODAL)

    def open_small_modal_and_get_text(self) -> str:
        self.open_small_modal()

        try:
            return self.modal_text()
        finally:
            self.close_modal()

    def open_large_modal_and_get_text(self) -> str:
        self.open_large_modal()

        try:
            return self.modal_text()
        finally:
            self.close_modal()
