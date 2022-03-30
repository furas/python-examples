# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.30
# [python - How can I scrape the content of a news, based on its title? - Stack Overflow](https://stackoverflow.com/questions/71667370/how-can-i-scrape-the-content-of-a-news-based-on-its-title/)

import tkinter as tk   # PEP8: `import *` is not preferred
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

# PEP8: all imports at the beginning

# --- functions ---   # PEP8: all functions directly after imports

def get_data_for(place):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    
    results = []
    
    response = requests.get(f'https://www.tuttomercatoweb.com/{place}/', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    news = soup.find_all('div', attrs={"class": "tcc-list-news"})

    for number, each in enumerate(news):
        for div in each.find_all("div"):
            time  = div.find('span', attrs={'class': 'hh serif'}).text
            title = " ".join(span.text for span in div.select("a > span"))
            news  = f" {time} {place.upper()}, {title} (TMW)"
            link  = div.find('a')['href']
            results.append( [-number, news, link] )
    
    return results

def all_titles():
    global allnews  # inform function to use global variable instead of local variable

    allnews = []

    for place in ['atalanta',  'bologna']: 
        print('search:', place)
        results = get_data_for(place)
        print('found:', len(results))
        allnews += results

    allnews.sort(reverse=True)

    listbox_title.delete('0', 'end')
    
    for number, news, url in allnews:
        listbox_title.insert('end', news)

#Download Content of News
def content():
    # tuple
    selection = listbox_title.curselection()
    print('selection:', selection)

    if selection:
        
        item = allnews[selection[-1]]
        print('item:', item)
        url = item[2]
        print('url:', url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
             
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        content_download = "\n".join(item.get_text() for item in soup.select("div.text.mbottom"))

        text_download.delete('1.0', 'end') # remove previous content)
        text_download.insert('end', content_download)

# --- main ---

allnews = []  # global variable with default value at start

window = tk.Tk()
window.geometry("800x800")

listbox_title = tk.Listbox(window, selectbackground="#960000", selectforeground="white", bg="white")
listbox_title.pack(fill='both', expand=True, pady=5, padx=5)

text_download = tk.Text(window, bg="white")
text_download.pack(fill='both', expand=True, pady=0, padx=5)

buttons_frame = tk.Frame(window)
buttons_frame.pack(fill='x')

button1 = tk.Button(buttons_frame, text="View Titles", command=all_titles)  # don't use `[]` to execute functions
button1.pack(side='left', pady=5, padx=5)

button2 = tk.Button(buttons_frame, text="View Content", command=content)   # don't use `[]` to execute functions
button2.pack(side='left', pady=5, padx=(0,5))

window.mainloop()
