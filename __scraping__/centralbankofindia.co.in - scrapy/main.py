
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.10.04
#
# title: Scrapy returning None on querying by xpath
# url: https://stackoverflow.com/questions/69442962/scrapy-returning-none-on-querying-by-xpath/69443343#69443343

# [Scrapy returning None on querying by xpath](https://stackoverflow.com/questions/69442962/scrapy-returning-none-on-querying-by-xpath/69443343#69443343)


import scrapy

class MySpider(scrapy.Spider):
    
    start_urls = [
        # f"https://www.centralbankofindia.co.in/en/branch-locator?field_state_target_id=All&combine=&page={i}"
        # for i in range(0, 5)
        
        # only first page - links to other pages it will find in HTML
        "https://www.centralbankofindia.co.in/en/branch-locator?field_state_target_id=All&combine=&page=0"
    ]
    
    name = "Central Bank of India"
    
    def parse(self, response):
        print(f'url: {response.url}')
        
        all_items = response.xpath('//*[@id="block-cbi-content"]//td[2]//span[2]/text()').extract()
        
        for address in all_items:
            print(address)
            yield {'address': address}

        # get link to next page
        
        next_page = response.xpath('//a[@rel="next"]/@href').extract_first()
        
        if next_page:
            print(f'Next Page: {next_page}')
            yield response.follow(next_page)
            
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(MySpider)
c.start()

