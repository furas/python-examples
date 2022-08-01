# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.07.19
# [php - How can I get a dataset from a graph in a website using dev tools and Python? - Stack Overflow](https://stackoverflow.com/questions/73038957/how-can-i-get-a-dataset-from-a-graph-in-a-website-using-dev-tools-and-python/)

import requests
from bs4 import BeautifulSoup

# --- field ---

url = "https://sasri.sasa.org.za/agronomy/mycanesimlite/mcl_single_run_get_input.php?start_date=2021-06-15&harvest_date=2022-06-15&ratoon=R&residue=0&tam=150&irrigation=Rainfed&weather_station=14&forecast=Normal"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

field = soup.find("input", {"id": "field_hidden"})

print('field:', field['value'])

# --- JSON data ---

url = "https://sasri.sasa.org.za/agronomy/mycanesimlite/mcl_crop_status_data.php"

payload = {"field": field['value']}

response = requests.post(url, data=payload)

data = response.json()

print(data)

# --- CSV data ---

import pandas as pd

url = 'https://sasri.sasa.org.za/agronomy/mycanesimlite/Daily_data{}.csv'.format(field['value'])

df = pd.read_csv(url)

print(df)

