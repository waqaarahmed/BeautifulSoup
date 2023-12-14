from bs4 import BeautifulSoup 
import requests

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find("table",{"class":"wikitable"})
for title in table:
	title = soup.find_all("th")

table_title = [title.text.strip() for title in title]
print(table_title)