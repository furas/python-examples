# 
# https://stackoverflow.com/a/47912816/1832058
# 

import googlemaps

API_KEY = '<YOUR-API-KEY>'

gmaps = googlemaps.Client(key=API_KEY)

results = gmaps.places('Rugby Club, London')

for key in results['results'][0].keys():
    print('key:', key)

print('-----')

for item in results['results']:
    print('name:', item['name'])
    print('lat:', item['geometry']['location']['lat'])
    print('lng:', item['geometry']['location']['lng'])
    print('location:', item['geometry']['location'])
    
    print('---')
    print('formatted_address:', item['formatted_address'])
    print('geometry:', item['geometry'])
    print('icon:', item['icon'])
    print('id:', item['id'])
    print('name:', item['name'])
    if 'opening_hours' in item:
        print('opening_hours:', item['opening_hours'])
    print('photos:', item['photos'])
    print('place_id:', item['place_id'])
    print('plus_code:', item['plus_code'])
    print('rating:', item['rating'])
    print('reference:', item['reference'])
    print('types:', item['types'])
    print('------------')

print('-----')
    

    
