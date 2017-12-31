import requests
from bs4 import BeautifulSoup
import webbrowser

# ---------------------------------------------------------------------

def display(content, filename='output.html'):
    with open(filename, 'w') as f:
        f.write(content)
    webbrowser.open(filename)

# ---------------------------------------------------------------------

session = requests.Session()
session.headers.update({'USER-AGENT': 'Mozilla/5.0'})

# main page

url = 'https://httpbin.org'
response = session.get(url)

# POST / XHR

params = {
    'id': '123',
}

headers = {'X-Requested-With': 'XMLHttpRequest'}
        
url = 'https://httpbin.org/post'

response = session.post(url, data=params, headers=headers)

print(response.text)

data = response.json()
print(data.keys())

# ---------------------------------------------------------------------

soup = BeautifulSoup(response.text, 'html.parser')
#divs = soup.find_all('div', class_='xxx') 
all_divs = soup.find_all('div', {'class': 'xxx'}) 

for div in all_divs:
   print(div.text)
