from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
driver.implicitly_wait(5)
waits = wait(driver,5)
print(driver.execute_script("return document.getElementsByClassName('largeTitle')[0].textContent"))
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")