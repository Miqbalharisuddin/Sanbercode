import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://itera-qa.azurewebsites.net/"


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_success_delete(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get(url)  # buka situs
        time.sleep(2)
        # klik tombol login
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys(
            "test-login")  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys(
            "login123")  # isi password
        time.sleep(1)
        # klik tombol login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(1)
        # klik tombol delete
        browser.find_element(
            By.XPATH, "/html/body/div/div/table/tbody/tr[3]/td[7]/a[3]").click()
        time.sleep(2)
        # klik tombol delete
        browser.find_element(
            By.XPATH, "/html/body/div/div/form/div/input").click()
        time.sleep(2)

    def test_02_failed_delete(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get(url)  # buka situs
        time.sleep(2)
        # klik tombol login
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys(
            "test-login")  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys(
            "login123")  # isi password
        time.sleep(1)
        # klik tombol login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(1)
        # klik tombol delete
        browser.find_element(
            By.XPATH, "/html/body/div/div/table/tbody/tr[3]/td[7]/a[3]").click()
        time.sleep(2)
        # klik tombol back to list
        browser.find_element(By.XPATH, "/html/body/div/div/form/div/a").click()
        time.sleep(2)


unittest.main()
