import requests
import datetime
import csv
import webbrowser


def get_data(name, timestamp1, timestamp2, csv_writer):
    
    url = 'https://graphs.coinmarketcap.com/currencies/{}/{}/{}/'.format(name, timestamp1, timestamp2)

    response = requests.get(url)
    
    try:
        data = response.json()
    except Exception:
        with open('output.html', 'w') as f:
            f.write(response.text)
        webbrowser.open('output.html')
        exit()

    for item1, item2, item3 in zip(data['price_btc'], data['price_usd'], data['volume_usd']): #[:10]:

        date = datetime.datetime.fromtimestamp(item1[0]//1000)
        date = date.strftime('%Y.%m.%d %H:%M:%S')

        row = (date, item1[1], item3[1], item3[1])
        csv_writer.writerow(row)

    
def scrape(name, start_date, finish_date):

    f = open(name + '.csv', 'w')
    csv_writer = csv.writer(f)

    row = ('date', 'price_btc', 'price_usd', 'volume_usd')
    csv_writer.writerow(row)

    one_day = datetime.timedelta(days=1)

    start_date = datetime.datetime.strptime(start_date, '%Y.%m.%d')
    finish_date = datetime.datetime.strptime(finish_date, '%Y.%m.%d')

    date1 = start_date
    date2 = start_date + one_day

    while date1 < finish_date:
        print(name, date1, date2)
        
        date1_timestamp = int(date1.timestamp() * 1000)
        date2_timestamp = int(date2.timestamp() * 1000)

        get_data(name, date1_timestamp, date2_timestamp, csv_writer)
        
        date1 = date2
        date2 += one_day
            
    f.close()    

# --- main ---

scrape('verge', '2016.01.01', '2017.01.01')
scrape('bitcoin', '2016.01.01', '2017.01.01')
scrape('ethereum', '2016.01.01', '2017.01.01')

