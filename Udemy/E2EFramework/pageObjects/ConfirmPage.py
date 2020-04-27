from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    delevLocationTxtBox = (By.ID,"country")
    termAndCondCheckBox = (By.XPATH,"//label[@for='checkbox2']")
    purchaseBtn = (By.CSS_SELECTOR,"[type='submit']")
    successMsgTxt = (By.CLASS_NAME,"alert-success")

    def getDelevLocationSearchBox(self):
        return self.driver.find_element(*ConfirmPage.delevLocationTxtBox)

    def getTermsAndCondCheckBox(self):
        return self.driver.find_element(*ConfirmPage.termAndCondCheckBox)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.successMsgTxt)
