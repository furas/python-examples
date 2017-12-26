import requests
import datetime
import csv

start_date = '2016.01.01'
finish_date = '2017.01.01'

start_date = datetime.datetime.strptime(start_date, '%Y.%m.%d')
finish_date = datetime.datetime.strptime(finish_date, '%Y.%m.%d')

start_timestamp = int(start_date.timestamp() * 1000)
one_day = datetime.timedelta(days=1)
finish_timestamp = int(finish_date.timestamp() * 1000)

print('dates:', start_timestamp, finish_timestamp)
print('-----')

f = open('output.csv', 'w')
csv_writer = csv.writer(f)

row = ('date', 'price_btc', 'price_usd', 'volume_usd')
csv_writer.writerow(row)

url = 'https://graphs.coinmarketcap.com/currencies/verge/{}/{}/'.format(start_timestamp, finish_timestamp)

response = requests.get(url)
data = response.json()

for key in data.keys():
    print('key:', key)
print('-----')

for item1, item2, item3 in zip(data['price_btc'], data['price_usd'], data['volume_usd']): #[:10]:

    date = datetime.datetime.fromtimestamp(item1[0]//1000)
    date = date.strftime('%Y.%m.%d %H:%M:%S')

    print('date:', date)
    print(' btc:', item1[1])
    print(' usd:', item2[1])
    print(' vol:', item3[1])
    print('-----')

    row = (date, item1[1], item3[1], item3[1])
    csv_writer.writerow(row)

f.close()    
