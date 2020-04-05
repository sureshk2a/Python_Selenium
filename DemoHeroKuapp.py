#Demo script to know about handling all web controls in selenium python'''
'''Author: Suresh Kumar
   Last Updated: 18March'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import threading
import time
import os
import datetime as dt
'''chome_Options = Options()
chome_Options.add_argument("--headless")
chome_Options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=chome_Options,executable_path= "Drivers/chromedriver.exe")'''
driver = webdriver.Chrome("Drivers/chromedriver.exe")
driver.implicitly_wait(20)
driver.delete_all_cookies()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
action = ActionChains(driver)
timeout = 5
def goBack():
        while str(driver.current_url) != "http://the-internet.herokuapp.com/":
            driver.back()
def takeScreenshot(fileNameToSave):
    try:
        driver.save_screenshot("Screenshots/"+str(fileNameToSave)+str(time.time())+".png")
    except Exception as e:
        print(e.with_traceback())
def gotToPage(nameOfPage):
    pages = driver.find_elements_by_xpath("//div[@id='content']/ul/li")
    for i in range(1,len(pages)+1):
        pageNavigator = driver.find_element_by_xpath("//div[@id='content']/ul/li["+str(i)+"]/a")
        if pageNavigator.text == nameOfPage:
            pageNavigator.click()
def addOrRemoveElement():
    driver.find_element_by_xpath("//div[@id='content']/ul/li[2]/a").click()
    WebDriverWait(driver,timeout).until(expected_conditions.url_contains("add_remove_elements"))
    driver.find_element_by_xpath("//button[text()='Add Element']").click()
    #WebDriverWait(driver,timeout).until(expected_conditions.element_to_be_clickable(By.XPATH("//button[text()='Delete']")))
    driver.find_element_by_xpath("//button[text()='Delete']").click()
    takeScreenshot("addOrRemove")
    goBack()
    return "Added and Removed an button"
def handleAuthentication(userName,passWord):
    driver.get("http://"+str(userName)+":"+str(passWord)+"@the-internet.herokuapp.com/digest_auth")
    afterLoginMessage = driver.find_element_by_xpath("//div[@id='content']/div/p").text
    if "Congratulations" in str(afterLoginMessage):
        takeScreenshot("authentication")
        goBack()
    return "Authentication successfull: " + str(afterLoginMessage)
def handleContextClick():
    driver.find_element_by_xpath("//div[@id='content']/ul/li[7]/a").click()
    action.move_to_element(driver.find_element_by_id("hot-spot")).context_click().perform()
    driver.switch_to.alert.accept()
    takeScreenshot("contextClick")
    goBack()
    return "Handled Context popup"
def handleDragAndDrop():
    driver.find_element_by_xpath("//div[@id='content']/ul/li[10]/a").click()
    staleElement = True
    for i in range(0,4):
        while(staleElement):
            try:
                action.drag_and_drop(driver.find_element_by_xpath("//div[@id='columns']/div[1]"), driver.find_element_by_xpath("//div[@id='columns']/div[2]")).perform()
                staleElement = False
            except StaleElementReferenceException as Exception:
                staleElement = True
    takeScreenshot("dragAndDrop")
    driver.back()
def handleDropDown(valueToSelect):
    driver.find_element_by_xpath("//div[@id='content']/ul/li[11]/a").click()
    select = Select(driver.find_element_by_id("dropdown"))
    select.select_by_visible_text(valueToSelect)
    takeScreenshot("dropDown")
    goBack()
    return "Selected '"+ str(valueToSelect) +"' from dropdown"
def handleFileDownload():
    driver.find_element_by_xpath("//div[@id='content']/ul/li[17]/a").click()
    filesToDownload = driver.find_elements_by_xpath("//div[@id='content']/div/a")
    for i in range(1,len(filesToDownload)+1):
        driver.find_element_by_xpath("//div[@id='content']/div/a["+str(i)+"]").click()
    takeScreenshot("fileDownload")
    goBack()
    return "Downloaded "+str(len(filesToDownload))+" files displayed"
def handleFileUpload():
    driver.find_element_by_xpath("//div[@id='content']/ul/li[18]/a").click()
    driver.find_element_by_id("file-upload").send_keys("C:/Users/suresha/Downloads/result.CSV")
    driver.find_element_by_id("file-submit").click()
    takeScreenshot("fileUpload")
    goBack()
    return "File Uploaded"
def highlightAnElement():
    element = driver.find_element_by_tag_name("h2")
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",element)
    takeScreenshot("highlight")
    return "Heading highlighted"
def handleIFrameEditor():
    gotToPage("WYSIWYG Editor")
print("Handle Add and remove control: ",addOrRemoveElement())
print("Handle context click: ",handleContextClick())
print("Handle JS Authentication: ",handleAuthentication("admin","admin"))
#print("Handle drag and drop", handleDragAndDrop())
print("Select given value from dropdown: ",handleDropDown("Option 1"))
#print("Download all files listed in the page",handleFileDownload())
print("Upload a file: ",handleFileUpload())
print("Highlight the heading: ",highlightAnElement())
print("Handle Editor inside iFrame: ",handleIFrameEditor())
driver.close()