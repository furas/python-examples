import requests
import pandas as pd

s = requests.Session()

url = 'https://www.nseindia.com/products/content/derivatives/equities/historical_fo.htm'
s.get(url)

url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?instrumentType=FUTIDX&symbol=NIFTY&expiryDate=select&optionType=select&strikePrice=&dateRange=day&fromDate=&toDate=&segmentLink=9&symbolCount="
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.nseindia.com/products/content/derivatives/equities/historical_fo.htm'
}

# get HTML from url    
r = requests.get(url, headers=headers)
print('status:', r.status_code)
#print(r.text)

# user pandas to parse tables in HTML to DataFrames
all_tables = pd.read_html(r.text)
print('tables:', len(all_tables))


# get first DataFrame
df = all_tables[0]
#print(df.columns)

# drop multilevel column index
df.columns = df.columns.droplevel()
#print(df.columns)

# droo unknow columns
df = df.drop(columns=['Unnamed: 14_level_1', 'Unnamed: 15_level_1', 'Unnamed: 16_level_1'])
print(df.columns)
