import sqlite3

import allure
import pytest
import requests
from faker import Faker


@allure.epic("Unit")
@allure.feature("Fixtures")
@pytest.mark.unit
class TestFixtures:
    @allure.story("faker")
    @allure.title("Faker fixture returns Faker instance")
    @allure.description("Verifies that the faker fixture returns a Faker instance.")
    @pytest.mark.positive
    def test_faker_fixture_instance(self, faker: Faker):
        assert isinstance(faker, Faker)

    @allure.story("faker")
    @allure.title("Faker generates first name")
    @allure.description("Verifies that Faker generates a non-empty first name.")
    @pytest.mark.positive
    def test_faker_first_name(self, faker: Faker):
        value = faker.first_name()

        assert isinstance(value, str)
        assert value

    @allure.story("faker")
    @allure.title("Faker generates email")
    @allure.description("Verifies that Faker generates a valid email string.")
    @pytest.mark.positive
    def test_faker_email(self, faker: Faker):
        email = faker.email()

        assert isinstance(email, str)
        assert "@" in email

    @allure.story("faker")
    @allure.title("Faker generates different values")
    @allure.description("Verifies that Faker generates different random values.")
    @pytest.mark.positive
    def test_faker_random_values(self, faker: Faker):
        assert faker.uuid4() != faker.uuid4()

    @allure.story("timeout")
    @allure.title("Timeout fixture returns integer")
    @allure.description("Verifies that the timeout fixture returns an integer.")
    @pytest.mark.positive
    def test_timeout_fixture_type(self, timeout: int):
        assert isinstance(timeout, int)

    @allure.story("timeout")
    @allure.title("Timeout fixture is positive")
    @allure.description("Verifies that the timeout fixture returns a positive value.")
    @pytest.mark.positive
    def test_timeout_fixture_positive(self, timeout: int):
        assert timeout > 0

    @allure.story("sqlite")
    @allure.title("SQLite connection type")
    @allure.description("Verifies that the SQLite fixture returns a Connection object.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_sqlite_connection_type(self, sqlite_connection: sqlite3.Connection):
        assert isinstance(sqlite_connection, sqlite3.Connection)

    @allure.story("sqlite")
    @allure.title("SQLite connection is opened")
    @allure.description(
        "Verifies that the SQLite connection is open and accepts queries."
    )
    @pytest.mark.db
    @pytest.mark.positive
    def test_sqlite_connection_open(self, sqlite_connection: sqlite3.Connection):
        sqlite_connection.execute("SELECT 1")

    @allure.story("sqlite")
    @allure.title("Cursor fixture returns cursor")
    @allure.description("Verifies that the cursor fixture returns a Cursor object.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_db_cursor_type(self, db_cursor: sqlite3.Cursor):
        assert isinstance(db_cursor, sqlite3.Cursor)

    @allure.story("sqlite")
    @allure.title("Cursor executes SQL")
    @allure.description(
        "Verifies that the cursor executes SQL statements successfully."
    )
    @pytest.mark.db
    @pytest.mark.positive
    def test_cursor_execute(self, db_cursor: sqlite3.Cursor):
        result = db_cursor.execute("SELECT 1").fetchone()

        assert result == (1,)

    @allure.story("sqlite")
    @allure.title("Cursor description exists")
    @allure.description(
        "Verifies that the cursor provides column metadata after executing a query."
    )
    @pytest.mark.db
    @pytest.mark.positive
    def test_cursor_description(self, db_cursor: sqlite3.Cursor):
        db_cursor.execute("SELECT 1")

        assert db_cursor.description is not None

    @allure.story("sqlite")
    @allure.title("Cursor can create temporary table")
    @allure.description("Verifies that a temporary table can be created and queried.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_create_temp_table(self, db_cursor: sqlite3.Cursor):
        db_cursor.execute("""
            CREATE TEMP TABLE test_table(
                id INTEGER
            )
            """)

        db_cursor.execute("""
            INSERT INTO test_table(id)
            VALUES(1)
            """)

        result = db_cursor.execute("""
            SELECT id
            FROM test_table
            """).fetchone()

        assert result == (1,)

    @allure.story("fixtures")
    @allure.title("api_session and sqlite fixtures coexist")
    @allure.description(
        "Verifies that API session and SQLite fixtures can be used together."
    )
    @pytest.mark.api
    @pytest.mark.db
    @pytest.mark.positive
    def test_multiple_fixtures(
        self, api_session: requests.Session, sqlite_connection: sqlite3.Connection
    ):
        assert isinstance(api_session, requests.Session)
        assert isinstance(sqlite_connection, sqlite3.Connection)

    @allure.story("fixtures")
    @allure.title("Several fixtures available together")
    @allure.description(
        "Verifies that all basic fixtures are available in a single test."
    )
    @pytest.mark.api
    @pytest.mark.db
    @pytest.mark.positive
    def test_all_basic_fixtures(
        self,
        faker: Faker,
        timeout: int,
        api_session: requests.Session,
        sqlite_connection: sqlite3.Connection,
    ):
        assert faker is not None
        assert timeout > 0
        assert api_session is not None
        assert sqlite_connection is not None
