
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.08.18
#
# title: How can I get the Changing Data Values from website with Beautiful Soup?
# url: https://stackoverflow.com/questions/68831680/how-can-i-get-the-changing-data-values-from-website-with-beautiful-soup/68832090#68832090

# [How can I get the Changing Data Values from website with Beautiful Soup?](https://stackoverflow.com/questions/68831680/how-can-i-get-the-changing-data-values-from-website-with-beautiful-soup/68832090#68832090)


import requests
import time

url = 'https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'

while True:
    response = requests.get(url)
    data = response.json() 
    print(data['price'])
    
    time.sleep(5)
