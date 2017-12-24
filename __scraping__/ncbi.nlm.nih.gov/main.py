
#
# https://stackoverflow.com/a/47706195/1832058
#

import requests
import re
from bs4 import BeautifulSoup

# Create a variable with the url
url = 'https://www.ncbi.nlm.nih.gov/protein/EGW15053.1?report=fasta'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'html.parser')


div = soup.find_all('div', attrs={'class', 'seq gbff'})
for each in div.children:
    print(each)
soup.find_all('span', aatrs={'class', 'ff_line'})


That's actually easy for me. div = soup.find_all('div', attrs={'class', 'seq gbff'}) contains the unique value for each page I want to access, just have to replace the id in each url.

url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=344258949&db=protein&report=fasta&extrafeat=0&fmt_mask=0&retmode=html&withmarkup=on&tool=portal&log$=seqview&maxdownloadsize=1000000'

I checked url need only three arguments to get data id=344258949&report=fasta&retmode=text 
