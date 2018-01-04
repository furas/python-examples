#!/usr/bin/env python3

import scrapy
from scrapy.pipelines.files import FilesPipeline
import os
import hashlib

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    #allowed_domains = ['https://www.olx.pl/']
    

    #def start_requests(self):
    #    for tag in self.tags:
    #        for page in range(self.pages):
    #            url = self.url_template.format(tag, page)
    #            yield scrapy.Request(url)

    def __init__(self, urls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = urls
        
    def parse(self, response):
        print('>>> url:', response.url)
        
        item = {}  

        item['url'] = response.url

        item['folder'] = response.url[26:-5]
        
        #item['tytul'] = response.css('.offer-titlebox h1::text').extract_first().strip()
        #item['miejsce'] = response.css('.offer-titlebox__details strong::text').extract_first()
        #item['dodano'] = response.css('.offer-titlebox__details em::text').extract_first().strip()[6:].strip()
        #item['cena'] = response.css('.price-label > strong::text').extract_first()
        #item['telefon'] = response.xpath('//*[@class="spoilerHidden"]//@data-phone').extract_first()
        
        #item['uzytkownik'] = response.xpath('//*[@class="offer-user__details"]/h4/a/text()').extract_first().strip()
        #item['uzytkownik_url'] = response.xpath('//*[@class="offer-user__details"]/h4/a/@href').extract_first()
        #item['tresc'] = '\n'.join(x.strip() for x in response.css('#textContent *::text').extract())
        #item['oferta od'] = response.css('.item .value  strong *::text')[1].extract().strip()
        #item['powierzchnia'] = response.css('.item .value  strong *::text')[3].extract().strip()
        
        images = []
        for x in response.css('img.bigImage ::attr(src)').extract():
            images.append(response.urljoin(x))
        item['file_urls']= images
        #print('>>> item["file_urls"]:', item['file_urls'])
        
        yield item
 
    def closed(self, reason):
        import os
        import datetime
        import logging

        self.log('spider closed: {}'.format(reason))
        
        if os.path.exists('output.csv'):
            filename = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M-output.csv')
            if os.path.exists(filename):
                self.log('Problem: file already exists {}'.format(filename))
            else:
                os.rename('output.csv', filename)
                self.log('Renamed: {}'.format(filename), logging.INFO)

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
                
class StoreImagesPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        print('>>> get_media_requests: url:', item['url'])
        print('>>> get_media_requests: name:', item['folder'])
        
        return [scrapy.Request(x, meta={'folder': item['folder']}) for x in item.get(self.files_urls_field, [])]
        
    def file_path(self, request, response=None, info=None):
        import hashlib
        from scrapy.utils.python import to_bytes
        import datetime
        
        folder = request.meta['folder']
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()

        #YEAR = 2018
        #filename = 'realty-sc/%s/%s/%s/%s.jpg' % (YEAR, image_guid[:2], image_guid[2:4], image_guid)
        
        filename = datetime.datetime.now().strftime('images/%Y.%m.%d-%H.%M/{}/{}.jpg'.format(folder, image_guid))
        
        return filename
                     
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

start_urls = [
    'https://www.olx.pl/oferta/nieruchomosc-na-sprzedaz-3-hale-i-dzialka-5500m2-atrakcyjna-cena-CID3-IDpjLu7.html#a959674638',
    'https://www.olx.pl/oferta/hala-magazyn-wiata-od-producenta-pod-wymiar-CID3-IDmqV3g.html#f550158a66',
    'https://www.olx.pl/oferta/nieruchomosc-z-budynkiem-biurowo-magazynowym-CID3-IDhsWkw.html#f550158a66',
]

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    
    # save in CSV
    'FEED_FORMAT': 'csv',     # 'json
    'FEED_URI': 'output.csv', # 'output.json

    # download files to `FILES_STORE/full`
    #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    #'ITEM_PIPELINES': {'__main__.SessionImagesPipeline': 1},
    'ITEM_PIPELINES': {'__main__.StoreImagesPipeline': 1},
    'FILES_STORE': '.',
})
c.crawl(MySpider, urls=start_urls)
c.start()
