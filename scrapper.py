from bs4 import BeautifulSoup 
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Pakistan'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find_all('table')[0]
titles = table.find_all('th')
table_title = [title.text.strip() for title in titles ]
column = table.find_all('tr')
for r in column:
	row = r.find_all('td')
	row_data = [data.text.strip() for data in row]
	print(row_data)

#df = pd.DataFrame(columns = table_title)