
# date: 2019.05.10
# https://stackoverflow.com/questions/56070434/my-code-wrongfully-downloads-a-csv-file-from-an-url-with-python/56071844#56071844

import requests
from bs4 import BeautifulSoup

s = requests.Session()

url='https://www.ishares.com/uk/individual/en/products/251567/ishares-asia-pacific-dividend-ucits-etf?switchLocale=y&siteEntryPassthrough=true'

response = s.get(url, allow_redirects=True)

if response.status_code == 200:
    print("Success")
else:
    print("Failure")

#find the url for the CSV
soup = BeautifulSoup(response.content,'lxml')

for i in soup.find_all('a',{'class':"icon-xls-export"}):
    print(i.get('href'))

# I get two types of files, one CSV and the other xls.
link_list=[]
for i in soup.find_all('a', {'class':"icon-xls-export"}):
    link_list.append(i.get('href'))

# I create the link with the CSV
url_csv = "https://www.ishares.com//"+link_list[0]

response_csv = s.get(url_csv)

if response_csv.status_code == 200:
    print("Success")
    f = open('dataset.csv', 'wb')
    f.write(response_csv.content)
    f.close()
else:
    print("Failure")

