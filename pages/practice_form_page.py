from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class PracticeFormPage(BasePage):
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

    MALE_RADIO = (
        By.CSS_SELECTOR,
        "label[for='gender-radio-1']",
    )

    FEMALE_RADIO = (
        By.CSS_SELECTOR,
        "label[for='gender-radio-2']",
    )

    OTHER_RADIO = (
        By.CSS_SELECTOR,
        "label[for='gender-radio-3']",
    )

    MOBILE_INPUT = (
        By.ID,
        "userNumber",
    )

    DATE_OF_BIRTH_INPUT = (
        By.ID,
        "dateOfBirthInput",
    )

    SUBJECTS_INPUT = (
        By.ID,
        "subjectsInput",
    )

    SPORTS_CHECKBOX = (
        By.CSS_SELECTOR,
        "label[for='hobbies-checkbox-1']",
    )

    READING_CHECKBOX = (
        By.CSS_SELECTOR,
        "label[for='hobbies-checkbox-2']",
    )

    MUSIC_CHECKBOX = (
        By.CSS_SELECTOR,
        "label[for='hobbies-checkbox-3']",
    )

    PICTURE_INPUT = (
        By.ID,
        "uploadPicture",
    )

    CURRENT_ADDRESS_TEXTAREA = (
        By.ID,
        "currentAddress",
    )

    STATE_INPUT = (
        By.ID,
        "react-select-3-input",
    )

    CITY_INPUT = (
        By.ID,
        "react-select-4-input",
    )

    SUBMIT_BUTTON = (
        By.ID,
        "submit",
    )

    MODAL = (
        By.CLASS_NAME,
        "modal-content",
    )

    MODAL_TITLE = (
        By.ID,
        "example-modal-sizes-title-lg",
    )

    RESULT_TABLE = (
        By.CLASS_NAME,
        "table",
    )

    RESULT_ROWS = (
        By.CSS_SELECTOR,
        ".table tbody tr",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def enter_first_name(self, first_name: str) -> None:
        self.type(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.type(self.LAST_NAME_INPUT, last_name)

    def enter_email(self, email: str) -> None:
        self.type(self.EMAIL_INPUT, email)

    def enter_mobile(self, mobile: str) -> None:
        self.type(self.MOBILE_INPUT, mobile)

    def first_name_value(self) -> str | None:
        return self.attribute(self.FIRST_NAME_INPUT, "value")

    def last_name_value(self) -> str | None:
        return self.attribute(self.LAST_NAME_INPUT, "value")

    def email_value(self) -> str | None:
        return self.attribute(self.EMAIL_INPUT, "value")

    def mobile_value(self) -> str | None:
        return self.attribute(self.MOBILE_INPUT, "value")

    def select_male(self) -> None:
        self.click(self.MALE_RADIO)

    def select_female(self) -> None:
        self.click(self.FEMALE_RADIO)

    def select_other(self) -> None:
        self.click(self.OTHER_RADIO)

    def male_selected(self) -> bool:
        return self.is_selected(
            (
                By.ID,
                "gender-radio-1"
            )
        )

    def female_selected(self) -> bool:
        return self.is_selected(
            (
                By.ID,
                "gender-radio-2"
            )
        )

    def other_selected(self) -> bool:
        return self.is_selected(
            (
                By.ID,
                "gender-radio-3"
            )
        )

    def enter_date_of_birth(self, date: str) -> None:
        self.click(self.DATE_OF_BIRTH_INPUT)

        self.execute_script(
            """
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(
                new Event('input', { bubbles: true })
            );
            arguments[0].dispatchEvent(
                new Event('change', { bubbles: true })
            );
            """,
            self.wait_visible(self.DATE_OF_BIRTH_INPUT),
            date,
        )

    def date_of_birth_value(self) -> str | None:
        return self.attribute(
            self.DATE_OF_BIRTH_INPUT,
            "value",
        )

    def enter_subject(self, subject: str) -> None:
        self.type(self.SUBJECTS_INPUT, subject)

    def select_subject(self, subject: str) -> None:
        self.enter_subject(subject)

        option = (
            By.XPATH,
            f"//div[contains(@class, 'subjects-auto-complete__option') "
            f"and normalize-space()='{subject}']",
        )

        self.click(option)

    def subjects_value(self) -> str | None:
        return self.attribute(
            self.SUBJECTS_INPUT,
            "value"
        )

    def select_sports(self) -> None:
        self.click(self.SPORTS_CHECKBOX)

    def select_reading(self) -> None:
        self.click(self.READING_CHECKBOX)

    def select_music(self) -> None:
        self.click(self.MUSIC_CHECKBOX)

    def sports_selected(self) -> bool:
        return self.is_selected(
            (
                By.ID,
                "hobbies-checkbox-1",
            )
        )

    def reading_selected(self) -> bool:
        return self.is_selected(
            (
                By.ID,
                "hobbies-checkbox-2",
            )
        )

    def music_selected(self) -> bool:
        return self.is_selected(
            (
                By.ID,
                "hobbies-checkbox-3",
            )
        )

    def upload_picture(self, file_path: str) -> None:
        self.wait_visible(self.PICTURE_INPUT).send_keys(file_path)

    def enter_current_address(self, address: str) -> None:
        self.type(self.CURRENT_ADDRESS_TEXTAREA, address)

    def current_address_value(self) -> str | None:
        return self.attribute(
            self.CURRENT_ADDRESS_TEXTAREA,
            "value",
        )

    def select_state(self, state: str) -> None:
        self.click(self.STATE_INPUT)

        option = (
            By.XPATH,
            f"//div[contains(@class, 'option') "
            f"and normalize-space()='{state}']",
        )

        self.click(option)

    def select_city(self, city: str) -> None:
        self.click(self.CITY_INPUT)

        option = (
            By.XPATH,
            f"//div[contains(@class, 'option') "
            f"and normalize-space()='{city}']",
        )

        self.click(option)

    def submit(self) -> None:
        self.js_click(self.SUBMIT_BUTTON)

    def result_visible(self) -> bool:
        return self.is_visible(self.MODAL)

    def result_title(self) -> str:
        return self.text(self.MODAL_TITLE)

    def result_table_visible(self) -> bool:
        return self.is_visible(self.RESULT_TABLE)

    def result_rows(self) -> list[str]:
        return [
            row.text
            for row in self.wait_all_present(self.RESULT_ROWS)
        ]

    def result_text(self) -> str:
        return self.text(self.RESULT_TABLE)

    def fill_form(
            self,
            first_name: str,
            last_name: str,
            email: str,
            gender: str,
            mobile: str,
            date_of_birth: str,
            subject: str,
            hobby: str,
            picture_path: str,
            current_address: str,
            state: str,
            city: str
    ) -> None:
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)

        gender_selectors = {
            "Male": self.select_male,
            "Female": self.select_female,
            "Other": self.select_other,
        }

        gender_selectors[gender]()

        self.enter_mobile(mobile)
        self.enter_date_of_birth(date_of_birth)
        self.select_subject(subject)

        hobby_selectors = {
            "Sports": self.select_sports,
            "Reading": self.select_reading,
            "Music": self.select_music,
        }

        hobby_selectors[hobby]()

        self.upload_picture(picture_path)
        self.enter_current_address(current_address)
        self.select_state(state)
        self.select_city(city)

    def submit_form(
            self,
            first_name: str,
            last_name: str,
            email: str,
            gender: str,
            mobile: str,
            date_of_birth: str,
            subject: str,
            hobby: str,
            picture_path: str,
            current_address: str,
            state: str,
            city: str
    ) -> None:
        self.fill_form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            mobile=mobile,
            date_of_birth=date_of_birth,
            subject=subject,
            hobby=hobby,
            picture_path=picture_path,
            current_address=current_address,
            state=state,
            city=city,
        )

        self.submit()
