import pytest


@pytest.mark.usefixtures("setup") #Globally assigning fixtures to all test cases in file
class TestExample: #Class name should also be start with Test

    def test_fixtureDemo(self):
        print("Im iron man")

    def test_demoFixture2(self):
        print("Im iron man")

    def test_demoFixture3(self):
        print("Im iron man")

    def test_demoFixture4(self):
        print("Im iron man")
