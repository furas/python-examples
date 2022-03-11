# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.10
# [python - Web Scraping Data from Online Interactive Map - Stack Overflow](https://stackoverflow.com/questions/71430166/web-scraping-data-from-online-interactive-map/71430802#71430802)
                                                                          
import requests

url = 'https://geokey.communitymaps.org.uk/api/communitymaps/projects/399/contributions/'

response = requests.get(url)

data = response.json()

for item in data['features'][:10]:
    val = item['display_field']['value']
    key = item['display_field']['key']
    print(f'{key:20} | {val:20}')
