import os

import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class DriverHelper:
    def __init__(self, headless: bool = True) -> None:
        self.chrome_driver_manager = ChromeDriverManager().install()
        self.chrome_service = ChromeService(self.chrome_driver_manager)

        self.chrome_options = ChromeOptions()
        if headless:
            self.chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)

    def save_websites_screenshots(self, websites: list[str], output_dir: str) -> bool:
        for website in websites:
            self.driver.get(website)
            file_path = FileHelper.get_file_path(output_dir, website)
            if self.driver.save_screenshot(file_path) != True:
                return False
        return True


class FileHelper:
    @staticmethod
    def get_websites(input_file_path: str) -> list[str]:
        return np.loadtxt(input_file_path, dtype=str)

    @staticmethod
    def get_file_path(output_dir: str, website: str) -> str:
        clean_website = website.replace("https://", "").replace("http://", "")
        return f"{os.path.join(output_dir, clean_website)}.png"