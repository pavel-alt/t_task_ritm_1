from typing import Union

import pytest

from selenium.webdriver import Chrome, Firefox
from t_task_ritm_1.framework.browser_factory import BrowserFactory
from t_task_ritm_1.pages.check_box_page import CheckBoxPage
from t_task_ritm_1.pages.elements_page import ElementsPage
from t_task_ritm_1.pages.home_page import HomePage


@pytest.fixture(scope='session')
def driver() -> Union[Chrome, Firefox]:
    instance = BrowserFactory().driver
    yield instance
    instance.quit()


@pytest.fixture(scope='session')
def home_page(driver: Union[Chrome, Firefox]) -> HomePage:
    return HomePage(driver)


@pytest.fixture(scope='session')
def elements_page(driver: Union[Chrome, Firefox]) -> ElementsPage:
    return ElementsPage(driver)


@pytest.fixture(scope='session')
def check_box_page(driver: Union[Chrome, Firefox]) -> CheckBoxPage:
    return CheckBoxPage(driver)
