# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.28
# [python - How to convert a soup to a Dataframe - Stack Overflow](https://stackoverflow.com/questions/72779612/how-to-convert-a-soup-to-a-dataframe/72780471?noredirect=1#comment128558903_72780471)

import requests
import requests_cache
import pandas as pd
import io

# without header `Content-Type` it will send `HTML` instead of `JSON`
headers = {
    'Content-Type': 'application/json; charset=utf-8',
}

url = 'https://droughtmonitor.unl.edu/DmData/GISData.aspx/ReturnDMWeeks'

response = requests.get(url, headers=headers)
data = response.json()

all_dates = [f"{d[:4]}-{d[4:6]}-{d[6:]}" for d in data['d']]
print(len(all_dates))

# --- before loop ---

all_dfs = []

# url without `2022-06-21` at the end
url = 'https://droughtmonitor.unl.edu/DmData/GISData.aspx/?mode=table&aoi=county&date='

# --- loop ---

requests_cache.install_cache('csv_cache')  # keep in cache to resuse from cache when it crash and it need to run again

for date in all_dates:
    print('date:', date)
    csv = requests.get(url + date)
    df = pd.read_csv(io.StringIO(csv.text))
    #df.to_csv(f"{date}.csv")  # to keep it when
    all_dfs.append( df )

# --- after loop ---

full_df = pd.concat(all_dfs)
print(full_df)
