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


class HomeTryOn(unittest.TestCase):

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

        :return:
        """
        # # click search button
        # search_button_element = WebDriverWait(self.driver, 10).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH, "//*[@href='search']/div[1]/div/section[2]/ul/li[1]/a"))
        # )
        search_button_element = self.driver.find_element(By.XPATH,
                                                         "/html/body/div[2]/div/header/nav/div[1]/div/section[2]/ul/li[1]/a/span/span")

        search_button_element.click()
        time.sleep(1)

        # finds search field element
        search_field_element = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/main/div/div/div/div/div/div/div[1]/input")

        # input string for search
        search_field_element.send_keys("percey")
        time.sleep(1)
        
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)