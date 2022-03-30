# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.30
# [python - How to export scraped data as readable json using Scrapy - Stack Overflow](https://stackoverflow.com/questions/71679403/how-to-export-scraped-data-as-readable-json-using-scrapy)

import time
import scrapy
#import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter

class SaveJsonPipeline:
    def process_item(self, item, spider):

        filename = item['filename']
        del item['filename']

        # if the file exists it will append the data 
        JsonLinesItemExporter(open(filename, "ab")).export_item(item)

        return item


DICT = {
    'quotes.toscrape.com': 'domain1.json',
    'stadt-koeln.de': 'domain2.json',
}


class PagingIncremental(CrawlSpider):
    name = "my_spider"

    allowed_domains = ['quotes.toscrape.com', 'stadt-koeln.de']

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        #'https://www.stadt-koeln.de/leben-in-koeln/planen-bauen/bebauungsplaene/aufstellen-eines-bauleitplanes'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': '0',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DEPTH_LIMIT': '1',
        'AUTOTHROTTLE_ENABLED': 'True',
        'AUTOTHROTTLE_START_DELAY': '1',
        'AUTOTHROTTLE_MAX_DELAY': '3'
    }
    # Visit all found sublinks
    rules = (
        Rule(LinkExtractor(allow=r""), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        item = {}

        # get domain from each sub page 
        domain = urlparse(response.url).netloc
        domain = domain.replace("www.", "")

        # if domain from DICT above matches with domain from subpage
        # all sublinks are stored in the same output file
        item["filename"] = DICT[domain]
        item["content"] = " ".join([x.strip() for x in response.xpath("//p/text()").getall()]).strip()
        item['scrape_date'] = int(time.time())

        yield item


if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'ITEM_PIPELINES': {'__main__.SaveJsonPipeline': 1},  # used Pipeline create in current file (needs __main___)
    })

    # process = CrawlerProcess()
    process.crawl(PagingIncremental)
    process.start()

    import pandas as pd
    df = pd.read_json('domain1.json', lines=True)
    print(df.head())
