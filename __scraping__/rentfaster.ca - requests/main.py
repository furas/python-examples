import urllib.request
import json

city_id = 1

def display_item(item):
    print('title:', item['title'])
    print('bedrooms:', item['bedrooms'])
    print('price:', item['price'])
    print('size:', item['sq_feet'].strip())

for page in range(10):
    url = 'https://www.rentfaster.ca/api/search.json?proximity_type=location-city&novacancy=0&cur_page={}&city_id={}'.format(page, city_id)
    
    r = urllib.request.urlopen(url)
    data = json.loads(r.read())
    
    for item in data['listings'][:3]:
        display_item(item)

    print('\nTotal:', data['total2'], '/', data['total'], '\n')
    
print('keys:', data.keys())
print('keys:', data['listings'][0].keys())
