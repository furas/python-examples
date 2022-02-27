
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.11
#
# title: scrape responsive table from site whose url doesnt change
# url: https://stackoverflow.com/questions/70317002/scrape-responsive-table-from-site-whose-url-doesnt-change/70317874#70317874

# [scrape responsive table from site whose url doesnt change](https://stackoverflow.com/questions/70317002/scrape-responsive-table-from-site-whose-url-doesnt-change/70317874#70317874)

# This page needs header `'X-Requested-With'`

# Using `start` (20, 40, etc.) you can get next pages in table

import requests

payload = {
 '_': '1639245456705',
 'columns[0][data]': 'DT_Row_Index',
 'columns[0][orderable]': 'false',
 'columns[0][search][regex]': 'false',
 'columns[0][searchable]': 'false',
 'columns[1][data]': 'published_date',
 'columns[1][orderable]': 'false',
 'columns[1][search][regex]': 'false',
 'columns[1][searchable]': 'true',
 'columns[2][data]': 'open',
 'columns[2][orderable]': 'false',
 'columns[2][search][regex]': 'false',
 'columns[2][searchable]': 'false',
 'columns[3][data]': 'high',
 'columns[3][orderable]': 'false',
 'columns[3][search][regex]': 'false',
 'columns[3][searchable]': 'false',
 'columns[4][data]': 'low',
 'columns[4][orderable]': 'false',
 'columns[4][search][regex]': 'false',
 'columns[4][searchable]': 'false',
 'columns[5][data]': 'close',
 'columns[5][orderable]': 'false',
 'columns[5][search][regex]': 'false',
 'columns[5][searchable]': 'false',
 'columns[6][data]': 'per_change',
 'columns[6][orderable]': 'false',
 'columns[6][search][regex]': 'false',
 'columns[6][searchable]': 'false',
 'columns[7][data]': 'traded_quantity',
 'columns[7][orderable]': 'false',
 'columns[7][search][regex]': 'false',
 'columns[7][searchable]': 'false',
 'columns[8][data]': 'traded_amount',
 'columns[8][orderable]': 'false',
 'columns[8][search][regex]': 'false',
 'columns[8][searchable]': 'false',
 'company': '95',
 'draw': '1',
 'length': '20',             # max 50
 'search[regex]': 'false',
 'start': '0'                # pagination 0, length*1, length*2, ...
}

headers = {
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'https://www.sharesansar.com/company-price-history'

response = requests.get(url, params=payload, headers=headers)
data = response.json() 
#print(data)

print('NR  | DATA       | OPEN   | CLOSE  |')
for number, item in enumerate(data['data'], 1):
    print(f'{number:3} |', item['published_date'], "|", item['open'], "|", item['close'], "|")

