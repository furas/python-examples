# date: 2020.02.29
# https://stackoverflow.com/questions/60461526/how-to-scrape-for-multiple-quotes-from-yahoo-using-beautiflul-soup

import requests

for symbol in ['AAPL', 'WYNN', 'PCB', 'AMZN', 'USAK']:
    params = {
        'symbols': symbol,
        'range': '1d',
        'interval': '5m',
        'indicators': 'close',
        'includeTimestamps': 'false',
        'includePrePost': 'false',
        'corsDomain': 'finance.yahoo.com',
        '.tsrc': 'finance'
    }
    
    url = 'https://query1.finance.yahoo.com/v7/finance/spark'
    
    r = requests.get(url, params=params)
    data = r.json()
    
    print('---', symbol, '---')
    print(data['spark']['result'][0]['response'][0]['indicators']['quote'][0]['close'])
    
    
