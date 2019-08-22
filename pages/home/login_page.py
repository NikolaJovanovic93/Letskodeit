from base.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Verify login methods
    def verify_login_successful(self):
        result = self.is_element_present("xpath", "// div[ @ id = 'navbar'] / div / div / div / ul / li[4] / a / img")
        return result

    def verify_login_failed(self):
        result = self.is_element_present("xpath", "//div[contains(text(),'Invalid email or password')]")
        return result

    def verify_login_title(self):
        return self.verify_title("Lets's Kode It")

    def login_verify(self, email="", password=""):
        self.login(email, password)


























