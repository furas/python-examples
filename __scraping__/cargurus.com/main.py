
#
# https://stackoverflow.com/a/47933667/1832058
#

from bs4 import BeautifulSoup
import requests

params = {
    'zip': '03062',
    'address': 'Nashua,+NH',
    'latitude': "42.73040008544922",
    'longitude': '-71.49479675292969',
    'distance': 50000,
    'selectedEntity': 'c24578',
    'entitySelectingHelper.selectedEntity2': 'c25202',
    'minPrice': '',
    'maxPrice': '', 
    'minMileage': '',   
    'maxMileage': '',   
    'transmission': 'ANY',
    'bodyTypeGroup': '',    
    'serviceProvider': '',  
    'page': 1,
    'filterBySourcesString': '',
    'filterFeaturedBySourcesString': '',
    'displayFeaturedListings': True,
    'searchSeoPageType': '',    
    'inventorySearchWidgetType': 'AUTO',
    'allYearsForTrimName': False,
    'daysOnMarketMin': '',  
    'daysOnMarketMax': '',
    'vehicleDamageCategoriesRaw': '',
    'minCo2Emission': '',
    'maxCo2Emission': '',
    'vatOnly': False,
    'minEngineDisplacement': '',
    'maxEngineDisplacement': '',
    'minMpg': '',
    'maxMpg': '',   
    'startYear': 2015,
    'endYear': 2016,
    'isRecentSearchView': False,
}

url = 'https://www.cargurus.com/Cars/inventorylisting/ajaxFetchSubsetInventoryListing.action?sourceContext=forSaleTab_false_0'

display_keys = True

for x in range(1, 4):

    params['page'] = x

    response = requests.post(url, data=params)
   
    data = response.json()

    if display_keys:
        display_keys = False
        for key in data.keys():
            print('key:', key)
        for key in data['listings'][0].keys():
            print("data['listings'] key:", key)
        print('-----')

    print('--- offers number:', len( data['listings']), '---')
    for item in data['listings'][:10]:
        print(item['id'], data['modelName'], item['modelName'], item['trimName'])
