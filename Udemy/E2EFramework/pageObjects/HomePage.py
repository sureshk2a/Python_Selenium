from selenium.webdriver.common.by import By

from Udemy.E2EFramework.pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, "name")
    password = (By.ID, "exampleInputPassword1")
    mailID = (By.NAME, "email")
    loceIceCreamCheckBox = (By.ID, "exampleCheck1")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    genderSelect = (By.ID,"exampleFormControlSelect1")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getMailID(self):
        return self.driver.find_element(*HomePage.mailID)

    def getIceCreamCheckbox(self):
        return self.driver.find_element(*HomePage.loceIceCreamCheckBox)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def selectGender(self):
        return self.driver.find_element(*HomePage.genderSelect)
