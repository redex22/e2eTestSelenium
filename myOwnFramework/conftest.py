import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name",
                     action="store",
                     default="firefox")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "firefox":
        service_obj = Service("../geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
