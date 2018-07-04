import pandas as pd

# single row headers
df = pd.DataFrame([[1,2,3],[4,5,6]], columns=['a','b','c'])

# add second row to headers
second = ['x', 'y', 'z']
df.columns = pd.MultiIndex.from_tuples(list(zip(df.columns, second)))

print(df)

#    a  b  c
#    x  y  z
# 0  1  2  3
# 1  4  5  6

# save in csv with two rows of headers
df.to_csv("test.csv", index=False)

# load from csv with two rows of headers
df = pd.read_csv("test.csv", header=[0,1])
                 
print(df)

#    a  b  c
#    x  y  z
# 0  1  2  3
# 1  4  5  6
                 
