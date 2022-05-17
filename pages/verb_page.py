from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class VerbPage(BasePage):
    """ Page Objects for verb page. """

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.CONJUGATION_INPUT = (By.ID, "txtVerb")
        self.PRINTER_BUTTON = (By.ID, "ch_lblPrint")
        self.FLAG_INFINITIVE = (By.CSS_SELECTOR, ".targetted-word-wrap span")
        self.BODY = (By.CSS_SELECTOR, "body")
        self.BASE = (By.XPATH, "/html/head/base")
        # self.AGREE_PRIVACY = (By.ID, "didomi-notice-agree-button")

    def get_verb_in_search_field(self) -> str:
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.visibility_of_element_located(self.CONJUGATION_INPUT))
        ele = self._driver.find_element(*self.CONJUGATION_INPUT)
        return ele.get_attribute('value')

    def get_verb_from_title(self) -> str:
        title = self._driver.title.partition('|')[0].partition(' ')[2].strip()
        return title

    def get_body_onload(self) -> str:
        ele = self._driver.find_element(*self.PRINTER_BUTTON)
        ele.click()
        wh = self._driver.window_handles
        print(wh)
        self._driver.switch_to.window(wh[-1])
        ele = self._driver.find_element(*self.BODY)
        atr = ele.get_attribute('onload')
        return atr

    def open_print_popup(self) -> str:  # FIXME
        ele = self._driver.find_element(*self.PRINTER_BUTTON)
        ele.click()

    def get_infinitive_flag_url(self) -> str:
        ele = self._driver.find_element(*self.FLAG_INFINITIVE)
        atr = ele.value_of_css_property('background-image')
        return atr

    def switch_to_print_window(self) -> None:   # FIXME
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.number_of_windows_to_be(3))
        # number of windows == 3
        wh = self._driver.window_handles
        print(wh)
        self._driver.switch_to.window(wh[1])

    def get_base_attribute(self) -> str:   # FIXME
        ele = self._driver.find_element(*self.BASE)
        atr = ele.get_attribute('href')
        return atr
