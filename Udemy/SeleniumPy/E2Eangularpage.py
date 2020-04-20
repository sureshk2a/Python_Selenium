from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.implicitly_wait(5)
waits = wait(driver,5)
driver.find_element_by_xpath("//a[text()='Shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
productNameList = []
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    productNameList.append(productName)
    if productName == "Blackberry": 
        product.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//*[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
waits.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//label[@for='checkbox2']").click()
driver.find_element_by_css_selector("[type='submit']").click()
successText = driver.find_element_by_class_name("alert-success").text
assert "Success!" in successText
driver.get_screenshot_as_file("screen.png")

