#!/usr/bin/env python3

#-----------------------------------------------------------
#
# Run without project
#
# $ python main.py 2018 2020
#
#-----------------------------------------------------------
#
# Run in code
#
# c.crawl(MySpider, start=2018, end=2020)
# 
# OR
#
# run(2018, 2020)
#
#-----------------------------------------------------------
#
# Run in project (if you put spider and pipeline in correct files)
#
# $ scrapy crawl myspider -a start=2018 -a end=2020
#
#-----------------------------------------------------------

import scrapy
from scrapy.pipelines.files import FilesPipeline


class MySpider(scrapy.Spider):

    name = 'myspider'

    def __init__(self, start=2020, end=2020, *args, **kwargs):  # <--- receive parameters
        """Get parameters `start` and `end`."""
        
        super().__init__(*args, **kwargs)
        self.start = int(start)  # <--- receive parameter
        self.end   = int(end)    # <--- receive parameter

    def start_requests(self):
        """Generate start requests using parameters `start` and `end`."""
        
        url_pattern = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?criteria=currentYearRevDateString&submitSearch=Find&value={}'
        
        for year in range(self.start, self.end+1):
            # generate `url` with `year`
            url = url_pattern.format(year)
            # send `year` to `parse` as parameter
            yield scrapy.Request(url, meta={'year': year})
            
    def parse(self, response):
        print('[parse] url:', response.url)
        
        # get `year`
        year = response.meta['year']
        print('[parse] year:', year)
        
        # find links to all PDF in table
        for link in response.xpath('//table[@class="picklist-dataTable"]//td/a'):
            url  = link.xpath('@href').get().strip()
            name = link.xpath('text()').get()
            #print('PDF url :', url)
            #print('PDF name:', name)
            
            # create `path` for downloaded file
            path = 'pdf/{name}/{name} - {year}.pdf'.format(name=name, year=year)

            yield {'file_urls': [url], 'path': path}

        # find link with text `Next`
        next_page = response.xpath('//div[@class="paginationBottom"]/a[contains(text(), "Next")]/@href').get()
        #print('next_page:', next_page)

        if next_page:
            next_page = response.urljoin(next_page)
            #print('next_page:', next_page)
            # send `year` to `parse`
            yield scrapy.Request(next_page, meta={'year': year})

class RenameFilesPipeline(FilesPipeline):

    # `item` needs `Scrapy 2.4+`
    def file_path(self, request, response=None, info=None, *, item=None):
        """Use `path` from `item` (created in `parse`) to rename downloaded file."""
        
        return item['path']


def run(start, end):
    from scrapy.crawler import CrawlerProcess

    c = CrawlerProcess({
        # download files to `FILES_STORE/full`
        # it needs `yield {'file_urls': [url]}` in `parse()`
        'ITEM_PIPELINES': {'__main__.RenameFilesPipeline': 1},  
        'FILES_STORE': '.',
    })
    c.crawl(MySpider, start=start, end=end)
    c.start()
    
if __name__ == '__main__':

    import sys
    
    if len(sys.argv) < 3:
        print("Need 'start' and 'end' year:\n\n  python main.py 2018 2020")
        exit(1)
        
    start = int(sys.argv[1])
    end   = int(sys.argv[2]) 
        
    run(start, end)
