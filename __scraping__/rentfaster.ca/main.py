
#
# https://stackoverflow.com/a/47494448/1832058
#

import urllib.request
import json

city_id = 1

url = 'https://www.rentfaster.ca/api/search.json?proximity_type=location-city&novacancy=0&city_id=' + str(city_id)

r = urllib.request.urlopen(url)
data = json.loads(r.read())

for item in data['listings']:
    print('title:',    item['title'])
    print('bedrooms:', item['bedrooms'])
    print('price:',    item['price'])
    print('size:',     item['sq_feet'])
