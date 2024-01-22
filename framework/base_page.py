from abc import ABC
from typing import Union
from selenium.webdriver import Chrome, Firefox

from t_task_ritm_1.framework.element import Element


class BasePage(ABC):
    check_element_xpath = ''
    url = ''

    def __init__(self, driver: Union[Chrome, Firefox]) -> None:
        self.driver = driver
        self.check_element = Element(driver, self.check_element_xpath)

    def open_page(self) -> None:
        """Метод переходит на страницу по УРЛ"""
        self.driver.get(self.url)

    def check_open_page(self) -> bool:
        """Метод проверяет видимость проверочного элемента"""
        return self.check_element.check_visibility()
