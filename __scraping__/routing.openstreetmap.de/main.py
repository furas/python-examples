# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.07
# [javascript - export gpx file with python? - Stack Overflow](https://stackoverflow.com/questions/71375579/export-gpx-file-with-python/71375874#71375874)

import requests

start_lon = -0.0898    # can be also as text
start_lat = 51.514739  # can be also as text

end_lon = -0.096656    # can be also as text
end_lat = 51.516214    # can be also as text

data = f"{start_lon},{start_lat};{end_lon},{end_lat}"

transport = 'bike'  # 'car', 'foot'

url = f'https://routing.openstreetmap.de/routed-{transport}/route/v1/driving/{data}'

payload = {
    'overview': 'false',     # can't be True/False
    'alternatives': 'true',  # can't be True/False
    'steps': 'true',         # can't be True/False
}

response = requests.get(url, params=payload)
print(response.url)
#print(response.text)
print('---')

data = response.json()

for point in data['waypoints']:
    print('name:', point['name'])
    print('distance:', point['distance'])
    print('location:', point['location'])
    print('---')    
