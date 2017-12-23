#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47858268/1832058
#

from bs4 import BeautifulSoup
import requests
import re
#import webbrowser

s = requests.Session()

def get_soup(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    
    r = s.get(url, headers=headers)
    
    #with open('temp.html', 'wb') as f:
    #    f.write(r.content)
    #    webbrowser.open('temp.html')
        
    if r.status_code != 200:
        print('status code:', r.status_code)
    else:
        return BeautifulSoup(r.text, 'html.parser')
    
def parse(url, response):
    
    if not response:
        print('no response:', url)
        return
    
    # get number of reviews
    num_reviews = response.find('span', class_='reviews_header_count').text
    num_reviews = num_reviews[1:-1] # remove `( )`
    num_reviews = num_reviews.replace(',', '') # remove `,`
    num_reviews = int(num_reviews)
    print('num_reviews:', num_reviews, type(num_reviews))
    
    # create template for urls to pages with reviews
    url = url.replace('.html', '-or{}.html')
    print('template:', url)
    
    # add requests to list
    for offset in range(0, num_reviews, 5):
        print('url:', url.format(offset))
        url_ = url.format(offset)
        parse_reviews(url_, get_soup(url_))
        #return # for test only - to stop after first page

def parse_reviews(url, response):
    print('review:', url)

    if not response:
        print('no response:', url)
        return
    
    for idx, review in enumerate(response.find_all('div', class_='review-container')):
        item = {
            'hotel_name': response.find('h1', class_='heading_title').text,
            'review_title': review.find('span', class_='noQuotes').text,
            'review_body': review.find('p', class_='partial_entry').text,
            'review_date': review.find('span', class_='relativeDate')['title'],#.text,#[idx],
            'num_reviews_reviewer': review.find('span', class_='badgetext').text,
            'reviewer_name': review.find('span', class_='scrname').text,
            'bubble_rating': review.select_one('div.reviewItemInline span.ui_bubble_rating')['class'][1][7:],
        }
        #~ yield item
        for key,val in item.items():
            print(key, ':', val)
        print('----')
        #return # for test only - to stop after first review
        
start_urls = [
    'https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html',
    #'https://www.tripadvisor.com/Hotel_Review-g60795-d102542-Reviews-Courtyard_Philadelphia_Airport-Philadelphia_Pennsylvania.html',
    #'https://www.tripadvisor.com/Hotel_Review-g60795-d122332-Reviews-The_Ritz_Carlton_Philadelphia-Philadelphia_Pennsylvania.html',
]

for url in start_urls:
    parse(url, get_soup(url))
