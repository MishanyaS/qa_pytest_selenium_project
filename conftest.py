import sqlite3
from pathlib import Path

import allure
import pytest
import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import (
    ALLURE_REPORT,
    ALLURE_RESULTS,
    DATABASE_DIR,
    DATABASE_PATH,
    DOWNLOADS_DIR,
    IMPLICIT_WAIT,
    LOGS_DIR,
    PAGE_LOAD_TIMEOUT,
    REQUEST_TIMEOUT,
    SCREENSHOTS_DIR,
)

DIRECTORIES = (
    DATABASE_DIR,
    SCREENSHOTS_DIR,
    LOGS_DIR,
    DOWNLOADS_DIR,
    ALLURE_RESULTS,
    ALLURE_REPORT,
)

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()

@pytest.fixture(scope="session")
def api_session() -> requests.Session:
    session = requests.Session()

    session.headers.update(
        {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    )

    yield session

    session.close()

@pytest.fixture(scope="session")
def timeout() -> int:
    return REQUEST_TIMEOUT

@pytest.fixture(scope="session")
def sqlite_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    yield connection

    connection.close()

@pytest.fixture()
def db_cursor(sqlite_connection):
    cursor = sqlite_connection.cursor()

    yield cursor

    sqlite_connection.commit()

    cursor.close()

@pytest.fixture()
def driver():
    options = Options()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-notifications")

    options.add_argument("--disable-infobars")

    options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--no-sandbox")

    options.add_argument("--disable-gpu")

    prefs = {
        "download.default_directory": str(DOWNLOADS_DIR),
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.implicitly_wait(IMPLICIT_WAIT)

    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()

    if report.when != "call":
        return
    
    if report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshot = driver.get_screenshot_as_png()

            allure.attach(
                screenshot, 
                name="Failure Screenshot", 
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture(autouse=True)
def test_logger(request):
    print()

    print("=" * 80)

    print(f"START TEST -> {request.node.name}")

    yield

    print(f"END TEST -> {request.node.name}")

    print("=" * 80)
