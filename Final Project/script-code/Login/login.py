import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

baseUrl = "https://demoqa.com/"
driverInstall = ChromeDriverManager().install()


class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(
            options=options, service=Service(driverInstall))
        self.browser.maximize_window()

    def test_success_link_button(self):
        # steps
        browser = self.browser
        browser.get(baseUrl + "links")
        time.sleep(3)
        browser.find_element(By.ID, "simpleLink").click()
        time.sleep(5)
        self.browser.close()

    def test_success_link_button_new_window(self):
        # steps
        browser = self.browser
        browser.get(baseUrl + "browser-windows")
        time.sleep(3)
        browser.find_element(By.ID, "simpleLink").click()
        time.sleep(5)
        self.browser.close()

    def test_success_link_button_new_window(self):
        # steps
        browser = self.browser
        browser.get(baseUrl + "browser-windows")
        time.sleep(3)
        browser.find_element(By.ID, "simpleLink").click()
        time.sleep(5)
        self.browser.close()

    def test_success_link_button_hover(self):
        # steps
        browser = self.browser
        browser.get(baseUrl + "tool-tips")
        time.sleep(3)
        browser.find_element(By.ID, "toolTipButton").click()
        time.sleep(5)
        self.browser.close()

    def test_success_link_button_change_color(self):
        # steps
        browser = self.browser
        browser.get(baseUrl + "dynamic-properties")
        time.sleep(3)
        browser.find_element(By.ID, "colorChange").click()
        time.sleep(5)
        self.browser.close()

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
