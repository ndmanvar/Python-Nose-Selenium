import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_python_org123(self):
        driver = self.driver
        driver.get("http://www.github.com")
        self.assertIn("GitHub", driver.title)

    def tearDown(self):
        self.driver.quit()