import unittest
from tests.home.test_login import TestLogin
from tests.courses.test_all_courses import TestAllCourses

# Get all tests from the test class
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestAllCourses)

# Create test suite
demoTest = unittest.TestSuite([tc1, tc2])

# Create runner
unittest.TextTestRunner(verbosity=2).run(demoTest)


















