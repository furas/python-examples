#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47858268/1832058
#

import requests               # to get html from server
from bs4 import BeautifulSoup # to search in html
#~ import webbrowser             # to open (downloaded) html file in web browser
import csv                    # to write in CSV 


# global variable to keep request session with all cookies, etc.
s = requests.Session()

# NEW: to get reviews in all languages - doesn't work, 
#      it gets only english reviews but page gives number of all reviews :(
s.cookies.set('TALanguage', 'ALL', domain='.tripadvisor.com', path='/') # other lanugages ie. 'en', 'es'
#s.cookies.set('TALanguage', 'es', domain='.tripadvisor.com', path='/') # other lanugages ie. 'en', 'es'

#print(s.cookies)

def get_soup(url):
    '''Read HTML from server and convert to Soup'''
    
    # some portals send correct HTML only if you have correct header 'user-agent'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    
    # get response with HTML
    r = s.get(url, headers=headers)
    #r = s.get(url + '?filterLang=ALL', headers=headers)

    #print(s.cookies)
    
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
    
    # get number of reviews in all languages
    num_reviews = response.find('span', class_='reviews_header_count').text # get text
    num_reviews = num_reviews[1:-1] # remove `( )`
    num_reviews = num_reviews.replace(',', '') # remove `,` in number (ie. 1,234)
    num_reviews = int(num_reviews) # convert text into integer
    print('[parse] num_reviews ALL:', num_reviews, type(num_reviews))
    
    num_reviews = response.select_one('div[data-value="en"] span').text # get text
    num_reviews = num_reviews[1:-1] # remove `( )`
    num_reviews = num_reviews.replace(',', '') # remove `,` in number (ie. 1,234)
    num_reviews = int(num_reviews) # convert text into integer
    print('[parse] num_reviews ENGLISH:', num_reviews, type(num_reviews))
    
    # create template url to subpages with reviews
    # ie. https://www.tripadvisor.com/Hotel_Review-g562819-d289642-or{}.html
    url_template = url.replace('.html', '-or{}.html')
    print('[parse] url_template:', url_template)
    
    # get subpages and parse reviewes.
    # every subpage has 5 reviews and it has url with -or0.html -or5.html -or10.html -or15.html etc.
    for offset in range(0, num_reviews, 5):
        subpage_url = url_template.format(offset)
        
        print('[parse] subpage_url:', subpage_url)
        
        parse_reviews(subpage_url, get_soup(subpage_url))
        
        #~ return # for test only - to stop after first page


def parse_reviews(url, response):
    '''Get all reviews from one page'''

    global csv_file
    
    print('[parse_reviews] url:', url)

    if not response:
        print('[parse_reviews] no response:', url)
        return
    
    hotel_name = response.find('h1', id='HEADING').text
    
    # find all reviews on page 
    for idx, review in enumerate(response.find_all('div', class_='review-container')):
        
        # it has to check if `badgets` (contributions/helpful_vote) exist on page 
        badgets = review.find_all('span', class_='badgetext')
        if len(badgets) > 0:
            contributions = badgets[0].text
        else:
            contributions = '0'

        if len(badgets) > 1:
            helpful_vote = badgets[1].text
        else:
            helpful_vote = '0'
        
        # it has to check if `user_loc` exists on page
        #user_loc = review.find_all('div[@class="userLoc"]/strong/text()')
        user_loc = review.select_one('div.userLoc strong')
        if user_loc:
            user_loc = user_loc.text
        else:
            user_loc = ''
            
        # it has to find value in class name (ie. "bubble_40" => "40", "bubble_50" => "50")
        #bubble_rating = $xpath->query('.//span[contains(@class, "ui_bubble_rating")]', $review)[0]->getAttribute('class');
        bubble_rating = review.select_one('span.ui_bubble_rating')['class']
        bubble_rating = bubble_rating[1].split('_')[-1]
        
        item = {
            'hotel name': hotel_name,
            
            'review title': review.find('span', class_='noQuotes').text,
            'review body': review.find('p', class_='partial_entry').text,
            'review date': review.find('span', class_='ratingDate')['title'], # 'ratingDate' instead of 'relativeDate'
            
            'contributions': contributions, # former 'num_reviews_reviewer'
            'helpful vote': helpful_vote, # new 
            
            'user name': review.find('div', class_='info_text').find('div').text, # former 'reviewer_name'
            'user location': user_loc, # new
             
            'rating': bubble_rating,
        }
        #~ yield item # generator which returns items 

        # append to CSV file 
        csv_file.writerow(item)
        
        # display on screen 
        print('\n--- review ---\n')
        for key,val in item.items():
            print(' ', key, ':', val)
        
        #~ return # for test only - to stop after first review

    print() # empty line after last review
    
#----------------------------------------------------------------------

if __name__ == '__main__':

    # some URLs for testing
    start_urls = [
        'https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html',
        #'https://www.tripadvisor.com/Hotel_Review-g60795-d102542-Reviews-Courtyard_Philadelphia_Airport-Philadelphia_Pennsylvania.html',
        #'https://www.tripadvisor.com/Hotel_Review-g60795-d122332-Reviews-The_Ritz_Carlton_Philadelphia-Philadelphia_Pennsylvania.html',
    ]

    with open('results.csv', 'w') as csvfile:
        csv_file = csv.DictWriter(csvfile, ['hotel name', 'review title', 'review body', 'review date', 'contributions', 'helpful vote', 'user name' , 'user location', 'rating'])

        csv_file.writeheader()
        for url in start_urls:
            parse(url, get_soup(url))
