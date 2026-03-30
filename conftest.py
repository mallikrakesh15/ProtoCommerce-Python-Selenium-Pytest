import os
from datetime import datetime
import base64
import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser Selection")


@pytest.fixture()
def browserInstances(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r'E:\TESTING\chromedriver.exe')
    elif browser_name == "firefox":
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(executable_path=r'E:\TESTING\geckodriver.exe',options=options)
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path=r'E:\TESTING\msedgedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("browserInstances", None)

        if report.failed and driver:

            reports_dir = os.path.join(os.getcwd(), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(file_path)

            # Attach screenshot to HTML report

            with open(file_path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()
            extra = getattr(report, "extra", [])
            extra.append(extras.image(encoded, mime_type="image/png"))
            report.extra = extra