#!/usr/bin/env python3

"""
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2024.04.21

# [python - Getting tabular data into a dataframe from a PHP webpage - Stack Overflow](https://stackoverflow.com/questions/78361743/getting-tabular-data-into-a-dataframe-from-a-php-webpage/78362597#78362597)

# I used button `Download CSV` and `Firefox Download Manager` with command `Copy Download Link` to get URLs

# Top 20 Gainers/ Losers

# https://www.nseindia.com/api/live-analysis-variations?index=loosers&type=BANKNIFTY&csv=true
"""

import requests

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0'}

url = 'https://www.nseindia.com/market-data/top-gainers-losers'
response = session.get(url, headers=headers)  
#print(response.text)

url = 'https://www.nseindia.com/api/live-analysis-variations?index=gainers&type=NIFTY&csv=true'
response = session.get(url, headers=headers)
response.encoding = "utf-8-sig"
gainers = response.text
print('\n--- gainers ---\n')
print(gainers)

url = 'https://www.nseindia.com/api/live-analysis-variations?index=loosers&type=NIFTY&csv=true'
response = session.get(url, headers=headers)
response.encoding = "utf-8-sig"
loosers = response.text
print('\n--- loosers ---\n')
print(loosers)

import pandas as pd
import io

df_gainers = pd.read_csv(io.StringIO(gainers))
print('\n--- gainers ---\n')
print(df_gainers)

df_loosers = pd.read_csv(io.StringIO(loosers))
print('\n--- loosers ---\n')
print(df_loosers)


