from selenium import webdriver


class BasePage(object):
    """ Initializes base page. """

    def __init__(self, driver):
        self._driver: webdriver = driver
