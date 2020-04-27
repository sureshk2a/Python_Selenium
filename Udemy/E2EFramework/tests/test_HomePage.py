import pytest
from Udemy.E2EFramework.pageObjects.HomePage import HomePage
from Udemy.E2EFramework.utilities.BaseClass import BaseClass
from Udemy.E2EFramework.TestData.HomePageData import HomePageData

class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["Name"])
        log.info("Entered first name as: "+str(getData["Name"]))
        homePage.getPassword().send_keys(getData["Password"])
        log.info("Entered password as: "+str(getData["Password"]))
        homePage.getMailID().send_keys(getData["Email"])
        log.info("Entered emailID as: "+str(getData["Email"]))
        homePage.getIceCreamCheckbox().click()
        self.selectOptionByText(homePage.selectGender(),getData["Gender"])
        submit = homePage.getSubmitButton()
        submit.click()
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getData())
    def getData(self,request):
        return request.param

