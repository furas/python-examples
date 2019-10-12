
# date: 2019.09.17
# 

import json
import scrapy

class MySpider(scrapy.Spider):
        name = 'spidyquotes'
        quotes_base_url = 'https://www.olx.co.id/api/relevance/search?category=198&facet_limit=100&location=1000001&location_facet_limit=20&page=%s'
        start_urls = [quotes_base_url % 1]
        download_delay = 1.5
        def parse(self, response):
            data = json.loads(response.body)
            for item in data.get('data', []):
                yield {
                    'car_id': item.get('id'),
                    'car_name' : item.get('title'),
                    'price': item.get('price.value.currency.display'),
                    'user_id': item.get('user_id')
                 #   'user_name':
                }

            metadata = data.get('metadata')
            if metadata:
                url = metadata.get('next_page_url')
                if url:
                    yield scrapy.Request(url)
                
            
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(MySpider)
c.start()                
