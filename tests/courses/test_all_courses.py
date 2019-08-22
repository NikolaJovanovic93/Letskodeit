import unittest
import pytest
from pages.courses.register_courses_page import RegisterCourses
from utilities.teststatus import TstStatus
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
import time


@pytest.mark.usefixtures("onetimesetup", "setup")
@ddt
class TestAllCourses(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectsetup(self):
        self.rc = RegisterCourses(self.driver)
        self.ts = TstStatus(self.driver)

    @pytest.mark.run(order=2)
    @data(*get_csv_data("C:\\Users\\Desktop\\PycharmProjects\\letskodeit\\testdata.csv"))
    @unpack
    def test_every_course(self, fullcoursename):
        self.rc.all_courses_check(fullcoursename)
        self.rc.allcourseslink()
        #result = self.rc.isenabled(locatortype="id", value="confirm-purchase")
        #self.ts.markfinal(testname="test_confirm_button", result=result, resultmessage="Element is not clickable")

    @pytest.mark.run(order=1)
    def test_sign_up(self):
        self.rc.login_register()
        self.rc.clcallcourses()
        time.sleep(2)


































