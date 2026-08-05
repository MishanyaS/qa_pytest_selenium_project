import allure
import pytest
from pathlib import Path

import config

@allure.epic("Unit")
@allure.feature("Config")
@pytest.mark.unit
class TestConfig:
    @allure.story("Project")
    @allure.title("Project root exists")
    @allure.description("Verifies that the project root directory exists.")
    @pytest.mark.positive
    def test_project_root_exists(self):
        assert config.PROJECT_ROOT.exists()

    @allure.story("Project")
    @allure.title("Project root is directory")
    @allure.description("Verifies that the project root is a directory.")
    @pytest.mark.positive
    def test_project_root_is_directory(self):
        assert config.PROJECT_ROOT.is_dir()

    @allure.story("API")
    @allure.title("Base API URL")
    @allure.description("Verifies that the base API URL matches the expected value.")
    @pytest.mark.api
    @pytest.mark.positive
    def test_base_api_url(self):
        assert config.BASE_API_URL == "https://dummyjson.com/"

    @allure.story("UI")
    @allure.title("Base UI URL")
    @allure.description("Verifies that the base UI URL matches the expected value.")
    @pytest.mark.ui
    @pytest.mark.positive
    def test_base_ui_url(self):
        assert config.BASE_UI_URL == "https://demoqa.com/"

    @allure.story("UI")
    @allure.title("The Internet URL")
    @allure.description("Verifies that The Internet URL matches the expected value.")
    @pytest.mark.ui
    @pytest.mark.positive
    def test_the_internet_url(self):
        assert config.THE_INTERNET_URL == "https://the-internet.herokuapp.com/"

    @allure.story("API")
    @allure.title("API URL starts with https")
    @allure.description("Verifies that the base API URL uses HTTPS.")
    @pytest.mark.api
    @pytest.mark.positive
    def test_api_url_https(self):
        assert config.BASE_API_URL.startswith("https://")

    @allure.story("UI")
    @allure.title("UI URL starts with https")
    @allure.description("Verifies that the UI URL uses HTTPS.")
    @pytest.mark.ui
    @pytest.mark.positive
    def test_ui_url_https(self):
        assert config.BASE_UI_URL.startswith("https://")

    @allure.story("Timeout")
    @allure.title("Request timeout")
    @allure.description("Verifies that the request timeout matches the expected value.")
    @pytest.mark.positive
    def test_request_timeout(self):
        assert config.REQUEST_TIMEOUT == 10

    @allure.story("Timeout")
    @allure.title("Implicit wait")
    @allure.description("Verifies that the implicit wait matches the expected value.")
    @pytest.mark.positive
    def test_implicit_wait(self):
        assert config.IMPLICIT_WAIT == 5

    @allure.story("Timeout")
    @allure.title("Page load timeout")
    @allure.description("Verifies that the page load timeout matches the expected value.")
    @pytest.mark.positive
    def test_page_load_timeout(self):
        assert config.PAGE_LOAD_TIMEOUT == 30

    @allure.story("Timeout")
    @allure.title("Timeout values are positive")
    @allure.description("Verifies that all timeout values are greater than zero.")
    @pytest.mark.positive
    def test_timeout_values_positive(self):
        assert config.REQUEST_TIMEOUT > 0
        assert config.IMPLICIT_WAIT > 0
        assert config.PAGE_LOAD_TIMEOUT > 0

    @allure.story("Timeout")
    @allure.title("Page load timeout is the greatest")
    @allure.description("Verifies that timeout values are configured in the expected order.")
    @pytest.mark.positive
    def test_timeout_order(self):
        assert config.PAGE_LOAD_TIMEOUT > config.REQUEST_TIMEOUT
        assert config.REQUEST_TIMEOUT > config.IMPLICIT_WAIT

    @allure.story("Database")
    @allure.title("Database directory type")
    @allure.description("Verifies that the database directory is a Path object.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_database_dir_type(self):
        assert isinstance(config.DATABASE_DIR, Path)

    @allure.story("Database")
    @allure.title("Database name")
    @allure.description("Verifies that the database filename matches the expected value.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_database_name(self):
        assert config.DATABASE_NAME == "test_database.sqlite3"

    @allure.story("Database")
    @allure.title("Database path type")
    @allure.description("Verifies that the database path is a Path object.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_database_path_type(self):
        assert isinstance(config.DATABASE_PATH, Path)

    @allure.story("Database")
    @allure.title("Database path contains filename")
    @allure.description("Verifies that the database path contains the expected filename.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_database_path_name(self):
        assert config.DATABASE_PATH.name == config.DATABASE_NAME

    @allure.story("Database")
    @allure.title("Database parent directory")
    @allure.description("Verifies that the database path belongs to the database directory.")
    @pytest.mark.db
    @pytest.mark.positive
    def test_database_parent(self):
        assert config.DATABASE_PATH.parent == config.DATABASE_DIR

    @allure.story("Directories")
    @allure.title("Screenshots directory type")
    @allure.description("Verifies that the screenshots directory is a Path object.")
    @pytest.mark.positive
    def test_screenshots_dir_type(self):
        assert isinstance(config.SCREENSHOTS_DIR, Path)

    @allure.story("Directories")
    @allure.title("Logs directory type")
    @allure.description("Verifies that the logs directory is a Path object.")
    @pytest.mark.positive
    def test_logs_dir_type(self):
        assert isinstance(config.LOGS_DIR, Path)

    @allure.story("Directories")
    @allure.title("Downloads directory type")
    @allure.description("Verifies that the downloads directory is a Path object.")
    @pytest.mark.positive
    def test_downloads_dir_type(self):
        assert isinstance(config.DOWNLOADS_DIR, Path)

    @allure.story("Directories")
    @allure.title("Allure results directory type")
    @allure.description("Verifies that the Allure results directory is a Path object.")
    @pytest.mark.positive
    def test_allure_results_type(self):
        assert isinstance(config.ALLURE_RESULTS, Path)

    @allure.story("Directories")
    @allure.title("Allure report directory type")
    @allure.description("Verifies that the Allure report directory is a Path object.")
    @pytest.mark.positive
    def test_allure_report_type(self):
        assert isinstance(config.ALLURE_REPORT, Path)

    @allure.story("Directories")
    @allure.title("Screenshots inside project")
    @allure.description("Verifies that the screenshots directory is located inside the project root.")
    @pytest.mark.positive
    def test_screenshots_inside_project(self):
        assert config.SCREENSHOTS_DIR.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Logs inside project")
    @allure.description("Verifies that the logs directory is located inside the project root.")
    @pytest.mark.positive
    def test_logs_inside_project(self):
        assert config.LOGS_DIR.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Downloads inside project")
    @allure.description("Verifies that the downloads directory is located inside the project root.")
    @pytest.mark.positive
    def test_downloads_inside_project(self):
        assert config.DOWNLOADS_DIR.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Allure results inside project")
    @allure.description("Verifies that the Allure results directory is located inside the project root.")
    @pytest.mark.positive
    def test_allure_results_inside_project(self):
        assert config.ALLURE_RESULTS.parent == config.PROJECT_ROOT

    @allure.story("Directories")
    @allure.title("Allure report inside project")
    @allure.description("Verifies that the Allure report directory is located inside the project root.")
    @pytest.mark.positive
    def test_allure_report_inside_project(self):
        assert config.ALLURE_REPORT.parent == config.PROJECT_ROOT

    @allure.story("Types")
    @allure.title("URLs are strings")
    @allure.description("Verifies that all URL constants are strings.")
    @pytest.mark.api
    @pytest.mark.ui
    @pytest.mark.positive
    def test_url_types(self):
        assert isinstance(config.BASE_API_URL, str)
        assert isinstance(config.BASE_UI_URL, str)
        assert isinstance(config.THE_INTERNET_URL, str)

    @allure.story("Types")
    @allure.title("Timeouts are integers")
    @allure.description("Verifies that all timeout values are integers.")
    @pytest.mark.positive
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
    @allure.description("Verifies that all directory constants are Path objects.")
    @pytest.mark.positive
    def test_path_objects(self, directory: Path):
        assert isinstance(directory, Path)
