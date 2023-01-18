import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_succces_login(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(8)
        # validasi
        expectedURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actualURL = browser.current_url
        self.assertEquals(expectedURL, actualURL)

    def test_failed_login_with_invalid_username_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Yantobasna")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("yanto123")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertIn(response_message, 'Invalid credentials')

    def test_failed_login_with_blank_username_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("")
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("")
        time.sleep(1)
        # klik buton login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
        self.assertIn(response_message, 'Required')

        response_message = browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text
        self.assertIn(response_message, 'Required')

    def test_successfull_search_without_filter(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(5)
        # isi username
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi username
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        # klik button login
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        # klik tombol recruitment
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
        time.sleep(5)
        # klik tombol search
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]").click()
        time.sleep(5)
        # validasi
        response_message = browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text
        self.assertIn('Found', response_message)

    def test_successfull_search_with_filter(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        browser.maximize_window()
        time.sleep(4)
        # isi username
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi username
        time.sleep(1)
        # isi password
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        # klik button login
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3)
        # klik tombol recruitment
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
        time.sleep(1)
        # klik dropwdown vacancy
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click()
        time.sleep(1)
        # pilih item dropdown vacancy
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        # click dropdown hiring manager
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(1)
        # pilih item dropdown hiring manager
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        # click dropdown status
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(1)
        # pilih item dropdown status
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[8]").click()
        time.sleep(3)
        # klik tombol search
        browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]").click()
        time.sleep(5)

        # validasi
        response_message = browser.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('Found', response_message)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
