#pytest -k CreditCard -v -s = To run only cases which has credit card in name
#pytest -m smoke -v -s = only run test with smoke marking
#@pytest.mark.skip #skip thwe testcase
#@pytest.mark.xfail
import pytest
@pytest.mark.xfail #without repoting in log Xpassed
def test_secondCreditCard():
    print("Credit Card Accepted")
@pytest.mark.smoke #custom marking tests
@pytest.mark.skip #skip thwe testcase
def test_secondFilePrg2():
    print("Credit Card Accepted")


