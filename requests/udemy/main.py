#!/usr/bin/env python3

import requests

query = input('Query [python]: ').strip()

if not query:
    query = 'python' 

headers = {
    #'User-Agent': 'Mozilla/5.0', 
    'Referer': 'https://www.udemy.com/courses/search/?src=sac&q=' + query.replace(' ', '%20')
}

url = 'https://www.udemy.com/api-2.0/search-courses/?src=sac&q=' + query.replace(' ', '+')

while True:
    print('----------')
    print('url:', url)
    print('----------')
    
    r = requests.get(url, headers=headers)
    data = r.json()
    
    for course in data['courses']:
        '''
        print(course.keys())
        
        dict_keys(['id', 'price', 'image_240x135', 'num_reviews', 
        'instructional_level', 'content_info', 'bestseller_badge_content', 
        '_class', 'image_304x171', 'discount_price', 'relevancy_score', 
        'image_125_H', 'avg_rating_recent', 'input_features', 
        'visible_instructors', 'is_paid', 'published_title', 'headline', 
        'num_published_lectures', 'url', 'title', 'predictive_score', 
        'avg_rating', 'image_480x270'])
        '''
        print('({:>5s})'.format(course['price']), course['title'])

    if 'next' not in data['pagination']:
        break
    
    url = 'https://www.udemy.com' + data['pagination']['next']['url']
