from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class FramesPage(BasePage):
    FRAME_1 = (
        By.ID,
        "Frame1"
    )

    FRAME_2 = (
        By.ID,
        "Frame2"
    )

    FRAME_HEADING = (
        By.ID,
        "sampleHeading"
    )

    def __init__(self, driver: WebDriver) -> None:
            super().__init__(driver)
    
    def frame_1_visible(self) -> bool:
        return self.is_visible(self.FRAME_1)

    def frame_2_visible(self) -> bool:
        return self.is_visible(self.FRAME_2)

    def switch_to_frame_1(self) -> None:
        self.switch_to_frame(self.FRAME_1)

    def switch_to_frame_2(self) -> None:
        self.switch_to_frame(self.FRAME_2)

    def switch_to_default_content(self) -> None:
        self.switch_default()

    def heading_visible(self) -> bool:
        return self.is_visible(self.FRAME_HEADING)

    def heading_text(self) -> str:
        return self.text(self.FRAME_HEADING)

    def frame_1_heading(self) -> str:
        self.switch_to_frame_1()

        try:
            return self.heading_text()
        finally:
            self.switch_to_default_content()

    def frame_2_heading(self) -> str:
        self.switch_to_frame_2()

        try:
            return self.heading_text()
        finally:
            self.switch_to_default_content()
