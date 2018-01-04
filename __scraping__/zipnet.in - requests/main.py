import requests
from bs4 import BeautifulSoup
from time import sleep

url = "http://zipnet.in/index.php?page=missing_person_search&criteria=browse_all&Page_No=1"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

all_tables = soup.findAll('table')

for table in all_tables:
    print('--- table ---')
    all_rows = table.findAll('tr')
    for row in all_rows:
        all_cols = row.findAll('td')
        if len(all_cols) > 1:
            fields = all_cols[0].string
            details = all_cols[1].string
            print(fields, details)S
