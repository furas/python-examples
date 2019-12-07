#!/usr/bin/env python3 

# date: 2019.12.06
# https://stackoverflow.com/questions/59205601/how-to-download-a-file-using-web-url-in-python-download-through-browser-works-b

import requests

headers = {'User-Agent': 'Mozilla/5.0'} # need header to download
url = 'https://www.nseindia.com/products/content/sec_bhavdata_full.csv'

r = requests.get(url, headers=headers)
#print(r.content)

with open('sec_bhavdata_full.csv', 'wb') as fh:
   fh.write(r.content)
   
print('---')   
import pandas as pd

df = pd.read_csv('sec_bhavdata_full.csv')   
print(df)
