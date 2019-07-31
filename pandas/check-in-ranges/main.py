
# date: 2019.07.30
# https://stackoverflow.com/questions/57261926/get-all-items-from-dfs-column-that-are-within-a-range-using-ranges-iterable

import pandas as pd

df = pd.DataFrame([
        ['c1', 137674167],
        ['c2', 2166178],
        ['c3', 268],
     ], columns=['c', 'C2017Value'])

ranges = [
    (261, 4760),
    (12273391, 11104571063),
    (45695385, 4134339925),
    (15266178, 1376748162),
    (10106104, 97810284),
    (6492248, 588025190)
]


def check_ranges(value, ranges):
    for a, b in ranges:
        if a <= value <= b:
            return True
    return False
    
results = df[ df['C2017Value'].apply(lambda x, r=ranges:check_ranges(x,r)) ]
print(results)


def get_range(value, ranges):
    for a, b in ranges:
        if a <= value <= b:
            return (a, b)
    return None
                    
df['range'] = df['C2017Value'].apply(lambda x, r=ranges:get_range(x,r))
print(df)

results = df[ df['range'].notnull() ]
print(results)
