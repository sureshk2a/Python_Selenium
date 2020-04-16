from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
#Implicit wait and explicit wait
#Pause test for few seconds using time()
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
displayedProducts = driver.find_elements_by_xpath("//div[@class='products']/div/div[3]/button")
for product in displayedProducts:
    product.click()
wait.until(expected_conditions.element_to_be_clickable(By.XPATH,"//img[@alt='Cart']"))
driver.find_element_by_xpath("//img[@alt='Cart']").click()

