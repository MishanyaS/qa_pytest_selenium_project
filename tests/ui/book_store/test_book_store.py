from __future__ import annotations

import allure
import pytest

from pages.book_store_page import BookStorePage
from pages.home_page import HomePage


@allure.epic("DemoQA UI")
@allure.feature("Alerts, Frame & Windows")
@pytest.mark.ui
@pytest.mark.regression
class TestBookStore:
    @allure.story("Book Store navigation")
    @allure.title("Book Store page opens successfully")
    @allure.description(
        "Verifies that the Book Store page can be opened successfully from the home page."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_book_store(self, driver):
        home_page = HomePage(driver)
        book_store_page = BookStorePage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Book Store page"):
            home_page.open_book_store()

        with allure.step("Verify Book Store page URL"):
            assert book_store_page.current_url.endswith("/books")

    @allure.story("Search")
    @allure.title("Search box is displayed")
    @allure.description("Verifies that the search box is visible.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_search_box_visible(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Verify search box is visible"):
            assert page.search_box_visible()

    @allure.story("Books")
    @allure.title("Books table is displayed")
    @allure.description("Verifies that the books table is visible.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_books_visible(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Verify books table is visible"):
            assert page.books_visible()

    @allure.story("Books")
    @allure.title("Books list is not empty")
    @allure.description("Verifies that the books table contains at least one book.")
    @pytest.mark.positive
    def test_books_count(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Verify books count"):
            assert page.books_count() > 0

    @allure.story("Books")
    @allure.title("Books titles are displayed")
    @allure.description("Verifies that the book titles are available.")
    @pytest.mark.positive
    def test_book_titles(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Verify book titles"):
            assert len(page.book_titles()) > 0

    @allure.story("Books")
    @allure.title("First book is visible")
    @allure.description("Verifies that the first book is visible.")
    @pytest.mark.positive
    def test_first_book_visible(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Verify first book is visibles"):
            assert page.book_visible(1)

    @allure.story("Search")
    @allure.title("Search filters books")
    @allure.description("Verifies that searching filters the displayed books.")
    @pytest.mark.positive
    def test_search_books(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Search for Git"):
            page.search("Git")

        with allure.step("Verify filtered results"):
            assert all("Git" in title for title in page.book_titles())

    @allure.story("Search")
    @allure.title("Search value is stored")
    @allure.description(
        "Verifies that the entered search value is displayed in the search field."
    )
    @pytest.mark.positive
    def test_search_value(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Enter search text"):
            page.search("JavaScript")

        with allure.step("Verify search value"):
            assert page.search_value() == "JavaScript"

    @allure.story("Search")
    @allure.title("Search can be cleared")
    @allure.description("Verifies that the search field can be cleared.")
    @pytest.mark.positive
    def test_clear_search(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Search for Python"):
            page.search("Python")

        with allure.step("Clear search"):
            page.clear_search()

        with allure.step("Verify search field is empty"):
            assert page.search_value() == ""

    @allure.story("Book details")
    @allure.title("Book details page opens")
    @allure.description("Verifies that clicking the first book opens its details page.")
    @pytest.mark.positive
    def test_open_first_book(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Open first book"):
            expected_title = page.book_title(1)
            page.open_first_book()

        with allure.step("Verify opened book"):
            assert page.current_url.endswith("/books?search=9781449325862")
            assert page.book_title_visible(expected_title)

    @allure.story("Authentication")
    @allure.title("Login button is displayed")
    @allure.description("Verifies that the Login button is visible.")
    @pytest.mark.positive
    def test_login_button_visible(self, driver):
        home_page = HomePage(driver)
        page = BookStorePage(driver)

        with allure.step("Open Book Store page"):
            home_page.open()
            home_page.open_book_store()

        with allure.step("Verify Login button is visible"):
            assert page.login_button_visible()
