
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.01
#
# title: why selinux with chromedriver crashed when i wanna get a website in centos?
# url: https://stackoverflow.com/questions/70184551/why-selinux-with-chromedriver-crashed-when-i-wanna-get-a-website-in-centos/70187741#70187741

# [why selinux with chromedriver crashed when i wanna get a website in centos?](https://stackoverflow.com/questions/70184551/why-selinux-with-chromedriver-crashed-when-i-wanna-get-a-website-in-centos/70187741#70187741)

# I needs header 'User-Agent': 'Mozilla/5.0' to work.

import requests
import lxml.html

headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://www.prodirectrunning.com/p/nike-air-zoom-tempo-next-percent-barely-volt-black-volt-hyper-orange-mens-shoes-243713/'

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.url)
print(r.history)

soup = lxml.html.fromstring(r.text)
items = soup.xpath('//img/@src')

for i in items:
    print(i)

# The same is with curl - it needs header User-Agent: Mozilla/5.0 to work.

# curl -H 'User-Agent: Mozilla/5.0' https://www.prodirectrunning.com/p/nike-air-zoom-tempo-next-percent-barely-volt-black-volt-hyper-orange-mens-shoes-243713/

# The same is with wget - it needs header User-Agent: Mozilla/5.0 to work.

# wget --header='User-Agent: Mozilla/5.0' https://www.prodirectrunning.com/p/nike-air-zoom-tempo-next-percent-barely-volt-black-volt-hyper-orange-mens-shoes-243713/


