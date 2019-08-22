#!/usr/bin/env python3

# date: 2019.08.14
# https://stackoverflow.com/questions/57490072/how-to-crawl-a-website-to-get-all-the-links-in-a-website-using-scrapy-in-python/57490431#57490072

import scrapy

class MySpider(scrapy.Spider):
    
    name = "MySpider"

    def __init__(self, allowed_domains=None, start_urls=None):
        super().__init__()

        # self.name = name
        if allowed_domains is None:
            self.allowed_domains = []
        else:
            self.allowed_domains = allowed_domains

        if start_urls is None:
            self.start_urls = []
        else:
            self.start_urls = start_urls  

    def parse(self, response):
        print('[parse] url:', response.url)

        # extract all links from page
        all_links = response.xpath('*//a/@href').extract()
        
        # iterate over links
        for link in all_links:
            print('[+] link:', link)
            #yield scrapy.http.Request(url="http://www.myntra.com" + link, callback=self.print_this_link)
            full_link = response.urljoin(link)
            yield scrapy.http.Request(url=full_link, callback=self.print_this_link)
            
            
    def print_this_link(self, response):
        print('[print_this_link] url:', response.url)
        title = response.xpath('//title/text()').get() # get() will replace extract() in the future
        body = response.xpath('//body//text()').getall()
        yield {'url': response.url, 'title': title, 'body': body}
            
        
# --- run without creating project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(MySpider)
c.crawl(MySpider, allowed_domains=["myntra.com"], start_urls=["http://www.myntra.com/"])
c.start()

