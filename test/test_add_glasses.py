import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_argument("--width=800")
opts.add_argument("--height=600")

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

    def test_filter_glasses(self):
        # select eyeglasses
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[2]/ul/li[2]/a").click()
        time.sleep(2)

        # select eyeglasses
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[2]/ul/li[2]/ul/li[1]/a/span").click()
        time.sleep(2)

        # select men eyeglasses
        mens_eyeglasses = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div/div[3]/div/div/div/div[1]/div/h1")
        time.sleep(2)
        self.assertEqual("Men's Eyeglasses", mens_eyeglasses.text)

        # select eyeglasses
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/button[2]").click()
        time.sleep(1)

        # select Shop Men
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[1]/div/div/div/div[2]/button[2]/span").click()
        time.sleep(1)

        # select new arrivals
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[3]/div/div/div/div[1]/div/div[2]/div/fieldset[3]/label").click()
        time.sleep(1)

        # select filter
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[3]/div/div/div/div[1]/div/div[1]/button[4]/span").click()
        time.sleep(1)

        # select medium
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[3]/div/div/div/div[1]/div/div[5]/div/fieldset[10]/label").click()
        time.sleep(1)

        # select color
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[5]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/a/div/div/div/img").click()
        time.sleep(2)

        # select lenses and purchase
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div[2]/div/div/div[6]/div/div/button[1]").click()
        time.sleep(1)

        # select medium
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div").click()
        time.sleep(1)

        # select single vision
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()
        time.sleep(1)

        # select standard
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()
        time.sleep(1)

        # select classic
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()
        time.sleep(1)

        # select polycarbonate
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button").click()
        time.sleep(1)

        # select add to cart
        cart_price = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[3]/div/div/div/button[1]")
        self.assertEqual("Add to cart: $95", cart_price.text)


    def test_filter_search(self):
        """
        test that search results contain the search term
        :return:
        """
        # click search button
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[1]/a/span/span").click()
        time.sleep(1)

        # finds search field element
        search_field_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/div/div[1]/input")

        # input string for search
        search_field_element.send_keys("per")
        time.sleep(5)

        # get the search results
        search_results = self.driver.find_elements(By.CLASS_NAME, "c-iSwBqf")

        # check that the search term is in the product name
        for search_result in search_results:
            product_name = search_result.find_element(By.TAG_NAME, 'h3')
            self.assertIn("per", product_name.text.lower())



    def tearDown(self):
        """
        tear down test and quit driver
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)