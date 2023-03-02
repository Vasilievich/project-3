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

class FilterGlassesAddToCart(unittest.TestCase):
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

    def test_apply_discount(self):
        """
        adds two pairs of glasses to the cart and verifies if the discount is applied in the cart
        """
        time.sleep(2)
        # # click search button
        # search_button_element = WebDriverWait(self.driver, 10).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH, "//*[@href='search']/div[1]/div/section[2]/ul/li[1]/a"))
        # )
        search_button_element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[1]/a/span/span")

        search_button_element.click()
        time.sleep(1)

        # finds search field element
        search_field_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/div/div[1]/input")

        # input string for search
        search_field_element.send_keys("blakeley")
        time.sleep(1)

        item_list = self.driver.find_elements(By.CLASS_NAME, "c-dDfmTE")[1].click()
        time.sleep(1)

        # select lenses and purchase ***********
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

        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[3]/div/div/div/button[1]").click()
        time.sleep(1)

        # find search button element again
        search_button_element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[1]/a/span/span")

        # click search button
        search_button_element.click()

        time.sleep(2)

        # find search field element again
        search_field_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/div/div[1]/input")

        # input string for search
        search_field_element.send_keys("landon")

        time.sleep(1)

        # selects the second glasses after search
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

        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[3]/div/div/div/button[1]").click()
        time.sleep(1)

        # finds discounted text from cart list
        discount_text_element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/section/div[1]/div[2]/ul/p[3]/li")

        # checks cart list to see if discount is applied for multiple pairs
        self.assertEqual("15% off for purchasing multiple pairs of prescription eyewear", discount_text_element.text)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)