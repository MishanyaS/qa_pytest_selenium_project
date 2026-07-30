from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LinkPage(BasePage):
    HOME_LINK = (
        By.ID,
        "simpleLink",
    )

    HOME_LINK_DYNAMIC = (
        By.ID,
        "dynamicLink",
    )

    CREATED_LINK = (
        By.ID,
        "created",
    )

    NO_CONTENT_LINK = (
        By.ID,
        "no-content",
    )

    MOVED_LINK = (
        By.ID,
        "moved",
    )

    BAD_REQUEST_LINK = (
        By.ID,
        "bad-request",
    )

    UNAUTHORIZED_LINK = (
        By.ID,
        "unauthorized",
    )

    FORBIDDEN_LINK = (
        By.ID,
        "forbidden",
    )

    NOT_FOUND_LINK = (
        By.ID,
        "invalid-url",
    )

    LINK_RESPONSE = (
        By.ID,
        "linkResponse",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def click_home(self) -> None:
        self.click(self.HOME_LINK)

    def click_dynamic_home(self) -> None:
        self.click(self.HOME_LINK_DYNAMIC)

    def click_created(self) -> None:
        self.click(self.CREATED_LINK)

    def click_no_content(self) -> None:
        self.click(self.NO_CONTENT_LINK)

    def click_moved(self) -> None:
        self.click(self.MOVED_LINK)

    def click_bad_request(self) -> None:
        self.click(self.BAD_REQUEST_LINK)

    def click_unauthorized(self) -> None:
        self.click(self.UNAUTHORIZED_LINK)

    def click_forbidden(self) -> None:
        self.click(self.FORBIDDEN_LINK)

    def click_not_found(self) -> None:
        self.click(self.NOT_FOUND_LINK)

    def response_visible(self) -> bool:
        return self.is_visible(self.LINK_RESPONSE)

    def response_text(self) -> str:
        return self.text(self.LINK_RESPONSE)

    def response_attribute(self, name: str) -> str | None:
        return self.attribute(self.LINK_RESPONSE, name)

    def wait_for_response_status(self, expected_status: str) -> None:
        self.wait.until(
            EC.text_to_be_present_in_element(self.LINK_RESPONSE, expected_status)
        )
