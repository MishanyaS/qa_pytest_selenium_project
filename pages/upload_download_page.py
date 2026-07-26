from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class UploadDownloadPage(BasePage):
    DOWNLOAD_LINK = (
        By.ID,
        "downloadButton",
    )

    UPLOAD_INPUT = (
        By.ID,
        "uploadFile",
    )

    UPLOADED_FILE_PATH = (
        By.ID,
        "uploadedFilePath",
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def download_link_visible(self) -> bool:
        return self.is_visible(self.DOWNLOAD_LINK)

    def upload_input_visible(self) -> bool:
        return self.is_visible(self.UPLOAD_INPUT)

    def uploaded_file_path_visible(self) -> bool:
        return self.is_visible(self.UPLOADED_FILE_PATH)

    def download_href(self) -> str | None:
        return self.attribute(self.DOWNLOAD_LINK, "href")

    def upload_file(self, file_path: str) -> None:
        self.wait_visible(self.UPLOAD_INPUT).send_keys(file_path)

    def uploaded_file_path(self) -> str:
        return self.text(self.UPLOADED_FILE_PATH)
