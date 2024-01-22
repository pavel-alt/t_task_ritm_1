from typing import List, Union

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Element:

    def __init__(self, driver: Union[Chrome, Firefox], xpath):
        self.driver = driver
        self.xpath = xpath

    def find_element_by_xpath(self) -> WebElement:
        """Поиск элемента по Хпасу"""
        return self.driver.find_element(by=By.XPATH, value=self.xpath)

    def find_elements_by_xpath(self) -> List[WebElement]:
        """Поиск списка элементов по Хпасу"""
        return self.driver.find_elements(by=By.XPATH, value=self.xpath)

    def check_visibility(self) -> bool:
        """Проверка видимости элемента пользователю"""
        return self.find_element_by_xpath().is_displayed()

    def click_on_element(self) -> None:
        """Клик по элементу"""
        self.find_element_by_xpath().click()
