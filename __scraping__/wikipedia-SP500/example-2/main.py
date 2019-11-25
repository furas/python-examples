#!/usr/bin/env python3 

# date: 2019.11.23
# https://stackoverflow.com/questions/59003872/running-for-loop-and-skipping-stocks-with-keyerror-date

from datetime import datetime, timedelta
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas_datareader import data as web

html = urlopen('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(html,'lxml')
sp500_raw = soup.find('table', {'class': 'wikitable sortable'})

spsymbol = []

for row in sp500_raw.findAll('tr')[1:]:
    spsymbols = row.findAll('td')[0].text.strip()
    spsymbol.append(spsymbols)

start = datetime(2008, 1, 1).date()
end = datetime.today().date()

for ticker in spsymbol:
    print(ticker)
    try:
        df = web.get_data_yahoo(ticker, start, end)
        df = df.reset_index()
        #print(df.head())
        df.to_csv(ticker + '.csv', header=True, index=True, columns=['Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'], sep=' ')
    except Exception as ex:
        print('Ex:', ex)
