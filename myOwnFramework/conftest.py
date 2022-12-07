import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.edge.service import Service as edgeService


driver = None


def pytest_addoption(parser):
    """
    This function gets an input from the console when the --browser_name parameter is added in order to set the browser
    :param parser:
    """
    parser.addoption("--browser_name",
                     action="store",
                     default="firefox")


@pytest.fixture(scope="class")
def setup(request):
    """
    Sets the initial configuration and behaviour of the test initializing the driver and service object and getting to
    the page to test before any other command in the test case is called.
    :param request:
    :return:
    """
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "firefox":
        service_obj = firefoxService("../geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser == "edge":
        service_obj = edgeService("../msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever the test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="../%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        """
        This function takes a screenshot
        :param name:
        :return:
        """
        driver.get_screenshot_as_file(name)
