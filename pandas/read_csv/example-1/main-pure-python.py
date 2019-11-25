import requests
import csv

def main(url):
    r = requests.get(url)

    lines = r.text.split('\n')

    headers = lines[0].split(',')

    data = []
    
    for line in lines[1:]:
        line = line.strip()
        if line: # skip empty lines
            row = line.strip().split(',')
            
            # convert string to float/int
            row[1] = float(row[1])
            row[2] = float(row[2])
            row[3] = float(row[3])
            row[4] = float(row[4])
            row[5] = float(row[5])
            row[6] = int(row[6])
            
            data.append(row)
    
    return headers, data
    
if __name__ == "__main__":    
    headers, data = main('http://193.1.33.31:88/pa1/GOOGL.csv')

    print(headers)
    
    print('--- data ---')
    print(data[0])
    print(data[-1])
    
    year2018 = []
    for row in data:
        if '2018-01-01' <= row[0] < '2019-01-01':
           year2018.append(row)
           
    print('--- year 2018 ---')
    print(year2018[0])
    print(year2018[-1])

    a = 0
    b = 0
    for row in year2018:
        a += row[5] * row[6]
        b += row[6]

    result = a/b
    
    print(result)
