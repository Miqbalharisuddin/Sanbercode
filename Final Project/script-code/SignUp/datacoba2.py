#farah amalia

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from data1 import datates
from data2 import datates2

def data(browser):
    browser.find_element(By.ID, "FirstName").send_keys(datates2.FirstName) # isi First Name
    time.sleep(1)
    browser.find_element(By.ID, "Surname").send_keys(datates2.Surname) # isi Surname
    time.sleep(1)
    browser.find_element(By.ID, "E_post").send_keys(datates2.E_post) # isi E_Post
    time.sleep(1)
    browser.find_element(By.ID, "Mobile").send_keys(datates2.Mobile) # isi Mobile