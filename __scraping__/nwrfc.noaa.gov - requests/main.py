# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.26
# [python - Reading a CSV file into Pandas - Stack Overflow](https://stackoverflow.com/questions/71273200/reading-a-csv-file-into-pandas/71273335?noredirect=1#comment125983964_71273335)

import pandas as pd
import requests
import io

url = "https://www.nwrfc.noaa.gov/natural/nat_norm_text.cgi?id=TDAO3.csv"

response = requests.get(url)

start = response.text.find('<pre>') + len('<pre>')
end   = response.text.find('</pre>')

pre = response.text[start:end]

text = pre.replace('<br>', '\n')

buf = io.StringIO(text)

df = pd.read_csv(buf, skiprows=2, low_memory=False)

print(df.to_string())

