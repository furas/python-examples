
# date: 2019.09.12
# https://stackoverflow.com/questions/57913629/scrap-dynamic-chart-data/57914736#57914736

import requests
import datetime

day = datetime.date(2019, 7, 4)

payload = {
    'api-method': 'pricesForAllSeriesGet',
    'resource': 'MarketPriceGraph_Block',
    'mc0': 'NL RTM',
    'mc1': 'AV G20',
}

url = 'https://shipandbunker.com/a/.json'
r = requests.post(url, data=payload)
data = r.json()

for number, value in data['api']['NL RTM']['data']['prices']['IFO380']['dayprice']:

    # convert day number to date object
    timestamp = data['api']['NL RTM']['data']['day_list']['IFO380'][str(number)]
    date = datetime.date.fromtimestamp(timestamp/1000)
    
    if date == day:
        print(day, value)
        break
