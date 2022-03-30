# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.27
# [python - Scrapy Next Page Links - Stack Overflow](https://stackoverflow.com/questions/71637596/scrapy-next-page-links/)

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'my_spyder'
    
    start_urls = ['https://www.bernama.com/en/crime_courts/']
    
    def parse(self, response):
        print("url:", response.url)
        
        
        
        sections = response.xpath('//div[@class="row"]/div[div[@class="row"]//span[contains(text(), "More news")]]')
        #print(sections)
        
        for news in sections[0].css('h6 a'):
        #for news in response.css('h6 a'):
            yield {
                    'title': news.css('::text').get(),
                    'link' : response.urljoin(news.css('::attr(href)').get()),
                    #'link' : response.urljoin(news.attrib['href']),
                    'page' : response.url,
                  }
            
        next_page = response.css('a.page-link::attr(href)').getall()
    
        if next_page[-1] != "#":
            yield response.follow(next_page[-1])
    
from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(MySpider)
c.start() 
