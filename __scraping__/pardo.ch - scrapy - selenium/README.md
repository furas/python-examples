
Stackoverflow: [https://stackoverflow.com/a/48017424/1832058](https://stackoverflow.com/a/48017424/1832058)

---

Portal uses different classes when client can run JavaScript (like `Selenium`)
and when client can't run JavaScript (like `scrapy` script or shell)

When you run shell

    scrapy shell https://pardo.ch/pardo/program/archive/2017/catalog-films.html

and try

    
    response.xpath('//article[@class="strip-list_link_all strip-list strip--color row row--5"]/a/@href').extract()'

then you get 23 results.

And this

    response.xpath('//article/@class').extract()

gives 23 times

    strip-list_link_all strip-list strip--color row row--5
    
The sam you get in script.

But when you use `Selenium` in `scrapy`

    self.driver = webdriver.Firefox()
    self.driver.get('https://pardo.ch/pardo/program/archive/2017/catalog-films.html')
    sel = Selector(text=self.driver.page_source)
    
    sel.xpath('//article[@class="strip-list_link_all strip-list strip--color row row--5"]/a/@href').extract()

then you get 11 results

And this

    sel.xpath('//article/@class').extract()
    
gives 

    strip-list_link_all strip-list strip--color row row--5
    strip-list_link_all strip-list strip--color row row--5 even
    strip-list_link_all strip-list strip--color row row--5
    strip-list_link_all strip-list strip--color row row--5 even
    strip-list_link_all strip-list strip--color row row--5
    strip-list_link_all strip-list strip--color row row--5 even
    ...

For this page you can use 

    response.xpath('//article/a/@hred').extract()
    
because there are no other `article`s so there is no need to use `class`.

---

BTW: similar problem is with Google Search results. 

For client which doesn't use JavaScript Google uses not only different classes but also different tags. It can use `<table><tr><td>` instead of `<div>`.
# https://stackoverflow.com/a/48017424/1832058
# https://stackoverflow.com/a/48017424/1832058
# https://stackoverflow.com/a/48017424/1832058
# https://stackoverflow.com/a/48017424/1832058
