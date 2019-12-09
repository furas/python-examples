#!/usr/bin/env python3

# date: 2019.12.09

import pandas as pd

df = pd.DataFrame({
    'X1': [1,2,3,4,5,6,7,8,9,10,11,12],
    'X2': [21,22,23,24,25,26,27,28,29,30,31,32],
    'label': ['a','a','a','a','b','b','b','b','c','c','c','c']
})

groups = df.groupby('label')

df2 = groups.head(2)
#df2 = groups.apply(lambda x:x.sample(frac=1)[:2])
print(df2)

df2 = df2.sample(frac=1).reset_index(drop=True)

X_train = df2[['X1','X2']]
y_train = df2['label']

print(X_train)
print(y_train)

    
