import unittest
import os
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):
    _multiprocess_can_split_ = True
    _multiprocess_shared_ = True


    def setUp(self):
        username = os.environ['SAUCE_USERNAME']
        access_key = os.environ['SAUCE_ACCESS_KEY']

        capabilities = {
            'platform': "XP",
            'browserName': "chrome",
            'version': "31",
            # 'name': self._testMethodName
            'name': self.id()
        }
        self.driver = webdriver.Remote(
            command_executor = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key),
            desired_capabilities = capabilities)

    def tearDown(self):
        self.driver.quit()

    def test_google(self):
        driver = self.driver
        driver.get("http://www.google.com")
        if not "Google" in driver.title:
            raise Exception("Unable to load google page!")
        elem = driver.find_element_by_name("q")
        elem.send_keys("Sauce Labs")
        elem.submit()
