#!/usr/bin/env python3

# date: 2019.08.06
# https://stackoverflow.com/questions/57366488/how-to-pass-the-single-link-in-a-nested-url-scrape

import scrapy

def clean(text):
    text = text.replace('\xa0', ' ')
    text = text.strip().split('\n')
    text = ' '.join(x.strip() for x in text)
    return text
    
class PaniniSpider(scrapy.Spider):

    name = "spiderP"
    start_urls = ["http://comics.panini.it/store/pub_ita_it/magazines.html"]

    def parse(self, response):
        for sel in response.xpath('//div[@id="products-list"]/div'):
            yield {
                'title': clean(sel.xpath('.//h3/a/text()').get()),
                'link':  clean(sel.xpath('.//h3/a/@href').get()),
                'price': clean(sel.xpath('.//p[@class="special-price"]//span/text()').get()),
            }     

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(PaniniSpider)
c.start()
