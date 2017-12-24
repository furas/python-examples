#!/usr/bin/env python3

import scrapy
#from scrapy.commands.view import open_in_browser
#import json

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    #allowed_domains = []
    
    start_urls = ['https://www.hltv.org/matches']

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

        days = response.css('.match-day')
        
        for day in days:
            
            date = day.css('.standard-headline::text').extract_first()
            print('date:', date)
            
            tables = day.css('table')
            
            for table in tables:
            
                time = table.css('div.time::text').extract_first()
                teams = table.css('.team::text').extract()
                event = table.css('.event-name::text').extract_first()
                placeholder = table.css('.placeholder-text-cell::text').extract_first()
            
                print('  time:', time)
                if teams:
                    print('    teams 1:', teams[0])
                    print('    teams 2:', teams[1])
                    print('    event:', event)
                else:
                    print('    placeholder:', placeholder)
                
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
    'FEED_FORMAT': 'csv',     # csv, json, xml
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

'''
url: https://www.hltv.org/matches
date: 2017-12-24
  time: 03:00
    teams 1: NSPR
    teams 2: MiTH
    event: WESG 2017 Thailand LAN
  time: 06:00
    teams 1: Signature
    teams 2: Beyond
    event: WESG 2017 Thailand LAN
  time: 09:00
    placeholder: WESG Thailand - Grand Final
  time: 10:00
    teams 1: DKISS
    teams 2: Izako Boars
    event: Winner of the Future 2017
date: 2017-12-26
  time: 14:00
    teams 1: Recca
    teams 2: Signature
    event: GOTV.GG Invitational #1
  time: 17:00
    teams 1: AGO
    teams 2: Vega Squadron
    event: LOOT.BET Cup 2
  time: 20:00
    teams 1: mousesports
    teams 2: Spirit
    event: LOOT.BET Cup 2
date: 2017-12-27
  time: 12:00
    teams 1: Singularity
    teams 2: GoodJob
    event: CSesport.com XMAS Cup
  time: 13:00
    placeholder: GOTV.GG - Semi-Final #1
  time: 15:00
    placeholder: GOTV.GG - Semi-Final #2
  time: 15:00
    teams 1: MANS NOT HOT
    teams 2: VenatoreS
    event: CSesport.com XMAS Cup
  time: 17:00
    teams 1: Heroic
    teams 2: Valiance
    event: LOOT.BET Cup 2
date: 2017-12-28
  time: 13:00
    placeholder: GOTV.GG - 3rd place decider
  time: 15:00
    placeholder: GOTV.GG - Grand Final
'''
