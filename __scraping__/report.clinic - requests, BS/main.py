import requests
from bs4 import BeautifulSoup
import pandas as pd

links = [
    'https://report.clinic/detail/L_1100170',
    'https://report.clinic/detail/L_3020779',
]

all_data = list()

for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
  
    data = {
        'tag': [],
        'name': "",
        'address': ""
    }
    
    for urls in soup.select(".menu_side_item .list_common .list_item_link .display_flex"):
        tag = urls.get_text(strip=True)
        data['tag'].append(tag)
        print('tag:', tag)

    name = soup.find("h1")
    if name:
        name = name.get_text(strip=True)
        data['name'] = name
        print('name:', name)

    for a in soup.find_all('div', class_="panel"):
        for b in a.find_all('p', class_="headline_h4", text="住所"):
            print('head:', b.get_text())
            address = b.findNext('p')
            if address:
                address = address.get_text(strip=True, separator=' | ')
                data['address'] = address
                print('address:', address)

    all_data.append(data)

# --- after loop ---

#print(all_data)

df = pd.DataFrame(all_data)

print(df[['address', 'name']])
