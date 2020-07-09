
# author: https://blog.furas.pl
# date: 2020.07.08
# 

from selenium import webdriver
  
url = 'https://www.howmanysyllables.com/syllable_counter/'

# open browser
driver = webdriver.Firefox()

# load page
driver.get(url)

# find field 
item = driver.find_element_by_id('syl_input')

# put text
item.send_keys('Hello World')

# find button 
item = driver.find_element_by_id('button_submit')

# click button
item.click()

# find all red numbers 
all_answers = driver.find_elements_by_class_name('Answer_Red')
#for answer in all_answers:
#    print(answer.text)

# display numbers
print('words:', all_answers[0].text)
print('syllables:', all_answers[1].text)
print('characters:', all_answers[2].text)

