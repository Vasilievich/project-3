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
        self.sign_in = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[3]/a').click()
        time.sleep(2)
        self.create_account = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[3]/div/div/div/a/span').click()
        time.sleep(2)
        self.full_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/label/input')
        self.full_name_field.send_keys("John Smith")
        time.sleep(4)
        self.email_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[2]/label/input')
        self.email_field.send_keys("1234567@gmail.com")
        time.sleep(4)
        self.password_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[3]/label/input')
        self.password_field.send_keys("1234567890")
        time.sleep(4)
        self.press_create = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[5]/button/span')
        self.assertEqual("Create account", self.press_create.text)
        time.sleep(3)


    def test_account_login(self):
        self.sign_in = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[3]/a').click()
        time.sleep(3)
        self.email_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/label/input')
        self.email_field.send_keys("1234567@gmail.com")
        time.sleep(4)
        self.password_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[2]/label/input')
        self.password_field.send_keys("1234567890")
        time.sleep(4)
        self.click_sign_in = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[4]/button/span').click()
        time.sleep(4)
        self.press_sign_out = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/p/a')
        self.assertEqual("Sign out", self.press_sign_out.text)
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)