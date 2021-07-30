
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.07.15
#
# title: Trouble outputting data with Scrapy
# url: https://stackoverflow.com/questions/68386890/trouble-outputting-data-with-scrapy/68387811#68387811


import scrapy
from scrapy.http import Request

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['artofmanliness.com']
    max_pages = 2

    def start_requests(self):
        for i in range(self.max_pages):
            yield scrapy.Request('http://artofmanliness.com/articles/page/%d/' % i, callback=self.parse)

    def parse(self, response):
        # AOM has a list of all articles in pages of about 189
        for article in response.xpath('//article[contains(@class, "aom-article-simple")]'):
            url = article.xpath('.//a/@href').extract()
            print('article url:', url)

            if url:
                yield Request(url=url[0], callback=self.parse_article)

    def parse_article(self, response):
        #title = response.xpath('//h1[@class="post-title entry-title"]/text()').extract()
        title = response.xpath('//h1[@itemprop="headline"]/text()').extract()
        
        category = response.xpath('//p[@class="in-category"]//a/text()').extract()

        #date = response.xpath('//p[@class="single-date"]//span[2]/text()').extract()
        date = response.xpath('//span[@itemprop="datePublished"]/text()').extract()

        yield {
            'Title': title,
            'Category': category,
            'Date': date,
            'URL': response.url           
        }
        
from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    # save in file CSV, JSON or XML
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(ArticlesSpider)
c.start() 
