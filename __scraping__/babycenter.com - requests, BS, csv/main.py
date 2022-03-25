# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.18
# [scraping baby names python - Stack Overflow](https://stackoverflow.com/questions/71525007/scraping-baby-names-python)

'''
Few mistakes and problems: 

- it has to be `class_=...` instead of `classname=....` 
(funny is because next functions you use correct `class_` or `{"class": ...}`)

- you search `<td class="row">` but this page doesn't have it - it has `<div class="row">`. 
(funny is, you assign it to variable `div_results` so maybe it is only typo) 
But it would be simpler to use `css selector` and search `select("td.nameCell.bodyLinks a")`

- you check `if name not in bodyLinks:` but you should do `if name not in babynames:`

- page uses relative urls `/baby-names-josiah-2356.htm` but `requests` needs absolute urls `https://www.babycenter.com/baby-names-josiah-2356.htm` and you have to add `https://www.babycenter.com` to url 

- you add result to `babnames[mean]` but you should use name `babnames[name]`


I see another problem: code may run long time and if you would like to stop it then you would have to use Ctr+C and it would not run code which save data in `csv` - it can be better to put `while True` in `with open() as ...:` and write new row directy when you get new name
'''

from bs4 import BeautifulSoup
import requests
import csv

babnames = {}
start_index = 0

with open('babnames.csv', 'w', newline='', encoding="utf-8") as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(['Name', 'Meanning'])

    while True:
        print('start_index:', start_index)
        req = requests.get(f"https://www.babycenter.com/babyNamerSearch.htm?startIndex={start_index}&excludeLimit=100&gender=MALE&containing=&origin=&includeLimit=100&sort=&meaning=&endsWith=&theme=&batchSize=40&includeExclude=ALL&numberOfSyllables=&startsWith=")
        soup = BeautifulSoup(req.content, "lxml")
    
        found = False
        
        results = soup.select('td.nameCell.bodyLinks a')
        print('results:', len(results))
        
        for result in results:
            name = result.get_text(strip=True)
            print('>>> name:', name)
                    
            if name in babnames:
                print('- skip -')
            else:
                print('name:', name)
                
                link = 'https://www.babycenter.com' + result['href']
                print('link:', link)
                
                response_details = requests.get(link)
                soup_details = BeautifulSoup(response_details.content, "lxml")
                      
                a_mean = soup_details.find("p", {"class": "bodyText"})
                if a_mean:
                    mean = a_mean.get_text(strip=True)
                else:
                    mean = '#'
                
                print('mean:', mean)
                
                babnames[name] = mean
                found = True
                csv_output.writerow([name, mean])
                        
        # Keep going until no new names found
        if found:
            start_index += 40
        else:
            break
    

