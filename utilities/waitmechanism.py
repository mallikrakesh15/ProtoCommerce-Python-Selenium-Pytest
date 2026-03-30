from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitMechanism:
    def __init__(self,driver):
        self.driver = driver

    def element_located(self,wait_element_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((wait_element_input)))

    def element_visibility(self,visible_element_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((visible_element_input)))