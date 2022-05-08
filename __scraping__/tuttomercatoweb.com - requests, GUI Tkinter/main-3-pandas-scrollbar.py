# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.30
# [python - How can I scrape the content of a news, based on its title? - Stack Overflow](https://stackoverflow.com/questions/71667370/how-can-i-scrape-the-content-of-a-news-based-on-its-title/)

import tkinter as tk   # PEP8: `import *` is not preferred
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText  # https://docs.python.org/3/library/tkinter.scrolledtext.html
import requests
import requests_cache  # https://github.com/reclosedev/requests-cache
from bs4 import BeautifulSoup
import pandas as pd

# PEP8: all imports at the beginning

# --- functions ---   # PEP8: all functions directly after imports

def get_data_for(place):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    results = []

    response = requests.get(f'https://www.tuttomercatoweb.com/{place}/', headers=headers)
    print('url:', response.url)
    print('status:', response.status_code)
    #print('html:', response.text[:1000])

    soup = BeautifulSoup(response.content, 'html.parser')

    news = soup.find_all('div', attrs={"class": "tcc-list-news"})

    for number, each in enumerate(news):
        for div in each.find_all("div"):
            time  = div.find('span', attrs={'class': 'hh serif'}).text
            title = " ".join(span.text for span in div.select("a > span"))
            news = f"{number:02} | {time} | {place.upper()} | {title} (TMW)"
            link  = div.find('a')['href']
            results.append( [number, time, place, title, news, link] )

    return results

def all_titles():
    global df

    allnews = []  # local variable

    for place in ['atalanta',  'bologna']:
        print('search:', place)
        results = get_data_for(place)
        print('found:', len(results))
        allnews += results
        text_download.insert('end', f"search: {place}\nfound: {len(results)}\n")

    df = pd.DataFrame(allnews, columns=['number', 'time', 'place', 'title', 'news', 'link'])
    df = df.sort_values(by=['number', 'time', 'place', 'title'], ascending=[True, False, True, True])
    df = df.reset_index()

    listbox_title.delete('0', 'end')

    for index, row in df.iterrows():
        listbox_title.insert('end', row['news'])

def content(event=None):   # `command=` executes without `event`, but `bind` executes with `event` - so it needs default value
    # tuple
    selection = listbox_title.curselection()
    print('selection:', selection)

    if selection:

        item = df.iloc[selection[-1]]
        #print('item:', item)

        url = item['link']
        #print('url:', url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

        # keep page in database `SQLite` 
        # https://github.com/reclosedev/requests-cache
        # https://sqlite.org/index.html
        session = requests_cache.CachedSession('titles')
        response = session.get(url, headers=headers)
        #response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        content_download = "\n".join(item.get_text() for item in soup.select("div.text.mbottom"))

        text_download.delete('1.0', 'end') # remove previous content)
        text_download.insert('end', content_download)

# --- main ---

df = None

window = tk.Tk()
window.geometry("800x800")

# ---
# [Tkinter: How to display Listbox with Scrollbar — furas.pl](https://blog.furas.pl/python-tkitner-how-to-display-listbox-with-scrollbar-gb.html)

frame_title = tk.Frame(window)
frame_title.pack(fill='both', expand=True, pady=5, padx=5)

listbox_title = tk.Listbox(frame_title, selectbackground="#960000", selectforeground="white", bg="white", font=('monospace'))
listbox_title.pack(side='left', fill='both', expand=True)

scrollbar_title = tk.Scrollbar(frame_title)
scrollbar_title.pack(side='left', fill='y')

scrollbar_title['command'] = listbox_title.yview
listbox_title.config(yscrollcommand=scrollbar_title.set)

listbox_title.bind('<Double-Button-1>', content)  # it executes `content(event)`

# ----

text_download = ScrolledText(window, bg="white")
text_download.pack(fill='both', expand=True, pady=0, padx=5)

# ----

buttons_frame = tk.Frame(window)
buttons_frame.pack(fill='x')

button1 = tk.Button(buttons_frame, text="View Titles", command=all_titles)  # don't use `[]` to execute functions
button1.pack(side='left', pady=5, padx=5)

button2 = tk.Button(buttons_frame, text="View Content", command=content)   # don't use `[]` to execute functions
button2.pack(side='left', pady=5, padx=(0,5))

window.mainloop()
