# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.05
# [python - How to grab image links correctly? My scraper only make blank folders - Stack Overflow](https://stackoverflow.com/questions/71355569/how-to-grab-image-links-correctly-my-scraper-only-make-blank-folders/71358233#71358233)

import requests
import parsel
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

for page in range(1, 310): # Total 309pages
    
    print(f'======= Scraping data from page {page} =======')
    
    url = f'https://www.bikeexif.com/page/{page}'

    response = requests.get(url, headers=headers)
    selector = parsel.Selector(response.text)

    containers = selector.xpath('//div[@class="container"]/div/article[@class="smallhalf"]')

    for v in containers:

        old_title = v.xpath('.//div[2]/h2/a/text()').get()#.replace(':', ' -')
        if old_title is not None:
            title = old_title.replace(':', ' -')

        title_url = v.xpath('.//div[2]/h2/a/@href').get()
        print(title, title_url)

        os.makedirs( os.path.join('img', title), exist_ok=True )  # it create only if doesn't exists

        response_article = requests.get(url=title_url, headers=headers)
        selector_article = parsel.Selector(response_article.text)
        
        # Full Size Images
        images_url = selector_article.xpath('//div[@id="content"]//img/@src').getall() + \
                     selector_article.xpath('//div[@id="content"]//img/@data-src').getall()

        print('len(images_url):', len(images_url))
        
        for img_url in images_url:

            response_image = requests.get(url=img_url, headers=headers)
            
            filename = img_url.split('/')[-1]

            with open( os.path.join('img', title, filename), 'wb') as f:
                f.write(response_image.content)
                print('Download complete!!:', filename)

