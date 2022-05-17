from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class ConjugationPage(BasePage):
    """ Page Objects for conjugation page. """

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.VERB_DAY = (By.ID, "verbDay")
        self.POPULAR_VERBS = (By.CSS_SELECTOR, "#ch_ExtrasVerbs ol li")
        self.MORE_PRODUCTS_DOTS = (By.CSS_SELECTOR, "#more-products-menu div.option.front")
        self.MORE_PRODUCTS_CONTENT = (By.CSS_SELECTOR, "#more-products-menu div.drop-down span.text")
        self.AGREE_PRIVACY = (By.ID, "didomi-notice-agree-button")

    def get_verb_of_the_day(self) -> str:
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.visibility_of_element_located(self.VERB_DAY))
        ele = self._driver.find_element(*self.VERB_DAY)
        return ele.text

    def get_popular_verbs(self) -> list:
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.visibility_of_element_located(self.POPULAR_VERBS))
        eles = self._driver.find_elements(*self.POPULAR_VERBS)
        popular_verbs = [ele.text for ele in eles]
        return popular_verbs

    def get_more_products(self) -> list:
        ele = self._driver.find_element(*self.MORE_PRODUCTS_DOTS)
        ele.click()
        wait = WebDriverWait(self._driver, 5)
        wait.until(ec.presence_of_all_elements_located(self.MORE_PRODUCTS_CONTENT))
        eles = self._driver.find_elements(*self.MORE_PRODUCTS_CONTENT)
        more_products = [ele.text for ele in eles]
        return more_products

    def close_privacy_popup2(self) -> None:    # REVIEW
        wait = WebDriverWait(self._driver, 5)
        try:
            wait.until(ec.visibility_of_element_located(self.AGREE_PRIVACY))
            ele = self._driver.find_element(*self.AGREE_PRIVACY)
            ele.click()
        except TimeoutException as e:
            print(e.msg)        
