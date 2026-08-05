from __future__ import annotations

import allure
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.web_tables_page import WebTablesPage


@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestWebTables:
    @allure.story("Web Tables navigation")
    @allure.title("Web Tables page opens successfully")
    @allure.description(
        "Verifies that the Web Tables page can be opened from the Elements section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_web_tables(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        web_tables_page = WebTablesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Verify Web Tables page URL"):
            assert web_tables_page.current_url.endswith("/webtables")

    @allure.story("Web Tables page")
    @allure.title("Web Tables elements are visible")
    @allure.description(
        "Verifies that the Web Tables page contains the Add button, Search field, table, and default records."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_web_tables_elements_visible(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Verify Add button is visible"):
            assert page.is_visible(page.ADD_BUTTON)

        with allure.step("Verify Search field is visible"):
            assert page.is_visible(page.SEARCH_INPUT)

        with allure.step("Verify table is visible"):
            assert page.is_visible(page.TABLE)

        with allure.step("Verify table contains records"):
            assert page.rows_count() > 0

    @allure.story("Web Tables page")
    @allure.title("Default records are displayed")
    @allure.description(
        "Verifies that the Web Tables page displays the three default records."
    )
    @pytest.mark.positive
    def test_default_records_are_displayed(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Wait for default records to be displayed"):
            WebDriverWait(driver, 10).until(lambda driver: len(page.row_texts()) == 3)

        with allure.step("Get default table records"):
            rows = page.row_texts()

        with allure.step("Verify number of default records"):
            assert len(rows) == 3

        with allure.step("Verify Cierra record"):
            assert any("Cierra" in row for row in rows)

        with allure.step("Verify Alden record"):
            assert any("Alden" in row for row in rows)

        with allure.step("Verify Kierra record"):
            assert any("Kierra" in row for row in rows)

    @allure.story("Registration form")
    @allure.title("Registration form opens")
    @allure.description(
        "Verifies that clicking the Add button opens the registration form with all required input fields."
    )
    @pytest.mark.positive
    def test_open_registration_form(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Verify registration form is initially closed"):
            assert not page.is_visible(page.FIRST_NAME_INPUT)

        with allure.step("Click Add button"):
            page.open_registration_form()

        with allure.step("Verify First Name field is visible"):
            assert page.is_visible(page.FIRST_NAME_INPUT)

        with allure.step("Verify Last Name field is visible"):
            assert page.is_visible(page.LAST_NAME_INPUT)

        with allure.step("Verify Email field is visible"):
            assert page.is_visible(page.EMAIL_INPUT)

        with allure.step("Verify Age field is visible"):
            assert page.is_visible(page.AGE_INPUT)

        with allure.step("Verify Salary field is visible"):
            assert page.is_visible(page.SALARY_INPUT)

        with allure.step("Verify Department field is visible"):
            assert page.is_visible(page.DEPARTMENT_INPUT)

        with allure.step("Verify Submit field is visible"):
            assert page.is_visible(page.SUBMIT_BUTTON)

    @allure.story("Record creation")
    @allure.title("New record can be added")
    @allure.description(
        "Verifies that a new record can be created using valid data and displayed in the Web Tables."
    )
    @pytest.mark.positive
    def test_add_record(self, driver, faker: Faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        age = faker.random_int(min=18, max=80)
        salary = faker.random_int(min=1000, max=100000)
        department = "Department"

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Add new record"):
            page.add_record(
                first_name=first_name,
                last_name=last_name,
                email=email,
                age=age,
                salary=salary,
                department=department,
            )

        with allure.step("Wait for new record to appear"):
            page.wait_until_record_exists(email)

        with allure.step("Verify First Name"):
            assert page.record_exists(first_name)

        with allure.step("Verify Last Name"):
            assert page.record_exists(last_name)

        with allure.step("Verify Email"):
            assert page.record_exists(email)

        with allure.step("Verify Age"):
            assert page.record_exists(str(age))

        with allure.step("Verify Salary"):
            assert page.record_exists(str(salary))

        with allure.step("Verify Department"):
            assert page.record_exists(department)

        with allure.step("Verify registration form is closed"):
            assert not page.is_visible(page.FIRST_NAME_INPUT)

    @allure.story("Search")
    @allure.title("Existing record can be searched")
    @allure.description(
        "Verifies that entering an existing user's name into the search field filters the table to the matching record."
    )
    @pytest.mark.positive
    def test_search_record(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        search_value = "Cierra"

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Search for existing record"):
            page.search(search_value)

        with allure.step("Wait for search results"):
            WebDriverWait(driver, 10).until(lambda driver: len(page.row_texts()) == 1)

        with allure.step("Verify search field value"):
            assert page.search_value() == search_value

        with allure.step("Get filtered rows"):
            rows = page.row_texts()

        with allure.step("Verify exactly one record is displayed"):
            assert len(rows) == 1

        with allure.step("Verify matching record"):
            assert "Cierra" in rows[0]

        with allure.step("Verify searched value exists in table"):
            assert page.record_exists(search_value)

    @allure.story("Search")
    @allure.title("Unknown record is not found")
    @allure.description(
        "Verifies that searching for a value that does not exist returns no table records."
    )
    @pytest.mark.negative
    def test_search_unknown_record(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        search_value = "UnknownUser123"

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Search for unknown record"):
            page.search(search_value)

        with allure.step("Wait for table to become empty"):
            WebDriverWait(driver, 10).until(lambda driver: page.row_texts() == [])

        with allure.step("Verify search field value"):
            assert page.search_value() == search_value

        with allure.step("Verify search value is absent"):
            assert page.record_not_exists(search_value)

        with allure.step("Verify no rows are displayed"):
            assert page.row_texts() == []

    @allure.story("Search")
    @allure.title("Search can be cleared")
    @allure.description(
        "Verifies that clearing the search field restores all default records."
    )
    @pytest.mark.positive
    def test_clear_search(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Search for Cierra"):
            page.search("Cierra")

        with allure.step("Wait for filtered result"):
            WebDriverWait(driver, 10).until(lambda driver: len(page.row_texts()) == 1)

        with allure.step("Verify search value"):
            assert page.search_value() == "Cierra"

        with allure.step("Verify one record is displayed"):
            assert page.rows_count() == 1

        with allure.step("Clear search field"):
            page.clear_search()

        with allure.step("Wait for all default records to return"):
            WebDriverWait(driver, 10).until(lambda driver: len(page.row_texts()) == 3)

        with allure.step("Verify search field is empty"):
            assert page.search_value() == ""

        with allure.step("Verify all three records are displayed"):
            assert page.rows_count() == 3

        with allure.step("Verify Cierra is displayed"):
            assert page.record_exists("Cierra")

        with allure.step("Verify Alden is displayed"):
            assert page.record_exists("Alden")

        with allure.step("Verify Kierra is displayed"):
            assert page.record_exists("Kierra")

    @allure.story("Record editing")
    @allure.title("Search can be edited")
    @allure.description(
        "Verifies that clicking the Edit button opens the registration form populated with the selected record."
    )
    @pytest.mark.positive
    def test_edit_record(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Click Edit for the first record"):
            page.edit_record()

        with allure.step("Verify registration form is opened"):
            assert page.is_visible(page.REGISTRATION_FORM)

        with allure.step("Verify First Name field"):
            assert page.is_visible(page.FIRST_NAME_INPUT)

        with allure.step("Verify Last Name field"):
            assert page.is_visible(page.LAST_NAME_INPUT)

        with allure.step("Verify Email field"):
            assert page.is_visible(page.EMAIL_INPUT)

        with allure.step("Verify Age field"):
            assert page.is_visible(page.AGE_INPUT)

        with allure.step("Verify Salary field"):
            assert page.is_visible(page.SALARY_INPUT)

        with allure.step("Verify Department field"):
            assert page.is_visible(page.DEPARTMENT_INPUT)

        with allure.step("Verify Submit button"):
            assert page.is_visible(page.SUBMIT_BUTTON)

    @allure.story("Record deletion")
    @allure.title("Record can be deleted")
    @allure.description(
        "Verifies that an existing record can be deleted and the number of table rows decreases by one."
    )
    @pytest.mark.positive
    def test_delete_record(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        email = "cierra@example.com"

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Verify target record exists"):
            assert page.record_exists(email)

        with allure.step("Save initial rows count"):
            initial_rows_count = page.rows_count()

        with allure.step("Delete target record"):
            page.delete_record()

        with allure.step("Wait until target record disappears"):
            page.wait_until_record_not_exists(email)

        with allure.step("Verify target record is deleted"):
            assert page.record_not_exists(email)

        with allure.step("Verify rows count decreased by one"):
            WebDriverWait(driver, 10).until(
                lambda driver: page.rows_count() == initial_rows_count - 1
            )

        assert page.rows_count() == initial_rows_count - 1

    @allure.story("Record lifecycle")
    @allure.title("Record can be created and deleted")
    @allure.description(
        "Verifies the complete lifecycle of a record: creation, search, verification, and deletion."
    )
    @pytest.mark.positive
    def test_create_and_delete_record(self, driver, faker: Faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        age = faker.random_int(min=18, max=80)
        salary = faker.random_int(min=1000, max=100000)
        department = "Department"

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Create a new record"):
            page.add_record(
                first_name=first_name,
                last_name=last_name,
                email=email,
                age=age,
                salary=salary,
                department=department,
            )

        with allure.step("Wait for created record"):
            page.wait_until_record_exists(email)

        with allure.step("Verify created record"):
            assert page.record_exists(email)

        with allure.step("Search for created record"):
            page.search(email)

        with allure.step("Wait for search result"):
            WebDriverWait(driver, 10).until(lambda driver: len(page.row_texts()) == 1)

        with allure.step("Verify exactly one matching row"):
            assert page.rows_count() == 1

        with allure.step("Delete created record"):
            page.delete_record()

        with allure.step("Wait until created record disappears"):
            page.wait_until_record_not_exists(email)

        with allure.step("Verify created record is deleted"):
            assert page.record_not_exists(email)

    @allure.story("Row actions")
    @allure.title("Every row has Edit and Delete buttons")
    @allure.description(
        "Verifies that every displayed table row contains both Edit and Delete action buttons."
    )
    @pytest.mark.positive
    def test_row_action_buttons_are_available(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = WebTablesPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Web Tables page"):
            elements_page.open_web_tables()

        with allure.step("Wait for default rows"):
            WebDriverWait(driver, 10).until(lambda driver: len(page.rows()) == 3)

        with allure.step("Get table rows"):
            rows = page.rows()

        with allure.step("Get Edit buttons"):
            edit_buttons = page.edit_buttons()

        with allure.step("Get Delete buttons"):
            delete_buttons = page.delete_buttons()

        with allure.step("Verify three rows are displayed"):
            assert len(rows) == 3

        with allure.step("Verify each row has an Edit button"):
            assert len(edit_buttons) == len(rows)

        with allure.step("Verify each row has an Delete button"):
            assert len(delete_buttons) == len(rows)

        with allure.step("Verify action buttons inside every row"):
            for row in rows:
                assert row.find_element(
                    By.CSS_SELECTOR, "[title='Edit']"
                ).is_displayed()
                assert row.find_element(
                    By.CSS_SELECTOR, "[title='Delete']"
                ).is_displayed()
