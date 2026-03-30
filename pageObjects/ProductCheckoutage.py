from selenium.webdriver.common.by import By


class ProductCheckout:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_productslist_input = (By.CSS_SELECTOR, '.table')
        self.checkout_productname_input = (By.CSS_SELECTOR, 'tr:first-child td:first-child')
        self.checkout_input = (By.CSS_SELECTOR, '.btn-success')

    def product_Checkout(self):
        checkoutProductLists = self.driver.find_elements(*self.checkout_productslist_input)
        for checkoutProduct in checkoutProductLists:
            checkoutProductName = checkoutProduct.find_element(*self.checkout_productname_input).text
            return checkoutProductName

    def checkout(self):
        self.driver.find_element(* self.checkout_input).click()