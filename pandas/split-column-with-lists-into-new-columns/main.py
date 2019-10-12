#!/usr/bin/env python


# date: 2019.09.21
# https://stackoverflow.com/questions/58037315/splitting-a-dataframe-column-from-scrapped-webpage-based-on-a-delimiter/58037773#58037773

# split column with lists into new columns


import urllib.request, json
import pandas as pd

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2016-10-01&endtime=2016-10-02"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

y = data['features']

for d in y:
    d.update(d.pop('geometry', {}))
    
for i in y:
    i.update(i.pop('properties', {}))
    
df = pd.DataFrame(y)
df = df.drop(['alert','cdi','detail','felt','id','ids','mmi','net','sources','updated','url'], axis=1)

# ----

df['x'] = df['coordinates'].apply(lambda x: x[0])
df['y'] = df['coordinates'].apply(lambda x: x[1])
df['z'] = df['coordinates'].apply(lambda x: x[2])
print(df1[['x', 'y', 'z', 'coordinates']].head())

# ----

df[['a', 'b', 'c']] = df['coordinates'].apply(pd.Series)

print(df1[['a', 'b', 'c', 'coordinates']].head())

# ----

'''Result:
            x          y      z                       coordinates
0 -118.895700  38.860700   5.30         [-118.8957, 38.8607, 5.3]
1 -124.254833  40.676333  27.40  [-124.2548333, 40.6763333, 27.4]
2 -116.020000  31.622500  10.19         [-116.02, 31.6225, 10.19]
3 -121.328167  36.698667   4.31  [-121.3281667, 36.6986667, 4.31]
4 -115.614500  33.140500   5.02        [-115.6145, 33.1405, 5.02]

            a          b      c                       coordinates
0 -118.895700  38.860700   5.30         [-118.8957, 38.8607, 5.3]
1 -124.254833  40.676333  27.40  [-124.2548333, 40.6763333, 27.4]
2 -116.020000  31.622500  10.19         [-116.02, 31.6225, 10.19]
3 -121.328167  36.698667   4.31  [-121.3281667, 36.6986667, 4.31]
4 -115.614500  33.140500   5.02        [-115.6145, 33.1405, 5.02]
'''

