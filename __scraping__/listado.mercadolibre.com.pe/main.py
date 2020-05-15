#!/usr/bin/env python3

# date: 2020.04.23
# https://stackoverflow.com/questions/61376200/i-dont-get-all-the-product-description-data-with-scrapy/61377436#61377436

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from mercadolibre.items import MercadolibreItem

class MercadolibreperuSpider(CrawlSpider):
    name = 'mercadolibreperu'
    allowed_domains = ['mercadolibre.com.pe']
    start_urls = ['https://listado.mercadolibre.com.pe/lima/mascarilla-n95_ITEM*CONDITION_2230284']

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(
            LinkExtractor(
                restrict_xpaths=(
                    '//section[@id="results-section"]',        
                ),
            ),
            callback='parse_item',
            follow=True
        ),
    )

    def parse_item_old(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        for element in response.xpath('//h2[@class="item__title list-view-item-title"]/a/span/text()').getall():
            #item = {}
            item = MercadolibreItem()
            item['descripcion'] = element
            yield item

    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        
        for element in response.xpath('//li[@class="results-item highlighted article stack item-without-installmets"]'):
            item = {}
            #item = MercadolibreItem()
            item['title'] = element.xpath('.//span[@class="main-title"]//text()').get()
            item['price_symbol'] = element.xpath('.//span[@class="price__symbol"]//text()').get()
            item['price_fraction'] = element.xpath('.//span[@class="price__fraction"]//text()').get()
            yield item

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(MercadolibreperuSpider)
c.start()
