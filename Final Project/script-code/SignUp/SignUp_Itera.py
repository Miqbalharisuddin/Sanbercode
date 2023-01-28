#farah amalia

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from data1 import datates
from data2 import datates2
import datacoba 
import datacoba2


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_01SignUp_Success(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.XPATH, "//nav/div/form[@class='form-inline my-2 my-lg-0']//a[@href='/UserRegister/NewUser']").click() # klik button sign-up
        time.sleep(1)
        datacoba.data(browser)
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys("TesItera5") # isi Username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys("Itera123") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "ConfirmPassword").send_keys("Itera123") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click() # klik tombol sign in
        time.sleep(1) 

        #validasi
        response_message = browser.find_element(By.CLASS_NAME,"label-success").text
        self.assertEqual(response_message, 'Registration Successful')  


    def test_02SignUp_Invalid_Username(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.XPATH, "//nav/div/form[@class='form-inline my-2 my-lg-0']//a[@href='/UserRegister/NewUser']").click() # klik button sign-up
        time.sleep(1)
        datacoba.data(browser)
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys("Tes Itera") # isi Username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys("Itera123") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "ConfirmPassword").send_keys("Itera123") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click() # klik tombol sign in
        time.sleep(1)

        #validasi
        response_message = browser.find_element(By.CLASS_NAME,"label-success").text
        self.assertEqual(response_message, 'Registration Successful')  
    
    def test_03SignUp_Invalid_Pass(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.XPATH, "//nav/div/form[@class='form-inline my-2 my-lg-0']//a[@href='/UserRegister/NewUser']").click() # klik button sign-up
        time.sleep(1)
        datacoba.data(browser)
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys("Testeraa") # isi Username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys("@@") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "ConfirmPassword").send_keys("@@") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click() # klik tombol sign in
        time.sleep(1)

        #validasi
        response_message = browser.find_element(By.CLASS_NAME,"label-success").text
        self.assertEqual(response_message, 'Registration Successful')  

    def test_04SignUp_BlankField(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.XPATH, "//nav/div/form[@class='form-inline my-2 my-lg-0']//a[@href='/UserRegister/NewUser']").click() # klik button sign-up
        time.sleep(1)
        datacoba2.data(browser)
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys("") # isi Username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "ConfirmPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click() # klik tombol sign in
        time.sleep(1) 

        #validasi
        response_message = browser.find_element(By.ID,"FirstName-error").text
        self.assertEqual(response_message, 'Please enter first name')  
        response_message = browser.find_element(By.ID,"Surname-error").text
        self.assertEqual(response_message, 'Please enter surname')
        response_message = browser.find_element(By.ID,"Username-error").text
        self.assertEqual(response_message, 'Please enter username')
        response_message = browser.find_element(By.ID,"Password-error").text
        self.assertEqual(response_message, 'Please enter password')

    def test_05SignUp_User_Existing(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.XPATH, "//nav/div/form[@class='form-inline my-2 my-lg-0']//a[@href='/UserRegister/NewUser']").click() # klik button sign-up
        time.sleep(1)
        datacoba.data(browser)
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys("Tesi tera") # isi Username
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys("Itera123") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "ConfirmPassword").send_keys("Itera123") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click() # klik tombol sign in
        time.sleep(1)

        #validasi
        response_message = browser.find_element(By.CLASS_NAME,"label-danger").text
        self.assertEqual(response_message, 'Username already exist')  


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()