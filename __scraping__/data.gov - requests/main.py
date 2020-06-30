
#
# https://api.data.gov/
# https://regulationsgov.github.io/developers/basics/
#
# https://stackoverflow.com/a/48030949/1832058
#

import requests
import json
import time

all_titles = ['EPA-HQ-OAR-2013-0602']

api_key = 'PB36zotwgisM02kED1vWwvf7BklqCObDGVoyssVE'
api_base='https://api.data.gov/regulations/v3/'

api_url = '{}docket.json?api_key={}&docketId='.format(api_base, api_key)

try:
    for title in all_titles:
        url = api_url + title
        print('url:', url)
        
        response = requests.get(url)
        data = response.json()
        
        print('--- data ---')
        print(data)
        print('--- keys ---')
        for key in data.keys():
            print('key:', key)

except Exception as ex:
    print('error:', ex)
