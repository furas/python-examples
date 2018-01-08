
#
# https://stackoverflow.com/a/48075115/1832058
# 

import requests
from bs4 import BeautifulSoup

url = 'https://www.bcdental.org/yourdentalhealth/findadentist.aspx'

# --- session ---

s = requests.Session() # to automatically copy cookies
#s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})

# --- GET request ---

# get page to get cookies and params
response = s.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# --- set params ---

params = {
    # session - copy from GET request
    #'EktronClientManager': '',
    #'__VIEWSTATE': '',
    #'__VIEWSTATEGENERATOR': '',
    #'__EVENTVALIDATION': '',
    # main options
    'ctl00$terms': '',
    'ctl00$mainContent$drpCity': '526',
    'ctl00$mainContent$txtPostalCode': '',
    'ctl00$mainContent$drpSpecialty': 'GP',
    'ctl00$mainContent$drpLanguage': '0',
    'ctl00$mainContent$drpSedation': '0',
    'ctl00$mainContent$btnSearch': '+Search+',
    # other options
    #'ctl00$mainContent$chkUndr4Ref': 'on',
}

# copy from GET request
for key in ['EktronClientManager', '__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION']:
    value = soup.find('input', id=key)['value']
    params[key] = value
    #print(key, ':', value)

# --- POST request ---

# get page with table - using params
response = s.post(url, data=params)#, headers={'Referer': url})
soup = BeautifulSoup(response.text, 'html.parser')

# --- data ---

table = soup.find('table', id='ctl00_mainContent_DataList1')

if not table:
    print('no table')
    #table = soup.find_all('table')
    #print('count:', len(table))
    #print(response.text)
else:   
    for row in table.find_all('table'):
        for column in row.find_all('td'):
            text = ', '.join(x.strip() for x in column.text.split('\n') if x.strip()).strip()
            print(text)

        print('-----')        
