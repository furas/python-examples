
# date: 2019.09.16
# https://stackoverflow.com/questions/57861715/scrapy-infinite-scrolling-no-pagination-indication
# http://www.aastocks.com
import requests

newstime = '934735827'
newsid = 'HKEX-EPS-20190815-003587368'

url = 'http://www.aastocks.com/tc/resources/datafeed/getmorenews.ashx?cat=all&newstime={}&newsid={}&period=0&key=&symbol=00001'
url_artickle = "http://www.aastocks.com/tc/stocks/analysis/stock-aafn-con/00001/{}/all"

for x in range(3):
    
    print('---', x, '----')
    print('data:', url.format(newstime, newsid))
    
    r = requests.get(url.format(newstime, newsid))
    data = r.json()

    #for item in data[:3]: # test only few links
    for item in data[:-1]: # skip last link which gets next page
        r = requests.get(url_artickle.format(item['id']))
        print('news:', r.status_code, url_artickle.format(item['id']))
        
    # get data for next page
    newstime = data[-1]['dtd']
    newsid = data[-1]['id']
    print('next page:', newstime, newsid)
