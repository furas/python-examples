# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.29

# [web scraping - How to webscrape an interactive webpage with python - Stack Overflow](https://stackoverflow.com/questions/72423199/how-to-webscrape-an-interactive-webpage-with-python/72425518#72425518)
    
import requests

url = 'http://chonos.ifop.cl/flow/mapclick'

params = {
    'REQUEST': 'GetFeatureInfo',
    'SERVICE': 'WMS',
    'SRS': 'EPSG:4326',
    'STYLES': '',
    'TRANSPARENT': 'true',
    'VERSION': '1.1.1',
    'FORMAT': 'image.png',
    'BBOX': '-84.48486328125,-50.16282433381728,-59.54589843750001,-45.75219336063107',
    'HEIGHT': '300',
    'WIDTH': '1135',
    'LAYERS': 'aguadulce:outlet_points',
    'QUERY_LAYERS': 'aguadulce:outlet_points',
    'INFO_FORMAT': 'text.html',
    'LAT': '-46.528634695271684',
    'LON': '-71.41113281250001',
    'X': '595',
    'Y': '51',
}

response = requests.get(url, params=params)

data = response.json()

# show first 5 values
for item in data['series']['sim'][:5]:
    print(item)
print('...')    




