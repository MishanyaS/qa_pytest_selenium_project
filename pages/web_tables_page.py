from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class WebTablesPage(BasePage):
    ADD_BUTTON = (
        By.ID,
        "addNewRecordButton",
    )

    SEARCH_INPUT = (
        By.ID,
        "searchBox",
    )

    TABLE = (
        By.CSS_SELECTOR,
        "table.table",
    )

    TABLE_ROWS = (
        By.CSS_SELECTOR,
        "table.table tbody tr",
    )
    
    TABLE_CELLS = (
        By.CSS_SELECTOR,
        "table.table tbody tr td",
    )

    REGISTRATION_FORM = (
        By.CSS_SELECTOR,
        ".modal-content",
    )

    FIRST_NAME_INPUT = (
        By.ID,
        "firstName",
    )

    LAST_NAME_INPUT = (
        By.ID,
        "lastName",
    )

    EMAIL_INPUT = (
        By.ID,
        "userEmail",
    )

    AGE_INPUT = (
        By.ID,
        "age",
    )

    SALARY_INPUT = (
        By.ID,
        "salary",
    )

    DEPARTMENT_INPUT = (
        By.ID,
        "department",
    )

    SUBMIT_BUTTON = (
        By.ID,
        "submit",
    )

    EDIT_BUTTONS = (
        By.CSS_SELECTOR,
        "table.table tbody tr [title='Edit']",
    )

    DELETE_BUTTONS = (
        By.CSS_SELECTOR,
        "table.table tbody tr [title='Delete']",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_registration_form(self) -> None:
        self.click(self.ADD_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(self.REGISTRATION_FORM)
        )

    def registration_form_visible(self) -> bool:
        elements = self.driver.find_elements(*self.REGISTRATION_FORM)

        return any(
            element.is_displayed()
            for element in elements
        )

    def enter_first_name(self, first_name: str) -> None:
        self.type(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.type(self.LAST_NAME_INPUT, last_name)

    def enter_email(self, email: str) -> None:
        self.type(self.EMAIL_INPUT, email)

    def enter_age(self, age: int | str) -> None:
        self.type(self.AGE_INPUT, str(age))

    def enter_salary(self, salary: int | str) -> None:
        self.type(self.SALARY_INPUT, str(salary))

    def enter_department(self, department: str) -> None:
        self.type(self.DEPARTMENT_INPUT, department)

    def submit_registration_form(self) -> None:
        self.click(self.SUBMIT_BUTTON)

        self.wait.until(
            EC.invisibility_of_element_located(self.REGISTRATION_FORM)
        )

    def add_record(self, first_name: str, last_name: str, email: str, age: int | str, salary: int | str, department: str) -> None:
        self.open_registration_form()

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_age(age)
        self.enter_salary(salary)
        self.enter_department(department)

        self.submit_registration_form()

    def search(self, value: str) -> None:
        search_input = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )

        search_input.click()
        search_input.send_keys(value)

        self.wait.until(
            lambda driver: self.search_value() == value
        )

    def clear_search(self) -> None:
        search_input = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )

        search_input.click()

        search_input.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)

        self.wait.until(
            lambda driver: self.search_value() == ""
        )

        self.wait.until(
            lambda driver: len(driver.find_elements(*self.TABLE_ROWS)) == 3
        )

    def search_value(self) -> str:
        return self.attribute(self.SEARCH_INPUT, "value")

    def table(self) -> WebElement:
        return self.wait.until(
            EC.visibility_of_element_located(self.TABLE)
        )

    def rows(self) -> list[WebElement]:
        return self.driver.find_elements(*self.TABLE_ROWS)

    def rows_count(self) -> int:
        return len(self.rows())

    def row_texts(self) -> list[str]:
        return [row.text for row in self.rows() if row.text.strip()]

    def table_text(self) -> str:
        return self.table().text

    def edit_buttons(self) -> list[WebElement]:
        return [
            button
            for button in self.driver.find_elements(*self.EDIT_BUTTONS)
            if button.is_displayed()
        ]

    def delete_buttons(self) -> list[WebElement]:
        return [
            button
            for button in self.driver.find_elements(*self.DELETE_BUTTONS)
            if button.is_displayed()
        ]

    def edit_record(self, index: int = 0) -> None:
        buttons = self.wait.until(
            lambda driver: [
                button
                for button in driver.find_elements(*self.EDIT_BUTTONS)
                if button.is_displayed()
            ]
        )

        if index >= len(buttons):
            raise IndexError(
                f"Edit button index {index} is out of range. "
                f"Available buttons: {len(buttons)}"
            )

        buttons[index].click()

        self.wait.until(
            EC.visibility_of_element_located(self.REGISTRATION_FORM)
        )

    def delete_record(self, index: int = 0) -> None:
        buttons = self.wait.until(
            lambda driver: [
                button
                for button in driver.find_elements(*self.DELETE_BUTTONS)
                if button.is_displayed()
            ]
        )

        initial_rows_count = self.rows_count()

        if index >= len(buttons):
            raise IndexError(
                f"Delete button index {index} is out of range. "
                f"Available buttons: {len(buttons)}"
            )

        buttons[index].click()

        self.wait.until(
            lambda driver: self.rows_count() < initial_rows_count
        )

    def record_exists(self, value: str) -> bool:
        return value in self.table_text()

    def record_not_exists(self, value: str) -> bool:
        return value not in self.table_text()

    def wait_until_record_exists(self, value: str) -> None:
        self.wait.until(
            lambda driver: value in driver.find_element(*self.TABLE).text
        )

    def wait_until_record_not_exists(self, value: str) -> None:
        self.wait.until(
            lambda driver: value not in driver.find_element(*self.TABLE).text
        )
