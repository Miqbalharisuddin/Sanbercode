import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://itera-qa.azurewebsites.net/"


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_success_search_by_name(self):
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
        browser.find_element(By.ID, "searching").send_keys(
            "Patsy")  # isi search
        time.sleep(1)
        # klik tombol search
        browser.find_element(
            By.XPATH, "/html/body/div/div/form/input[2]").click()
        time.sleep(3)

    def test_02_success_search_by_email(self):
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
        browser.find_element(By.ID, "searching").send_keys(
            "derandals@")  # isi search
        time.sleep(1)
        # klik tombol search
        browser.find_element(
            By.XPATH, "/html/body/div/div/form/input[2]").click()
        time.sleep(3)

    def test_03_failed_search_by_company(self):
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
        browser.find_element(By.ID, "searching").send_keys(
            "Frogbox")  # isi search
        time.sleep(1)
        # klik tombol search
        browser.find_element(
            By.XPATH, "/html/body/div/div/form/input[2]").click()
        time.sleep(3)

    def test_04_failed_search_by_city(self):
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
        browser.find_element(By.ID, "searching").send_keys(
            "Bandung")  # isi search
        time.sleep(1)
        # klik tombol search
        browser.find_element(
            By.XPATH, "/html/body/div/div/form/input[2]").click()
        time.sleep(3)


unittest.main()
