#!/usr/bin/env python3

# date: 2019.05.07
# author: Bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/56012860/first-scrapy-spider/56014596#56014596

import scrapy
from scrapy.http import Request
import json

class MySpider(scrapy.Spider):

    name = 'myspider'

    allowed_domains = ['soundcloud.com']

    start_urls = [
        'https://api-v2.soundcloud.com/users/7436630/tracks?offset=0&limit=20&client_id=Q11Oe0rIPEuxvMeMbdXV7qaowYzlaESv&app_version=1556892058&app_locale=en',
        'https://api-v2.soundcloud.com/users/4803918/tracks?offset=0&limit=20&client_id=Q11Oe0rIPEuxvMeMbdXV7qaowYzlaESv&app_version=1556892058&app_locale=en',
        'https://api-v2.soundcloud.com/users/17364233/tracks?offset=0&limit=20&client_id=Q11Oe0rIPEuxvMeMbdXV7qaowYzlaESv&app_version=1556892058&app_locale=en',
        'https://api-v2.soundcloud.com/users/19697240/tracks?offset=0&limit=20&client_id=Q11Oe0rIPEuxvMeMbdXV7qaowYzlaESv&app_version=1556892058&app_locale=en',
        'https://api-v2.soundcloud.com/users/5949564/tracks?offset=0&limit=20&client_id=Q11Oe0rIPEuxvMeMbdXV7qaowYzlaESv&app_version=1556892058&app_locale=en'
    ]

    def parse(self, response):

        data = json.loads(response.text)

        if len(data['collection']) > 0:
            artist_info = data['collection'][0]['user']

            artistItem = {
                'artist_id': artist_info.get('id'),
                'username': artist_info.get('username'),
                'url':  artist_info.get('permalink_url'),
            }

            print('>>>', artistItem['url'])
            # make requests to url `artistItem['url']`,
            # parse response in `parse_artist`,
            # send `artistItem` to `parse_artist`
            return Request(artistItem['url'], self.parse_artist, meta={'item': artistItem})
        else:
            print("ERROR: no collections in data")


    def parse_artist(self, response):

        artistItem = response.meta['item']

        data = response.css('script::text').extract()

        # add data to artistItem
        #print(data)
        artistItem['new data'] =  'some new data'

        #print('>>>', response.urljoin('tracks'))
        print('>>>', response.url + '/tracks')
        # make requests to url `artistItem['url']`,
        # parse response in `parse_tracks`,
        # send `artistItem` to `parse_tracks`
        return Request(response.url + '/tracks', self.parse_tracks, meta={'item': artistItem})


    def parse_tracks(self, response):
        artistItem = response.meta['item']

        artistItem['tracks'] =  'some tracks'

        # send to CSV file
        return artistItem


#------------------------------------------------------------------------------
# run it without creating project
#------------------------------------------------------------------------------

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(MySpider)
c.start()
