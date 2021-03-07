from bs4 import BeautifulSoup
import requests
import csv

url = requests.get('https://www.cricingif.com/match/9102/karachi-kings-vs-quetta-gladiators-1st-match-2021/points-table')
soup = BeautifulSoup(url.text, 'html.parser')

table = soup.find('table', id='teams-points-table')
rows = table.find_all('tr')

with open("points_table.csv", "wt+", newline="") as pt:
    csv_writer = csv.writer(pt)
    for row in rows:
        csv_row = []
        for cell in row.find_all(['td', 'th']):
            csv_row.append(cell.get_text())
        csv_writer.writerow(csv_row)
