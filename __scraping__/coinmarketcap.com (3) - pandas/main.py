
# author: https://blog.furas.pl
# date: 2020.07.25
# link: https://stackoverflow.com/questions/63075215/read-html-where-required-table-needs-users-input/

import pandas as pd

all_dfs = pd.read_html('https://coinmarketcap.com/exchanges/bitfinex/')

df = all_dfs[2]

df[ df['Pair'].str.endswith('USD') ]
