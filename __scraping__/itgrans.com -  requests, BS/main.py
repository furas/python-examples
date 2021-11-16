
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.10
#
# title: I'm receiving a 419 page expired status code when trying to use requests. How do I successfully login?
# url: https://stackoverflow.com/questions/69906196/im-receiving-a-419-page-expired-status-code-when-trying-to-use-requests-how-do/69920886#69920886

# [I'm receiving a 419 page expired status code when trying to use requests. How do I successfully login?](https://stackoverflow.com/questions/69906196/im-receiving-a-419-page-expired-status-code-when-trying-to-use-requests-how-do/69920886#69920886)


import requests
from bs4 import BeautifulSoup

url = 'https://rates.itgtrans.com/login'

headers = {
    #'authority': 'rates.itgtrans.com',
    #'cache-control': 'max-age=0',
    #'origin': 'https://rates.itgtrans.com',
    #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'referer': 'https://rates.itgtrans.com/login',
    #'accept-language': 'en-US,en;q=0.9',
}

data = {
  '_token': '-empty-',
  'email': '****',
  'password': '****',
  'button': ''
}


with requests.Session() as s:
    
    response = s.get(url='https://rates.itgtrans.com/login', headers=headers)
    #print(response.text)
    
    soup = BeautifulSoup(response.text)
    token = soup.find('input', {'name': "_token"})['value']
    
    print('token:', token)
    data['_token'] = token
    
    response = s.post(url='https://rates.itgtrans.com/login', data=data, headers=headers)
    #print(response.text)
    print('status_code:', response.status_code)ma
