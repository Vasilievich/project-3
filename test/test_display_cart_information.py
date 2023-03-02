import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_argument("--width=800")
opts.add_argument("--height=600")

class DisplayCartInformation(unittest.TestCase):
    """
    This class will use the site filters to select a pair of glasses and add to the cart
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

    def test_display_cart_info(self):
        """
        adds one pair of glasses to the cart and verifies the information
        """
        # click the search button
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[1]/a/span/span").click()
        time.sleep(1)

        # finds search field element
        search_field_element = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/main/div/div/div/div/div/div/div[1]/input")
        # input string for search
        search_field_element.send_keys("chamberlain")
        time.sleep(1)

        item_list = self.driver.find_elements(By.CLASS_NAME, "c-dDfmTE")[1].click()
        time.sleep(1)

        # select lenses and purchase
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[1]/div/div/div[2]/div/div/div[6]/div/div/button[1]").click()

        time.sleep(1)
        # select medium
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div").click()
        time.sleep(1)

        # select single vision
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()

        time.sleep(1)
        # select standard
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()
        time.sleep(1)
        # select classic
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()
        time.sleep(1)

        # select polycarbonate
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()
        time.sleep(1)

        # select add to cart
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[3]/div/div/div/button[1]").click()
        time.sleep(1)


    def tearDown(self):
        """
        tear down test and quit driver
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)