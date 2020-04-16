from selenium import webdriver
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Suresh")
driver.find_element_by_id("exampleInputPassword1").send_keys("password")
driver.find_element_by_name("email").send_keys("as@d.com")
driver.find_element_by_id("exampleCheck1").click()
submit = driver.find_element_by_xpath("//input[@type='submit']")
submit.get_attribute("")
submit.click()


