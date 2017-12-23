#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47842359/1832058
#

import requests

url = 'http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i=9211775239375291&Top=999999&A=0'

r = requests.get(url)

print(r.text[:50]) # first 50 chars

data = r.text.split(';')

print('number od days:', len(data))

for row in data: # data[:5]: # first 5 rows
    row = row.split('@')
    print('date:', row[0], '|', row[1:4]) # first 3 values

'''
Result (small preview)

20171213@901.00@863.00@893.00@901.00@901.00@859.00

number od days: 1202

date: 20171213 | ['901.00', '863.00', '893.00']
date: 20171212 | ['859.00', '859.00', '859.00']
date: 20171211 | ['823.00', '782.00', '819.00']
date: 20171210 | ['796.00', '780.00', '784.00']
date: 20171209 | ['797.00', '781.00', '787.00']
...
'''
