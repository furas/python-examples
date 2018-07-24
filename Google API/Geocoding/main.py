
import googlemaps

API_KEY = '<YOUR-API-KEY-FOR-PLACES-API>'

gmaps = googlemaps.Client(key=API_KEY)

results = gmaps.geocode('221B Baker Street, London, United Kingdom')

for key in results[0].keys():
    print('key:', key)

print('-----')

item = results[0]
print('formatted_address:', item['formatted_address'])
print('lat:', item['geometry']['location']['lat'])
print('lng:', item['geometry']['location']['lng'])
print('location:', item['geometry']['location'])

for part in item['address_components']:
    print(part)

print('---')
print('address_components:', item['address_components'])
print('formatted_address:', item['formatted_address'])
print('geometry:', item['geometry'])
print('place_id:', item['place_id'])
print('types:', item['types'])
print('-----')
    

    
