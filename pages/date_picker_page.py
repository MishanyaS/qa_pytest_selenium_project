from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class DatePickerPage(BasePage):
    SELECT_DATE_INPUT = (
        By.ID,
        "datePickerMonthYearInput"
    )

    DATE_AND_TIME_INPUT = (
        By.ID,
        "dateAndTimePickerInput"
    )

    MONTH_SELECT = (
        By.CLASS_NAME,
        "react-datepicker__month-select"
    )

    YEAR_SELECT = (
        By.CLASS_NAME,
        "react-datepicker__year-select"
    )

    PREVIOUS_MONTH_BUTTON = (
        By.CSS_SELECTOR,
        ".react-datepicker__navigation--previous"
    )

    NEXT_MONTH_BUTTON = (
        By.CSS_SELECTOR,
        ".react-datepicker__navigation--next"
    )

    DATE_PICKER = (
        By.CLASS_NAME,
        "react-datepicker"
    )

    DATE_AND_TIME_PICKER = (
        By.CLASS_NAME,
        "react-datepicker"
    )

    SELECTED_DATE = (
        By.CSS_SELECTOR,
        ".react-datepicker__day--selected"
    )

    TIME_LIST = (
        By.CSS_SELECTOR,
        ".react-datepicker__time-list-item"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
                            
    def open_date_picker(self) -> None:
        self.click(self.SELECT_DATE_INPUT)

    def open_date_and_time_picker(self) -> None:
        self.click(self.DATE_AND_TIME_INPUT)

    def date_input_visible(self) -> bool:
        return self.is_visible(self.SELECT_DATE_INPUT)

    def date_and_time_input_visible(self) -> bool:
        return self.is_visible(self.DATE_AND_TIME_INPUT)

    def date_input_value(self) -> str | None:
        return self.attribute(self.SELECT_DATE_INPUT, "value")

    def date_and_time_input_value(self) -> str | None:
        return self.attribute(self.DATE_AND_TIME_INPUT, "value")

    def date_picker_visible(self) -> bool:
        return self.is_visible(self.DATE_PICKER)

    def date_and_time_picker_visible(self) -> bool:
        return self.is_visible(self.DATE_AND_TIME_PICKER)

    def select_month(self, month: str) -> None:
        self.select_by_text(self.MONTH_SELECT, month)

    def select_year(self, year: str) -> None:
        self.select_by_value(self.YEAR_SELECT, year)

    def previous_month(self) -> None:
        self.click(self.PREVIOUS_MONTH_BUTTON)

    def next_month(self) -> None:
        self.click(self.NEXT_MONTH_BUTTON)

    def select_date(self, day: str) -> None:
        date = (
            By.XPATH,
            "//div[contains(@class, 'react-datepicker__day') "
            f"and normalize-space()='{day}' "
            "and not(contains(@class, 'react-datepicker__day--outside-month'))]",
        )

        self.click(date)

    def selected_date_visible(self) -> bool:
        return self.is_visible(self.SELECTED_DATE)

    def selected_date_text(self) -> str:
        return self.text(self.SELECTED_DATE)

    def select_date_by_month_year(self, month: str, year: str, day: str) -> None:
        self.open_date_picker()
        self.select_month(month)
        self.select_year(year)
        self.select_date(day)

    def select_date_and_time(self, month: str, year: str, day: str, time: str) -> None:
        self.open_date_and_time_picker()
        self.select_date(day)
        self.select_time(time)

    def time_options(self) -> list[str]:
        return [
            option.text
            for option in self.find_all(self.TIME_LIST)
        ]

    def select_time(self, time: str) -> None:
        time_option = (
            By.XPATH,
            "//li[contains(@class, "
            "'react-datepicker__time-list-item') "
            f"and normalize-space()='{time}']",
        )

        self.click(time_option)

    def time_options_visible(self) -> bool:
        return self.exists(self.TIME_LIST)

    def clear_date(self) -> None:
        self.clear(self.SELECT_DATE_INPUT)

    def clear_date_and_time(self) -> None:
        self.clear(self.DATE_AND_TIME_INPUT)
