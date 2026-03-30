from selenium.webdriver.common.by import By


class ProductListPage:
    def __init__(self,driver):
        self.driver = driver
        self.product_list_input = (By.CLASS_NAME, 'card')
        self.search_product_input = (By.CSS_SELECTOR, '.card-body h4')
        self.select_product_input = (By.CSS_SELECTOR, '.card-footer button')

        self.checkout_input = (By.CSS_SELECTOR, '.navbar-collapse a')

    def addProductToCart(self,productName):
        productlist = self.driver.find_elements(*self.product_list_input)
        for product in productlist:
            if product.find_element(*self.search_product_input).text == productName:
                product.find_element(*self.select_product_input).click()

    def productCheckout(self):
        self.driver.find_element(*self.checkout_input).click()