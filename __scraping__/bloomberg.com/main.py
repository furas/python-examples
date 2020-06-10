# if it get data then it works event with less headers
# but when it get title `Bloomberg - Are you a robot?`
# then it can get recaptcha which you may see when you open page in browser.
# Sometimes it needs all headers again and it has to wait few seconds before request
# but sometimes it need to resolve recaptcha.

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

s = requests.Session()
s.headers.update(headers)

#print(s.headers)

# --- get main page to get Cookies ---

#url = 'https://www.bloomberg.com'
#print('url:', url)
#source = s.get(url, headers=headers)
#soup = BeautifulSoup(source.content, 'lxml')
#print('title:', soup.find('title').text)

#print(source.content)

# --- get page with data ---

url = 'https://www.bloomberg.com/profile/company/AAPL:US'
print('url:', url)
source = s.get(url, headers=headers)
soup = BeautifulSoup(source.content, 'lxml')
print('title:', soup.find('title').text)

#print(source.content)

soup = BeautifulSoup(source.content, 'lxml')
company_name = soup.findAll('h1', class_= 'companyName__9bd88132')
company_description = soup.findAll('div', class_ = 'description__ce057c5c')

print('company_name:', company_name[0].text if company_name else company_name)
print('company_description:', company_description[0].text if company_description else company_description)
