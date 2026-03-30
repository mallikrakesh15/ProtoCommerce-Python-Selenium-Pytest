from selenium.webdriver.common.by import By
from utilities.waitmechanism import WaitMechanism


class OrderConfirmationPage(WaitMechanism):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.search_input = (By.ID, 'country')
        self.country_list_input = (By.CSS_SELECTOR, ".suggestions a")
        self.country_checkbox_input = (By.CLASS_NAME, "checkbox")
        self.purchage_input = (By.XPATH, "//input[@value='Purchase']")
        self.successmsg_input = (By.CLASS_NAME, "alert-success")
        self.closeorder_input = (By.CSS_SELECTOR, ".alert-success a")
        self.wait_element_input = (By.CSS_SELECTOR, ".suggestions a")

    def orderConfirmation(self,countryName):
        self.driver.find_element(*self.search_input).send_keys('Ind')
        super().element_located(self.wait_element_input)
        countryList = self.driver.find_elements(* self.country_list_input)
        for country in countryList:
            if country.text == countryName:
                country.click()
                break
        self.driver.find_element(*self.country_checkbox_input).click()

    def placeOrder(self):
        self.driver.find_element(*self.purchage_input).click()
        orderMsg = self.driver.find_element(*self.successmsg_input).text
        return orderMsg

    def closeOrderPage(self):
        self.driver.find_element(*self.closeorder_input).click()