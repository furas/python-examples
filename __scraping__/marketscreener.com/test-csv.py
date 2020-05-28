import pandas as pd

df = pd.read_csv(f'table1.csv', index_col=0) #, header=[0,1])
print(df)
    
df = pd.read_csv(f'table2.csv', index_col=0) #, header=[0,1])
print(df)
    
df = pd.read_csv(f'table3.csv') #, index_col=0)
print(df)
    
df = pd.read_csv(f'table4.csv', index_col=0)
print(df)
    
df = pd.read_csv(f'table5.csv') #, index_col=0)
print(df)
    
