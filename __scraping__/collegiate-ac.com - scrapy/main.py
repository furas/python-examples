#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47729218/1832058
#

import scrapy

class CollegiateSpider(scrapy.Spider):

    name = 'Collegiate'

    allowed_domains = ['collegiate-ac.com']

    start_urls = ['https://collegiate-ac.com/uk-student-accommodation/']

    # Step 1 - Get the area links

    def parse(self, response):
        for url in response.xpath('//*[@id="top"]/div[1]/div/div[1]/div/ul/li/a/@href').extract():
            url = response.urljoin(url)
            #print('>>>', url)
            yield scrapy.Request(url, callback=self.parse_area_page)

    # Step 2 - Get the block links

    def parse_area_page(self, response):
        for url in response.xpath('//div[3]/div/div/div/a/@href').extract():
            url = response.urljoin(url)
            yield scrapy.Request(response.urljoin(url), callback=self.parse_unitpage)

    # Step 3 Get the room links 

    def parse_unitpage(self, response):
        for url in response.xpath('//*[@id="subnav"]/div/div[2]/ul/li[5]/a/@href').extract():
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_final)

    # Step 4 - Scrape the data

    def parse_final(self, response):
        # show some information for test
        print('>>> parse_final:', response.url)
        # send url as item so it can save it in file
        yield {'final_url': response.url}

# --- run it without project ---

import scrapy.crawler 

c = scrapy.crawler.CrawlerProcess({
    "FEED_FORMAT": 'csv',
    "FEED_URI": 'output.csv'
})
c.crawl(CollegiateSpider)
c.start()
