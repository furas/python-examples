
# date: 2020.03.01
# https://stackoverflow.com/questions/60471569/turning-for-loop-into-multiprocessing-loop/

import requests
import time

def get_data(query):

    url = 'https://site.web.api.espn.com/apis/common/v3/search?region=us&lang=en&query={}&limit=5&mode=prefix&type=player'.format(query)

    r = requests.get(url)
    data = r.json()
    
    id_ = data['items'][0]['id']
    name = data['items'][0]['displayName'] 

    #url = 'https://site.web.api.espn.com/apis/common/v3/sports/basketball/mens-college-basketball/athletes/{}?region=us&lang=en&contentorigin=espn'.format(id_)
    #r = requests.get(url)
    #data = r.json()

    url = 'https://site.web.api.espn.com/apis/common/v3/sports/basketball/mens-college-basketball/athletes/{}/overview?region=us&lang=en&contentorigin=espn'.format(id_)
    r = requests.get(url)
    data = r.json()

    labels = data['nextGame']['statistics']['labels']
    stats = data['nextGame']['statistics']['splits'][0]['stats']

    return (id_, name, labels, stats)

# --- main ---

start = time.time()

query = 'markell'

id_, name, labels, stats = get_data(query)

print('id:', id_)
print('name:', name)
for l, s in zip(labels, stats):
    print(l, s)

end = time.time()
print('time:', end-start, 's')

