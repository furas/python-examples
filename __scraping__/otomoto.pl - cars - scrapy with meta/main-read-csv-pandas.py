import pandas as pd

df = pd.read_csv('output.csv')

print('columns:', df.columns)
print(df.head())
print(df['number'][:10])

for col in df.columns:
    print('\n---', col, '---\n')
    print(df[col][:10])
    

