
# date: 2020.09.11
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)
# https://stackoverflow.com/questions/63840415/how-to-scrape-website-tables-where-the-value-can-be-different-as-we-chose-but-th

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://id.investing.com/instruments/HistoricalDataAjax'

payload = {
    "curr_id": "8830",
    "smlID": "300004",
    "header": "Data+Historis+Emas+Berjangka",
    "st_date": "01/30/2020",
    "end_date": "12/31/2020",
    "interval_sec": "Daily",
    "sort_col": "date",
    "sort_ord": "DESC",
    "action":"historical_data"
}

headers = {
    #"Referer": "https://id.investing.com/commodities/gold-historical-data",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
    "X-Requested-With": "XMLHttpRequest"
}

fh = open('output.csv', 'w')
csv_writer = csv.writer(fh)

for year in range(2010, 2021):
    print('year:', year)
    
    payload["st_date"] = f"01/01/{year}"
    payload["end_date"] = f"12/31/{year}"
    
    r = requests.post(url, data=payload, headers=headers)
    #print(r.text)
    
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find('table')
    for row in table.find_all('tr')[1:]: # [1:] to skip header
        row_data = [item.text for item in row.find_all('td')]
        print(row_data)
        csv_writer.writerow(row_data)
        
fh.close()        