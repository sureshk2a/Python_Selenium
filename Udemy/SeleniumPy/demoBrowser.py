from selenium import webdriver
driver = webdriver.Chrome("C:\\chromedriver.exe")
#driver = webdriver.Firefox("C:\\geckodriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
driver.back()
driver.refresh()
driver.close()