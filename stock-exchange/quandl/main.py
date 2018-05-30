#!/usr/bin/env python3

import quandl

data = quandl.get('WSE/PZU')

print('    columns:', list(data.columns))
print('start index:', data.index[0])
print('  end index:', data.index[-1])

#     columns: ['Open', 'High', 'Low', 'Close', '%Change', 'Volume', '# of Trades', 'Turnover (1000)']
# start index: 2010-05-12 00:00:00
#   end index: 2018-05-29 00:00:00
