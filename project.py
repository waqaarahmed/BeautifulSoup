from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time
from bs4 import BeautifulSoup

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://www.powersweeping.org/finding-a-sweeping-contractor-advanced-search/')
input_element = driver.find_element(By.NAME, "frmCertifed")
input_element.click()
input_element_ii = driver.find_element(By.CLASS_NAME, "submit" )
input_element_ii.click()
time.sleep(30)
driver.quit()