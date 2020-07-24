
# author: https://blog.furas.pl
# date: 2020.07.09
# link: https://stackoverflow.com/questions/62812282/why-arent-the-table-data-tags-available-in-the-soup/

import requests

url = 'https://www.grainger.com/product/tableview/GRAINGER-APPROVED-Type-F-Stainless-Steel-Cam-WP11501162?breadcrumbCatId=1001429'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
data = r.json()

for item in data['headers']:
    print(item['title'])

for item in data['records'][0]['children']:
    for x in item['techAttributes']:
        print(' >', x['name'], '=',  x['value'])
    print('---')
