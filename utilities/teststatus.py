from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging


class TstStatus(SeleniumDriver):

    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultlist = []

    def setresult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("VERIFICATION SUCCESSFUL")
                else:
                    self.resultlist.append("FAIL")
                    self.log.error("VERIFICATION FAILED :: +" + resultmessage)
                    self.screenshot(resultmessage)
        except:
            self.resultlist.append("FAIL")
            self.log.error("THERE IS AN EXCEPTION !!!!")
            self.screenshot(resultmessage)

    def mark(self, result, resultmessage):

        self.setresult(result, resultmessage)

    def markfinal(self, testname, result, resultmessage):

        self.setresult(result, resultmessage)

        if "FAIL" in self.resultlist:
            self.log.error(testname + "TEST FAILED")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(testname + "TEST SUCCESSFUL")
            self.resultlist.clear()
            assert True == True








































