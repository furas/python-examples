#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47948138/1832058
#

import scrapy
#from scrapy.commands.view import open_in_browser
#import json

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    allowed_domains = ['www.ofri.ch/firmen']
    start_urls = ['http://www.ofri.ch/firmen/Abbruchunternehmen/']

    #def start_requests(self):
    #    self.url_template = http://quotes.toscrape.com/tag/{}/page/{}/
    #    self.tags = ['love', 'inspirational', 'life', 'humor', 'books']
    #    self.pages = 10
    # 
    #    for tag in self.tags:
    #        for page in range(self.pages):
    #            url = self.url_template.format(tag, page)
    #            yield scrapy.Request(url)

    def parse(self, response):
        print('url:', response.url)

        entries_description = response.xpath('//div[@class="directory-entry"]//div[@class="directory-entry-description"]')
        
        for entry_description in entries_description:
            company_name = entry_description.xpath('.//h2/a/text()').extract_first()
            address_street = entry_description.xpath('.//p[@itemprop="address"]/span[@itemprop="streetAddress"]/text()').extract_first()
            zip_locality = entry_description.xpath('.//p[@itemprop="address"]/span[@itemprop="addressLocality"]/text()').extract_first()
            contact_data = entry_description.xpath('.//*[@id="business_directory_contact_data"]/div/ul').extract_first()
            tel = entry_description.xpath('.//span[@itemprop="telephone"]//text()').extract_first()
            company_url = entry_description.xpath('.//a[@itemprop="url"]/@href').extract_first()
            
            item = {
                'name': company_name,
                'street': address_street,
                'zip_locality': zip_locality,
                'tel': tel,
                'url':company_url
            }    

            print(item)
            
            yield item
            
        #open_in_browser(response)
        
        # save JSON in separated file
        #number = response.url.split('/')[-1]
        #filename = 'page-{}.json'.format(number)
        #with open(filename, 'wb') as f:
        #   f.write(response.body)

        # convert JSON into Python's dictionary
        #data = json.loads(response.text)

        # download files
        #for href in response.css('img::attr(href)').extract():
        #   url = response.urljoin(src)
        #   yield {'file_urls': [url]}

        # download images and convert to JPG
        #for src in response.css('img::attr(src)').extract():
        #   url = response.urljoin(src)
        #   yield {'image_urls': [url]}

        #item = {'url': '...', 'title': '...'}
        #yield self.Request(url, meta={'item': item}, callback=self.parse_details)
        
    #def parse_details(self, response):
    #   item = response.meta['item']
    #   item['more'] = 'More and more data'
    #   yield item  
    
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'json',     # csv, json, xml
    'FEED_URI': 'output.csv', # 

    # download files to `FILES_STORE/full`
    # it needs `yield {'file_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    #'FILES_STORE': '/path/to/valid/dir',

    # download images and convert to JPG
    # it needs `yield {'image_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    #'IMAGES_STORE': '/path/to/valid/dir',
})
c.crawl(MySpider)
c.start()
