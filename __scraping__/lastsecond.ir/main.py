#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47956427/1832058
# 

import scrapy
#from scrapy.commands.view import open_in_browser
import json

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    #allowed_domains = []
    
    start_urls = ['https://lastsecond.ir/hotels']

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

        html = response.body_as_unicode()
        
        start = html.find("var csrftoken = '")
        start = start + len(b"var csrftoken = '")
        end = html.find("';" , start)
        
        self.csrftoken = html[start:end]
        
        print('csrftoken:', self.csrftoken)
        
        yield self.get_page('1')

    def get_page(self, page):
        ''' 
        subfunction can't use `yield, it has to `return` Request to `parser`
        and `parser` can use `yield`
        '''
        
        print('yield page:', page)

        url = 'https://lastsecond.ir/hotels/ajax'

        headers = {
            'X-CSRF-TOKEN': self.csrftoken,
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'filter_score': '',
            'sort': 'reviewed_at',
            'duration': '0',
            'page': page,
            'base_location_id': '1',
        }

        return scrapy.FormRequest(url, 
            callback=self.parse_details, 
            formdata=params, 
            headers=headers, 
            dont_filter=True, 
        )
        
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
        
    def parse_details(self, response):
        print('url:', response.url)
        
        data = json.loads(response.body_as_unicode())

        current = data['pagination']['current']
        last = data['pagination']['last']

        print('page:', current, '/', last)

        print('keys:', data.keys())
        print('keys[hotels]:', data['hotels'][0].keys())
        print('pagination:', data['pagination'])
        
        for hotel in data['hotels']:
            print('title_en:', hotel['title_en'])
            yield hotel
            
        if current != last:
            yield self.get_page( str(int(current) + 1) )
            
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


# ----

'''
page: 1

keys: dict_keys(['hotels', 'pagination', 'grades', 'locations', 'scores'])
keys[hotels]: dict_keys(['id', 'title_fa', 'title_en', 'link', 'logo_link', 'decorated_grade', 'location', 'rank', 'is_recommended_percent', 'decorated_score', 'reviews_count'])

title_en: Heliya Kish hotel
title_en: Amara Prestige Elite
title_en: All Seasons Hotel
title_en: Hotel Grand Unal
title_en: Marmaray hotel
title_en: Nova Plaza Taksim Square
title_en: Flora Grand Hotel
title_en: Boulevard Autograph Collection hotel
title_en: Alfa Istanbul hotel
title_en: Ramada Hotel & Suites Istanbul Merter
title_en: Sabena hotel
title_en: Taksim Gonen
title_en: Fame Residence Lara & SPA
title_en: Palazzo Donizetti Hotel
title_en: Twin Towers hotel
title_en: Grand Hotel de Pera hotel
title_en: Grand Hotel Halic
title_en: Grand Pamir hotel
title_en: St George hotel
title_en: The Royal Paradise hotel

page: 2

keys: dict_keys(['hotels', 'pagination', 'grades', 'locations', 'scores'])
keys[hotels]: dict_keys(['id', 'title_fa', 'title_en', 'link', 'logo_link', 'decorated_grade', 'location', 'rank', 'is_recommended_percent', 'decorated_score', 'reviews_count'])

title_en: Radisson Royal moscow hotel
title_en: Avenue hotel
title_en: jamshid esfahan hotel
title_en: Aquatek hotel
title_en: Adalya Elite Lara
title_en: Federal Kuala Lumpur hotel
title_en: Feronya Hotel
title_en: Dolabauri Tbilisi hotel
title_en: Limak Limra hotel
title_en: Urban Boutique Hotel
title_en: Doubletree Hilton Piyalepasa hotel
title_en: Ferman Hilal hotel
title_en: Grand Oztanik Hotel
title_en: Lara Family Club hotel
title_en: Swissotel The Bosphorus
title_en: Berjaya Times Square hotel
title_en: Gardenia hotel
title_en: Rixos Sungate
title_en: Jumeirah Emirates Towers hotel
title_en: Kervansaray Lara Hotel
'''
