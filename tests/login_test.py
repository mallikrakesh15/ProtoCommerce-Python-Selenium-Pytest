import pytest
from pageObjects.login import LoginPage

username = "rahulshettyacademy"
password = "Learning@830$3mK"

@pytest.mark.order(2)
def test_loinCheck(browserInstances):
    driver = browserInstances

    loginPage = LoginPage(driver)
    loginPage.login(username, password)
    errorMsg = loginPage.loginErrorCheck()
    assert "Incorrect" in errorMsg, "Login Validation Failed"