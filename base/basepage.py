from base.selenium_driver import SeleniumDriver
from traceback import print_stack


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_title(self, titletoverify):
        try:
            actualtitle = self.gettitle()
            if titletoverify.lower() in actualtitle.lower():
                return True
            else:
                self.log.info("Titles does not match")
                return False
        except:
            self.log.error("Failed to get page title!")
            print_stack()
            return False

    # LOGIN INTO ACCOUNT STUFF
    # Values
    login_text = "Login"
    email_field = "user_email"
    password_field = "user_password"
    loginbtn_name = "commit"

    # Element find methods and element action methods
    def login_action_method(self):
        self.element_click("link_text", self.login_text)

    def email_action_method(self, email):
        self.element_sendkeys(email, "id", self.email_field)

    def password_action_method(self, password):
        self.element_sendkeys(password, "id", self.password_field)

    def loginbtn_action_method(self):
        self.element_click("name", self.loginbtn_name)

    # LOGIN METHOD

    def login(self, email="", password=""):
        self.login_action_method()
        self.email_action_method(email)
        self.password_action_method(password)
        self.loginbtn_action_method()





































