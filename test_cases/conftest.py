import pytest
from selenium import webdriver
from utilities.readconfig import read_configuration


@pytest.fixture(scope='class')
def setup(request):
    driver = None
    browser = read_configuration.get_browser()
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    if browser.__eq__("edge"):
        driver = webdriver.Edge()

    driver.maximize_window()
    url = read_configuration.geturl()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
