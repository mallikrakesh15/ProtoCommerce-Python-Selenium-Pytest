from selenium.webdriver.common.by import By
from utilities.waitmechanism import WaitMechanism


class LoginPage(WaitMechanism):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signinBtn_input = (By.ID, "signInBtn")
        self.visible_element_input = (By.CSS_SELECTOR, ".alert-danger")

    def login(self,username,password):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signinBtn_input).click()

    def loginErrorCheck(self):
        super().element_visibility(self.visible_element_input)
        errorMsg = self.driver.find_element(By.CLASS_NAME,"alert-danger").text
        return errorMsg
