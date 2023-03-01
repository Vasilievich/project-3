import unittest
import time
from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

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

    def test_filter_glasses(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[2]/ul/li[2]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[2]/ul/li[2]/ul/li[1]/a/span").click()
        time.sleep(5)
        mens_eyglasses = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div/div[3]/div/div/div/div[1]/div/h1")
        time.sleep(5)
        self.assertEqual("Men's Eyeglasses", mens_eyglasses.text)
        # select eyeglasses
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/button[2]").click()
        time.sleep(2)
        # select Shop Men
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[1]/div/div/div/div[2]/button[2]/span").click()
        time.sleep(2)
        # select new arrivals
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[3]/div/div/div/div[1]/div/div[2]/div/fieldset[3]/label").click()
        time.sleep(2)
        # select filter
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[3]/div/div/div/div[1]/div/div[1]/button[4]/span").click()
        time.sleep(2)
        # select medium
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[3]/div/div/div/div[1]/div/div[5]/div/fieldset[10]/label").click()
        time.sleep(2)
        # select color
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[5]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/a/div/div/div/img").click()
        time.sleep(2)
        # select green
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[5]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/a/div/div/div/img").click()
        time.sleep(2)
        # select glasses
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[2]/div[1]/div/button/span").click()
        time.sleep(2)
        # select lenses and purchase
        self.driver.find_element(By.CLASS_NAME, "c-cFaYiI c-cFaYiI-heklHU-space-3 c-cFaYiI-jroWjL-alignX-center c-cFaYiI-fBJgOB-alignX-start")[0].click()
        time.sleep(3)
        # select wide
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[2]/div[1]/div/button").click()
        time.sleep(3)
        # select single vision
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button/span").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div[1]/button/span").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[3]/div/div/div/button[1]/div/span").click()
        time.sleep(3)
        cart_price = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/section/div[1]/header/div/h2")
        self.assertEqual("Your cart: $95", cart_price.text)







    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)