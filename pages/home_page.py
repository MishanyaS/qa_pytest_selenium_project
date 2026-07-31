from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_UI_URL
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = BASE_UI_URL

    ELEMENTS_CARD = (
        By.XPATH,
        "//h5[text()='Elements']",
    )

    FORMS_CARD = (
        By.XPATH,
        "//h5[text()='Forms']",
    )

    ALERTS_FRAME_WINDOWS_CARD = (
        By.XPATH,
        "//h5[text()='Alerts, Frame & Windows']",
    )

    WIDGETS_CARD = (
        By.XPATH,
        "//h5[text()='Widgets']",
    )

    INTERACTIONS_CARD = (
        By.XPATH,
        "//h5[text()='Interactions']",
    )

    BOOK_STORE_CARD = (
        By.XPATH,
        "//h5[text()='Book Store Application']",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self) -> None:
        super().open(self.URL)

    def open_elements(self) -> None:
        self.click(self.ELEMENTS_CARD)

    def open_forms(self) -> None:
        self.click(self.FORMS_CARD)

    def open_alerts_frame_windows(self) -> None:
        self.click(self.ALERTS_FRAME_WINDOWS_CARD)

    def open_widgets(self) -> None:
        self.click(self.WIDGETS_CARD)

    def open_interactions(self) -> None:
        self.click(self.INTERACTIONS_CARD)

    def open_book_store(self) -> None:
        self.click_with_fallback(self.BOOK_STORE_CARD)

    def elements_visible(self) -> bool:
        return self.is_visible(self.ELEMENTS_CARD)

    def forms_visible(self) -> bool:
        return self.is_visible(self.FORMS_CARD)

    def alerts_frame_windows_visible(self) -> bool:
        return self.is_visible(self.ALERTS_FRAME_WINDOWS_CARD)

    def widgets_visible(self) -> bool:
        return self.is_visible(self.WIDGETS_CARD)

    def interactions_visible(self) -> bool:
        return self.is_visible(self.INTERACTIONS_CARD)

    def book_store_visible(self) -> bool:
        return self.is_visible(self.BOOK_STORE_CARD)
