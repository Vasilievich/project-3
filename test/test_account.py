import unittest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestAccount(unittest.TestCase):
    """
    testing account creation and log in to the webpage
    """
    def setUp(self):
        """
        set up unittest, navigate to site
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.warbyparker.com/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_account_creation(self):
        pass

    def test_account_login(self):
        pass



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)