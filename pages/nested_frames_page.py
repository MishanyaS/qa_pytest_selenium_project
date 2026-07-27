from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class NestedFramesPage(BasePage):
    PARENT_FRAME = (
        By.ID,
        "frame1"
    )

    CHILD_FRAME = (
        By.TAG_NAME,
        "iframe"
    )

    PARENT_FRAME_TEXT = (
        By.TAG_NAME,
        "body"
    )

    CHILD_FRAME_TEXT = (
        By.TAG_NAME,
        "p"
    )

    def __init__(self, driver: WebDriver) -> None:
                super().__init__(driver)
        
    def parent_frame_visible(self) -> bool:
        return self.is_visible(self.PARENT_FRAME)

    def switch_to_parent_frame(self) -> None:
        self.switch_to_frame(self.PARENT_FRAME)

    def switch_to_child_frame(self) -> None:
        self.switch_to_frame(self.CHILD_FRAME)

    def switch_to_nested_frame(self) -> None:
        self.switch_to_parent_frame()
        self.switch_to_child_frame()

    def switch_to_default_content(self) -> None:
        self.switch_default()

    def parent_frame_text(self) -> str:
        return self.text(self.PARENT_FRAME_TEXT)

    def child_frame_text(self) -> str:
        return self.text(self.CHILD_FRAME_TEXT)

    def get_parent_frame_text(self) -> str:
        self.switch_to_parent_frame()

        try:
            return self.parent_frame_text()
        finally:
            self.switch_to_default_content()

    def get_child_frame_text(self) -> str:
        self.switch_to_parent_frame()

        try:
            self.switch_to_child_frame()

            return self.child_frame_text()
        finally:
            self.switch_to_default_content()
