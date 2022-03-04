# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.03
# [python - Using scrapy crawler to extract Json Data? - Stack Overflow](https://stackoverflow.com/questions/71316380/using-scrapy-crawler-to-extract-json-data/71331322#71331322)

import scrapy
import json
from scrapy.spiders import Spider

class PwspiderSpider(Spider):

    name = 'pwspider'
    
    allowed_domains = ['midwayusa.com']
    
    start_urls = ['https://www.midwayusa.com/s?searchTerm=backpack']
    
    
    def parse(self, response):
        print('url:', response.url)
        
        script = response.xpath('//script[contains(text(), "window.icvData")]/text()').get()
        #print(script)
        
        text = script.split("window.icvData = ")[-1].split('\n')[0].strip()

        try:
            data = json.loads(text)
        except Exception as ex:
            print('Exception:', ex)
            print(text)
            return
        
        #print(data["searchResult"].keys())
        
        products = data["searchResult"]['products']
        
        for item in products:
            #print(item)
            colors = [color['name'] for color in item['swatches']]
            print(item['description'], colors)
            yield response.follow(item['link'], callback=self.parse_product, cb_kwargs={'colors': colors})
        
    def parse_product(self, response, colors):
        print('url:', response.url)
        
        script = response.xpath('//script[contains(text(), "window.icvData")]/text()').get()
        #print(script)
        
        # I uses `.split('\n')[0]` because sometimes it may have second line with `window.icvData.firstSaleItemId = ...` 
        text = script.split("window.icvData = ")[-1].split('\n')[0].strip()
        
        try:
            data = json.loads(text)
            data['colors'] = colors
        except Exception as ex:
            print('Exception:', ex)
            print(text)
            return

        yield data

# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/5.0',
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    # save in file CSV, JSON or XML
    'FEEDS': {'output.json': {'format': 'json'}},  # new in 2.1
})
c.crawl(PwspiderSpider)
c.start() 
