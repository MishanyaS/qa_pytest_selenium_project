from __future__ import annotations

import allure
import pytest

from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.upload_download_page import UploadDownloadPage

@allure.epic("DemoQA UI")
@allure.feature("Elements")
@pytest.mark.ui
@pytest.mark.regression
class TestUploadDownload:
    @allure.story("Upload and Download navigation")
    @allure.title("Upload and Download page opens successfully")
    @allure.description("Verifies that the Upload and Download page can be opened from the Elements section.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_upload_download(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        upload_and_download_page = UploadDownloadPage(driver)

        with allure.step("Open DemoQA home page"):
            home_page.open()

        with allure.step("Open Elements section"):
            home_page.open_elements()

        with allure.step("Open Upload and Download page"):
            elements_page.open_upload_download()

        with allure.step("Verify Upload and Download page URL"):
            assert upload_and_download_page.current_url.endswith("/upload-download")

    @allure.story("Upload and Download page")
    @allure.title("Upload and Download elements are visible")
    @allure.description("Verifies that the Download link and Upload file input are displayed on the Upload and Download page.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_upload_download_elements_visible(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = UploadDownloadPage(driver)

        with allure.step("Open Upload and Download page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_upload_download()

        with allure.step("Verify Download link is visible"):
            assert page.download_link_visible()

        with allure.step("Verify Upload input is visible"):
            assert page.upload_input_visible()

    @allure.story("Download")
    @allure.title("Download link contains a valid href")
    @allure.description("Verifies that the Download link contains a non-empty destination URL.")
    @pytest.mark.positive
    def test_download_href(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = UploadDownloadPage(driver)

        with allure.step("Open Upload and Download page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_upload_download()

        with allure.step("Get Download link href"):
            href = page.download_href()

        with allure.step("Verify Download link href"):
            assert href
            assert href.startswith(("http://", "https://", "data:"))

    @allure.story("Download")
    @allure.title("File can be downloaded")
    @allure.description("Verifies that the Download link can be clicked without errors.")
    @pytest.mark.positive
    def test_download_file(self, driver):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = UploadDownloadPage(driver)

        with allure.step("Open Upload and Download page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_upload_download()

        with allure.step("Get Download link href"):
            href = page.download_href()

        with allure.step("Verify Download link is configured"):
            assert href

        with allure.step("Click Download link"):
            page.click(page.DOWNLOAD_LINK)

        with allure.step("Verify browser starts download"):
            assert page.download_link_visible()

    @allure.story("Upload")
    @allure.title("User can upload a file")
    @allure.description("Verifies that a file can be selected through the Upload file input and that the uploaded file path is displayed.")
    @pytest.mark.positive
    def test_upload_file(self, driver, tmp_path):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = UploadDownloadPage(driver)

        file_name = "test_upload.txt"
        file_path = tmp_path / file_name
        file_path.write_text("DemoQA upload test file", encoding="utf-8")

        with allure.step("Open Upload and Download page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_upload_download()

        with allure.step("Upload test file"):
            page.upload_file(str(file_path))

        with allure.step("Verify uploaded file path is visible"):
            assert page.uploaded_file_path_visible()

        with allure.step("Get uploaded file path"):
            uploaded_path = page.uploaded_file_path()

        with allure.step("Verify uploaded file name"):
            assert uploaded_path.endswith(file_name)

    @allure.story("Upload")
    @allure.title("Uploaded file name is displayed correctly")
    @allure.description("Verifies that the file name displayed after upload matches the selected file name.")
    @pytest.mark.positive
    def test_uploaded_file_name(self, driver, tmp_path):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = UploadDownloadPage(driver)

        file_name = "document.txt"
        file_path = tmp_path / file_name
        file_path.write_text("Upload test content", encoding="utf-8")

        with allure.step("Open Upload and Download page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_upload_download()

        with allure.step("Upload test file"):
            page.upload_file(str(file_path))

        with allure.step("Verify uploaded file path"):
            uploaded_path = page.uploaded_file_path()

            assert uploaded_path.endswith(file_name)

    @allure.story("Upload")
    @allure.title("Different files can be uploaded")
    @allure.description("Verifies that the Upload file input accepts different files and displays the currently selected file.")
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "file_name",
        [
            "first_file.txt",
            "second_file.txt",
            "report.txt",
        ]
    )
    def test_uploaded_different_files(self, driver, tmp_path, file_name):
        home_page = HomePage(driver)
        elements_page = ElementsPage(driver)
        page = UploadDownloadPage(driver)

        file_path = tmp_path / file_name
        file_path.write_text("DemoQA upload test content", encoding="utf-8")

        with allure.step("Open Upload and Download page"):
            home_page.open()
            home_page.open_elements()
            elements_page.open_upload_download()

        with allure.step(f"Upload {file_name}"):
            page.upload_file(str(file_path))

        with allure.step(f"Verify uploaded file path"):
            assert page.uploaded_file_path_visible()

        with allure.step(f"Verify uploaded file name"):
            assert page.uploaded_file_path().endswith(file_name)
    