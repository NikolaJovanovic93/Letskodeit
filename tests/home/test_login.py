import unittest
import pytest
from pages.home.login_page import LoginPage
from utilities.teststatus import TstStatus


@pytest.mark.usefixtures("onetimesetup", "setup")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectssetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TstStatus(self.driver)

    @pytest.mark.run(2)
    def test_login_sucs(self):
        # Try to login
        self.lp.login_verify("dz.0ni12111993@gmail.com", "hunt3r993")
        # Check for element after login
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verify_login_successful()
        self.ts.markfinal("test_valid_login", result2, "Login failed")

    @pytest.mark.run(1)
    def test_login_fail(self):
        # Try to login
        self.lp.login_verify()
        # Check for element after login fails
        result = self.lp.verify_login_failed()
        self.ts.markfinal("test_fail_login", result, "Login successful")


























