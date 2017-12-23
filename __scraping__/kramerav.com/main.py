#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47899992/1832058
#



You can concatenate all items inside for loop

    all_divs = soup.select("div.large-image")

    for item in all_divs:
        div += str(item)
        time += 1

or using join()

    time = len(all_divs)

    div = ''.join(str(item) for item in all_divs)

You can also write in file directly inside for loop and you get to row

    for item in all_divs:
        csv_writer.writerow( [str(item).strip()] )
        time += 1

Working example

import urllib.request
from bs4 import BeautifulSoup
import csv

div = ""
time = 0

f = open('output.csv', 'w')
csv_writer = csv.writer(f)

all_urls = [
  "https://www.kramerav.com/de/Product/VM-2N",
  "https://www.kramerav.com/de/Product/SDIA-IN2-F16",
]

for url in all_urls:
    print('url:', url)

    html = urllib.request.urlopen(url).read()

    try:
        soup = BeautifulSoup(html)
        all_divs = soup.select("div.large-image")

        for item in all_divs:
            div += str(item)
            time += 1

        # or     
        time = len(all_divs)
        div = ''.join(str(item) for item in all_divs)

        # or

        for item in all_divs:
            #div += str(item)
            #time += 1
            csv_writer.writerow( [time, str(item).strip()] )

    except IndexError as ex:
        print('Error:', ex)
        time += 1
    finally:
        print(time, div)

f.close()        


