import csv
import pandas as pd


f1 = open('sample.csv')
f2 = open('temp.csv', 'w')
reader = csv.reader(f1)
for row in reader:
    f2.write(row[0] + '\n')
f2.close()
f1.close()


df = pd.read_csv('temp.csv')

print(len(df.columns))
print(df)
