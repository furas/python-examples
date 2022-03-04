# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.04
# [python - scrape next page by changing the number of page in URL - Stack Overflow](https://stackoverflow.com/questions/71344116/scrape-next-page-by-changing-the-number-of-page-in-url/71345039#71345039)

from bs4 import BeautifulSoup
import requests

url = "https://www.mubawab.ma/fr/ct/marrakech/immobilier-a-vendre-all:sc:apartments-for-sale:p:1"

appart_no = 0

while True:
    print('\n--- new page ---\n')
    print('url:', url, '\n')
          
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    apparts = soup.find_all('div', {'class': 'contentBox'})  
    
    for appart in apparts:
        name_tag = appart.find('h2', {'class': 'listingTit'})
        name = name_tag.text.strip()
        
        link = appart.find('a').get('href', 'N\A')
        
        if link == 'N/A' or link == '#':
            print('SKIP:', name, link)
        else:
            #print('OK')
            
            appart_response = requests.get(link)
            appart_soup = BeautifulSoup(appart_response.text, 'html.parser')
            
            room_tag = appart_soup.find('div', {'class': 'catNav'})
            room = room_tag.get_text(strip=True, separator='|')  if room_tag else "N/A"
            appart_no += 1
            
            # clear it
            parts = room.split('\n')
            room  = " ".join(x.strip() for x in parts)
            
            print('name :', name)
            print('link :', link,)
            print('rooms:', room)
        print('---')

    # there are always two `arrowDot` (left, right) but some can be hidden
    arrow_tags = soup.find_all('a', {'class': 'arrowDot'})
    #print(arrow_tags)
    
    if len(arrow_tags) > 1 and arrow_tags[-1].get('href'):
        url = arrow_tags[-1].get('href')
    else:
        break
        
print("Total apparts:", appart_no)

