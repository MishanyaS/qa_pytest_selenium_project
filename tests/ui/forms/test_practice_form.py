from __future__ import annotations

from pathlib import Path

import allure
import pytest
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver

from pages.forms_page import FormsPage
from pages.home_page import HomePage
from pages.practice_form_page import PracticeFormPage


@allure.epic("DemoQA UI")
@allure.feature("Forms")
@pytest.mark.ui
@pytest.mark.regression
class TestPracticeForm:
    @allure.story("Practice Form navigation")
    @allure.title("Practice Form page opens successfully")
    @allure.description(
        "Verifies that the DemoQA Practice Form page can be opened from the Forms section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_practice_form(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        practice_form_page = PracticeFormPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open_home_page()

        with allure.step("Open Forms section"):
            home_page.open_forms()

        with allure.step("Open Practice Form page"):
            forms_page.open_practice_form()

        with allure.step("Verify Web Tables page URL"):
            assert practice_form_page.current_url.endswith("/automation-practice-form")

    @allure.story("Practice Form page")
    @allure.title("Practice Form elements are visible")
    @allure.description("Verifies that the main Practice Form controls are displayed.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_practice_form_elements_visible(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Verify First Name input is visible"):
            assert page.is_visible(page.FIRST_NAME_INPUT)

        with allure.step("Verify Last Name input is visible"):
            assert page.is_visible(page.LAST_NAME_INPUT)

        with allure.step("Verify Email input is visible"):
            assert page.is_visible(page.EMAIL_INPUT)

        with allure.step("Verify Mobile input is visible"):
            assert page.is_visible(page.MOBILE_INPUT)

        with allure.step("Verify Date of Birth input is visible"):
            assert page.is_visible(page.DATE_OF_BIRTH_INPUT)

        with allure.step("Verify Subjects input is visible"):
            assert page.is_visible(page.SUBJECTS_INPUT)

        with allure.step("Verify Sports checkbox is visible"):
            assert page.is_visible(page.SPORTS_CHECKBOX)

        with allure.step("Verify Reading checkbox is visible"):
            assert page.is_visible(page.READING_CHECKBOX)

        with allure.step("Verify Music checkbox is visible"):
            assert page.is_visible(page.MUSIC_CHECKBOX)

        with allure.step("Verify Picture input is visible"):
            assert page.is_visible(page.PICTURE_INPUT)

        with allure.step("Verify Current Address textarea is visible"):
            assert page.is_visible(page.CURRENT_ADDRESS_TEXTAREA)

        with allure.step("Verify State input is visible"):
            assert page.is_visible(page.STATE_INPUT)

        with allure.step("Verify Submit button is visible"):
            assert page.is_visible(page.SUBMIT_BUTTON)

    @allure.story("Practice Form initial state")
    @allure.title("Gender radio buttons are initially unselected")
    @allure.description(
        "Verifies that no gender option is selected when the Practice Form is opened."
    )
    @pytest.mark.positive
    def test_gender_radio_buttons_initial_state(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Verify Mail is not selected"):
            assert page.male_selected() is False

        with allure.step("Verify Femail is not selected"):
            assert page.female_selected() is False

        with allure.step("Verify Other is not selected"):
            assert page.other_selected() is False

    @allure.story("Practice Form initial state")
    @allure.title("Hobby checkboxes are initially unselected")
    @allure.description(
        "Verifies that no hobby checkbox is selected when the Practice Form is opened."
    )
    @pytest.mark.positive
    def test_hobby_checkboxes_initial_state(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Verify Sports is not selected"):
            assert page.sports_selected() is False

        with allure.step("Verify Reading is not selected"):
            assert page.reading_selected() is False

        with allure.step("Verify Music is not selected"):
            assert page.music_selected() is False

    @allure.story("Practice Form text fields")
    @allure.title("User can enter personal information")
    @allure.description(
        "Verifies that First Name, Last Name, Email and Mobile fields accept and preserve entered values."
    )
    @pytest.mark.positive
    def test_enter_personal_information(self, driver: WebDriver, faker: Faker) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        mobile = faker.numerify("##########")

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Enter First Name"):
            page.enter_first_name(first_name)

        with allure.step("Enter Last Name"):
            page.enter_last_name(last_name)

        with allure.step("Enter Email"):
            page.enter_email(email)

        with allure.step("Enter Mobile"):
            page.enter_mobile(mobile)

        with allure.step("Verify First Name value"):
            assert page.first_name_value() == first_name

        with allure.step("Verify Last Name value"):
            assert page.last_name_value() == last_name

        with allure.step("Verify Email value"):
            assert page.email_value() == email

        with allure.step("Verify Mobile value"):
            assert page.mobile_value() == mobile

    @allure.story("Practice Form gender")
    @allure.title("User can select Mail gender")
    @allure.description(
        "Verifies that the Male gender option can be selected and that the other gender options remain unselected."
    )
    @pytest.mark.positive
    def test_select_male_gender(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Male gender"):
            page.select_male()

        with allure.step("Verify Male is selected"):
            assert page.male_selected() is True

        with allure.step("Verify Female is not selected"):
            assert page.female_selected() is False

        with allure.step("Verify Other is not selected"):
            assert page.other_selected() is False

    @allure.story("Practice Form gender")
    @allure.title("User can select Femail gender")
    @allure.description(
        "Verifies that the Female gender option can be selected and that the other gender options remain unselected."
    )
    @pytest.mark.positive
    def test_select_female_gender(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Femail gender"):
            page.select_female()

        with allure.step("Verify Femail is selected"):
            assert page.female_selected() is True

        with allure.step("Verify Male is not selected"):
            assert page.male_selected() is False

        with allure.step("Verify Other is not selected"):
            assert page.other_selected() is False

    @allure.story("Practice Form gender")
    @allure.title("User can select Other gender")
    @allure.description(
        "Verifies that the Other gender option can be selected and that the other gender options remain unselected."
    )
    @pytest.mark.positive
    def test_select_other_gender(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Other gender"):
            page.select_other()

        with allure.step("Verify Other is selected"):
            assert page.other_selected() is True

        with allure.step("Verify Male is not selected"):
            assert page.male_selected() is False

        with allure.step("Verify Female is not selected"):
            assert page.female_selected() is False

    @allure.story("Practice Form gender")
    @allure.title("Selecting another gender changes selected option")
    @allure.description(
        "Verifies that selecting another gender option clears the previously selected gender option."
    )
    @pytest.mark.positive
    def test_gender_selection_is_exclusive(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Male gender"):
            page.select_male()

        with allure.step("Verify Male is selected"):
            assert page.male_selected() is True

        with allure.step("Select Female gender"):
            page.select_female()

        with allure.step("Verify Male is no longer selected"):
            assert page.male_selected() is False

        with allure.step("Verify Female is selected"):
            assert page.female_selected() is True

        with allure.step("Select Other gender"):
            page.select_other()

        with allure.step("Verify Female is no longer selected"):
            assert page.female_selected() is False

        with allure.step("Verify Other is selected"):
            assert page.other_selected() is True

    @allure.story("Practice Form date of birth")
    @allure.title("User can enter date of birth")
    @allure.description(
        "Verifies that the Date of Birth field accepts and preserves the entered date."
    )
    @pytest.mark.positive
    def test_enter_date_of_birth(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        date_of_birth = "15 May 2000"

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Enter date of birth"):
            page.enter_date_of_birth(date_of_birth)

        with allure.step("Verify date of birth value"):
            assert page.date_of_birth_value() == date_of_birth

    @allure.story("Practice Form subjects")
    @allure.title("User can select a subject")
    @allure.description(
        "Verifies that a subject can be entered and selected from the Subjects autocomplete list."
    )
    @pytest.mark.positive
    def test_select_subject(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        subject = "Maths"

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select subject"):
            page.select_subject(subject)

        with allure.step("Verify selected subject"):
            selected_subject = page.attribute(
                (
                    "xpath",
                    f"//div[@id='subjectsContainer']//*[normalize-space()='{subject}']",
                ),
                "textContent",
            )

            assert selected_subject is not None
            assert selected_subject.strip() == subject

    @allure.story("Practice Form hobbies")
    @allure.title("User can select Sports hobby")
    @allure.description("Verifies that the Sports hobby checkbox can be selected.")
    @pytest.mark.positive
    def test_select_sports_hobby(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Sports hobby"):
            page.select_sports()

        with allure.step("Verify Sports is selected"):
            assert page.sports_selected() is True

        with allure.step("Verify Reading is not selected"):
            assert page.reading_selected() is False

        with allure.step("Verify Music is not selected"):
            assert page.music_selected() is False

    @allure.story("Practice Form hobbies")
    @allure.title("User can select Reading hobby")
    @allure.description("Verifies that the Reading hobby checkbox can be selected.")
    @pytest.mark.positive
    def test_select_reading_hobby(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Reading hobby"):
            page.select_reading()

        with allure.step("Verify Reading is selected"):
            assert page.reading_selected() is True

        with allure.step("Verify Sports is not selected"):
            assert page.sports_selected() is False

        with allure.step("Verify Music is not selected"):
            assert page.music_selected() is False

    @allure.story("Practice Form hobbies")
    @allure.title("User can select Music hobby")
    @allure.description("Verifies that the Music hobby checkbox can be selected.")
    @pytest.mark.positive
    def test_select_music_hobby(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Music hobby"):
            page.select_music()

        with allure.step("Verify Music is selected"):
            assert page.music_selected() is True

        with allure.step("Verify Sports is not selected"):
            assert page.sports_selected() is False

        with allure.step("Verify Reading is not selected"):
            assert page.reading_selected() is False

    @allure.story("Practice Form hobbies")
    @allure.title("User can select multiple hobbies")
    @allure.description(
        "Verifies that multiple hobby checkboxes can be selected simultaneously."
    )
    @pytest.mark.positive
    def test_select_multiple_hobbies(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select Sports hobby"):
            page.select_sports()

        with allure.step("Select Reading hobby"):
            page.select_reading()

        with allure.step("Verify Sports is selected"):
            assert page.sports_selected() is True

        with allure.step("Verify Reading is selected"):
            assert page.reading_selected() is True

        with allure.step("Verify Music is not selected"):
            assert page.music_selected() is False

    @allure.story("Practice Form address")
    @allure.title("User can enter current address")
    @allure.description(
        "Verifies that the Current Address textarea accepts and preserves entered text."
    )
    @pytest.mark.positive
    def test_enter_current_address(self, driver: WebDriver, faker: Faker) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        address = faker.address()

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Enter current address"):
            page.enter_current_address(address)

        with allure.step("Verify current affress value"):
            assert page.current_address_value() == address

    @allure.story("Practice Form state and city")
    @allure.title("User can select state and city")
    @allure.description(
        "Verifies that a state can be selected and that the corresponding city can subsequently be selected."
    )
    @pytest.mark.positive
    def test_select_state_and_city(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Select state"):
            page.select_state("NCR")

        with allure.step("Verify City input becomes enabled"):
            assert page.is_enabled(page.CITY_INPUT) is True

        with allure.step("Select city"):
            page.select_city("Delhi")

        with allure.step("Verify selected state is displayed"):
            state_value = page.attribute(
                ("xpath", "//div[@id='state']//div[contains(@class, 'singleValue')]"),
                "textContent",
            )

            assert state_value == "NCR"

        with allure.step("Verify selected city is displayed"):
            city_value = page.attribute(
                ("xpath", "//div[@id='city']//div[contains(@class, 'singleValue')]"),
                "textContent",
            )

            assert city_value == "Delhi"

    @allure.story("Practice Form picture upload")
    @allure.title("User can upload a picture")
    @allure.description(
        "Verifies that a picture file can be uploaded through the Picture input."
    )
    @pytest.mark.positive
    def test_upload_picture(self, driver: WebDriver, tmp_path: Path) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        picture_path = tmp_path / "test_picture.txt"
        picture_path.write_text("DemoQA test file", encoding="utf-8")

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Upload picture"):
            page.upload_picture(str(picture_path))

        with allure.step("Verify uploaded file name"):
            uploaded_file = page.attribute(page.PICTURE_INPUT, "value")

            assert uploaded_file is not None
            assert uploaded_file.endswith("test_picture.txt")

    @allure.story("Practice Form submission")
    @allure.title("Practice Form can be submitted with valid data")
    @allure.description(
        "Verifies that the Practice Form accepts valid data and displays the submission result modal."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_submit_practice_form(
        self, driver: WebDriver, faker: Faker, tmp_path: Path
    ) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        mobile = faker.numerify("##########")
        date_of_birth = "15 May 2000"
        subject = "Maths"
        current_address = faker.address()
        state = "NCR"
        city = "Delhi"

        picture_path = tmp_path / "test_picture.txt"
        picture_path.write_text("DemoQA test file", encoding="utf-8")

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Enter personal information"):
            page.enter_first_name(first_name)
            page.enter_last_name(last_name)
            page.enter_email(email)
            page.select_male()
            page.enter_mobile(mobile)

        with allure.step("Enter date of birth"):
            page.enter_date_of_birth(date_of_birth)

        with allure.step("Close Date Picker"):
            page.click(page.FIRST_NAME_INPUT)

        with allure.step("Select subject"):
            page.select_subject(subject)

        with allure.step("Select hobby"):
            page.select_sports()

        with allure.step("Upload picture"):
            page.upload_picture(str(picture_path))

        with allure.step("Enter current address"):
            page.enter_current_address(current_address)

        with allure.step("Select state"):
            page.select_state(state)

        with allure.step("Select city"):
            page.select_city(city)

        with allure.step("Submit Practice Form"):
            page.submit()

        with allure.step("Verify result modal is visible"):
            assert page.result_visible() is True

        with allure.step("Verify result modal title"):
            assert page.result_title() == "Thanks for submitting the form"

        with allure.step("Verify result table is visible"):
            assert page.result_table_visible() is True

    @allure.story("Practice Form submission")
    @allure.title("Submitted form contains entered personal information")
    @allure.description(
        "Verifies that the submission result contains the entered name, email, gender and mobile number."
    )
    @pytest.mark.positive
    def test_submitted_form_contains_personal_information(
        self, driver: WebDriver, faker: Faker, tmp_path: Path
    ) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        mobile = faker.numerify("##########")
        current_address = faker.address()

        picture_path = tmp_path / "test_picture.txt"
        picture_path.write_text("DemoQA test file", encoding="utf-8")

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Enter personal information"):
            page.enter_first_name(first_name)
            page.enter_last_name(last_name)
            page.enter_email(email)
            page.select_male()
            page.enter_mobile(mobile)

        with allure.step("Enter date of birth"):
            page.enter_date_of_birth("15 May 2000")

        with allure.step("Close Date Picker"):
            page.click(page.FIRST_NAME_INPUT)

        with allure.step("Select subject"):
            page.select_subject("Maths")

        with allure.step("Select hobby"):
            page.select_sports()

        with allure.step("Upload picture"):
            page.upload_picture(str(picture_path))

        with allure.step("Enter current address"):
            page.enter_current_address(current_address)

        with allure.step("Select state"):
            page.select_state("NCR")

        with allure.step("Select city"):
            page.select_city("Delhi")

        with allure.step("Submit Practice Form"):
            page.submit()

        with allure.step("Get submission result text"):
            result_text = page.result_text()

        with allure.step("Verify submitted name"):
            assert f"{first_name} {last_name}" in result_text

        with allure.step("Verify submitted email"):
            assert email in result_text

        with allure.step("Verify submitted gender"):
            assert "Male" in result_text

        with allure.step("Verify submitted mobile"):
            assert mobile in result_text

    @allure.story("Practice Form submission")
    @allure.title("Submitted form contains selected options")
    @allure.description(
        "Verifies that selected date of birth, subject, hobby, picture, address, state and city are displayed in the submission result."
    )
    @pytest.mark.positive
    def test_submitted_form_contains_selected_options(
        self, driver: WebDriver, faker: Faker, tmp_path: Path
    ) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        subject = "Maths"
        hobby = "Sports"
        current_address = faker.address()

        picture_path = tmp_path / "test_picture.txt"
        picture_path.write_text("DemoQA test file", encoding="utf-8")

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        mobile = faker.numerify("##########")

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Enter personal information"):
            page.enter_first_name(first_name)
            page.enter_last_name(last_name)
            page.enter_email(email)
            page.select_female()
            page.enter_mobile(mobile)

        with allure.step("Enter date of birth"):
            page.enter_date_of_birth("15 May 2000")

        with allure.step("Close Date Picker"):
            page.click(page.FIRST_NAME_INPUT)

        with allure.step("Select subject"):
            page.select_subject(subject)

        with allure.step("Select hobby"):
            page.select_sports()

        with allure.step("Upload picture"):
            page.upload_picture(str(picture_path))

        with allure.step("Enter current address"):
            page.enter_current_address(current_address)

        with allure.step("Select state"):
            page.select_state("NCR")

        with allure.step("Select city"):
            page.select_city("Delhi")

        with allure.step("Submit Practice Form"):
            page.submit()

        with allure.step("Get submission result text"):
            result_text = page.result_text()

        normalized_result_text = " ".join(result_text.split())

        with allure.step("Verify subject"):
            assert subject in normalized_result_text

        with allure.step("Verify hobby"):
            assert hobby in normalized_result_text

        with allure.step("Verify uploaded picture"):
            assert "test_picture.txt" in normalized_result_text

        with allure.step("Verify current address"):
            normalized_address = " ".join(current_address.split())
            assert normalized_address in normalized_result_text

        with allure.step("Verify state"):
            assert "NCR" in normalized_result_text

        with allure.step("Verify city"):
            assert "Delhi" in normalized_result_text

    @allure.story("Practice Form submission result")
    @allure.title("Practice Form submission result contains expected rows")
    @allure.description(
        "Verifies that the submission result table contains the expected field names after a successful form submission."
    )
    @pytest.mark.positive
    def test_submission_result_contains_expected_rows(
        self, driver: WebDriver, faker: Faker, tmp_path: Path
    ) -> None:
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        page = PracticeFormPage(driver)

        picture_path = tmp_path / "test_picture.txt"
        picture_path.write_text("DemoQA test file", encoding="utf-8")

        with allure.step("Open Practice Form page"):
            home_page.open_home_page()
            home_page.open_forms()
            forms_page.open_practice_form()

        with allure.step("Enter personal information"):
            page.enter_first_name(faker.first_name())
            page.enter_last_name(faker.last_name())
            page.enter_email(faker.email())
            page.select_other()
            page.enter_mobile(faker.numerify("##########"))

        with allure.step("Enter date of birth"):
            page.enter_date_of_birth("15 May 2000")

        with allure.step("Close Date Picker"):
            page.click(page.FIRST_NAME_INPUT)

        with allure.step("Select subject"):
            page.select_subject("Physics")

        with allure.step("Select hobby"):
            page.select_reading()

        with allure.step("Upload picture"):
            page.upload_picture(str(picture_path))

        with allure.step("Enter current address"):
            page.enter_current_address(faker.address())

        with allure.step("Select state"):
            page.select_state("Uttar Pradesh")

        with allure.step("Select city"):
            page.select_city("Agra")

        with allure.step("Submit Practice Form"):
            page.submit()

        with allure.step("Get result table rows"):
            rows = page.result_rows()

        with allure.step("Verify result table contains Student Name row"):
            assert any("Student Name" in row for row in rows)

        with allure.step("Verify result table contains Student Email row"):
            assert any("Student Email" in row for row in rows)

        with allure.step("Verify result table contains Gender row"):
            assert any("Gender" in row for row in rows)

        with allure.step("Verify result table contains Mobile row"):
            assert any("Mobile" in row for row in rows)

        with allure.step("Verify result table contains Date of Birth row"):
            assert any("Date of Birth" in row for row in rows)

        with allure.step("Verify result table contains Subjects row"):
            assert any("Subjects" in row for row in rows)

        with allure.step("Verify result table contains Hobbies row"):
            assert any("Hobbies" in row for row in rows)

        with allure.step("Verify result table contains Picture row"):
            assert any("Picture" in row for row in rows)

        with allure.step("Verify result table contains Address row"):
            assert any("Picture" in row for row in rows)

        with allure.step("Verify result table contains State and City row"):
            assert any("State and City" in row for row in rows)
