
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.09.08
# https://stackoverflow.com/questions/63785398/web-scraping-using-python-scrapy-or-beautiful-soup-fails-to-extract-data-from-ls

import requests
from bs4 import BeautifulSoup
import json   # only to display with indents (pretty print)

url = 'https://www.londonstockexchange.com/stock/GSK/glaxosmithkline-plc/fundamentals?lang=en'

r = requests.get(url)#, headers=headers)
print('len(text):', len(r.text))

#soup = BeautifulSoup(r.text, 'html.parser')  # doesn't parse 
#soup = BeautifulSoup(r.text, 'lxml')         # doesn't parse
soup = BeautifulSoup(r.text, 'html5lib')      # OK

all_scripts = soup.find_all('script', {'type': 'application/json'})

print('len(all_scripts):', len(all_scripts))

for item in all_scripts:
    #print(item)
    #print('item:', item.get('type'), len(item.get_text(strip=True)), len(item.text))
    
    # replace some values to have correct JSON 
    text = item.text.replace('&q;', '"').replace('&a;', '&')
    
    # convert JSON to Python structure (lists/dicts)
    data = json.loads(text)
    
    #---------------------------------------------
    
    # first key has strange and long value 
    #main_key = list(data.keys())[0]
    #print('main key:', main_key)

    # starting point in structure
    #start = data[main_key]['body']['components'][2]['status']['childComponents'][1]['content']['fundamentals']

    #print(json.dumps(start['incomeStatement']))  # pretty print
    #print(json.dumps(start['balanceSheet']))     # pretty print
    #print(json.dumps(start['ratios']))           # pretty print

    # testing content for different values
    #value = start['incomeStatement']['items'][0]['revenue']
    
    # display content and check which subelement has value `23,923.00` which is kept as `'23923000000'
    #if isinstance(value, list):
    #    for i, v in enumerate(value):
    #        print('>', i, '|', '23923' in json.dumps(v, indent=2))
    #if isinstance(value, dict):
    #    for k, v in value.items():
    #        print('>', k, '|', '23923' in json.dumps(v, indent=2))
            
    #print(value['label'], int(value['value'])/(1000000))

    #---------------------------------------------
    
    # first key has strange and long value 
    main_key = list(data.keys())[0]
    print('main key:', main_key)
    
    # first key has strange and long value 
    start = data[main_key]['body']['components'][2]['status']['childComponents'][1]['content']['fundamentals']

    # display all sections
    for key, val in start.items():
        
        values = val['items']
        print('--- {} ({}) ---'.format(key, len(values)))  # incomeStatement, balanceSheet, ratios
    
        # display all values in section (list of values)
        for value in values:
            max_len = max(len(v['label']) for v in value.values() if isinstance(v, dict))
            for k, v in value.items():
                if isinstance(v, dict):
                    print('dict | {:{}} = {:15} | values["{}"]'.format(v['label'], max_len, v['value'], k))
                #else:
                #    print(type(v), '| key:', k, '| val:', v)
            print('-----')
