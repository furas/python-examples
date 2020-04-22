#!/usr/bin/env python3

# date: 2020.04.23
#https://stackoverflow.com/questions/61374853/scrape-dynamic-web-page-with-python-input-dates/

import requests

#url = 'https://www.nnbulgaria.com/life-insurance/insurance-plans/investment-insurance-nn-pro/value-of-investment-unit'

#url = 'https://www.nnbulgaria.com/Orchard.Nn/public/chartsUVData?chart-startdate=2004-06-01&chart-enddate=2020-04-23&value-per-share-type=LiPro'

url = 'https://www.nnbulgaria.com/Orchard.Nn/public/chartsUVData'

params = {
    'chart-startdate': '2004-06-01',
    'chart-enddate': '2020-04-23',
    'value-per-share-type': 'LiPro',
}

r = requests.get(url, params=params)
data = r.json()

print(data.keys())

for label, lowrisk, balanced in zip(data['labels'], data['dataLowRisk'], data['dataBalanced']):
    print(label, lowrisk, balanced)

