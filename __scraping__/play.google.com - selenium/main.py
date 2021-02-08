
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.02.08
# https://stackoverflow.com/questions/66095101/python-3-6-web-crawler-using-selenium-cannot-grab-the-dates-and-ratings-of-use

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://play.google.com/store/apps/details?id=io.silvrr.installment&hl=en_US&gl=US&showAllReviews=true' 

#browser = webdriver.Chrome(path)
browser = webdriver.Firefox()

browser.get(url)

cards = browser.find_elements_by_class_name('d15Mdf.bAhLNe')  # it has to be `dot` in place of `space`
user_reviews = []

for number, item in enumerate(cards, 1):  
    review = item.find_element_by_class_name('UD7Dzf').text
    date = item.find_element_by_class_name('p2TkOb').text
    user = item.find_element_by_class_name('X43Kjb').text
    rated = item.find_element_by_xpath('.//div[@class="pf5lIe"]/div').get_attribute('aria-label').split(' ')[1] # relative xpath with dot at the beginning

    user_reviews.append({
               'number': number, 
               'review': review, 
               'date': date, 
               'user': user,
               'rated': rated,
    })

for item in user_reviews:  
    print('---', item['number'], '---')
    print('date:', item['date'])
    print('user:', item['user'])
    print('rated:', item['rated'])
    print('review:', item['review'][:50], '...')

