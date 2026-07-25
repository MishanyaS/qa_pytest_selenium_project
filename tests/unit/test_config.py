import allure
import pytest
from pathlib import Path

import config

allure.epic("Unit")
@allure.feature("Config")
@pytest.mark.unit
class TestConfig:
    @allure.story("Project")
    @allure.title("Project root exists")
    def test_project_root_exists(self):
        assert config.PROJECT_ROOT.exists()

    @allure.story("Project")
    @allure.title("Project root is directory")
    def test_project_root_is_directory(self):
        assert config.PROJECT_ROOT.exists()

    @allure.story("API")
    @allure.title("Base API URL")
    def test_base_api_url(self):
        assert config.BASE_API_URL == "https://dummyjson.com/"

    @allure.story("UI")
    @allure.title("Base UI URL")
    def test_base_ui_url(self):
        assert config.BASE_UI_URL == "https://demoqa.com/"

    @allure.story("UI")
    @allure.title("The Internet URL")
    def test_the_internet_url(self):
        assert config.THE_INTERNET_URL == "https://the-internet.herokuapp.com/"

    @allure.story("API")
    @allure.title("API URL starts with https")
    def test_api_url_https(self):
        assert config.BASE_API_URL.startswith("https://")

    @allure.story("UI")
    @allure.title("UI URL starts with https")
    def test_ui_url_https(self):
        assert config.BASE_UI_URL.startswith("https://")

    @allure.story("Timeout")
    @allure.title("Request timeout")
    def test_request_timeout(self):
        assert config.REQUEST_TIMEOUT == 10

    @allure.story("Timeout")
    @allure.title("Implicit wait")
    def test_implicit_wait(self):
        assert config.IMPLICIT_WAIT == 5

    @allure.story("Timeout")
    @allure.title("Page load timeout")
    def test_page_load_timeout(self):
        assert config.PAGE_LOAD_TIMEOUT == 30

    @allure.story("Timeout")
    @allure.title("Timeout values are positive")
    def test_timeout_values_positive(self):
        assert config.REQUEST_TIMEOUT > 0
        assert config.IMPLICIT_WAIT > 0
        assert config.PAGE_LOAD_TIMEOUT > 0

    @allure.story("Timeout")
    @allure.title("Page load timeout is the greatest")
    def test_timeout_order(self):
        assert config.PAGE_LOAD_TIMEOUT > config.REQUEST_TIMEOUT
        assert config.REQUEST_TIMEOUT > config.IMPLICIT_WAIT

    @allure.story("Database")
    @allure.title("Database directory type")
    def test_database_dir_type(self):
        assert isinstance(config.DATABASE_DIR, Path)

    @allure.story("Database")
    @allure.title("Database name")
    def test_database_name(self):
        assert config.DATABASE_NAME == "test_database.sqlite3"

    @allure.story("Database")
    @allure.title("Database path type")
    def test_database_path_type(self):
        assert isinstance(config.DATABASE_PATH, Path)

    @allure.story("Database")
    @allure.title("Database path contains filename")
    def test_database_path_name(self):
        assert config.DATABASE_PATH.name == config.DATABASE_NAME

    @allure.story("Database")
    @allure.title("Database parent directory")
    def test_database_parent(self):
        assert config.DATABASE_PATH.parent == config.DATABASE_DIR

    @allure.story("Directories")
    @allure.title("Screenshots directory type")
    def test_screenshots_dir_type(self):
        assert isinstance(config.SCREENSHOTS_DIR, Path)

    @allure.story("Directories")
    @allure.title("Logs directory type")
    def test_logs_dir_type(self):
        assert isinstance(config.LOGS_DIR, Path)

    @allure.story("Directories")
    @allure.title("Downloads directory type")
    def test_downloads_dir_type(self):
        assert isinstance(config.DOWNLOADS_DIR, Path)

    @allure.story("Directories")
    @allure.title("Allure results directory type")
    def test_allure_results_type(self):
        assert isinstance(config.ALLURE_RESULTS, Path)

    @allure.story("Directories")
    @allure.title("Allure report directory type")
    def test_allure_report_type(self):
        assert isinstance(config.ALLURE_REPORT, Path)

    @allure.story("Directories")
    @allure.title("Screenshots inside project")
    def test_screenshots_inside_project(self):
        assert config.SCREENSHOTS_DIR.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Logs inside project")
    def test_logs_inside_project(self):
        assert config.LOGS_DIR.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Downloads inside project")
    def test_downloads_inside_project(self):
        assert config.DOWNLOADS_DIR.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Allure results inside project")
    def test_allure_results_inside_project(self):
        assert config.ALLURE_RESULTS.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Allure report inside project")
    def test_allure_report_inside_project(self):
        assert config.ALLURE_REPORT.parent == config.PROJECT_ROOT

    @allure.story("Types")
    @allure.title("URLs are strings")
    def test_url_types(self):
        assert isinstance(config.BASE_API_URL, str)
        assert isinstance(config.BASE_UI_URL, str)
        assert isinstance(config.THE_INTERNET_URL, str)

    @allure.story("Types")
    @allure.title("URTimeouts are integers")
    def test_timeout_types(self):
        assert isinstance(config.REQUEST_TIMEOUT, int)
        assert isinstance(config.IMPLICIT_WAIT, int)
        assert isinstance(config.PAGE_LOAD_TIMEOUT, int)

    @allure.story("Types")
    @allure.title("Directory constants are Path objects")
    @pytest.mark.parametrize(
        "directory",
        [
            config.PROJECT_ROOT,
            config.DATABASE_DIR,
            config.DATABASE_PATH,
            config.SCREENSHOTS_DIR,
            config.LOGS_DIR,
            config.ALLURE_RESULTS,
            config.ALLURE_REPORT,
            config.DOWNLOADS_DIR
        ]
    )
    def test_path_objects(self, directory: Path):
        assert isinstance(directory, Path)
