from __future__ import annotations

from typing import Any

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import (
    alert_is_present,
    element_to_be_clickable,
    invisibility_of_element_located,
    presence_of_all_elements_located,
    presence_of_element_located,
    text_to_be_present_in_element,
    url_contains,
    visibility_of_element_located,
)
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from config import PAGE_LOAD_TIMEOUT

type Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = PAGE_LOAD_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def refresh(self) -> None:
        self.driver.refresh()

    def back(self) -> None:
        self.driver.back()

    def forward(self) -> None:
        self.driver.forward()

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    @property
    def title(self) -> str:
        return self.driver.title

    def find(self, locator: Locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_all(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator: Locator) -> WebElement:
        return self.wait.until(visibility_of_element_located(locator))

    def wait_present(self, locator: Locator) -> WebElement:
        return self.wait.until(presence_of_element_located(locator))

    def wait_all_present(self, locator: Locator) -> list[WebElement]:
        return self.wait.until(presence_of_all_elements_located(locator))

    def wait_clickable(self, locator: Locator) -> WebElement:
        return self.wait.until(element_to_be_clickable(locator))

    def wait_invisible(self, locator: Locator) -> bool:
        return bool(self.wait.until(invisibility_of_element_located(locator)))

    def wait_text(self, locator: Locator, text: str) -> bool:
        return self.wait.until(text_to_be_present_in_element(locator, text))

    def wait_url_contains(self, value: str) -> bool:
        return self.wait.until(url_contains(value))

    def click(self, locator: Locator) -> None:
        self.wait_clickable(locator).click()

    def click_with_fallback(self, locator: Locator) -> None:
        try:
            self.click(locator)
        except ElementClickInterceptedException:
            self.js_click(locator)

    def type(self, locator: Locator, text: str) -> None:
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator: Locator) -> None:
        self.wait_visible(locator).clear()

    def text(self, locator: Locator) -> str:
        return self.wait_visible(locator).text

    def attribute(self, locator: Locator, name: str) -> str | None:
        return self.wait_visible(locator).get_attribute(name)

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except TimeoutException:
            return False

    def exists(self, locator: Locator) -> bool:
        return len(self.find_all(locator)) > 0

    def is_enabled(self, locator: Locator) -> bool:
        return self.wait_visible(locator).is_enabled()

    def is_selected(self, locator: Locator) -> bool:
        return self.wait_visible(locator).is_selected()

    def execute_script(self, script: str, *args: Any) -> Any:
        return self.driver.execute_script(script, *args)

    def js_click(self, locator: Locator) -> None:
        element = self.wait_visible(locator)

        self.execute_script(
            "arguments[0].click();",
            element,
        )

    def scroll_to(self, locator: Locator) -> None:
        element = self.wait_visible(locator)

        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def scroll_top(self) -> None:
        self.execute_script(
            "window.scrollTo(0, 0);",
        )

    def scroll_bottom(self) -> None:
        self.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
        )

    def hover(self, locator: Locator) -> None:
        element = self.wait_visible(locator)

        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator: Locator) -> None:
        element = self.wait_visible(locator)

        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator: Locator) -> None:
        element = self.wait_visible(locator)

        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source: Locator, target: Locator) -> None:
        source_element = self.wait_visible(source)
        target_element = self.wait_visible(target)

        actions = ActionChains(self.driver)

        (
            actions.click_and_hold(source_element)
            .pause(0.2)
            .move_to_element(target_element)
            .pause(0.2)
            .release()
            .perform()
        )

    def drag_and_drop_by_hold(self, source: Locator, target: Locator) -> None:
        source_element = self.wait_visible(source)
        target_element = self.wait_visible(target)

        actions = ActionChains(self.driver)

        (
            actions.click_and_hold(source_element)
            .move_to_element(target_element)
            .move_by_offset(0, 10)
            .pause(0.2)
            .release()
            .perform()
        )

    def select_by_text(self, locator: Locator, text: str) -> None:
        Select(self.wait_visible(locator)).select_by_visible_text(text)

    def select_by_value(self, locator: Locator, value: str) -> None:
        Select(self.wait_visible(locator)).select_by_value(value)

    def select_by_index(self, locator: Locator, index: int) -> None:
        Select(self.wait_visible(locator)).select_by_index(index)

    def wait_alert(self) -> Alert:
        return self.wait.until(alert_is_present())

    def accept_alert(self) -> None:
        self.wait_alert().accept()

    def dismiss_alert(self) -> None:
        self.wait_alert().dismiss()

    def alert_text(self) -> str:
        return self.wait_alert().text

    def switch_to_frame(self, locator: Locator) -> None:
        frame = self.wait_present(locator)

        self.driver.switch_to.frame(frame)

    def switch_default(self) -> None:
        self.driver.switch_to.default_content()

    def switch_to_window(self, index: int) -> None:
        self.driver.switch_to.window(self.driver.window_handles[index])

    def switch_to_window_handle(self, hande: str) -> None:
        self.driver.switch_to.window(hande)

    def close_window(self) -> None:
        self.driver.close()

    def add_cookie(self, cookie: dict) -> None:
        self.driver.add_cookie(cookie)

    def delete_cookie(self, name: str) -> None:
        self.driver.delete_cookie(name)

    def clear_cookies(self) -> None:
        self.driver.delete_all_cookies()

    def save_screenshot(self, path: str) -> None:
        self.driver.save_screenshot(path)

    def alert_send_keys(self, text: str) -> None:
        self.wait_alert().send_keys(text)

    def drag_by_offset(self, locator: Locator, x_offset: int, y_offset: int) -> None:
        element = self.wait_visible(locator)

        ActionChains(self.driver).move_to_element(
            element
        ).click_and_hold().move_by_offset(x_offset, y_offset).release().perform()
