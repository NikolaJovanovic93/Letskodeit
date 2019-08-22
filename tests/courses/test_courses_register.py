import unittest
import pytest
from pages.courses.register_courses_page import RegisterCourses
from utilities.teststatus import TstStatus

# 1. Test login with correct account and password
# 2. Test search for JavaScript in search box
# 3. Test elect course
# 4. Test click on enroll in course button
# 5. Test scroll to the bottom of the page and enter fake information in text boxes
# 6. Test try to click on enroll in course button(it should be unable to click because of fake info)


@pytest.mark.usefixtures("onetimesetup", "setup")
class TestRegister(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectsetup(self):
        self.rc = RegisterCourses(self.driver)
        self.ts = TstStatus(self.driver)

    @pytest.mark.run(1)
    def test_jscript_course(self):
        self.rc.login_register()
        self.rc.course_all_in(fullcoursename="JavaScript for beginners", num=2134124, exp=20, cvc=10, postal=123)
        result = self.rc.isenabled(locatortype="id", value="confirm-purchase")
        self.ts.markfinal(testname="test_confirm_button", result=result, resultmessage="Element is not clickable")



































