import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def chrome_headless(request):
    """Create Chrome browser instance in headless mode."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--proxy-server='direct://'")
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    _driver = webdriver.Chrome(options=options)
    _driver.maximize_window()
    request.driver = _driver
    yield _driver
    _driver.quit()
