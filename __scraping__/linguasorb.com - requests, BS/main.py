# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.17


from bs4 import BeautifulSoup
import requests


url = f"https://www.linguasorb.com/spanish/verbs/beginning-with-a"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

all_pages = soup.find('ul', class_='pagination').find_all('a', href=True)

all_verbs = []

for page in all_pages:
    new_url = "https://www.linguasorb.com" + page['href']
    print('url:', new_url)
    
    new_response = requests.get(new_url)
    new_soup = BeautifulSoup(new_response.content, 'html.parser')
    
    verb_table = new_soup.find('table', class_='table-striped')
    findatag = verb_table.find_all('a', class_=None)
    for verb in findatag:
        all_verbs.append(verb.span.text)
        
print(all_verbs)
print(len(all_verbs), len(set(all_verbs)))
