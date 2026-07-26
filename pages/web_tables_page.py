from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

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

    REGISTRATION_FORM = (
        By.CLASS_NAME,
        "modal-content",
    )

    TABLE_ROWS = (
        By.CSS_SELECTOR,
        ".rt-tbody .rt-tr-group",
    )

    TABLE_CELLS = (
        By.CSS_SELECTOR,
        ".rt-tbody .rt-tr-group .rt-td",
    )

    EDIT_BUTTONS = (
        By.CSS_SELECTOR,
        ".rt-tbody .rt-tr-group .action-buttons span[title='Edit']",
    )

    DELETE_BUTTONS = (
        By.CSS_SELECTOR,
        ".rt-tbody .rt-tr-group .action-buttons span[title='Delete']",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_registration_form(self) -> None:
        self.click(self.ADD_BUTTON)

    def registration_form_visible(self) -> bool:
        return self.is_visible(self.REGISTRATION_FORM)

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
        self.type(self.SEARCH_INPUT, value)

    def clear_search(self) -> None:
        self.clear(self.SEARCH_INPUT)

    def search_value(self) -> str:
        return self.attribute(self.SEARCH_INPUT, "value")

    def rows(self) -> list[WebElement]:
        return self.find_all(self.TABLE_ROWS)

    def rows_count(self) -> int:
        return len(self.rows())

    def row_texts(self) -> list[str]:
        return [row.text for row in self.rows() if row.text.strip()]

    def table_text(self) -> str:
        return self.text(
            (
                By.CSS_SELECTOR,
                ".rt-table",
            )
        )

    def edit_buttons(self) -> list[WebElement]:
        return self.find_all(self.EDIT_BUTTONS)

    def delete_buttons(self) -> list[WebElement]:
        return self.find_all(self.DELETE_BUTTONS)

    def edit_record(self, index: int = 0) -> None:
        buttons = self.edit_buttons()

        buttons[index].click()

    def delete_record(self, index: int = 0) -> None:
        buttons = self.delete_buttons()

        buttons[index].click()

    def record_exists(self, value: str) -> bool:
        return value in self.table_text()

    def record_not_exists(self, value: str) -> bool:
        return value not in self.table_text()
