# QA Automation Framework (pytest + Selenium)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python\&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest\&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium\&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-2A6DB2)
![Allure](https://img.shields.io/badge/Allure-Report-FF6A00)
![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Validation-85EA2D)
![Ruff](https://img.shields.io/badge/Ruff-Linter-D7FF64?logo=ruff\&logoColor=black)
![Black](https://img.shields.io/badge/Black-Formatter-000000?logo=python\&logoColor=white)
![mypy](https://img.shields.io/badge/mypy-Type%20Checking-2A6DB2?logo=python\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions\&logoColor=white)

## About the Project

A **Python-based QA Automation Framework** designed for automated **API, UI, and unit testing**.

The project demonstrates a structured approach to test automation, including:

* Page Object Model for UI automation
* API client abstraction
* JSON Schema response validation
* reusable pytest fixtures
* test parametrization
* test markers
* Allure reporting
* screenshots and logs for failed UI tests
* static code analysis and formatting
* type checking with mypy
* Docker-based execution
* CI automation with GitHub Actions
* manual execution of individual test suites, directories, or test files

The framework is designed as a portfolio project demonstrating practical **QA Automation Engineer** skills.

---

## Tech Stack

| Technology                  | Purpose                                               |
| --------------------------- | ----------------------------------------------------- |
| **Python 3.12**             | Main programming language                             |
| **Pytest**                  | Test framework, fixtures, parametrization and markers |
| **Selenium WebDriver**      | UI test automation                                    |
| **Requests**                | HTTP/API testing                                      |
| **JSON Schema**             | API response contract validation                      |
| **Allure**                  | Test reporting                                        |
| **Faker**                   | Test data generation                                  |
| **Ruff**                    | Linting and code quality                              |
| **Black**                   | Code formatting                                       |
| **mypy**                    | Static type checking                                  |
| **Docker / Docker Compose** | Containerized test execution                          |
| **GitHub Actions**          | CI automation                                         |
| **Git / GitHub**            | Version control                                       |

---

## Testing Scope

The framework contains three main test layers.

### Unit Tests

Unit tests validate isolated components and application logic.

```text
tests/unit/
```

Covered areas include:

* isolated functions and methods
* API client behavior
* mocked HTTP interactions
* validation of request/response handling
* error scenarios

#### Unit tests result
![Unit tests](project_description/unit/unit_tests.png)

---

### API Tests

API tests validate REST endpoints and HTTP behavior.

```text
tests/api/
```

The API test suite covers:

* `GET`
* `POST`
* `PUT`
* `PATCH`
* `DELETE`
* positive scenarios
* negative scenarios
* request payload validation
* response status codes
* response body validation
* JSON Schema validation
* generated test data
* boundary and invalid-data scenarios

API tests use reusable fixtures and API client abstraction.

Example flow:

```text
Test
 ↓
ApiClient
 ↓
HTTP Request
 ↓
Response
 ↓
Status Code Validation
 ↓
JSON Validation
 ↓
JSON Schema Validation
```

#### API tests result for User
![API tests for User](project_description/api/api_test_get_users_result.png)
![API tests for User](project_description/api/api_test_post_users_result.png)
![API tests for User](project_description/api/api_test_put_users_result.png)
![API tests for User](project_description/api/api_test_patch_users_result.png)
![API tests for User](project_description/api/api_test_delete_users_result.png)

#### API tests result for Post
![API tests for User](project_description/api/api_test_get_posts_result.png)
![API tests for User](project_description/api/api_test_post_posts_result.png)
![API tests for User](project_description/api/api_test_put_posts_result.png)
![API tests for User](project_description/api/api_test_patch_posts_result.png)
![API tests for User](project_description/api/api_test_delete_posts_result.png)

#### API tests result for Comment
![API tests for User](project_description/api/api_test_get_comments_result.png)
![API tests for User](project_description/api/api_test_post_comments_result.png)
![API tests for User](project_description/api/api_test_put_comments_result.png)
![API tests for User](project_description/api/api_test_patch_comments_result.png)
![API tests for User](project_description/api/api_test_delete_comments_result.png)

---

### UI Tests

UI tests use **Selenium WebDriver** and follow the **Page Object Model**.

```text
tests/ui/
pages/
```

The UI suite covers functionality of the DemoQA web application, including:

* forms
* buttons
* checkboxes
* radio buttons
* text boxes
* web tables
* select menus
* widgets
* browser interactions
* alerts
* windows
* frames
* draggable/resizable elements
* other interactive UI components

The Page Object approach keeps locators and page interaction logic separated from test scenarios.

Example flow:

```text
Test
 ↓
Page Object
 ↓
Selenium WebDriver
 ↓
Browser
 ↓
Assertion
```

#### UI tests result for DemoQA home page
![UI tests for DemoQA home page](project_description/ui/ui_test_home_tests_result.png)

#### UI tests result for DemoQA Elements section
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_text_box_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_check_box_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_radio_button_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_web_tables_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_buttons_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_links_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_broken_links_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_upload_download_result.png)
![UI tests for DemoQA Elements section](project_description/ui/ui_elements_test_dynamic_properties_result.png)

#### UI tests result for DemoQA Forms section
![UI tests for DemoQA Forms section](project_description/ui/ui_forms_tests_result.png)

#### UI tests result for DemoQA Alerts, Frame & Windows section
![UI tests for DemoQA Alerts, Frame & Windows section](project_description/ui/ui_alerts_tests_result.png)

#### UI tests result for DemoQA Widgets section
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_accordion_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_auto_complete_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_date_picker_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_slider_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_progress_bar_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_tabs_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_tooltips_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_menu_result.png)
![UI tests for DemoQA Widgets section](project_description/ui/ui_widgets_test_select_menu_result.png)

#### UI tests result for DemoQA Interactions section
![UI tests for DemoQA Interactions section](project_description/ui/ui_interactions_tests_result.png)

#### UI tests result for DemoQA Book Store section
![UI tests for DemoQA Book Store section](project_description/ui/ui_book_store_tests_result.png)

---

## Test Architecture

```text
                    QA Automation Framework
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
        Unit Tests        API Tests         UI Tests
             │                │                │
             │                ▼                ▼
             │           ApiClient        Page Objects
             │                │                │
             │                ▼                ▼
             │             REST API        Selenium
             │                                 │
             └────────────────┬────────────────┘
                              │
                              ▼
                           Pytest
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
         Allure           Screenshots        Logs
                              │
                              ▼
                       GitHub Actions
```

---

## Code Quality

The project uses automated static analysis, formatting, and type checking.

### Ruff

```bash
ruff check .
```

#### Ruff check result
![Ruff check result](project_description/ruff_check/ruff_check.png)

### Black

```bash
black --check .
```

#### Black check result
![Black check result](project_description/black_check/black_check.png)

### mypy

```bash
mypy .
```

#### mypy check result
![mypy check result](project_description/mypy_check/mypy_check.png)

These checks are also executed in GitHub Actions before the test jobs.

---

## GitHub Actions

The CI pipeline automatically runs on:

* push to `main`
* push to `master`
* push to `develop`
* pull requests
* manual workflow execution

### Pipeline

```text
Checkout
   ↓
Python Setup
   ↓
Install Dependencies
   ↓
Ruff
   ↓
Black
   ↓
mypy
   ↓
Pytest
   ↓
Allure Results
   ↓
Artifacts
```

#### GitHub Actions workflow result
![GitHub Actions workflow result](project_description/github_actions/workflow_run.png)
![GitHub Actions workflow result](project_description/github_actions/workflow_run_result.png)

### Manual Test Execution

The workflow supports manual execution of:

* all tests
* unit tests
* API tests
* UI tests
* individual test files
* individual test directories
* tests selected by markers
* tests selected with `-k`
* additional pytest arguments

For example:

```text
Suite:
api

Test Path:
tests/api/test_post_comments.py

Pytest Arguments:
-k create -m smoke
```

This allows a specific test file or subset of tests to be executed directly from GitHub Actions without modifying the workflow.

---

## Docker

The project supports containerized test execution using Docker and Docker Compose.

Build the image:

```bash
docker compose build
```

Run the unit tests suite:

```bash
docker compose run --rm tests pytest tests/unit
```

Docker provides a reproducible environment for running the automation framework independently from the host machine.

#### Unit tests running with help of Docker Compose
![Unit tests running with help of Docker Compose](project_description/docker/run_tests_with_docker_compose.png)

---

## Reporting

Test execution produces **Allure results**.

```bash
pytest --alluredir=allure-results
```

Open the report locally:

```bash
allure serve allure-results
```

The framework also stores additional execution artifacts:

* screenshots
* logs
* downloaded files
* pytest cache

These artifacts are uploaded by GitHub Actions even when tests fail, making debugging failed CI runs easier.

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pages/
│   ├── ...
│   └── ...
│
├── tests/
│   ├── unit/
│   ├── api/
│   └── ui/
│
├── schemas/
│   └── ...
│
├── utils/
│   └── ...
│
├── screenshots/
├── downloads/
├── logs/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── config.py
├── conftest.py
├── mypy.ini
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Running Tests Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest
```

### Run Unit Tests

```bash
pytest tests/unit
```

### Run API Tests

```bash
pytest tests/api
```

### Run UI Tests

```bash
pytest tests/ui
```

### Run a Specific Test File

```bash
pytest tests/api/test_post_comments.py
```

### Run Smoke Tests

```bash
pytest -m smoke
```

### Run Tests by Name

```bash
pytest -k login
```

### Run Tests in Parallel

```bash
pytest -n auto
```

### Generate Allure Results

```bash
pytest --alluredir=allure-results
```

### Open Allure Report

```bash
allure serve allure-results
```

---

## Project Goals

The main goal of the project is to demonstrate practical skills in:

* Python test automation
* API testing
* UI automation
* unit testing
* test framework architecture
* Page Object Model
* reusable pytest fixtures
* parametrization
* test data generation
* JSON Schema validation
* Allure reporting
* static code analysis
* type checking
* Docker
* CI/CD
* test debugging
* test artifacts and reporting

---

## Author

**Misha Shylin**