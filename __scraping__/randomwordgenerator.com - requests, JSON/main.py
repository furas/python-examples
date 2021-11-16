
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.07
#
# title: Extracting a specific line on a website using python requests
# url: https://stackoverflow.com/questions/69875305/extracting-a-specific-line-on-a-website-using-python-requests/69875925#69875925

# [Extracting a specific line on a website using python requests](https://stackoverflow.com/questions/69875305/extracting-a-specific-line-on-a-website-using-python-requests/69875925#69875925)

import requests

response = requests.get('https://randomwordgenerator.com/json/sentences.json')

data = response.json()

print('len:', len(data["data"]))  # 724

for item in data["data"]:
    print(item['sentence'])
   print('---')
