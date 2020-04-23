# files name should start with test or end with test, function names should start with test
# test -v = test with more info
# test -v -s = test with console output
# every method name should be diff or else it will be overridden
# pytest <testName> = to run one file
def test_firstProgramCreditCard():
    print("firstFile credit card rejected")


def test_secondProgram():
    msg = "Good Morning"
    assert msg == "Good Mrning", "Displayed msg is not the expected msg"


def test_crossbrowsertest(crossBrowser):
    print(crossBrowser)
