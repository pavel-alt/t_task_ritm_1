from t_task_ritm_1.framework.element import Element
from t_task_ritm_1.framework.base_page import BasePage


class ElementsPage(BasePage):
    check_element_xpath = '//div[contains(@class, "playgound-header")]//div[contains(text(), "Elements")]'
    url = 'https://demoqa.com/elements'

    def __init__(self, driver):
        super().__init__(driver)
        self.check_box = Element(driver, '//li/span[contains(text(), "Check Box")]')
