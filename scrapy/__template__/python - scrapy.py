#!/usr/bin/env python3

# date: 2019.12.07

import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
#from scrapy.commands.view import open_in_browser
#import json

class MySpider(scrapy.Spider):

    name = 'myspider'

    #allowed_domains = []

    # see page created for scraping: http://toscrape.com/
    start_urls = ['http://books.toscrape.com/'] #'http://quotes.toscrape.com']

    #def __init__(self, urls, *args, **kwargs):
    #    '''generate start_urls list'''
    #    super().__init__(*args, **kwargs)
    #    self.start_urls = urls.split(';')

    #def start_requests(self):
    #    '''generate requests instead of using start_ulrs'''
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

        #open_in_browser(response)

        # save JSON in separated file
        #number = response.url.split('/')[-1]
        #filename = 'page-{}.json'.format(number)
        #with open(filename, 'wb') as f:
        #   f.write(response.body)

        # convert JSON into Python's dictionary
        #data = json.loads(response.text)

        # download files (not only images, but without converting to JPG)
        #for url in response.css('img::attr(src)').extract():
        #    url = response.urljoin(url)
        #    yield {'file_urls': [url], 'session_path': 'hello_world'}

        # download images and convert to JPG (even if it is already JPG)
        #for url in response.css('img::attr(src)').extract():
        #    url = response.urljoin(url)
        #    yield {'image_urls': [url], 'session_path': 'hello_world'}

        # send item to other parser as `meta`
        #item = {'url': '...', 'title': '...'}
        #yield self.Request(url, meta={'item': item}, callback=self.parse_details)

    #def parse_details(self, response):
    #   item = response.meta['item']   # get item from previous parser
    #   item['more'] = 'More and more data'
    #   yield item

    #def closed(self, reason):
    #    import os
    #    import datetime
    #    import logging
    #
    #    self.log('spider closed: {}'.format(reason))
    #
    #    if os.path.exists('output.csv'):
    #        filename = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S-output.csv')
    #        if os.path.exists(filename):
    #            self.log('Problem: exists {}'.format(filename))
    #        else:
    #            os.rename('output.csv', filename)
    #            self.log('Renamed: {}'.format(filename), logging.INFO)

class SessionFilesPipeline(FilesPipeline):
    '''Pipeline to move downloaded files to folders'''

    def item_completed(self, results, item, info):
        import os

        # filter results
        
        results = [name for ok, name in results if ok]
        
        # iterate over the local file paths of all downloaded files

        for result in results:

            path = result['path']

            # create the session-path where the files should be at the end

            target_path = os.path.join(item['session_path'], os.path.basename(path))

            # try to move the file and raise exception if not possible

            try:
                #os.replace(path, target_path)
                os.rename(path, target_path)
            except Exception as ex:
                raise ImageException("Could not move FILE to target folder")

            # write out the result with the new path if there is a result field in the item (just like in the original code)

            #if self.FILES_RESULT_FIELD in item.fields:  # Scrapy item has fields
            if self.FILES_RESULT_FIELD in item.keys():   # but dictionary has keys
                result['path'] = target_path
                item[self.FILES_RESULT_FIELD].append(result)

        return item

class SessionImagesPipeline(ImagesPipeline):
    '''Pipeline to move downloaded files to folders'''

    def item_completed(self, results, item, info):
        import os

        # filter results
        
        results = [name for ok, name in results if ok]
        
        # iterate over the local file paths of all downloaded images

        for result in results:

            path = result['path']

            # create the session-path where the image should be at the end

            target_path = os.path.join(item['session_path'], os.path.basename(path))

            # try to move the file and raise exception if not possible

            try:
                #os.replace(path, target_path)
                os.rename(path, target_path)
            except Exception as ex:
                raise ImageException("Could not move IMAGE to target folder")

            # write out the result with the new path if there is a result field in the item (just like in the original code)

            #if self.IMAGES_RESULT_FIELD in item.fields:  # Scrapy item has fields
            if self.IMAGES_RESULT_FIELD in item.keys():   # but dictionary has keys
                result['path'] = target_path
                item[self.IMAGES_RESULT_FIELD].append(result)

        return item

class RenameImagePipeline(ImagesPipeline):
    '''Pipeline to change file names - to add folder name with date and time'''

    def file_path(self, request, response=None, info=None):
        '''Changing file name - adding folder name with date and time'''

        from scrapy.utils.python import to_bytes
        import hashlib
        import datetime

        # from original function file_path
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()

        # add folder name with date and time
        filename = datetime.datetime.now().strftime('images/%Y.%m.%d-%H.%M.%S/{}.jpg'.format(image_guid))

        return filename

# --- run without project and save in `output.csv` ---

# scrapy runspider script.py -s USER_AGENT="Mozilla/5.0" -o output.csv -a urls="http://quotes.toscrape.com/tag/love/;http://quotes.toscrape.com/tag/inspirational/http://quotes.toscrape.com/tag/life/"

# --- run without project and save in `output.csv` ---

#import scrapy.cmdline

#start_urls = "http://quotes.toscrape.com/tag/love/;http://quotes.toscrape.com/tag/inspirational/http://quotes.toscrape.com/tag/life/"

#scrapy.cmdline.execute(['scrapy', 'crawl', 'myspider', '-o', 'output.csv', '-a',  'urls=' + start_urls])

# --- run without project and save in `output.csv` ---

# python script.py

#start_urls = [
#    'http://quotes.toscrape.com/tag/love/',
#    'http://quotes.toscrape.com/tag/inspirational/',
#    'http://quotes.toscrape.com/tag/life/',
#]

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #

    # download files to `FILES_STORE/full` (standard folder)
    # it needs `yield {'file_urls': [url]}` in `parse()` and both ITEM_PIPELINES and FILES_STORE to work

    #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},   # used standard FilesPipeline (download to FILES_STORE/full)
    #'ITEM_PIPELINES': {'__main__.SessionFilesPipeline': 1},          # used Pipeline create in current file (needs __main___)
    #'FILES_STORE': '/path/to/valid/dir',  # this folder has to exist before downloading
    #'FILES_STORE': '.',                   # this folder has to exist before downloading

    # download images to `IMAGES_STORE/full` (standard folder) and convert to JPG (even if it is already JPG)
    # it needs `yield {'image_urls': [url]}` in `parse()` and both ITEM_PIPELINES and IMAGES_STORE to work

    #'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},  # used standard ImagePipeline (download to IMAGES_STORE/full)
    #'ITEM_PIPELINES': {'__main__.RenameImagePipeline': 1},            # used Pipeline create in current file (needs __main___)
    #'ITEM_PIPELINES': {'__main__.SessionImagesPipeline': 1},          # used Pipeline create in current file (needs __main___)
    #'IMAGES_STORE': '/path/to/valid/dir',  # this folder has to exist before downloading
    #'IMAGES_STORE': '.',                   # this folder has to exist before downloading

})
c.crawl(MySpider)
#start_urls = "http://quotes.toscrape.com/tag/love/;http://quotes.toscrape.com/tag/inspirational/http://quotes.toscrape.com/tag/life/"
#c.crawl(MySpider, urls=start_urls)  # use extra argument `url` which has to be in `__init___(..., urls)` and can be used in command line with "-a urls=url1;url2;url3"
c.start()
