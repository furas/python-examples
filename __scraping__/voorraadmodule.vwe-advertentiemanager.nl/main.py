
#
# https://stackoverflow.com/a/47852250/1832058
#

from bs4 import BeautifulSoup
import requests

url = "http://voorraadmodule.vwe-advertentiemanager.nl/s9376368b43e8fd6a8025bfa284d8e732/e7c2/stock/vehicles/100/"
img_pre_url = "http://voorraadmodule.vwe-advertentiemanager.nl/s4c74bf131813e9d7d3232b46224830a2"
getpage = requests.get(url)
soup = BeautifulSoup(getpage.text, "html.parser")

for listingparse in soup.find_all("div", class_="row clearfix "):

    ftch_id = listingparse.get("id")[8:]
    ftch_imgurl = listingparse.find("div", class_="columnPhoto").img["src"]

    url_parts = ftch_imgurl.split('/')

    if url_parts[-2] == "260x195":
        verkocht = "verkocht"
    else:
        verkocht = ""

    print("List id:", ftch_id)
    print("Image url:", img_pre_url+ftch_imgurl)
    print("image size:", url_parts[-2], verkocht)
    print('---')
    
'''
Result:

List id: 15668794
Image url: http://voorraadmodule.vwe-advertentiemanager.nl/s4c74bf131813e9d7d3232b46224830a2/vehicle-images/15668794/1/1513180329/320x213/citroen-xsara-picasso-1-6i-attraction-zeer-ruime-gezinsauto
image size: 320x213 
---
List id: 15529833
Image url: http://voorraadmodule.vwe-advertentiemanager.nl/s4c74bf131813e9d7d3232b46224830a2/vehicle-images/15529833/1/1512131899/260x195/dacia-logan-mcv-1-6-laureate-zeer-ruime-buitenkans
image size: 260x195 verkocht
---
List id: 15427090
Image url: http://voorraadmodule.vwe-advertentiemanager.nl/s4c74bf131813e9d7d3232b46224830a2/vehicle-images/15427090/1/1510153600/320x213/fiat-punto-evo-1-3-m-jet-dynamic
image size: 320x213 
---
List id: 15287283
Image url: http://voorraadmodule.vwe-advertentiemanager.nl/s4c74bf131813e9d7d3232b46224830a2/vehicle-images/15287283/1/1508421733/320x213/hyundai-matrix-1-6i-active-ek-2008-automaat-parkeersensoor-achter
image size: 320x213 
---
List id: 15218532
Image url: http://voorraadmodule.vwe-advertentiemanager.nl/s4c74bf131813e9d7d3232b46224830a2/vehicle-images/15218532/1/1513263561/260x195/land-rover-range-rover-sport-3-6-tdv8-hse-vol-met-opties
image size: 260x195 verkocht
---
List id: 13888171
Image url: http://voorraadmodule.vwe-advertentiemanager.nl/s4c74bf131813e9d7d3232b46224830a2/vehicle-images/13888171/1/1491479399/320x213/maserati-quattroporte-4-7-s
image size: 320x213 
---
'''
    
