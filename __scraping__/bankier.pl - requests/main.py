import requests
import datetime
import time

# https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=CDPROJEKT

def one_day(symbol):

    print('Symbol:', symbol)

    # jeden dzien
    url = f'https://www.bankier.pl/new-charts/get-data\
?symbol={symbol}\
&intraday=true\
&today=true\
&type=area\
&init=true'
    
    r = requests.get(url)
    data = r.json()

    print('keys:', data.keys())

    print('Intraday:', data['intraday'])

    #print('Volume:', data['volume'][0])
    #print('Interval:', data['interval'])

    # timestamp jest przesunięty o 2 ogdziu
    h2 = datetime.timedelta(hours=2)

    # timestamp jest podany w milisekundach 
    # więc trzeba podzielic przez 1000 by otrzymać timestamp dla "datetime"
    dt = datetime.datetime.fromtimestamp(data['today']/1000) - h2
    
    print('Data:', dt.strftime('%Y.%m.%d %H:%M:%S'))

    # pierwsze 3 notowania
    for ts, val in data['main'][:3]:
        dt = datetime.datetime.fromtimestamp(ts/1000) - h2
        print(dt.strftime('  %Y.%m.%d | %H:%M:%S |'), val)
    print('  ...')

    # ostatnie 3 notowania
    for ts, val in data['main'][-3:]:
        dt = datetime.datetime.fromtimestamp(ts/1000) - h2
        print(dt.strftime('  %Y.%m.%d | %H:%M:%S |'), val)

    minimal = data['main'][0][1]
    minimal_timestamp = data['main'][0][0]
    maximal = data['main'][0][1]
    maximal_timestamp = data['main'][0][0]
    
    for ts, val in data['main']:
        if val < minimal:
            minimal = val
            minimal_timestamp = ts
        elif val > maximal:
            maximal = val
            maximal_timestamp = ts
            
    dt1 = datetime.datetime.fromtimestamp(minimal_timestamp/1000) - h2
    print('min:', minimal, dt1.strftime('| %Y.%m.%d | %H:%M:%S |'))
    dt2 = datetime.datetime.fromtimestamp(maximal_timestamp/1000) - h2
    print('max:', maximal, dt2.strftime('| %Y.%m.%d | %H:%M:%S |'))
    
    dt = dt1 - dt2 + datetime.timedelta(hours=24)
    print('diff:', maximal - minimal, '(', dt.days, 'dni )')
    
def week(symbol):
    # tydzien
    url = f'https://www.bankier.pl/new-charts/get-data\
?symbol={symbol}\
&intraday=true\
&type=area'

    r = requests.get(url)
    data = r.json()

    print('keys:', data.keys())

def month(symbol):
    # miesiac
    url = f'https://www.bankier.pl/new-charts/get-data\
?date_from=1523232000000\
&date_to=1525824000000\
&symbol={symbol}\
&intraday=false\
&type=area'

#----------------------------------------------------------------------

symbol = '11BIT'
one_day(symbol)

symbol = 'CDPROJEKT'
one_day(symbol)

