import requests

# set the apikey and limit
API_KEY = "LIVDSRZULELA"  # test value
search_term = "cat"

def get_urls(search, limit=8):
    payload = {
        'key': API_KEY,
        'limit': limit,
        'q': search,
    }
    # our test search
    
    # get the top 8 GIFs for the search term
    r = requests.get("https://g.tenor.com/v1/search", params=payload)
    
    results = []
    
    if r.status_code == 200:
        data = r.json()
        #print('[DEBUG] data:', data)
    
        for item in data['results']:
            #print('[DEBUG] item:', item)
            for media in item['media']:
                #print('[DEBUG] media:', media)
                #for key, value in media.items():
                #    print(f'{key:10}:', value['url'])
                #print('----')

                if 'tinygif' in media:
                    results.append(media['tinygif']['url'])
    else:
        results = []
        
    return results 

# --- main --- 

cat_encouragements = get_urls('cat')

for url in cat_encouragements:
    print(url)
    
    
