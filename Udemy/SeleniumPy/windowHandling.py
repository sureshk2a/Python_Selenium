from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)
waits = wait(driver,5)
driver.find_element_by_xpath("//a[text()='Click Here']").click()
windowHandles = driver.window_handles
driver.switch_to.window(windowHandles[1])
newWindowText = driver.find_element_by_tag_name("h3").text
assert "New Window" == newWindowText