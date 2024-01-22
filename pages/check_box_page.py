from t_task_ritm_1.framework.element import Element
from t_task_ritm_1.framework.base_page import BasePage


class CheckBoxPage(BasePage):
    check_element_xpath = '//div[@class="main-header"][contains(text(), "Check Box")]'
    url = 'https://demoqa.com/checkbox'

    def __init__(self, driver):
        super().__init__(driver)

        self.expand_home_dir = Element(driver, self.__get_expanders_xpath('home'))
        self.check_home_dir_expanded = Element(driver, self.__get_check_open_node_xpath('home'))
        self.expand_download_dir = Element(driver, self.__get_expanders_xpath('downloads'))
        self.check_download_dir_expanded = Element(driver, self.__get_check_open_node_xpath('download'))

        self.word_file_check_box_unchecked = Element(driver, self.__get_check_box_condition_xpath('uncheck'))
        self.word_file_check_box_checked = Element(driver, self.__get_check_box_condition_xpath('check'))
        self.result_text = Element(driver, '//div[@id="result"]/span')

    @staticmethod
    def __get_expanders_xpath(nodes_name: str) -> str:
        return f'//label[contains(@for, "{nodes_name}")]/preceding-sibling::button'

    @staticmethod
    def __get_check_open_node_xpath(nodes_name: str) -> str:
        return f'//label[contains(@for, "{nodes_name}")]//*[name()="svg" and contains(@class, "open")]'

    @staticmethod
    def __get_check_box_condition_xpath(condition: str) -> str:
        return f'//label[contains(@for, "wordFile")]//*[name()="svg" and contains(@class, "-{condition}")]'

    def get_actual_result(self) -> str:
        """Возвращает текст выведенного результата"""
        actual_result = ''
        for el in Element.find_elements_by_xpath(self.result_text):
            actual_result += el.text
        return actual_result
