import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

url = "https://itera-qa.azurewebsites.net/"
driverInstall = ChromeDriverManager().install()


class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(
            options=options, service=Service(driverInstall))
        self.browser.maximize_window()

    def test_a_success_logout(self):
        # stepds
        browser = self.browser  # buka web browser
        browser.get(url)  # buka situs
        time.sleep(3)

        # isi email
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        browser.find_element(By.ID, "Username").send_keys(
            "testing01")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys(
            "123456")  # isi password
        time.sleep(1)
        browser.find_element(By.NAME, "login").click()  # klik tombol sign in
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
