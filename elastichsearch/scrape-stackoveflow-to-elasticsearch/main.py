#!/usr/bin/env python3

# date: 2019.10.17
# https://stackoverflow.com/questions/58419896/writing-scrapped-data-into-json-using-python

from urllib.request import urlopen
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

es = Elasticsearch()

for page in range(2):
    url = "https://stackoverflow.com/questions?tab=unanswered&page={}".format(page)
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    
    container = soup.find_all("div", {"class":"question-summary"})
    for item in container:
        try:
            job = {
                'Title': item.find("a", {"class":"question-hyperlink"}).get_text(strip=True),
                'Description': item.find("div", {"class":"excerpt"}).get_text(strip=True),
                'Tags': item.find("div",{"class":"tags"}).get_text(strip=True),
                'Votes': item.find("div",{"class":"votes"}).get_text(strip=True),
                'Answers': item.find("div",{"class":"status"}).get_text(strip=True),
                'Views': item.find("div",{"class":"views"}).get_text(strip=True),
                'Time': item.find("span",{"class":"relativetime"}).get_text(strip=True),
            }
        except AttributeError as ex:
            print('Error:', ex)
            continue
            
        # --- importing job to Elasticsearch ---
        
        res = es.index(index="stackoverflow", doc_type='job', body=job) # without `id` to autocreate `id` 
        print(res['result'])


# --- searching ---

#es.indices.refresh(index="stackoverflow")

res = es.search(index="stackoverflow", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    #print(hit)
    print("%(Title)s: %(Tags)s" % hit["_source"])


