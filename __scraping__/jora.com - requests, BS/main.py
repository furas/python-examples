# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.05
# [python - WebScraping Application - Stack Overflow](https://stackoverflow.com/questions/71745973/webscraping-application/)

from bs4 import BeautifulSoup
import requests
    
html_text = requests.get('https://au.jora.com/jobs-in-Maryborough-QLD?sp=facet&l=Maryborough+QLD&st=date').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find('div', class_="jobresults").find_all('article')
jobs = soup.select('div.jobresults article')  # CSS selector
print('len(jobs):', len(jobs))

for job in jobs:
   #job_title = job.text.replace(' ', ' ')
    location = job.find('span', class_='job-location').text.strip()
    #print(location.text)
    if 'Maryborough' in location:
        company_name = job.find('span', class_='job-company').text.strip()  # PEP8: inside `()` use `=` without spaces
        job_title = job.find('h3', class_='job-title').text.strip() 
        print(f'''
Company Name: {company_name}
Location: {location}
Job Title: {job_title}
''')

