#!/usr/bin/env python3

# date: 2019.08.06
# https://stackoverflow.com/questions/57366488/how-to-pass-the-single-link-in-a-nested-url-scrape

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

def clean(text):
    text = text.replace('\xa0', ' ')
    text = text.strip().split('\n')
    text = ' '.join(x.strip() for x in text)
    return text

class ComicscraperItem(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(clean))
    link = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(clean))
    
class PaniniSpider(scrapy.Spider):

    name = "spiderP"
    start_urls = ["http://comics.panini.it/store/pub_ita_it/magazines.html"]

    def parse(self, response):
        for sel in response.xpath("//div[@class='list-group']//h3/a"):
            l = ItemLoader(item=ComicscraperItem(), selector=sel)
            l.add_xpath('title', './text()')
            l.add_xpath('link', './@href')

            request = scrapy.Request(sel.xpath('./@href').extract_first(), callback=self.parse_isbn, dont_filter=True)
            request.meta['l'] = l
            yield request

    def parse_isbn(self, response):
        l = response.meta['l']
        l.add_value('price', response.xpath("//p[@class='special-price']//span/text()").get())
        return l.load_item()   

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(PaniniSpider)
c.start()
