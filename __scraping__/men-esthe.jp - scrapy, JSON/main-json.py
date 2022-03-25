# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.17
# [web scraping - Python Playwright's async does not process all of the scraped pages - Stack Overflow](https://stackoverflow.com/questions/71500291/python-playwrights-async-does-not-process-all-of-the-scraped-pages/71507497#71507497)

# scrapy runspider main-2-more.py -o output.csv

import scrapy
from time import sleep
from scrapy.selector import Selector

class KutiSpider(scrapy.Spider):
    name = 'kuti'
    allowed_domains = ['men-esthe.jp']
    start_urls = ['https://men-esthe.jp/']


    def parse(self, response):
        print('[parse] url:', response.url)
        
        urls = response.xpath('//ul[@class="areaList"]/a/@href')[0].get()
        print('[parse] len(urls):', len(urls), type(urls))
        
        yield response.follow(url=urls, callback=self.parse_area)

        # urls = response.xpath('//ul[@class="areaList"]')
        # for url in urls:
        #     yield response.follow(url=url.xpath('.//a/@href').get(), callback=self.parse_area)


    def parse_area(self, response):
        print('[parse_area] url:', response.url)

        urls = response.xpath('//div[@class="salonName"]')
        print('[parse_area] len(urls):', len(urls), type(urls))

        for url in urls:
            url = url.xpath('.//h3/a/@href').get()
            yield response.follow(url, callback=self.parse_shop)

        # next_page = response.xpath('//div[@class="pager"]//li/a[contains(text(), "次へ")]/@href').get()
        # if next_page:
        #     yield response.follow(url=next_page, callback=self.parse_area)

    def parse_shop(self, response):
        print('[parse_shop] url:', response.url)

        urls = response.xpath('//div[@class="viewMore"]/a/@href')
        print('[parse_shop] len(urls):', len(urls), type(urls))

        for url in urls.getall():
            print('[parse_shop] url:', url)

            yield response.follow(url=url + '&more', callback=self.parse_therapist)

            yield {
                'shop_name': response.xpath('//span[@class="now"]/a/span/text()').get(),
                'shop_url': response.xpath('//dd/a/@href').get(),
                'area': response.xpath('//div[@class="basicInfo"]/dl/dt[contains(text(), "エリア")]/following-sibling::dd/text()').get(),
                'report-therapi-name': response.xpath('//div[@class="heading"]//span[@class="thName"]/a[1]/text()').get(),
                'report': response.css('div.abbr.uTxt2').get(),
                'therapist_name': "",
            }


    def parse_therapist(self, response):
        print('[parse_therapist] url:', response.url)

        data = response.json()

        for item in data:
            url = '/therapist.php?id=' + item['id']
            yield response.follow(url=url, callback=self.parse_thera_page)

    def parse_thera_page(self, response):
        print('[parse_thera_page] url:', response.url)
        
        print('now:', response.xpath('//p[@class="TopicPath"]/span[@class="now"]/a/span/text()'))
        
        yield {
            'shop_name': '',
            'shop_url': '',
            'area': '',
            'report-therapi-name': '',
            'report': '',
            'therapist_name': response.xpath('//p[@class="TopicPath"]/span[@class="now"]/a/span/text()').get(),
        }

