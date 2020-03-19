from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time
driver = webdriver.Chrome("Drivers/chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
def tableFindInstructor(instructorToFind):
    namecount = 0
    tableParent = driver.find_element_by_xpath("//table[@id='product']")
    rows = driver.find_elements_by_xpath("//table[@id='product']/tbody/tr")
    for i in range(2, len(rows)):
        name = driver.find_element_by_xpath("//table[@id='product']/tbody/tr[" + str(i) + "]/td[1]")
        if name.text == instructorToFind:
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
def selectRadioButton(valueToSelect):
    option = driver.find_element_by_xpath("//input[@value='"+str(valueToSelect).lower()+"']")
    option.click()
    if option.is_selected():
        return valueToSelect
    else:
        return "Given value is not selected"
def windowHandle():
    parentHandle = driver.current_window_handle
    openWindowBtn = driver.find_element_by_id("openwindow")
    openWindowBtn.click()
    time.sleep(4)
    allWindows = driver.window_handles
    for i in range(0,len(allWindows)):
        currentWindow = allWindows[i]
        if currentWindow != parentHandle:
            driver.switch_to.window(allWindows[i])
            newWindowUrl = driver.current_url
            driver.close()
            driver.switch_to.window(parentHandle)
            return newWindowUrl
def handleJSAlert(nameToDisplay,alertDecision):
    decision = str(alertDecision).lower()
    txtBox = driver.find_element_by_xpath("//input[@name='enter-name']")
    txtBox.send_keys(nameToDisplay)
    driver.find_element_by_id("confirmbtn").click()
    alert = driver.switch_to.alert
    if decision == "accept":
        alert.accept()
    elif decision == "reject":
        alert.dismiss()
    else:
        return alertDecision," decision is invalid on alert"
    return "Alert accepted"
def handleMouseHover(optionToSelect):
    mouseOverBtn = driver.find_element_by_id("mousehover")
    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_id("mousehover")).perform()
    if str(optionToSelect).lower() == "top":
        tempCounter = 1
    elif str(optionToSelect).lower() == "reload":
        tempCounter = 2
    else:
        return "Given option is invalid"
    action.move_to_element(driver.find_element_by_xpath("//div[@class='mouse-hover-content']/a["+str(tempCounter)+"]")).click().perform()
    return "Selected"+str(optionToSelect)
def footerIterations():
    footerParent = driver.find_element_by_id("gf-BIG")
    totalCategories = driver.find_elements_by_xpath("//div[@id='gf-BIG']/table/tbody/tr/td")
    print("There are "+str(len(totalCategories))+" categories in footer")
    mainList = []
    for i in range(1,len(totalCategories)+1):
        categoryName = driver.find_element_by_xpath("//div[@id='gf-BIG']/table/tbody/tr/td[" + str(i) + "]/ul/li/h3/a")
        underCategoryLists = driver.find_elements_by_xpath("//div[@id='gf-BIG']/table/tbody/tr/td[" + str(i) + "]/ul/li")
        print("Under "+str(categoryName.text+" there are "+str(len(underCategoryLists))+" items"))
        for j in range(2, len(underCategoryLists)+1):
            category = driver.find_element_by_xpath("//div[@id='gf-BIG']/table/tbody/tr/td[" + str(i) + "]/ul/li["+str(j)+"]/a")
            mainList.append(category.text)
    return mainList
def handleiFrames():
    driver.switch_to.frame(driver.find_element_by_id("courses-iframe"))

print("Total number of instructors whose name is 'Rahul Shetty' is:'", tableFindInstructor("Rahul Shetty"))
print("Total price of all the available courses present is: ",tableTotalCoursePrice())
print("Value selected from the dropdown is: ",selectDropDown("Option2"))
print("Radio button option selected was: ",selectRadioButton("Radio2"))
print("Switch to a new window and got the URL: ", windowHandle())
print("Handled JS alert shown on screen:",handleJSAlert("HAI","accept"))
print("Handled move hover and selected :",handleMouseHover("Top"))
print("Read all categories from footer of the page:",footerIterations())
