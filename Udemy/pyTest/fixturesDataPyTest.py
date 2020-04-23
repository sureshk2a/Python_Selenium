import pytest

from Udemy.pyTest.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.test_LoggingDemo()
        log.info("Hai")
        print(dataLoad[0])


