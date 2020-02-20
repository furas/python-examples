#!/usr/bin/env python3

# date: 2020.02.16
# https://stackoverflow.com/questions/60249794/cant-figure-out-what-is-wrong-with-this-spider

from scrapy import Spider
from scrapy.http import Request

# Define spider settings
class WickesSpider(Spider):
    name = 'wickes'
    allowed_domains = ['wickes.co.uk']
    start_urls = ['https://www.wickes.co.uk/Products/Building-Materials/c/1000173']

    def parse(self, response):
        # this will call self.parse by default for all your categories
        for url in response.xpath('.//ul[@class="aside-nav2__list"]/li/a/@href').extract():
            yield Request(response.urljoin(url),
                         callback=self.parse_details)  

    def parse_details(self, response):
        # you can get it once - and use `strip()` to remove spaces
        category = response.xpath('//h1/text()').extract_first().strip()
        
        # you should search cards which keeps items separatelly - and don't extract it
        items = response.xpath('//div[@class="product-card__content"]') #.extract()
        print(len(items))
        
        for item in items:
            # you have to use `item.xpath` instead of `response.xpath`
            title = item.xpath('.//*[@class="product-card__title product-card__title-v2"]/text()').extract_first()
            price = item.xpath('.//*[@class="product-card__price-value "]/text()').extract_first()
            url = item.xpath('.//*[@class="product-card__title product-card__title-v2"]/@href').extract_first()

            if title and price and url:
                yield {
                    'category': category,
                    'title': title.strip(),
                    'price': price.strip(),
                    'url': url.strip()
                }
                
from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    #'USER_AGENT': 'Mozilla/5.0',
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(WickesSpider)
c.start() 
