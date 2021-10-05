
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.08.04
#
# title: Scrape data from div as shown on the page
# url: https://stackoverflow.com/questions/68657663/scrape-data-from-div-as-shown-on-the-page/68658718#68658718

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'

    start_urls = ['https://eksisozluk.com/mortingen-sitraze--1277239']

    def parse(self, response):
        print('url:', response.url)

        data = {}
        
        title = response.css('[itemprop="name"]::text').get()
        data["title"] = title
        
        for count, content in enumerate(response.css('li .content')):
            text = content.css('::text').getall()
            text = "".join(text).strip()
            print(count, '|', text)
            data[f"content {count}"] = text

        yield data
    
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(MySpider)
c.start()

