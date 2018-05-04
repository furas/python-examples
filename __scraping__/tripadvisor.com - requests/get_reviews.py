#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47858268/1832058
#

import requests               # to get html from server
from bs4 import BeautifulSoup # to search in html
#~ import webbrowser             # to open (downloaded) html file in web browser

# global variable to keep request session with all cookies, etc.
s = requests.Session()

# NEW: get reviews in all languages - doesn't work, it gets only english reviews but page gives number of all reviews :(
s.cookies.set('TALanguage', 'ALL', domain='.google.co.uk', path='/') # other lanugages ie. 'en', 'es'


def get_soup(url):
    '''Read HTML from server and convert to Soup'''
    
    # some portals send correct HTML only if you have correct header 'user-agent'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    
    # get response with HTML
    r = s.get(url, headers=headers)
    
    # write html in file temp.html and open it in web browser.
    # it is useful to see/test what we get from server.
    #~ with open('temp.html', 'wb') as f:
    #~     f.write(r.content)
    #~     webbrowser.open('temp.html')
        
    # check if 
    if r.status_code != 200: # not OK
        print('[get_soup] status code:', r.status_code)
        # (as default) it will returns None instead of Soup
    else:
        return BeautifulSoup(r.text, 'html.parser')

    
def parse(url, response):
    '''Get number of reviews and start getting subpages with reviews'''
    
    print('[parse] url:', url)

    if not response:
        print('[parse] no response:', url)
        return
    
    # get number of reviews
    num_reviews = response.find('span', class_='reviews_header_count').text # get text
    num_reviews = num_reviews[1:-1] # remove `( )`
    num_reviews = num_reviews.replace(',', '') # remove `,`
    num_reviews = int(num_reviews) # convert text into integer
    print('[parse] num_reviews:', num_reviews, type(num_reviews))
    
    # create template url to subpages with reviews
    # ie. https://www.tripadvisor.com/Hotel_Review-g562819-d289642-or{}.html
    url_template = url.replace('.html', '-or{}.html')
    print('[parse] url_template:', url_template)
    
    # get subpages and parse reviwes.
    # every subpage has 5 reviews so pages has urls with -or0 -or5 -or10 etc.
    for offset in range(0, num_reviews, 5):
        subpage_url = url_template.format(offset)
        
        print('[parse] subpage_url:', subpage_url)
        
        parse_reviews(subpage_url, get_soup(subpage_url))
        
        #~ return # for test only - to stop after first page


def parse_reviews(url, response):
    '''Get all reviews from one page'''
    
    print('[parse_reviews] url:', url)

    if not response:
        print('[parse_reviews] no response:', url)
        return
    
    # find all reviews on page 
    for idx, review in enumerate(response.find_all('div', class_='review-container')):
        
        # NEW: works - it has to check if `badgetext` exists on page
        badgetext = review.find('span', class_='badgetext')
        if badgetext:
            badgetext = badgetext.text
        else:
            badgetext = ''
            
        item = {
            #'hotel_name': response.find('h1', class_='heading_title').text, # OLD: doesn't work
            'review_title': review.find('span', class_='noQuotes').text,
            'review_body': review.find('p', class_='partial_entry').text,
            #'review_date': review.find('span', class_='relativeDate')['title'],#.text,#[idx], # OLD: doesn't work
            'review_date': review.find('span', class_='ratingDate')['title'],#.text,#[idx], # NEW: works - 'ratingDate' instead of 'relativeDate'
            
            #'num_reviews_reviewer': review.find('span', class_='badgetext').text, # OLD: doesn't work 
            'num_reviews_reviewer': badgetext, # NEW: works - it has to check if `badgetext` exists on page
            
            #'reviewer_name': review.find('span', class_='scrname').text, # OLD: doesn't work
            #'bubble_rating': review.select_one('div.reviewItemInline span.ui_bubble_rating')['class'][1][7:], # OLD: doesn't work
        }
        #~ yield item # generator which returns items 
        
        # display on screen 
        print('--- review ---')
        for key,val in item.items():
            print(' ', key, ':', val)
        
        #~ return # for test only - to stop after first review


#----------------------------------------------------------------------

if __name__ == '__main__':

    # some URLs for testing
    start_urls = [
        'https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html',
        #'https://www.tripadvisor.com/Hotel_Review-g60795-d102542-Reviews-Courtyard_Philadelphia_Airport-Philadelphia_Pennsylvania.html',
        #'https://www.tripadvisor.com/Hotel_Review-g60795-d122332-Reviews-The_Ritz_Carlton_Philadelphia-Philadelphia_Pennsylvania.html',
    ]

    for url in start_urls:
        parse(url, get_soup(url))
