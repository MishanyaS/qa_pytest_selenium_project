from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    FULL_NAME_INPUT = (
        By.ID,
        "userName",
    )

    EMAIL_INPUT = (
        By.ID,
        "userEmail",
    )

    CURRENT_ADDRESS_TEXTAREA = (
        By.ID,
        "currentAddress",
    )

    PERMANENT_ADDRESS_TEXTAREA = (
        By.ID,
        "permanentAddress",
    )

    SUBMIT_BUTTON = (
        By.ID,
        "submit",
    )

    OUTPUT_SECTION = (
        By.ID,
        "output",
    )

    OUTPUT_NAME = (
        By.CSS_SELECTOR,
        "#output #name",
    )

    OUTPUT_EMAIL = (
        By.CSS_SELECTOR,
        "#output #email",
    )

    OUTPUT_CURRENT_ADDRESS = (
        By.CSS_SELECTOR,
        "#output #currentAddress",
    )

    OUTPUT_PERMANENT_ADDRESS = (
        By.CSS_SELECTOR,
        "#output #permanentAddress",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def enter_full_name(self, full_name: str) -> None:
        self.type(self.FULL_NAME_INPUT, full_name)

    def enter_email(self, email: str) -> None:
        self.type(self.EMAIL_INPUT, email)

    def enter_current_address(self, address: str) -> None:
        self.type(self.CURRENT_ADDRESS_TEXTAREA, address)

    def enter_permanent_address(self, address: str) -> None:
        self.type(self.PERMANENT_ADDRESS_TEXTAREA, address)

    def click_submit(self) -> None:
        self.click(self.SUBMIT_BUTTON)

    def fill_form(
        self, full_name: str, email: str, current_address: str, permanent_address: str
    ) -> None:
        self.enter_full_name(full_name)
        self.enter_email(email)
        self.enter_current_address(current_address)
        self.enter_permanent_address(permanent_address)

    def submit_form(
        self, full_name: str, email: str, current_address: str, permanent_address: str
    ) -> None:
        self.fill_form(
            full_name=full_name,
            email=email,
            current_address=current_address,
            permanent_address=permanent_address,
        )

        self.click_submit()

    def output_visible(self) -> bool:
        return self.is_visible(self.OUTPUT_SECTION)

    def output_name(self) -> str:
        return self.text(self.OUTPUT_NAME)

    def output_email(self) -> str:
        return self.text(self.OUTPUT_EMAIL)

    def output_current_address(self) -> str:
        return self.text(self.OUTPUT_CURRENT_ADDRESS)

    def output_permanent_address(self) -> str:
        return self.text(self.OUTPUT_PERMANENT_ADDRESS)

    def full_name_value(self) -> str | None:
        return self.attribute(self.FULL_NAME_INPUT, "value")

    def email_value(self) -> str | None:
        return self.attribute(self.EMAIL_INPUT, "value")

    def current_address_value(self) -> str | None:
        return self.attribute(self.CURRENT_ADDRESS_TEXTAREA, "value")

    def permanent_address_value(self) -> str | None:
        return self.attribute(self.PERMANENT_ADDRESS_TEXTAREA, "value")
