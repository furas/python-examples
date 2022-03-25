# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.17
# [python - How do I scrape the jobs available on this site? - Stack Overflow](https://stackoverflow.com/questions/71507207/how-do-i-scrape-the-jobs-available-on-this-site/71507423?noredirect=1#comment126394939_71507423)

from bs4 import BeautifulSoup
import requests

url = 'https://ng.indeed.com/jobs'

payload = {
    'q': 'customer service',
    'start': 0,
}

all_rows = []

for start in range(0, 70, 10):

    print('\n--- start:', start, '---\n')
    
    payload['start'] = start
    response = requests.get(url, params=payload)
    #print(response.status_code)
    
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div', class_='job_seen_beacon')

    for soup in jobs:
        
        company_name = soup.find('span', class_='companyName').text.strip()
            
        salary = soup.find('div', class_='metadata salary-snippet-container')
        if salary:
            salary = salary.text.strip()  
            
        published_date = soup.find('span', class_='date').text.strip()
            
        location = soup.find('div', class_='companyLocation').text.strip()
        
        row = [ company_name, salary, published_date, location]
        all_rows.append(row)
        
        print(f'''Company Name: {company_name}
salary: {salary}
Published Date: {published_date}
Location: {location}
---''')
        
# --- after loop ---

# - csv -

import csv

with open('output_1.csv', 'w') as f:
    csv_writer = csv.writer(f)
    
    headers = ["Company Name", "Salary", "Published Date", "Location"]
    csv_writer.writerow(headers)  # `writerow` without char `s` - to write single row

    csv_writers.writerow(all_rows)  # `writerows` with char `s` - to write list of rows

# - pandas -

import pandas as pd

df = pd.DataFrame(all_rows, columns=["Company Name", "Salary", "Published Date", "Location"])

df.to_csv('output_2.csv', index=False)
