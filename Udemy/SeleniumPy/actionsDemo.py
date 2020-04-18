from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
driver.implicitly_wait(5)
waits = wait(driver,5)
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//button[text()='Search']")).click().perform()
driver.find_element_by_link_text("Genealogies").click()