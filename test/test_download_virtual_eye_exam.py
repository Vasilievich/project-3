import unittest
import time
from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

opts = ChromeOptions()
opts.add_argument("--width=800")
opts.add_argument("--height=600")


# opts.add_argument("--headless")


class DownloadVirtualEyeExam(unittest.TestCase):

    def setUp(self) -> None:
        """
        set up unittest, navigate to site
        :return:
        """
        self.driver = webdriver.Chrome(options=opts, executable_path="chromedriver.exe")
        self.driver.get("https://www.warbyparker.com/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
    def test_download_virtual_eye_exam(self):
        """
        testing the download virtual eye exam option
        :return:
        """
        get_a_prescription = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[2]/ul/li[6]/a").click()
        time.sleep(2)
        download_virtual_test = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div/div[2]/div/div[2]/div/div[3]/a").click()
        time.sleep(2)
        virtual_vision_title = self.driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/section[1]/div/div[2]/header/h1")
        self.assertEqual("Virtual Vision Test 12+", virtual_vision_title.text)
        time.sleep(2)

        
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)