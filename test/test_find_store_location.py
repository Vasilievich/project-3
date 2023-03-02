import unittest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

opts = ChromeOptions()
opts.add_argument("--width=800")
opts.add_argument("--height=600")


# opts.add_argument("--headless")


class FindStoreLocation(unittest.TestCase):
    """
    testing store locator and optometrist locator
    """

    def setUp(self) -> None:
        """
        set up unittest, navigate to site
        :return:
        """
        self.driver = webdriver.Chrome(options=opts, executable_path="chromedriver.exe")
        self.driver.get("https://www.warbyparker.com/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_find_store_location(self):
        """
        testing the store locator option
        :return:
        """
        locations = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[2]/a").click()
        time.sleep(2)
        self.address_field = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div[1]/div/div[1]/input")
        self.address_field.send_keys("94502")
        time.sleep(4)
        self.address_field.send_keys(Keys.ENTER)
        time.sleep(2)
        address_selection = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div[2]/div[1]/div[1]/a").click()
        time.sleep(2)
        store_location = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div/div[2]/div/div/h1")
        self.assertEqual("Fourth St.", store_location.text)
        time.sleep(2)

    def test_eye_exam_location(self):
        """
        testing to find store locations with eye exam
        :return:
        """
        locations = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[2]/a").click()
        time.sleep(2)
        exam_locations = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div[1]/label/div/div").click()
        time.sleep(2)
        self.address_field = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div[1]/div/div[1]/input")
        self.address_field.send_keys("94502")
        time.sleep(4)
        self.address_field.send_keys(Keys.ENTER)
        time.sleep(2)
        address_selection = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div[2]/div[1]/div[1]/a[1]").click()
        time.sleep(2)
        burlingame_store_location = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div/div[2]/div/div/h1")
        self.assertEqual("Burlingame Ave.", burlingame_store_location.text)
        time.sleep(2)
        book_exam = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div/section[1]/div/div/div/div/button").click()
        time.sleep(2)
        select_continue = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[2]/div/div[2]/section/div[1]/div[2]/button").click()
        time.sleep(2)
        select_time = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[2]/div/div/form/div/fieldset/legend")
        self.assertEqual("Select an exam time", select_time.text)
        time.sleep(2)


    def tearDown(self):
        """
        tear down test and quit driver
        """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)