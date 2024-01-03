<<<<<<< HEAD
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
=======
import requests
from bs4 import BeautifulSoup

url = "https://www.powersweeping.org/sweep-results/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find_all('strong')
print(title)
>>>>>>> 5103b975902aa88f81e30382477e5c2e2dea81c1
