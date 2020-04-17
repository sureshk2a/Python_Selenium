from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
waits = wait(driver,5)
#Implicit wait and explicit wait
#Pause test for few seconds using time()
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(3)
displayedProducts = driver.find_elements_by_xpath("//div[@class='products']/div/div[3]/button")
print(str(len(displayedProducts))+" products where displayed after search")
productList = []
for index in range(1,len(displayedProducts)+1):
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='products']/div["+str(index)+"]/div[3]/button").click()
    productList.append(driver.find_element_by_xpath("//div[@class='products']/div[" + str(index) + "]/h4").text)
print(str(productList)+ " where added to cart")
waits.until(EC.presence_of_element_located((By.XPATH,"//img[@alt='Cart']")))
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//*[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
orders = driver.find_elements_by_xpath("//table[@class='cartTable']/tr/td[1]/img")
print(str(len(orders))+" orders where displayed in cart")
cartList = []
for cartindex in range(2,len(orders)+1):
    cartList.append(driver.find_element_by_xpath("//table[@class='cartTable']/tr["+str(cartindex)+"]/td[2]/p").text)
print(str(cartList)+ " where displayed in cart")
assert productList == cartList
