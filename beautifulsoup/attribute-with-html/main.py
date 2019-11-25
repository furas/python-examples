from bs4 import BeautifulSoup as BS

text = '''
<tr data-title='<img src="url1.jpg" alt="1">' >
<tr data-title='<img src="url2.jpg" alt="2">' >
'''

soup = BS(text, 'html.parser')

all_items = soup.find_all('tr', {"data-title": True})

for item in all_items:
    print('item:', item['data-title'])
    #print('item:', item.attrs.get('data-title'))
    #print('item:', item.attrs['data-title'])
    #print('item:', item.get('data-title'))
    
    link = item.get('data-title')
    s = BS(link, 'html.parser')
    print('src:', s.find('img')['src'])
    
 

