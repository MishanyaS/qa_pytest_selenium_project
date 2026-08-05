from __future__ import annotations

import allure
import pytest

from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.text_box_page import TextBoxPage


@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestTextBox:
    @allure.story("Text Box navigation")
    @allure.title("Text Box page opens successfully")
    @allure.description(
        "Verifies that the Text Box page can be opened from the Elements section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_text_box(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        text_box_page = TextBoxPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Text Box page"):
            elements_page.open_text_box()

        with allure.step("Verify Text Box page URL"):
            assert text_box_page.current_url.endswith("/text-box")

    @allure.story("Text Box page")
    @allure.title("Text Box form fields are visible")
    @allure.description(
        "Verifies that all required Text Box form fields and the Submit button are displayed."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_text_box_form_fields_visible(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Text Box page"):
            elements_page.open_text_box()

        with allure.step("Verify Full Name field"):
            assert page.is_visible(page.FULL_NAME_INPUT)

        with allure.step("Verify Email field"):
            assert page.is_visible(page.FULL_NAME_INPUT)

        with allure.step("Verify Current Address field"):
            assert page.is_visible(page.CURRENT_ADDRESS_TEXTAREA)

        with allure.step("Verify Permanent Address field"):
            assert page.is_visible(page.PERMANENT_ADDRESS_TEXTAREA)

        with allure.step("Verify Submit button"):
            assert page.is_visible(page.SUBMIT_BUTTON)

    @allure.story("Text Box input")
    @allure.title("User can enter full name")
    @allure.description(
        "Verifies that the Full Name input accepts and stores the entered value."
    )
    @pytest.mark.positive
    def test_enter_full_name(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        full_name = faker.name()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Enter full name"):
            page.enter_full_name(full_name)

        with allure.step("Verify entered full name"):
            assert page.full_name_value() == full_name

    @allure.story("Text Box input")
    @allure.title("User can enter email")
    @allure.description(
        "Verifies that the Email input accepts and stores a valid email address."
    )
    @pytest.mark.positive
    def test_enter_email(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        email = faker.email()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Enter email"):
            page.enter_email(email)

        with allure.step("Verify entered email"):
            assert page.email_value() == email

    @allure.story("Text Box input")
    @allure.title("User can enter current address")
    @allure.description(
        "Verifies that the Current Address textarea accepts and stores the entered value."
    )
    @pytest.mark.positive
    def test_enter_current_address(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        current_address = faker.address()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Enter current address"):
            page.enter_current_address(current_address)

        with allure.step("Verify entered current address"):
            assert page.current_address_value() == current_address

    @allure.story("Text Box input")
    @allure.title("User can enter permanent address")
    @allure.description(
        "Verifies that the Permanent Address textarea accepts and stores the entered value."
    )
    @pytest.mark.positive
    def test_enter_permanent_address(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        permanent_address = faker.address()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Enter permanent address"):
            page.enter_permanent_address(permanent_address)

        with allure.step("Verify entered permanent address"):
            assert page.permanent_address_value() == permanent_address

    @allure.story("Text Box form")
    @allure.title("User can fill the entire Text Box form")
    @allure.description(
        "Verifies that all Text Box fields can be populated with valid data."
    )
    @pytest.mark.positive
    def test_fill_form(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        full_name = faker.name()
        email = faker.email()
        current_address = faker.address()
        permanent_address = faker.address()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Fill Text Box form"):
            page.fill_form(
                full_name=full_name,
                email=email,
                current_address=current_address,
                permanent_address=permanent_address,
            )

        with allure.step("Verify Full Name value"):
            assert page.full_name_value() == full_name

        with allure.step("Verify Email value"):
            assert page.email_value() == email

        with allure.step("Verify Current Address value"):
            assert page.current_address_value() == current_address

        with allure.step("Verify Permanent Address value"):
            assert page.permanent_address_value() == permanent_address

    @allure.story("Text Box submission")
    @allure.title("Submitted data is displayed in output section")
    @allure.description(
        "Verifies that submitting the Text Box form displays the output section with entered data."
    )
    @pytest.mark.positive
    def test_submitted_data_is_displayed(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        full_name = faker.name()
        email = faker.email()
        current_address = faker.address()
        permanent_address = faker.address()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Submit Text Box form"):
            page.submit_form(
                full_name=full_name,
                email=email,
                current_address=current_address,
                permanent_address=permanent_address,
            )

        with allure.step("Verify output section is visible"):
            assert page.output_visible()

        with allure.step("Verify submitted name"):
            assert page.output_name() == f"Name:{full_name}"

        with allure.step("Verify submitted email"):
            assert page.output_email() == f"Email:{email}"

        with allure.step("Verify submitted current address"):
            actual_current_address = " ".join(page.output_current_address().split())
            expected_current_address = " ".join(current_address.split())

            assert (
                actual_current_address == f"Current Address :{expected_current_address}"
            )

        with allure.step("Verify submitted permanent address"):
            actual_permanent_address = " ".join(page.output_permanent_address().split())
            expected_permanent_address = " ".join(permanent_address.split())

            assert (
                actual_permanent_address
                == f"Permananet Address :{expected_permanent_address}"
            )

    @allure.story("Text Box submission")
    @allure.title("Submitted data is displayed correctly")
    @allure.description(
        "Verifies that each submitted field is displayed with the correct value in the output section."
    )
    @pytest.mark.positive
    def test_submitted_data_is_displayed_correctly(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        full_name = faker.name()
        email = faker.email()
        current_address = faker.address()
        permanent_address = faker.address()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Submit form with valid data"):
            page.submit_form(
                full_name=full_name,
                email=email,
                current_address=current_address,
                permanent_address=permanent_address,
            )

        with allure.step("Normalize current address"):
            actual_current_address = " ".join(page.output_current_address().split())
            expected_current_address = " ".join(current_address.split())

        with allure.step("Normalize permanent address"):
            actual_permanent_address = " ".join(page.output_permanent_address().split())
            expected_permanent_address = " ".join(permanent_address.split())

        with allure.step("Verify submitted name"):
            assert page.output_name() == f"Name:{full_name}"

        with allure.step("Verify submitted email"):
            assert page.output_email() == f"Email:{email}"

        with allure.step("Verify submitted current address"):
            actual_current_address = " ".join(page.output_current_address().split())
            expected_current_address = " ".join(current_address.split())

            assert (
                actual_current_address == f"Current Address :{expected_current_address}"
            )

        with allure.step("Verify submitted permanent address"):
            actual_permanent_address = " ".join(page.output_permanent_address().split())
            expected_permanent_address = " ".join(permanent_address.split())

            assert (
                actual_permanent_address
                == f"Permananet Address :{expected_permanent_address}"
            )

    @allure.story("Text Box validation")
    @allure.title("Invalid email is rejected by HTML validation")
    @allure.description(
        "Verifies that an invalid email value makes the Email input Invalid according to the browser HTML5 constraint validation."
    )
    @pytest.mark.negative
    def test_invalid_email(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        invalid_email = "invalid-email"

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Enter invalid email"):
            page.enter_email(invalid_email)

        with allure.step("Check HTML5 email validity"):
            email_element = page.find(page.EMAIL_INPUT)

            is_valid = page.execute_script(
                "return arguments[0].validity.valid;", email_element
            )

        with allure.step("Verify email is invalid"):
            assert is_valid is False

    @allure.story("Text Box validation")
    @allure.title("Valid email passes HTML validation")
    @allure.description(
        "Verifies that a correctly formatted email is considered valid by browser HTML5 constraint validation."
    )
    @pytest.mark.positive
    def test_valid_email(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        valid_email = faker.email()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Enter valid email"):
            page.enter_email(valid_email)

        with allure.step("Check HTML5 email validity"):
            email_element = page.find(page.EMAIL_INPUT)

            is_valid = page.execute_script(
                "return arguments[0].validity.valid;", email_element
            )

        with allure.step("Verify email is valid"):
            assert is_valid is True

    @allure.story("Text Box validation")
    @allure.title("Empty email field is accepted by HTML validation")
    @allure.description(
        "Verifies that an empty Email field is considered valid because the DemoQA Email input is not marked as required."
    )
    @pytest.mark.positive
    def test_empty_email(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Verify email field is empty"):
            assert page.email_value() == ""

        with allure.step("Check HTML5 email validity"):
            email_element = page.find(page.EMAIL_INPUT)

            is_valid = page.execute_script(
                "return arguments[0].validity.valid;", email_element
            )

        with allure.step("Verify empty email is accepted"):
            assert is_valid is True

    @allure.story("Text Box form")
    @allure.title("Form can be submitted with valid data")
    @allure.description(
        "Verifies that the Text Box form accepts valid input and displays the output section after submission."
    )
    @pytest.mark.positive
    def test_submit_valid_form(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        full_name = faker.name()
        email = faker.email()
        current_address = faker.address()
        permanent_address = faker.address()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Submit valid form"):
            page.submit_form(
                full_name=full_name,
                email=email,
                current_address=current_address,
                permanent_address=permanent_address,
            )

        with allure.step("Verify output section"):
            assert page.output_visible()

    @allure.story("Text Box clearing")
    @allure.title("Form fields can be cleared")
    @allure.description(
        "Verifies that entered values can be cleared from all Text Box form fields."
    )
    @pytest.mark.positive
    def test_clear_form_fields(self, driver, faker):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = TextBoxPage(driver)

        full_name = faker.name()
        email = faker.email()
        current_address = faker.address()
        permanent_address = faker.address()

        with allure.step("Open Text Box page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_text_box()

        with allure.step("Fill form"):
            page.fill_form(
                full_name=full_name,
                email=email,
                current_address=current_address,
                permanent_address=permanent_address,
            )

        with allure.step("Clear Full Name"):
            page.clear(page.FULL_NAME_INPUT)

        with allure.step("Clear Email"):
            page.clear(page.EMAIL_INPUT)

        with allure.step("Clear Current Address"):
            page.clear(page.CURRENT_ADDRESS_TEXTAREA)

        with allure.step("Clear Permanent Address"):
            page.clear(page.PERMANENT_ADDRESS_TEXTAREA)

        with allure.step("Verify Full Name is empty"):
            assert page.full_name_value() == ""

        with allure.step("Verify Email is empty"):
            assert page.email_value() == ""

        with allure.step("Verify Current Address is empty"):
            assert page.current_address_value() == ""

        with allure.step("Verify Permanent Address is empty"):
            assert page.permanent_address_value() == ""
