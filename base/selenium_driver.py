from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as cl
import logging
import os
import time


class SeleniumDriver(object):
    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, resultmessage):
        fileName = resultmessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotsDirectory = "../screenshots/"
        relativeFileName = screenshotsDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotsDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved in file :" + destinationFile)
        except:
            self.log.error("There is an ERROR!!!!")
            print_stack()

    def gettitle(self):
        return self.driver.title

    def get_bytype(self, locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css_selector":
            return By.CSS_SELECTOR
        elif locatortype == "class_name":
            return By.CLASS_NAME
        elif locatortype == "link_text":
            return By.LINK_TEXT
        elif locatortype == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        elif locatortype == "tag_name":
            return By.TAG_NAME
        else:
            self.log.error("ByType is not valid")
            return False

    def get_element(self, locatortype, value):
        element = None
        try:
            locatortype = locatortype.lower()
            bytype = self.get_bytype(locatortype)
            element = self.driver.find_element(bytype, value)
            self.log.info("Element found")
        except:
            self.log.error("Element not found")
        return element

    def get_elements(self, locatortype, value):
        element = None
        try:
            locatortype = locatortype.lower()
            bytype = self.get_bytype(locatortype)
            element = self.driver.find_elements(bytype, value)
            self.log.info("Elements are found")
        except:
            self.log.error("Elements are not found")
            return element

    def gettext(self, locatortype, value="", element=None):
        try:
            if value:
                element = self.get_element(locatortype, value)
            text = element.text
            self.log.debug("After finding element size is:" + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("The text is:" + text)
                text = text.strip()
        except:
            self.log.error("Failed to get text on element")
            print_stack()
            text = None
        return text

    def element_click(self, locatortype, value="", element=None):
        try:
            if value:
                element = self.get_element(locatortype, value)
            element.click()
            self.log.info("Clicked on element with value:" + value + " " + "and locatortype:" + locatortype)
        except:
            self.log.error("Cant click on element with value of:" + value + " " + " and locatortype:" + locatortype)
            print_stack()

    def element_sendkeys(self, text, locatortype, value="", element=None):
        try:
            if value:
                element = self.get_element(locatortype, value)
            element.send_keys(text)
            self.log.info("Text written in element with value:" + value + " " + "and locatortype:" + locatortype)
        except:
            self.log.error("Cant send keys to element with value:" + value + " " + "and locatortype:" + locatortype)
            print_stack()

    def is_element_displayed(self, locatortype, value="", element=None):

        isDisplayed = False
        try:
            if value:  # This means if value is not empty
                element = self.get_element(locatortype, value)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with value:" + value + "and locatortype:" + locatortype)
            else:
                self.log.info("Element is not displayed with value:" + value + "and locatortype:" + locatortype)
            return isDisplayed
        except:
            self.log.error("Element not found")
            return False

    def is_element_present(self, locatortype, value="", element=None):
        try:
            if value:  # If value is not empty
                element = self.get_element(locatortype, value)
            if element is not None:
                self.log.info("Element with value:" + value + " " + "and locatortype:"
                              + locatortype + " " + "is present")
                return True
            else:
                self.log.info("Element with value:" + value + " " + "and locatortype:"
                              + locatortype + " " + "is not present")
                return False
        except:
            self.log.error("There is an error")
            return False

    def element_check(self, locatortype, value):
        try:
            elementlist = self.get_elements(locatortype, value)
            if len(elementlist) > 0:
                self.log.info("Element with value:" + value + " " + "and locatortype:"
                              + locatortype + " " + "is found")
                return True
            else:
                self.log.info("Element with value:" + value + " " + "and locatortype:"
                              + locatortype + " " + "is not found")
                return False
        except:
            self.log.error("There is an error")
            return False

    def wait_for_element(self, locatortype, value, timeout=10, pollfrequency=1):
        element = None
        try:
            locatortype = locatortype.lower()
            bytupe = self.get_bytype(locatortype)
            self.log.info("Waiting for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollfrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((bytupe, value)))
            self.log.info("Element appeared on web page")
        except:
            self.log.error("Element not appeared on web page")
            print_stack()
        return element

    def scrolling(self, direction):

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0,-10000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0,10000);")

    def switchtoframe(self, name="", id="", index=None):

        if name:
            self.driver.switch_to.frame(name)
        elif id:
            self.driver.switch_to.frame(id)
        else:
            self.driver.switch_to.frame(index)

    def switchtodefaultcontent(self):
        self.driver.switch_to.default_content()

    def getelementattributevalue(self, attribute, element=None, locatortype="", value=""):
        if value:
            element = self.get_element(locatortype, value)
        atr = element.get_attribute(attribute)
        return atr

    def isenabled(self, locatortype, value):

        element = self.get_element(locatortype, value)
        enabled = False
        try:
            attributevalue = self.getelementattributevalue(element=element, attribute="disabled")
            if attributevalue is not None:
                enabled = element.is_enabled()
            else:
                val = self.getelementattributevalue(element=element, attribute="class")
                enabled = not ("disabled" in val)
            if element == True:
                self.log.info("Element is enabled")
            else:
                self.log.info("Element is disabled")
        except:
            self.log.error("Element state could not be found")
        return enabled




























