import pandas as pd

df = pd.read_csv('http://193.1.33.31:88/pa1/GOOGL.csv')
#df['Date'] = pandas.to_datetime(df['Date'])

#print(df.columns)

year2018 = df[ (df['Date'] >= '2018-01-01') & (df['Date'] < '2019-01-01') ]

result = (year2018['Volume'] * year2018['Adj Close']).sum() / year2018['Volume'].sum()

#print(result)

all_results = []
for year in range(2004, 2019):
    year = str(year)
    data = df[ df['Date'].str.startswith(year) ]
    result = (data['Volume'] * data['Adj Close']).sum() / data['Volume'].sum()

    all_results.append( (result, year) )
    #print(year, result)

print('--- sorted by result ---')

sorted_results = sorted(all_results)

for result, year in sorted_results:
    print(year, result)
