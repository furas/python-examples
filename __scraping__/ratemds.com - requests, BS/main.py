
# date: 2020.07.01
# https://stackoverflow.com/questions/62672619/scrapy-extracting-data-using-response-text

import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0',
}

url = 'https://www.ratemds.com/doctor-ratings/dr-zach-olesinski-toronto-on-ca'

r = requests.get(url, headers=headers)
#print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')

all_scripts = soup.find_all('script')
print('len:', len(all_scripts))

for script in all_scripts:
    if 'window.DATA.doctorDetailProps = JSON.parse("' in script.text:
        text = script.text 
       
        start = text.find('window.DATA.doctorDetailProps = JSON.parse("') + len('window.DATA.doctorDetailProps = JSON.parse("')
        end   = text.find('")', start)
        #print(text[start:end])

        text = text[start:end]
        #text = text.replace(r'\u0022', '"')
        text = text.encode().decode('raw_unicode_escape')
        data = json.loads(text)
        
        #print(json.dumps(data['doctor'], indent=2))
        #print(data['doctor'].keys())
        
        print('\n--- full_name ---\n')
        print(data['doctor']['full_name'])
        
        print('\n--- sample_rating_comment ---\n')
        print(data['doctor']['sample_rating_comment'])
        
        print('\n--- comments ---\n')
        for result in data['ratingsPage']['results']:
            print(result['comment'])#.encode().decode('raw_unicode_escape')) # convert `\uXXXX'
            print('\n---\n')

