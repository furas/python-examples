# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.07.21
# 

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.city-data.com/city/Adak-Alaska.html"
response = requests.get(url)
#print('status:', response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

religion_population = soup.find(id="religion").find_all('tr')

data = []

for row in religion_population:
    columns = row.find_all('td')
    if columns:
        religion = columns[0].get_text(strip=True)
        number   = columns[1].get_text(strip=True).replace(",", "")
        print(f'religion: {religion} | number: {number}')
        data.append([religion, int(number)])

# ---------------------------------------------

df = pd.DataFrame(data, columns=['religion', 'number'])
df['percentage'] = (df['number'] / df['number'].sum()) * 100

print(df)

