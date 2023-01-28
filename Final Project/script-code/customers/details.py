import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://itera-qa.azurewebsites.net/"


class TestDetail(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_succces_detail(self):
        # step
        # buka browser
        browser = self.browser
        # buka situs
        browser.get(url)
        browser.maximize_window()
        time.sleep(3)
        # klik menu login
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        time.sleep(2)
        # isi username
        browser.find_element(
            By.ID, "Username").send_keys("ita")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.ID, "Password").send_keys("itu")
        time.sleep(1)
        # klik button login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(2)
        # search
        browser.find_element(
            By.ID, "searching").send_keys("ita")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div/form/input[2]").click()
        time.sleep(1)
        # klik button detail
        browser.find_element(
            By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]").click()
        time.sleep(2)
        # klik button back to list
        browser.find_element(
            By.XPATH, "/html/body/div/p/a[2]").click()
        time.sleep(2)
        # validasi
        expectedURL = "https://itera-qa.azurewebsites.net/Dashboard"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def test_succces_detail_with_blank_field(self):
        # step
        # buka browser
        browser = self.browser
        # buka situs
        browser.get(url)
        browser.maximize_window()
        time.sleep(3)
        # klik menu login
        browser.find_element(
            By.XPATH, "/html/body/nav/div/form/ul/li[2]/a").click()
        time.sleep(2)
        # isi username
        browser.find_element(
            By.ID, "Username").send_keys("ita")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.ID, "Password").send_keys("itu")
        time.sleep(1)
        # klik button login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(2)
        # klik button detail
        browser.find_element(By.XPATH, "/html/body/div/div/table/tbody/tr[2]")
        browser.find_element(
            By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]").click()
        time.sleep(2)
        # klik edit button
        browser.find_element(
            By.XPATH, "/html/body/div/p/a[1]").click()
        time.sleep(2)
        # hapus name
        edit_name = browser.find_element(By.ID, "Name")
        edit_name.clear()
        time.sleep(1)
        # hapus company
        edit_company = browser.find_element(By.ID, "Company")
        edit_company.clear()
        time.sleep(1)
        # hapus Address
        edit_address = browser.find_element(By.ID, "Address")
        edit_address.clear()
        time.sleep(1)
        # hapus City
        edit_city = browser.find_element(By.ID, "City")
        edit_city.clear()
        time.sleep(1)
        # hapus Phone
        edit_phone = browser.find_element(By.ID, "Phone")
        edit_phone.clear()
        time.sleep(1)
        # hapus Email
        edit_email = browser.find_element(By.ID, "Email")
        edit_email.clear()
        time.sleep(1)
        # klik button Save
        browser.find_element(
            By.XPATH, "/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(3)
        # klik button detail
        browser.find_element(By.XPATH, "/html/body/div/div/table/tbody/tr[2]")
        browser.find_element(
            By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]").click()
        time.sleep(2)
        # Klik Button back to list
        browser.find_element(
            By.XPATH, "/html/body/div/p/a[2]").click()
        time.sleep(2)
        # validasi
        expectedURL = "https://itera-qa.azurewebsites.net/Dashboard"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
