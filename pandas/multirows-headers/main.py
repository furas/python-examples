import pandas as pd

#
# more in documentation: https://pandas.pydata.org/pandas-docs/stable/advanced.html
#

#----------------------------------------------------------------------

# doesn't works
df = pd.DataFrame([[1,2,3],[4,5,6]], 
            columns=[('a', 'x'), ('b', 'y'), ('c', 'z')])

print(df)

#    (a, x)  (b, y)  (c, z)
# 0       1       2       3
# 1       4       5       6

# works
df = pd.DataFrame([[1,2,3],[4,5,6]], 
            columns=pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')]))

print(df)

#    a  b  c
#    x  y  z
# 0  1  2  3
# 1  4  5  6

# ---------------------------------------------------------------------

# add second row to existing headers

# single row headers
df = pd.DataFrame([[1,2,3],[4,5,6]], columns=['a','b','c'])

print(df)

#    a  b  c
# 0  1  2  3
# 1  4  5  6

second = ['x', 'y', 'z']
tuples = list(zip(df.columns, second))

print(tuples)

# [('a', 'x'), ('b', 'y'), ('c', 'z')]

df.columns = pd.MultiIndex.from_tuples(tuples)

print(df)

#    a  b  c
#    x  y  z
# 0  1  2  3
# 1  4  5  6

# ---------------------------------------------------------------------

# save in csv with two rows of headers (without indexes)
df.to_csv("test.csv", index=False)

# ---------------------------------------------------------------------

# load from csv with two rows of headers - in rows 0 and 1
df = pd.read_csv("test.csv", header=[0,1])

print(df)

#    a  b  c
#    x  y  z
# 0  1  2  3
# 1  4  5  6

# ---------------------------------------------------------------------

# without headers - data in first rows
df = pd.DataFrame([['a','b','c'],['x','y','z'],[1,2,3],[4,5,6]])

# add headers 
df.columns = pd.MultiIndex(levels=[['a','b','c'],['x','y','z']], labels=[[0,1,2],[0,1,2]])

# remove rows
df = df.drop([0,1])

# reindex from 0 
df = df.reset_index(drop=True)

print(df)

# ---------------------------------------------------------------------

# without headers - data in first rows
df = pd.DataFrame([['a','b','c'],['x','y','z'],[1,2,3],[4,5,6]])

# add headers 
df.columns = pd.MultiIndex.from_tuples(list(zip(df.iloc[0], df.iloc[1])))

# remove rows
df = df.drop([0,1])

# reindex from 0 
df = df.reset_index(drop=True)

print(df)

