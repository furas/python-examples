#!/usr/bin/env python3

# date: 2020.02.24
# https://stackoverflow.com/questions/60383237/itemloader-in-scrapy/

import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider
import logging
from scrapy.utils.log import configure_logging

class MediumItem(scrapy.Item):
    Title = scrapy.Field()
    Name = scrapy.Field()
    Date = scrapy.Field()
    Read = scrapy.Field()
    Publication = scrapy.Field()
    Claps = scrapy.Field()
    Responses = scrapy.Field()
    Page = scrapy.Field()

class DataSpider(CrawlSpider):
    custom_settings = {
         'LOG_FILE': 'my_log.log',
         'LOG_LEVEL': 'ERROR'}
    logging.getLogger().addHandler(logging.StreamHandler())
    name = 'data'
    allowed_domains = ['medium.com', 'towardsdatascience.com']
    start_urls = ['https://medium.com/tag/python/archive/02/01']
    #handle_httpstatus_list = [302]

    def parse(self,response):
        print('url:', response.url)
        articles = response.xpath('//div[@class="postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls"]')
        for article in articles:

            if article.xpath('.//a[@class="button button--smaller button--chromeless u-baseColor--buttonNormal"]/@href').extract_first():
                l = ItemLoader(item = MediumItem(), selector = article)
                l.default_output_processor = scrapy.loader.processors.TakeFirst()
                l.add_css('Title','div > h3::text')
                l.add_xpath('Name','.//a[@class="ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken"]/text()')
                l.add_css('Read','span::attr(title)')
                l.add_xpath('Publication', './/a[@class="ds-link ds-link--styleSubtle link--darkenlink--accent u-accentColor--textNormal"]/text()')
                l.add_xpath('Claps','.//button[@class="button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton u-disablePointerEvents"]/text()')
                l.add_xpath('Responses','.//a[@class="button button--chromeless u-baseColor--buttonNormal"]/text()')
                l.add_value('Page', response.url)
                yield l.load_item()
                
from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(DataSpider)
c.start()
