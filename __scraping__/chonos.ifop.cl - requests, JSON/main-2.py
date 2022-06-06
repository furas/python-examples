# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.29

# [web scraping - How to webscrape an interactive webpage with python - Stack Overflow](https://stackoverflow.com/questions/72423199/how-to-webscrape-an-interactive-webpage-with-python/72425518#72425518)
    
import requests
    
url = 'http://chonos.ifop.cl/flow/stnclick'

params = {
    'index': 0
}

for number in range(10):
    params['index'] = number
    
    response = requests.get(url, params=params)

    data = response.json()

    print('\n---', data['name'], '---\n')
    
    # show first 5 values
    for item in data['series']['sim'][:5]:
        print(item)
    print('...')
