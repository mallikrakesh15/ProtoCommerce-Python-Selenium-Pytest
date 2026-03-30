from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r'E:\TESTING\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

productName = "Samsung Note 8"
countryName = "India"
username = "rahulshettyacademy"
password = "Learning@830$3mK2"

driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"signInBtn").click()

productlist = driver.find_elements(By.CLASS_NAME,'card')
for product in productlist:
    if product.find_element(By.CSS_SELECTOR,'.card-body h4').text == productName:
        product.find_element(By.CSS_SELECTOR, '.card-footer button').click()

driver.find_element(By.CSS_SELECTOR,'.navbar-collapse a').click()

checkoutProductLists = driver.find_elements(By.CSS_SELECTOR,'.table')
for checkoutProduct in checkoutProductLists:
    checkoutProductName = checkoutProduct.find_element(By.CSS_SELECTOR,'tr:first-child td:first-child').text
    checkoutProductQuantity = checkoutProduct.find_element(By.CSS_SELECTOR,'tr:first-child td:nth-child(2)').text
    checkoutProductPrice = checkoutProduct.find_element(By.CSS_SELECTOR,'tr:first-child td:nth-child(3)').text
    checkoutProductTotalPrice = checkoutProduct.find_element(By.CSS_SELECTOR,'tr:first-child td:nth-child(4)').text

driver.find_element(By.CSS_SELECTOR,'.btn-success').click()
driver.find_element(By.ID,'country').send_keys('Ind')
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".suggestions a")))
countryList = driver.find_elements(By.CSS_SELECTOR,".suggestions a")
for country in countryList:
    if country.text == countryName:
        country.click()
        break

driver.find_element(By.CLASS_NAME,"checkbox").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
orderMsg = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success" in orderMsg
driver.find_element(By.CSS_SELECTOR,".alert-success a").click()


driver.close()


