import requests
from bs4 import BeautifulSoup

url = "https://www.pro-football-reference.com/years/2021/passing.htm"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_ = 'per_match_toggle sortable stats_table')

for name in league_table.find_all('tbody'):
    rows = name.find_all('tr')
    for row in rows:
        name = row.find('td', class_ = 'left').text.strip()
        yards = row.find_all('td', class_ = 'right')[7].text
        touchdowns = row.find_all('td', class_ = 'right')[8].text
        print("Name " + name + " Yards " + yards +  " Touchdowns " + touchdowns)

