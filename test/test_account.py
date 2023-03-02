import unittest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_argument("--width=800")
opts.add_argument("--height=600")
# opts.add_argument("--headless")

class TestAccount(unittest.TestCase):
    """
    testing account creation and log in to the webpage
    """
    def setUp(self):
        """
        set up unittest, navigate to site
        :return:
        """
        self.driver = webdriver.Chrome(options=opts, executable_path="chromedriver.exe")
        self.driver.get("https://www.warbyparker.com/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_account_creation(self):
        """
        test creating account function
        """
        # click sign in
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[3]/a').click()
        time.sleep(2)
        # create account
        self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[3]/div/div/div/a/span').click()
        time.sleep(2)
        full_name_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/label/input')
        full_name_field.send_keys("John Smith")
        time.sleep(4)
        email_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[2]/label/input')
        email_field.send_keys("1234567@gmail.com")
        time.sleep(4)
        password_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[3]/label/input')
        password_field.send_keys("1234567890")
        time.sleep(4)
        press_create = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[5]/button/span')
        self.assertEqual("Create account", press_create.text)
        time.sleep(3)


    def test_account_login(self):
        """
        test sign in function
        """
        # click sign in page
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[3]/a').click()
        time.sleep(3)
        email_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/label/input')
        email_field.send_keys("1234567@gmail.com")
        time.sleep(4)
        password_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[2]/label/input')
        password_field.send_keys("1234567890")
        time.sleep(4)
        # click sign in button
        self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[4]/button/span').click()
        time.sleep(4)
        press_sign_out = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/p/a')
        self.assertEqual("Sign out", press_sign_out.text)
        time.sleep(3)


    def tearDown(self):
        """
        tear down test and quit driver
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)