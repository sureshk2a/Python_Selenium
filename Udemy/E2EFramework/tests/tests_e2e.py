from Udemy.E2EFramework.pageObjects.HomePage import HomePage
from Udemy.E2EFramework.utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self, setup):
        log = self.getLogger()
        homePage = HomePage(driver=self.driver)
        checkoutPage = homePage.shopItems() #CLicks the shop button and returns the next page object
        log.info("Navigated to products page")
        products = checkoutPage.getProducts()
        log.info("Got all products displayed")
        productNameList = []
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            productNameList.append(productName)
            if productName == "Blackberry":
                product.find_element_by_xpath("div[2]/button").click()
        checkoutPage.getCheckoutBtn().click()
        confirmPage = checkoutPage.ClickProductCheckOutBtn()
        confirmPage.getDelevLocationSearchBox().send_keys("Ind")
        self.verifyLinkTextLocated("India").click()
        confirmPage.getTermsAndCondCheckBox().click()
        confirmPage.purchaseButton().click()
        log.info("Clicked purchase the product button")
        successText = confirmPage.getSuccessMsg().text
        assert "Sucess!" in successText
        #self.driver.get_screenshot_as_file(str(time.time())+"screen.png")