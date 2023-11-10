import os
from ssl import Options
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import ssl
from selenium.common.exceptions import NoSuchElementException


username = "anubhas"
access_key = "JvGShZ2Bm8RdgmGFbbx4ZtbOb6DeQ8nqSvtHDZdDY7PzqaZMTq"

class FirstSampleTest(unittest.TestCase):
    def setUp(self):

        options = ChromeOptions()
        options.browser_version = "114.0"
        options.platform_name = "Windows 10"

        lt_options = {
            "username": "anubhas",
            "accessKey": "JvGShZ2Bm8RdgmGFbbx4ZtbOb6DeQ8nqSvtHDZdDY7PzqaZMTq",
            "project": "Untitled",
            "w3c": True,
            "plugin": "python-python"
        }

        options.set_capability('LT:Options', lt_options)
        self.driver = webdriver.Remote(
            command_executor=f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub",
            options=options
        )

    def tearDown(self):
        self.driver.quit()

    def test_demo_site(self):

        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        try:
            print('Loading URL')
            driver.get("https://stage-lambda-devops-use-only.lambdatestinternal.com/To-do-app/index.html")

            driver.find_element(By.NAME, "li1").click()
            location = driver.find_element(By.NAME, "li2")
            location.click()
            print("Clicked on the second element")

            driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
            add_button = driver.find_element(By.ID, "addbutton")
            add_button.click()
            print("Added LambdaTest checkbox")

            search = driver.find_element(By.CSS_SELECTOR, ".container h2")
            assert search.is_displayed(), "heading is not displayed"
            print(search.text)
            search.click()
            driver.implicitly_wait(3)
            heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
            if heading.is_displayed():
                heading.click()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")

        except NoSuchElementException:
            print("Heading element is not found. Test failed!")
            driver.execute_script("lambda-status=failed")


if __name__ == "__main__":
    unittest.main()
