import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


opts = ChromeOptions()
opts.add_argument("--width=800")
opts.add_argument("--height=600")


class HomeTryOn(unittest.TestCase):
    """
    testing home try on function
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

    def test_home_try_on(self):
        """
        testing home try on option
        :return:
        """
        # click search button
        search_button_element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[1]/a/span/span").click()
        time.sleep(1)

        # finds search field element
        search_field_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/div/div[1]/input")

        # input string for search
        search_field_element.send_keys("percey")
        time.sleep(1)

        # click on a search result
        item_list = self.driver.find_elements(By.CLASS_NAME, "c-dDfmTE")[1].click()
        time.sleep(1)

        # select home try on
        self.driver.find_element(By.XPATH, "//*[@id='cta-try-frame-at-home-large-pill-blue-try-at-home-for-free']").click()
        time.sleep(1)

        # select medium
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[12]/div[1]/div[2]/div[2]/div[2]/div/div/div/label[1]/div[1]/div").click()
        time.sleep(1)

        # find the cart
        cart_link = self.driver.find_element(By.XPATH, f"//a[@href='/cart']")
        cart_link.click()
        time.sleep(1)

        # check that home try on appears in the cart
        home_try_on_count = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/section/div[1]/div[1]/h2')
        self.assertEqual(home_try_on_count.text, "1 of 5 Home Try-On frames chosen")


    def tearDown(self):
        """
        tear down test and quit driver
        """
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main(verbosity=2)