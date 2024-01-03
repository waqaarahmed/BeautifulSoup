import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url = "https://www.cityof.com/fl/tampa/title-companies"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting company names and addresses (replace with actual HTML structure)
    company_names = [name.text.strip() for name in soup.find_all('div', class_='company-name')]
    addresses = [address.text.strip() for address in soup.find_all('div', class_='company-address')]

    # Create a Pandas DataFrame
    data = {'Company Name': company_names, 'Address': addresses}
    df = pd.DataFrame(data)

    # Export to Excel
    df.to_excel('scraped_data.xlsx', index=False)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
