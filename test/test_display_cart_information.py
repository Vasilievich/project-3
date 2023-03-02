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
        # select wide
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[2]/div[1]/div").click()
        time.sleep(1)

        # select non-prescription
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[3]/div[1]/div[1]/button").click()

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

        # finds type of glasses and assertEqual the type information
        glasses_type = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/section/div[1]/div[1]/div/span/div/div[2]/h4/a")
        self.assertEqual("Chamberlain", glasses_type.text)

        # finds subtype of glasses and assertEqual the subtype information
        glasses_subtype = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/section/div[1]/div[1]/div/span/div/div[2]/div[1]/div[1]")
        self.assertEqual("Whiskey Tortoise", glasses_subtype.text)

        # finds frame width of glasses and assertEqual the frame width information
        glasses_frame_width = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/section/div[1]/div[1]/div/span/div/div[2]/div[1]/div[2]/p")
        self.assertEqual("Wide", glasses_frame_width.text)

        # finds prescription type of glasses and assertEqual the prescription type information
        glasses_prescription_type = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/section/div[1]/div[1]/div/span/div/div[2]/div[1]/div[3]/div/div[1]/p")
        self.assertEqual("Non-prescription     $95", glasses_prescription_type.text)

        # finds lens type of glasses and assertEqual the lens type information
        glasses_lens_type = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/section/div[1]/div[1]/div/span/div/div[2]/div[1]/div[3]/div/div[2]/p")
        self.assertEqual("Classic  Free", glasses_lens_type.text)


    def tearDown(self):
        """
        tear down test and quit driver
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)