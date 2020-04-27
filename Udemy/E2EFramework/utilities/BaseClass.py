import pytest
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkTextLocated(self, txtToVerify):
        element = wait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, txtToVerify)))
        return element

    def selectOptionByText(self, locator, txtToSelect):
        gender = Select(locator)
        gender.select_by_visible_text(txtToSelect)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # asctime,levelname,name,message will be taken in runtime

        fileHandler = logging.FileHandler("lgofile.log")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object should be passed here, to save logs in file

        logger.setLevel(logging.DEBUG)  # Define the level of from u need to see the log
        return logger
