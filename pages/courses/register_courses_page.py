from base.basepage import BasePage
import time
# 1. Login with correct account and password
# 2. Search for JavaScript in search box
# 3. Select course
# 4. Click on enroll in course button
# 5. Scroll to the bottom of the page and enter fake information in text boxes
# 6. Try to click on enroll in course button(it should be unable to click because of fake info)


class RegisterCourses(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Values
    coursesSearchBox = "search-courses"  # ID
    searchButton = "search-course-button"  # ID
    courseslink = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"  # XPATH
    enroll_btn = "enroll-button-top"  # ID
    card_num = "//input[@aria-label='Credit or debit card number']"  # XPATH
    card_date = "exp-date"  # Name
    card_cvc = "cvc"  # Name
    card_postal = "postal"  # Name
    termsOfSrvc = "agreed_to_terms_checkbox"  # ID
    allcourses = "//a[contains(text(),'All Courses')]"  # XPATH

    # Login
    def login_register(self):
        self.login(email="dz.0ni12111993@gmail.com", password="hunt3r993")

    # Search for JavaScript course
    def jscript_search(self):
        self.element_sendkeys(text="JavaScript", locatortype="id", value=self.coursesSearchBox)
        self.element_click(locatortype="id", value=self.searchButton)

    # Click on Java Script course
    def course_click(self, fullcoursename):
        self.element_click(locatortype="xpath", value=self.courseslink.format(fullcoursename))

    # Click on enroll button
    def click_enroll(self):
        self.element_click(locatortype="id", value=self.enroll_btn)

    # Scroll down
    def course_scroll(self):
        self.scrolling(direction="down")

    # Credit card name
    def entercardnum(self, num):
        self.switchtoframe(name="__privateStripeFrame8")
        self.element_sendkeys(num, locatortype="xpath", value=self.card_num)
        self.switchtodefaultcontent()

    # Credit card expiration date
    def entercardexp(self, exp):
        self.switchtoframe(name="__privateStripeFrame9")
        self.element_sendkeys(exp, locatortype="name", value=self.card_date)
        self.switchtodefaultcontent()

    # Credit card cvc
    def entercardcvc(self, cvc):
        self.switchtoframe(name="__privateStripeFrame10")
        self.element_sendkeys(cvc, locatortype="name", value=self.card_cvc)
        self.switchtodefaultcontent()

    # Postal code
    def enterpostalcode(self, postal):
        self.switchtoframe(name="__privateStripeFrame11")
        self.element_sendkeys(postal, locatortype="name", value=self.card_postal)
        self.switchtodefaultcontent()

    # Agree with terms of service
    def termsagreecheck(self):
        self.element_click(locatortype="id", value=self.termsOfSrvc)

    # Click on all courses link
    def allcourseslink(self):
        self.scrolling("up")
        self.element_click(locatortype="xpath", value="//div[@id='navbar']/div/div/a")
        self.element_click(locatortype="xpath", value=self.allcourses)

    def clcallcourses(self):
        self.element_click(locatortype="xpath", value=self.allcourses)

    # Find course and enroll method
    def course_check(self, fulcoursename):
        self.jscript_search()
        self.course_click(fulcoursename)
        self.click_enroll()
        self.course_scroll()    # Improvised
        self.termsagreecheck()  # Improvised

    # Payment page method
    def course_payment(self, num, exp, cvc, postal):
        self.entercardnum(num)
        self.entercardexp(exp)
        self.entercardcvc(cvc)
        self.enterpostalcode(postal)

    # All courses check method
    def all_courses_check(self, fullcoursename):
        self.course_click(fullcoursename)
        self.click_enroll()
        #self.course_scroll()
        #self.termsagreecheck()

    def course_all_in(self, fullcoursename, num, exp, cvc, postal):
        self.course_check(fullcoursename)
        self.course_scroll()
        self.course_payment(num, exp, cvc, postal)
        self.termsagreecheck()









































