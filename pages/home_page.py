from t_task_ritm_1.framework.element import Element
from t_task_ritm_1.framework.base_page import BasePage


class HomePage(BasePage):
    check_element_xpath = '//div[@class="home-banner"]'
    url = 'https://demoqa.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.elements = Element(driver, '//div[@class="card-body"]/h5[contains(text(), "Element")]')
