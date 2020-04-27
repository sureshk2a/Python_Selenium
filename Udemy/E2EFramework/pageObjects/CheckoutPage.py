from selenium.webdriver.common.by import By

from Udemy.E2EFramework.pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH,"div/h4/a")
    checkoutBtn1 = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
    checkoutBtn2 = (By.XPATH,"//*[@class='btn btn-success']")

    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getProductFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getCheckoutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkoutBtn1)

    def ClickProductCheckOutBtn(self):
        self.driver.find_element(*CheckOutPage.checkoutBtn2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage