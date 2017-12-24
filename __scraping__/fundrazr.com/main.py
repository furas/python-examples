
#
# https://stackoverflow.com/a/47495628/1832058
#

import scrapy
import pyquery

class MySpider(scrapy.Spider):

    name = 'myspider'

    start_urls = ['https://fundrazr.com/find?category=Health']

    def parse(self, response):
        print('--- css 1 ---')
        for title in response.css('h2'):
            print('>>>', title)

        print('--- css 2 ---')
        for title in response.css('h2'):
            print('>>>', title.extract()) # without _first())
            print('>>>', title.css('a').extract_first())
            print('>>>', title.css('a ::text').extract_first())
            print('-----')

        print('--- css 3 ---')
        for title in response.css('h2 a ::text'):
            print('>>>', title.extract()) # without _first())

        print('--- pyquery 1 ---')
        p = pyquery.PyQuery(response.body)
        for title in p('h2'):
            print('>>>', title, title.text, '<<<') # `title.text` gives "\n"

        print('--- pyquery 2 ---')
        p = pyquery.PyQuery(response.body)
        for title in p('h2').text():
            print('>>>', title)
        print(p('h2').text())

        print('--- pyquery 3 ---')
        p = pyquery.PyQuery(response.body)
        for title in p('h2 a'):
            print('>>>', title, title.text)

# ---------------------------------------------------------------------

from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start()
