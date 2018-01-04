#!/usr/bin/env python3

import scrapy
#from scrapy.commands.view import open_in_browser
#import json

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    #allowed_domains = []
    
    start_urls = ['http://quotes.toscrape.com']

    #def __init__(self, urls, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.start_urls = urls.split(';')

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

#~ class SessionImagesPipeline(FilesPipeline):
    
    #~ def item_completed(self, results, item, info):
        #~ # iterate over the local file paths of all downloaded images
        #~ for result in [x for ok, x in results if ok]:
            #~ path = result['path']
            #~ # here we create the session-path where the files should be in the end
            #~ # you'll have to change this path creation depending on your needs
            #~ target_path = os.path.join((item['session_path'], os.basename(path)))

            #~ # try to move the file and raise exception if not possible
            #~ if not os.rename(path, target_path):
                #~ raise ImageException("Could not move image to target folder")

            #~ # here we'll write out the result with the new path,
            #~ # if there is a result field on the item (just like the original code does)
            #~ if self.IMAGES_RESULT_FIELD in item.fields:
                #~ result['path'] = target_path
                #~ item[self.IMAGES_RESULT_FIELD].append(result)

        #~ return item

#class StoreImagePipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        from scrapy.utils.python import to_bytes
        import hashlib
        import datetime
        
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        filename = datetime.datetime.now().strftime('images/%Y.%m.%d-%H.%M.%S/{}.jpg'.format(image_guid))
        
        return filename
        
# --- run without project and save in `output.csv` ---

# scrapy runspider script.py -s USER_AGENT="Mozilla/5.0" -o output.csv -a urls="http://quotes.toscrape.com/tag/love/;http://quotes.toscrape.com/tag/inspirational/http://quotes.toscrape.com/tag/life/"

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

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 

    # download files to `FILES_STORE/full`
    # it needs `yield {'file_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    #'ITEM_PIPELINES': {'__main__.SessionImagesPipeline': 1},
    #'FILES_STORE': '/path/to/valid/dir',
    #'FILES_STORE': '.',

    # download images and convert to JPG
    # it needs `yield {'image_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    #'ITEM_PIPELINES': {'__main__.StoreImagePipeline': 1},
    #'IMAGES_STORE': '/path/to/valid/dir',
    #'IMAGES_STORE': '.',
    
})
c.crawl(MySpider)
#start_urls = "http://quotes.toscrape.com/tag/love/;http://quotes.toscrape.com/tag/inspirational/http://quotes.toscrape.com/tag/life/"
#c.crawl(MySpider, urls=start_urls)
c.start()
