from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class TranslationPage(BasePage):
    """ Page Objects for translation page. """

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.INPUT_ENTRY = (By.ID, "entry")
        self.HIGHLIGHTED = (By.XPATH, "//span[@class='text'][@lang='pt']/em")
        self.EXAMPLE_SRC = (By.CSS_SELECTOR, "#examples-content > div:nth-child(1) div.src")


    def get_verb_in_search_field(self) -> str:
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.visibility_of_element_located(self.INPUT_ENTRY))
        ele = self._driver.find_element(*self.INPUT_ENTRY)
        return ele.get_attribute('value')

    def get_verb_from_title(self) -> str:
        title = self._driver.title.partition(' ')[0]
        return title

    def get_highlight_css_for_verb(self) -> set:
        eles = self._driver.find_elements(*self.HIGHLIGHTED)
        atrs = set()
        for ele in eles:
            atrs.add(ele.value_of_css_property('background-color'))
        return atrs

    def hover_over_example(self):
        ac = ActionChains(self._driver)
        ele = self._driver.find_element(*self.HIGHLIGHTED)
        ac.move_to_element(ele).perform()
