import urllib.request
import lxml.html

# --- functions ---

def get_top_tags(html):
    all_items = html.findall('.//span[@class="tag-item"]/a')
    for item in all_items:
        print(item.text_content(), '->', item.attrib['href'])

def get_queues(html):
    all_items = html.findall('.//div[@class="quote"]')
    for item in all_items:
    
        all_text = item.findall('./span[@class="text"]')
        for txt in all_text:
            print(txt.text_content())
    
        all_authors = item.findall('./span/small[@class="author"]')
        for txt in all_authors:
            print('author:', txt.text_content())
    
        all_urls = item.findall('./span/a')
        for txt in all_urls:
            print('url:', txt.text_content(), txt.attrib['href'])
    
        all_tags = item.findall('./div/a')
        for txt in all_tags:
            print('tag:', txt.text_content(), txt.attrib['href'])
    
        print('---')

def get_next_page(html):
    all_items = html.findall('.//li[@class="next"]/a')
    for item in all_items:
        print('url:', item.text_content(), txt.attrib['href'])
        return txt.attrib['href']

def read_page(url):
    r = urllib.request.urlopen(url)
    text = r.read()
    html = lxml.html.fromstring(text)
    return html

# --- main ---

url = 'http://quotes.toscrape.com/'
html = read_page(url)
get_top_tags(html)

url = 'http://quotes.toscrape.com/'
html = read_page(url)
get_next_page(html)

url = 'http://quotes.toscrape.com/page/{}'
for x in range(1, 1):
    html = read_page(url.format(x))
    #get_queues(html)
