from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import threading
import time
driver = webdriver.Chrome("Drivers/chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
def tableFindInstructor():
    namecount = 0
    tableParent = driver.find_element_by_xpath("//table[@id='product']")
    rows = driver.find_elements_by_xpath("//table[@id='product']/tbody/tr")
    for i in range(2, len(rows)):
        name = driver.find_element_by_xpath("//table[@id='product']/tbody/tr[" + str(i) + "]/td[1]")
        if name.text == "Rahul Shetty":
            namecount += 1
    return namecount
def tableTotalCoursePrice():
    totalPrice = 0
    tableParent = driver.find_element_by_xpath("//table[@id='product']")
    rows = driver.find_elements_by_xpath("//table[@id='product']/tbody/tr")
    for i in range(2, len(rows)):
        price = driver.find_element_by_xpath("//table[@id='product']/tbody/tr[" + str(i) + "]/td[3]")
        totalPrice += int(price.text)
    return totalPrice
def selectDropDown(valueToSelect):
    select = Select(driver.find_element_by_id("dropdown-class-example"))
    select.select_by_visible_text(valueToSelect)
    return select.first_selected_option.text
print("Total number of instructors whose name is 'Rahul Shetty is:'", tableFindInstructor())
print("Total price of all the available courses present is: ",tableTotalCoursePrice())
print("Value selected from the dropdown is: ",selectDropDown("Option2"))

