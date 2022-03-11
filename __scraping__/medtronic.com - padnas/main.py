# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.10
# 

url = "https://www.medtronic.com/covidien/en-us/products/brain-monitoring/bis-monitoring-system.html"

import pandas as pd

all_tables = pd.read_html(url)

for table in all_tables:
    print(table.to_string())
