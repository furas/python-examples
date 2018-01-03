#!/usr/bin/env python3

from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):

    name = 'myspider'

    sitemap_urls = ['http://www.washingtonpost.com/news-politics-sitemap.xml']
    sitemap_rules = [('trump', 'parse_article')]

    def parse_article(self, response):
        print('parse_article url:', response.url)
      
        yield {'url': response.url}
        
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
