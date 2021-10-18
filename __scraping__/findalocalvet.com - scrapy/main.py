import scrapy


class VetSpider(scrapy.Spider):
    
    name = 'vet_project'
    start_urls = ['http://findalocalvet.com/Find-a-Veterinarian.aspx']

    def parse(self, response):
        print('[parse] url:', response.url)
        
        for link in response.css('#SideByCity .itemresult a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_city)
            
    def parse_city(self, response):
        print('[parse_city] url:', response.url)
        
        for link in response.css('.org::attr(href)').getall():
            yield response.follow(link, callback=self.parse_clinic)
            
        next_link = response.css('a.dataheader:contains("Next")::attr(href)').get()
        
        if next_link:
            next_link = response.urljoin(next_link)
            yield response.follow(next_link, callback=self.parse_city)


    def parse_clinic(self, response):
        print('[parse_clinic] url:', response.url)

        yield {
            'Name': response.css('.Results-Header h1::text').get(),
            'City': response.css('.locality::text').get(),
            'State': response.css('.region::text').get(),
            'Phone': response.css('.Phone::text').get(),
            'Link': response.url,

        }
        
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file CSV, JSON or XML
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(VetSpider)
c.start() 
