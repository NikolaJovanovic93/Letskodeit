from selenium import webdriver

# Class with basic test case stuff


class WebDriverFactory(object):

    def __init__(self, browser):
        self.browser = browser

    def getwebdriverinstance(self):
        baseurl = "https://learn.letskodeit.com"
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "ie":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseurl)

        return driver





















