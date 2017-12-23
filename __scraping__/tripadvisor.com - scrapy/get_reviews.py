#!/usr/bin/env python3

# 
# https://stackoverflow.com/a/47721321/1832058
# 

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'
    allowed_domains = ['tripadvisor.com']

    start_urls = [
        'https://www.tripadvisor.com/Hotel_Review-g60795-d102542-Reviews-Courtyard_Philadelphia_Airport-Philadelphia_Pennsylvania.html',
        'https://www.tripadvisor.com/Hotel_Review-g60795-d122332-Reviews-The_Ritz_Carlton_Philadelphia-Philadelphia_Pennsylvania.html',
    ]

    def parse(self, response):
        # get number of reviews
        num_reviews = response.css('span.reviews_header_count::text').extract_first()
        num_reviews = num_reviews[1:-1] # remove `( )`
        num_reviews = num_reviews.replace(',', '') # remove `,`
        num_reviews = int(num_reviews)
        print('num_reviews:', num_reviews, type(num_reviews))
        
        # create template for urls to pages with reviews
        url = response.url.replace('.html', '-or{}.html')
        print('template:', url)
        
        # add requests to list
        for offset in range(0, num_reviews, 5):
            print('url:', url.format(offset))
            yield scrapy.Request(url=url.format(offset), callback=self.parse_reviews)

    def parse_reviews(self, response):
        print('review:', response.url)
        for idx,review in enumerate(response.css('div.review-container')):
            item = {
                'num_reviews': response.css('span.reviews_header_count::text')[0].re(r'\d{0,3}\,?\d{1,3}'),
                'hotel_name': response.css('h1.heading_title::text').extract_first(),
                'review_title': review.css('span.noQuotes::text').extract_first(),
                'review_body': review.css('p.partial_entry::text').extract_first(),
                'review_date': review.xpath('//*[@class="ratingDate relativeDate"]/@title')[idx].extract(),
                'num_reviews_reviewer': review.css('span.badgetext::text').extract_first(),
                'reviewer_name': review.css('span.scrname::text').extract(),
                'bubble_rating': review.xpath("//div[contains(@class, 'reviewItemInline')]//span[contains(@class, 'ui_bubble_rating')]/@class")[idx].re(r'(?<=ui_bubble_rating bubble_).+?(?=0)')
            }
            yield item
        
        
# --- run without project ---

import scrapy.crawler

c = scrapy.crawler.CrawlerProcess({
    "FEED_FORMAT": 'csv',
    "FEED_URI": 'output.csv',
})
c.crawl(MySpider)
c.start()
