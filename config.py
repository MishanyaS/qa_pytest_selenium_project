from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

BASE_API_URL = "https://dummyjson.com/"

BASE_UI_URL = "https://demoqa.com/"

THE_INTERNET_URL = "https://the-internet.herokuapp.com/"

REQUEST_TIMEOUT = 10

IMPLICIT_WAIT = 5

PAGE_LOAD_TIMEOUT = 30

DATABASE_DIR = PROJECT_ROOT / "database"

DATABASE_NAME = "test_database.sqlite3"

DATABASE_PATH = DATABASE_DIR / DATABASE_NAME

SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"

LOGS_DIR = PROJECT_ROOT / "logs"

ALLURE_RESULTS = PROJECT_ROOT / "allure-results"

ALLURE_REPORT = PROJECT_ROOT / "allure-report"

DOWNLOADS_DIR = PROJECT_ROOT / "downloads"
