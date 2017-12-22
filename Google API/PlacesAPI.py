import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBiC8vKEEF-MLP9a2de0PLs-S_XrEL0kSQ')

results = gmaps.places('Rugby Club, London')

for key in item.keys():
    print('key:', key)

print('-----')

for item in results['results']:
    print('name:', item['name'])
    print('lat:', item['geometry']['location']['lat'])
    print('lng:', item['geometry']['location']['lng'])
    print('location:', item['geometry']['location'])
    print('---')
    
print('-----')
    
#for item in results['results'][:1]:
#    for key, value in item.items():
#        print(key, ':', value)

    
