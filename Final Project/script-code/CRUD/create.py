import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://itera-qa.azurewebsites.net/"


class TestCreate(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_01_success_create(self):
        # steps
        browser = self.browser
        browser.get(url)
        time.sleep(2)
        # click button login
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys(
            "test-login")  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys(
            "login123")  # isi password
        time.sleep(1)
        # click button login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(1)
        # click button Create Customer
        browser.find_element(By.XPATH, "/html/body/div/div/p[1]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "Name").send_keys("ilham")  # isi name
        time.sleep(1)
        browser.find_element(By.ID, "Company").send_keys(
            "go-to")  # filling company
        time.sleep(1)
        browser.find_element(By.ID, "Address").send_keys(
            "jl.blablabla")  # filling address
        time.sleep(1)
        browser.find_element(By.ID, "City").send_keys("klaten")  # filling city
        time.sleep(1)
        browser.find_element(By.ID, "Phone").send_keys(
            "089786780")  # filling phone
        time.sleep(1)
        browser.find_element(By.ID, "Email").send_keys(
            "ilham@gmail.com")  # filling email
        time.sleep(1)
        # klik tombol create
        browser.find_element(
            By.XPATH, "/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(1)

    def test_02_failed_create_with_balnk_data(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get(url)  # buka situs
        time.sleep(2)
        # klik tombol login
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys(
            "test-login")  # filling username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys(
            "login123")  # filling password
        time.sleep(1)
        # click button login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(1)
        # click button create customer
        browser.find_element(By.XPATH, "/html/body/div/div/p[1]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "Name").send_keys("")  # isi name
        time.sleep(1)
        browser.find_element(By.ID, "Company").send_keys("")  # isi company
        time.sleep(1)
        browser.find_element(By.ID, "Address").send_keys("")  # isi address
        time.sleep(1)
        browser.find_element(By.ID, "City").send_keys("")  # isi city
        time.sleep(1)
        browser.find_element(By.ID, "Phone").send_keys("")  # isi phone
        time.sleep(1)
        browser.find_element(By.ID, "Email").send_keys("")  # isi email
        time.sleep(1)
        # click button create customer
        browser.find_element(
            By.XPATH, "/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(2)


unittest.main()
