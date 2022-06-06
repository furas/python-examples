# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.26
# [python - Scrapy : Crawled 0 pages (at 0 pages/min), scraped 0 items - Stack Overflow](https://stackoverflow.com/questions/72392931/scrapy-crawled-0-pages-at-0-pages-min-scraped-0-items/72394049)

import scrapy
 
class lngspider(scrapy.Spider):
    
    name = 'scrapylng'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    start_urls = ['https://directory.lubesngreases.com/LngMain/includes/themes/MuraBootstrap3/remote/api?fn=searchcompany&name&query&STATE&brand&COUNTRY&query2&mode=advanced&filters=%7B%7D&page=1&datatype=html']
 
    def parse(self, response):
    
        print('url:', response.url)

        # see HTML
        #print(response.body.decode())

        # save HTML in file to see it later in browser
        #with open('output.html', 'wb') as f:
        #    f.write(response.body)
            
        for company in response.css('div.company-item.row'):
            name = company.css('span.CompanyHead::text').get()
            
            print('name:', name)
            
            yield {
                'name': name,
            }
             
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'FEEDS': {'output.csv': {'format': 'csv'}},
})
c.crawl(lngspider)
c.start() 
