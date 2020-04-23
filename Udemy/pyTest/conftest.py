# this is the file to create setup and yield
# file name should exactly this
# the fixtures available to all files inside this directory
import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed as a setup")
    yield
    print("I'm executed as a teardown")


@pytest.fixture()
def dataLoad():
    print("User profile data is beign extracted")
    return ["Rahul", "Shetty", "rahulshetty.com"]


@pytest.fixture(params=[("chrome","Suresh"), ("firefox","Kumar"), "IE"])
def crossBrowser(request):
    return request.param
