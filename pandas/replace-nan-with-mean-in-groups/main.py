
# date: 2019.04.16
# https://stackoverflow.com/questions/55699046/filling-specific-missing-value-in-python?noredirect=1#comment98080392_55699046

job_title = '''ANALYST, BRAND DEVELOPMENT
ANESTHESIOLOGIST
ANESTHESIOLOGIST
BUSINESS INTELLIGENCE ANALYSTS
CIVIL ENGINEER
CIVIL ENGINEER
COMPUTER PROGRAMMER
COMPUTER PROGRAMMER ANALYST
COMPUTER SYSTEM ANALYST
COMPUTER SYSTEM ANALYST
COMPUTER SYSTEMS ANAGLYST
COMPUTER SYSTEMS ANALYST
CONSULTANT
CORPORATE COMMUNICATIONS SPECIALIST
COUNSELOR
DESIGN
ELEMENTARY CO-TEACHER
FASHION MODEL
FIELD ENGINEER
FINANCIAL ANALYST
FINANCIAL SENIOR ANALYST
FINANCIAL SPECIALIST'''.split('\n')

job_title = list(set(job_title))

# --- create random data with some NaN
import random

data = []

for _ in range(1):
    for item in job_title:
        data.append( (item, None))

for _ in range(2):    
    for item in job_title:
        data.append( (item, random.randint(10000,100000)))    

random.shuffle(data)

# --- get mean salary for JOB_TITLE ---

import pandas as pd

df = pd.DataFrame(data, columns=['JOB_TITLE', 'SALARY'])

rows_with_na = df['SALARY'].isna()

print('\n--- before ---\n')
print(df[ rows_with_na ])

print('\n--- mean ---\n')
groups = df.groupby(['JOB_TITLE'])


# it doesn't work as I expected - it doesn't change data in original `df`
# (or i would say I expected this will not work but I still hoped it will work :)

for idx, grp in groups:
    mean = grp['SALARY'].mean()
    print('mean:', mean, idx)
    print(grp['SALARY'].fillna(mean)) 
    print('---')

# this works
#df['SALARY'] = groups.transform(lambda x: x.fillna(x.mean()))
#df['SALARY'] = groups.transform(lambda x: x.fillna(x.mean()))['SALARY']
df['SALARY'] = groups['SALARY'].transform(lambda x: x.fillna(x.mean()))
    
print('\n--- after ---\n')
print(df[ rows_with_na ])

