
# author: https://blog.furas.pl
# date: 2020.07.16
# link: 

import scrapy
import json

class MainSpider(scrapy.Spider):
    
    name = 'main'
    # allowed_domains = ['longandfoster.com']
    
    start_urls = ['https://www.longandfoster.com/include/ajax/api.aspx?op=SearchAgents&firstname=&lastname=&page=1&pagesize=200']

    def parse(self, response):
        resp = json.loads(json.loads(response.body)['Entity'])
        for each in resp:
            name = each.get('DisplayName')

            yield {
                "Name": name,
            }

# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(MainSpider)
c.start() 
