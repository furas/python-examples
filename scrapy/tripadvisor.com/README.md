## get-reviews.py

I use normal url - without `-or{}` - to get page and find number of reviews.  
Next I add `-or{}` to url - it can be in any place - to generate urls to pages with reviews.  
And then I use `for` loop and `Request()` to get pages with reviews.  
Reviews are parsed by different method - `parse_reviews()`.

I use `scrapy.crawler.CrawlerProcess()` to run it without full project, so everyone can easily run and test it.

It saves data in `output.csv`.

---

**BTW:** to get page you need urls like

    https://www.tripadvisor.com/g60795-d102542
    https://www.tripadvisor.com/g60795-d102542-or0
    https://www.tripadvisor.com/g60795-d102542-or5

Other words in url are only for `SEO` - to get better position in Google search results.

---

In folder [__scraping__/tripadvisor.com - requests](../../__scraping__/tripadvisor.com - requests)` is example for `requests/BeautifulSoup`.
