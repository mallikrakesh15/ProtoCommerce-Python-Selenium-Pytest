import pytest
from pageObjects.ProductCheckoutage import ProductCheckout
from pageObjects.confirmationage import OrderConfirmationPage
from pageObjects.login import LoginPage
from pageObjects.productsPage import ProductListPage
from utilities.filereader import FileReader

countryName = "India"
''' Reading the data from the Json file'''
fileReader = FileReader()
loin_test_data = fileReader.json_fileReader()

@pytest.mark.order(1)
@pytest.mark.parametrize("login_data",loin_test_data)
def test_orderProduct(browserInstances,login_data):
    driver = browserInstances
    username = login_data["username"]
    password = login_data["password"]
    productName = login_data["productName"]
    loginPage = LoginPage(driver)
    loginPage.login(username,password)

    productListPage = ProductListPage(driver)
    productListPage.addProductToCart(productName)
    productListPage.productCheckout()

    productCheckout = ProductCheckout(driver)
    checkoutProductName = productCheckout.product_Checkout()
    productCheckout.checkout()
    assert productName in checkoutProductName

    orderConfirmationPage = OrderConfirmationPage(driver)
    orderConfirmationPage.orderConfirmation(countryName)
    orderMsg = orderConfirmationPage.placeOrder()
    orderConfirmationPage.closeOrderPage()
    assert "Success" in orderMsg



