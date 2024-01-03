
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

