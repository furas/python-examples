# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.24
# [python - Scrapy crawler not yielding any Data - Stack Overflow](https://stackoverflow.com/questions/71593213/scrapy-crawler-not-yielding-any-data/)

import scrapy
import json

class ZillowScraper(scrapy.Spider):

    name = "zillow"

    # custom_settings = {
    #     "FEED_FORMAT": "csv",
    #     "FEED_URI": "zillow_data.csv",
    # }

    # base URL
    base_url = "https://www.zillow.com/homes/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-118.34704399108887%2C%22east%22%3A-118.24130058288574%2C%22south%22%3A34.05770827438846%2C%22north%22%3A34.12736593680466%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"

    # custom headers
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
    }

    # string query parameters
    params = {
        "searchQueryState": '{"pagination":{"currentPage":2},"usersSearchTerm":"Los Angeles, CA","mapBounds":{"west":-119.257679765625,"east":-117.565785234375,"south":33.46151132910718,"north":34.57696456062683},"mapZoom":9,"regionSelection":[{"regionId":12447,"regionType":6}],"isMapVisible":false,"filterState":{"ah":{"value":true},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}',
    }

    def start_requests(self):
        yield scrapy.Request(
            url=self.base_url, headers=self.headers, callback=self.parse_links
        )

    def parse_links(self, response):
        print('[parse_links] url:', response.url)
        
        results_selector = response.css(
            'script[data-zrr-shared-data-key="mobileSearchPageStore"]'
        ).get()
        
        clean_json = (
            results_selector.replace(
                '<script type="application/json" data-zrr-shared-data-key="mobileSearchPageStore"><!--',
                "",
            )
            .replace("</script>", "")
            .replace("-->", "")
        )
        
        parsed_data = json.loads(clean_json)
        data = parsed_data["cat1"]["searchResults"]["listResults"]

        for listing in data:
            yield scrapy.Request(
                url=listing["detailUrl"],
                headers=self.headers,
                callback=self.parse_detail,
                meta={'data': listing}
            )

    def parse_detail(self, response):
        print('[parse_detail] url:', response.url)

        listing_url = response.url.split("/")
        parse_id = [u for u in listing_url if u]
        
        listing_id = parse_id[4][:8]
        zid = response.meta['data']        

        #print('listing_id:', listing_id)
        #print("zid['id']:", zid['id'])
        
        if zid['id'] == listing_id:

            api_endpoint = response.css('script[id="hdpApolloPreloadedData"]').get()
            
            clean_json = api_endpoint.replace(
                '<script id="hdpApolloPreloadedData" type="application/json">', ""
            ).replace("</script>", "")
            
            parsed_data = json.loads(clean_json)
            sub_data = json.loads(parsed_data["apiCache"])
            
            id_ = zid['id']
            
            key_1 = f'ForSaleDoubleScrollFullRenderQuery{{"zpid":{id_},"contactFormRenderParameter":{{"zpid":{id_},"platform":"desktop","isDoubleScroll":true}}}}' 
            key_2 = f'VariantQuery{{"zpid":{id_},"altId":null}}'

            properties_1 = sub_data[key_1]["property"]
            properties_2 = sub_data[key_2]["property"]

            item = {}
            
            item["date"]        = properties_1["datePostedString"]
            item["home_status"] = properties_1["hdpTypeDimension"]
            item["home_type"]   = properties_1["homeType"]
            item["sqft"]        = properties_1["livingArea"]
            
            item["street_address"] = properties_2["streetAddress"]
            item["city"]           = properties_2["city"]
            item["state"]          = properties_2["state"]
            item["zipcode"]        = properties_2["zipcode"]
            item["price"]          = properties_2["price"]
            
            item["zestimate"]     = properties_1["zestimate"]
            item["parcel_number"] = properties_1["resoFacts"]["parcelNumber"]

            yield item
        
from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(ZillowScraper)
c.start() 
