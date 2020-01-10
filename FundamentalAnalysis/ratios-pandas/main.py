#!/usr/bin/env python3 

# date: 2020.01.02
# ???

import FundamentalAnalysis as fa
import pandas as pd
import io

text='''Ticker                      Company
A    Agilent Technologies Inc.
AA            ALCOA CORPORATION
AAC             AAC Holdings Inc
AAL  AMERICAN AIRLINES GROUP INC
AAME      Atlantic American Corp.'''

df = pd.read_csv(io.StringIO(text), sep='\s{2,}')

symbols = df['Ticker'].to_list()
#symbols = ["TSLA" , "AAPL" , "MSFT"]
print(symbols)

ratios = list()
for s in symbols:
    try:
        ratios.append(fa.ratios(s))
    except Exception as ex:
        print(s, ex)

df = pd.concat(ratios, axis=1)
print(df.columns)
print(df)

