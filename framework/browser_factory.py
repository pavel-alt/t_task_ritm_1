import os
from typing import Union

from dotenv import load_dotenv
from selenium.webdriver import Chrome, Firefox, ChromeOptions, FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


load_dotenv()


class BrowserFactory:
    browser = os.getenv('BROWSER', 'chrome')

    def __init__(self):
        self.driver = self.__get_driver()

    def __get_driver(self) -> Union[Chrome, Firefox]:
        if self.browser == 'chrome':
            return self.__get_chrome_driver()
        elif self.browser == 'firefox':
            return self.__get_ff_driver()
        else:
            raise ValueError('Допустимые значения для BROWSER: chrome, firefox')

    @staticmethod
    def __get_chrome_driver() -> Chrome:
        options = ChromeOptions()
        options.add_argument('--headless=new')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = Chrome(service=service, options=options)
        return driver

    @staticmethod
    def __get_ff_driver() -> Firefox:
        options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = Firefox(service=service, options=options)
        return driver
