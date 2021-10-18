
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.10.07
#
# title: 'NoneType' object is not subscriptable when webscraping image title
# url: https://stackoverflow.com/questions/69475748/nonetype-object-is-not-subscriptable-when-webscraping-image-title/69477667#69477667

# ['NoneType' object is not subscriptable when webscraping image title](https://stackoverflow.com/questions/69475748/nonetype-object-is-not-subscriptable-when-webscraping-image-title/69477667#69477667)

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

url2 = 'https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708'

# opening up connection, grabbing page
uclient = ureq(url2)
html = uclient.read()
uclient.close()

# html parsing
page_soup = soup(html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

#print(containers[15].div.div.a.img["title"])

for number, container in enumerate(containers):
    print("---", number, "---")

    #if container.div.div.a.img:
    #    brand = container.div.div.a.img["title"]
    #else:
    #    brand = '???'
        
    brand = container.div.find("img", {"title": True})["title"]
        
    product_name = container.find("a", {"class": "item-title"}).text
    shipping = container.find("li", {"class": "price-ship"}).text.strip()

    print(brand)
    print(product_name)
    print(shipping)

