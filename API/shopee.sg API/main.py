
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.07.22
#
# title: How to use loops to scrape data from API
# url: https://stackoverflow.com/questions/68478524/how-to-use-loops-to-scrape-data-from-api/68479878?noredirect=1#comment121025287_68479878

import requests

# --- functions ---

def main(search_term, items_number=250):
    
    url = "https://shopee.sg/api/v4/search/search_items"

    params = {
        "by": "relevancy",
        "categoryids": 100630,
        "keyword": search_term,
        "limit": 100,
        "newest": 0,  # default value at start
        "order": "desc",
        "page_type": "search",
        "scenario": "PAGE_GLOBAL_SEARCH",
        "version": "2"
    }

    for offset in range(0, items_number, 100):

        print('\n--- offset:', offset, '---\n')

        params["newest"] = offset   # other parameters are the same
        
        limit = items_number - offset
        if  limit < 100:
            params["limit"] = limit
        
        r = requests.get(url, params=params)
        data = r.json()    

        print('>> items number in data:', len(data['items']), '\n')
        
        for number, item in enumerate(data['items']):

            print('number:', offset+number+1)
            
            basic = item['item_basic']
            
            #print('keys:', basic.keys())
            #for key, value in basic.items():
            #    print(f"{key}: {value}")
            
            # NAME
            name = basic['name']
            #name = basic.get('name', '- unknown -')  # safer if `name` may not exists in `data`
            print("Name:", name)
        
            # BRAND
            #brand = basic['brand']
            brand = basic.get('brand')  # safer if `brand` may not exists in `data`
            if brand is None:
                print()
            else:
                print("Brand:", brand)

            print('---')
            
# --- main ---

main("make-up")
#main("make-up", 60)
#main("make-up", 270)
