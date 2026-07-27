from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class AccordionPage(BasePage):
    SECTION_1_HEADER = (
        By.ID,
        "section1Header"
    )

    SECTION_2_HEADER = (
        By.ID,
        "section2Header"
    )

    SECTION_3_HEADER = (
        By.ID,
        "section3Header"
    )

    SECTION_1_CONTENT = (
        By.ID,
        "section1Content"
    )

    SECTION_2_CONTENT = (
        By.ID,
        "section2Content"
    )

    SECTION_3_CONTENT = (
        By.ID,
        "section3Content"
    )

    def __init__(self, driver: WebDriver) -> None:
                super().__init__(driver)
                    
    def open_section_1(self) -> None:
        self.click(self.SECTION_1_HEADER)

    def open_section_2(self) -> None:
        self.click(self.SECTION_2_HEADER)

    def open_section_3(self) -> None:
        self.click(self.SECTION_3_HEADER)

    def section_1_visible(self) -> bool:
        return self.is_visible(self.SECTION_1_HEADER)

    def section_2_visible(self) -> bool:
        return self.is_visible(self.SECTION_2_HEADER)

    def section_3_visible(self) -> bool:
        return self.is_visible(self.SECTION_3_HEADER)

    def section_1_content_visible(self) -> bool:
        return self.is_visible(self.SECTION_1_CONTENT)

    def section_2_content_visible(self) -> bool:
        return self.is_visible(self.SECTION_2_CONTENT)

    def section_3_content_visible(self) -> bool:
        return self.is_visible(self.SECTION_3_CONTENT)

    def section_1_content(self) -> str:
        return self.text(self.SECTION_1_CONTENT)

    def section_2_content(self) -> str:
        return self.text(self.SECTION_2_CONTENT)

    def section_3_content(self) -> str:
        return self.text(self.SECTION_3_CONTENT)

    def open_section_1_get_content(self) -> str:
        self.open_section_1()
        return self.section_1_content()

    def open_section_2_get_content(self) -> str:
        self.open_section_2()
        return self.section_2_content()

    def open_section_3_get_content(self) -> str:
        self.open_section_3()
        return self.section_3_content()
