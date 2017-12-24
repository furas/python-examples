
#
# https://stackoverflow.com/a/47679861/1832058
#

class BlueBet(scrapy.Spider):
    name = "BlueBet"
    start_urls = ['https://www.bluebet.com.au/api/sports/SportsMasterCategory?withLevelledMarkets=true&id=100']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'odds.csv',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        data = json.loads(response.body)

        for master_category in data['MasterCategories']:
            for category in master_category['Categories']:
                for event in category['MasterEvents']:
                    item = {}
                    item['Event_name'] = event.get('MasterEventName')
                    item['Outcomes'] = {}
                    try:
                        for market in event['Markets']:
                            item['Outcomes'][market.get('OutcomeName')] = market.get('Price')
                    except TypeError:
                        continue
                    yield item


data = {'Event_name': 'Melbourne Victory v Adelaide United', 
  'Outcomes': {'Melbourne Victory': 2.05, 'Draw': 3.5, 'Adelaide United': 3.4}}

# ---

item = {'Event_name': data['Event_name']}

for number, (key, val) in enumerate(data['Outcomes'].items(), 1):
    number = str(number)
    print(number, key, val)
    item["key"+number] = key
    item["val"+number] = val

print(item)
