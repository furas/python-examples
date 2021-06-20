
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.06.13
#
# title: Scrapy Beginner: Not able to get data in text Form From css selector, got empty array
# url: https://stackoverflow.com/questions/67954326/scrapy-beginner-not-able-to-get-data-in-text-form-from-css-selector-got-empty/

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'

    start_urls = ['https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1']

    def parse(self, response):
        print('url:', response.url)

        all_rows = response.css('table.items tr.odd, table.items tr.even')
        print('len(all_rows):', len(all_rows))
        
        for row in all_rows:
            info = row.css('td.hauptlink a::text').extract()
            print('info:', info)
            position = row.css('table.inline-table td::text').extract()
            print('position:', position[4])
            
            yield {
                'name': info[0],
                'left': info[1],
                'joined': info[2],
                'value':info[3],
                'position': position[4]
            }
            
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
#    'USER_AGENT': 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    # save in file CSV, JSON or XML
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(MySpider)
c.start() 
