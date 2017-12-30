import requests
from bs4 import BeautifulSoup
from threading import Thread
import queue

# --- functions ---

def worker(url, queue): # get queue as argument
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find("span", {"class": "text"}).get_text()

    # send result to main thread using queue
    queue.put(data)

# --- main ---

all_links = [
    'http://quotes.toscrape.com/page/' + str(i) for i in range(1, 11)
]

all_threads = []
all_results = []
my_queue = queue.Queue()

# run threads
for url in all_links:
    t = Thread(target=worker, args=(url, my_queue))
    t.start()
    all_threads.append(t)

# get results from queue    
while len(all_results) < len(all_links):
    # get result from queue
    data = my_queue.get()
    all_results.append(data)

    # or with queue.empty if loop has to do something more
    # because queue.get() wait for data if queue is empty and blocks loop

    #if not my_queue.empty():
    #    data = my_queue.get()
    #    all_results.append(data)

# display results        
for item in all_results:        
    print(item[:50], '...')    
