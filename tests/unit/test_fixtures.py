import sqlite3

import allure
import pytest
import requests
from faker import Faker

allure.epic("Unit")
@allure.feature("Fixtures")
@pytest.mark.unit
class TestFixtures:
    @allure.story("faker")
    @allure.title("Faker fixture returns Faker instance")
    def test_faker_fixture_instance(self, faker: Faker):
        assert isinstance(faker, Faker)

    @allure.story("faker")
    @allure.title("Faker generates first name")
    def test_faker_first_name(self, faker: Faker):
        value = faker.first_name()

        assert isinstance(value, str)
        assert value

    @allure.story("faker")
    @allure.title("Faker generates email")
    def test_faker_email(self, faker: Faker):
        email = faker.email()

        assert isinstance(email, str)
        assert "@" in email

    @allure.story("faker")
    @allure.title("Faker generates different values")
    def test_faker_random_values(self, faker: Faker):
        assert faker.uuid4() != faker.uuid4()

    @allure.story("timeout")
    @allure.title("Timeout fixture returns integer")
    def test_timeout_fixture_type(self, timeout: int):
        assert isinstance(timeout, int)

    @allure.story("timeout")
    @allure.title("Timeout fixture is positive")
    def test_timeout_fixture_positive(self, timeout: int):
        assert timeout > 0

    @allure.story("sqlite")
    @allure.title("SQLite connection type")
    def test_sqlite_connection_type(self, sqlite_connection: sqlite3.Connection):
        assert isinstance(sqlite_connection, sqlite3.Connection)

    @allure.story("sqlite")
    @allure.title("SQLite connection is opened")
    def test_sqlite_connection_open(self, sqlite_connection: sqlite3.Connection):
        sqlite_connection.execute("SELECT 1")

    @allure.story("sqlite")
    @allure.title("Cursor fixture returns cursor")
    def test_db_cursor_type(self, db_cursor: sqlite3.Cursor):
        assert isinstance(db_cursor, sqlite3.Cursor)

    @allure.story("sqlite")
    @allure.title("Cursor executes SQL")
    def test_cursor_execute(self, db_cursor: sqlite3.Cursor):
        result = db_cursor.execute("SELECT 1").fetchone()

        assert result == (1,)

    @allure.story("sqlite")
    @allure.title("Cursor description exists")
    def test_cursor_description(self, db_cursor: sqlite3.Cursor):
        db_cursor.execute("SELECT 1")

        assert db_cursor.description is not None

    @allure.story("sqlite")
    @allure.title("Cursor can create temporary table")
    def test_create_temp_table(self, db_cursor: sqlite3.Cursor):
        db_cursor.execute(
            """
            CREATE TEMP TABLE test_table(
                id INTEGER
            )
            """
        )

        db_cursor.execute(
            """
            INSERT INTO test_table(id)
            VALUES(1)
            """
        )

        result = db_cursor.execute(
            """
            SELECT id
            FROM test_table
            """
        ).fetchone()

        assert result == (1,)

    @allure.story("fixtures")
    @allure.title("api_session and sqlite fixtures coexist")
    def test_multiple_fixtures(self, api_session: requests.Session, sqlite_connection: sqlite3.Connection):
        assert isinstance(api_session, requests.Session)
        assert isinstance(sqlite_connection, sqlite3.Connection)

    @allure.story("fixtures")
    @allure.title("Several fixtures available together")
    def test_all_basic_fixtures(self, faker: Faker, timeout: int, api_session: requests.Session, sqlite_connection: sqlite3.Connection):
        assert faker is not None
        assert timeout > 0
        assert api_session is not None
        assert sqlite_connection is not None
