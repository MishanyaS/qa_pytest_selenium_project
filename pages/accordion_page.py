from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AccordionPage(BasePage):
    SECTION_1_HEADING = (
        By.XPATH,
        "//div[@id='accordianContainer']"
        "//button[normalize-space()='What is Lorem Ipsum?']",
    )

    SECTION_2_HEADING = (
        By.XPATH,
        "//div[@id='accordianContainer']"
        "//button[normalize-space()='Where does it come from?']",
    )

    SECTION_3_HEADING = (
        By.XPATH,
        "//div[@id='accordianContainer']"
        "//button[normalize-space()='Why do we use it?']",
    )

    SECTION_1_CONTENT = (
        By.XPATH,
        "//div[@id='accordianContainer']"
        "//div[contains(@class, 'accordion-item')]"
        "[.//button[normalize-space()='What is Lorem Ipsum?']]"
        "//div[contains(@class, 'accordion-body')]",
    )

    SECTION_2_CONTENT = (
        By.XPATH,
        "//div[@id='accordianContainer']"
        "//div[contains(@class, 'accordion-item')]"
        "[.//button[normalize-space()='Where does it come from?']]"
        "//div[contains(@class, 'accordion-body')]",
    )

    SECTION_3_CONTENT = (
        By.XPATH,
        "//div[@id='accordianContainer']"
        "//div[contains(@class, 'accordion-item')]"
        "[.//button[normalize-space()='Why do we use it?']]"
        "//div[contains(@class, 'accordion-body')]",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_section_1(self) -> None:
        if self.attribute(self.SECTION_1_HEADING, "aria-expanded") != "true":
            self.click(self.SECTION_1_HEADING)

        self._wait_for_section_content(self.SECTION_1_HEADING, self.SECTION_1_CONTENT)

    def open_section_2(self) -> None:
        if self.attribute(self.SECTION_2_HEADING, "aria-expanded") != "true":
            self.click(self.SECTION_2_HEADING)

        self._wait_for_section_content(self.SECTION_2_HEADING, self.SECTION_2_CONTENT)

    def open_section_3(self) -> None:
        if self.attribute(self.SECTION_3_HEADING, "aria-expanded") != "true":
            self.click(self.SECTION_3_HEADING)

        self._wait_for_section_content(self.SECTION_3_HEADING, self.SECTION_3_CONTENT)

    def _wait_for_section_content(
        self, heading_locator: tuple[str, str], content_locator: tuple[str, str]
    ) -> None:
        self.wait.until(
            lambda _: (
                self.attribute(heading_locator, "aria-expanded") == "true"
                and self.is_visible(content_locator)
                and bool(self.text(content_locator).strip())
            )
        )

    def section_1_visible(self) -> bool:
        return self.is_visible(self.SECTION_1_HEADING)

    def section_2_visible(self) -> bool:
        return self.is_visible(self.SECTION_2_HEADING)

    def section_3_visible(self) -> bool:
        return self.is_visible(self.SECTION_3_HEADING)

    def section_1_expanded(self) -> bool:
        return self.attribute(self.SECTION_1_HEADING, "aria-expanded") == "true"

    def section_2_expanded(self) -> bool:
        return self.attribute(self.SECTION_2_HEADING, "aria-expanded") == "true"

    def section_3_expanded(self) -> bool:
        return self.attribute(self.SECTION_3_HEADING, "aria-expanded") == "true"

    def section_1_content_visible(self) -> bool:
        return self.is_visible(self.SECTION_1_CONTENT)

    def section_2_content_visible(self) -> bool:
        return self.is_visible(self.SECTION_2_CONTENT)

    def section_3_content_visible(self) -> bool:
        return self.is_visible(self.SECTION_3_CONTENT)

    def section_1_content(self) -> str:
        return self.text(self.SECTION_1_CONTENT).strip()

    def section_2_content(self) -> str:
        return self.text(self.SECTION_2_CONTENT).strip()

    def section_3_content(self) -> str:
        return self.text(self.SECTION_3_CONTENT).strip()

    def open_section_1_get_content(self) -> str:
        self.open_section_1()
        return self.section_1_content()

    def open_section_2_get_content(self) -> str:
        self.open_section_2()
        return self.section_2_content()

    def open_section_3_get_content(self) -> str:
        self.open_section_3()
        return self.section_3_content()
