
# tripadvisor.com - using `Requests`

Portal: [tripadvisor.com](https://www.tripadvisor.com/)

Example to read reviews from tripadvisor.com

### History

**2017.12.17:** 

- oryginal code from my answer on Stackoverflow.com: [Scraping reviews from tripadvisor](https://stackoverflow.com/a/47858268/1832058)

**2018.05.05:** 

- tripadvisor.com changed some elements on page so old code doesn't work. I made some changes but not all elements are working yet.

**2018.05.06:** 

- Python example get all elements. 

- I rewrote Python example in PHP. 

- both versions write in "results.csv" in columns (mostly based on CSS class names)
    - hotel name 
    - review title 
    - review body 
    - review date (former relativeDate, format: October 23, 2017)
    - contributions (former num_reviews_reviewers)
    - helpful vote (new)
    - user name (former reviewer_name)
    - user location  (new)
    - rating (former bubble_rating, values: 0, 10, 20, 30, 40, 50)

**2018.05.07:** 

- Python example can 

    - read reviews in selected language (ALL, en, es, pl, etc.)
    
    - sometimes review show only partial description and link "More" which read rest text using AJAX. Current code read it full description from AJAX request.
    
    - in "unused-function.py" I keep functions and information which I don't use in main code but they seem interesting.
    
    - code first reads all reviews and next it writes in CSV (CVS file name based on HTML file name and selected language) but it can be changed to database or other file format. 
    Previous version saved in file during getting items so it could save some item even if there was error/exception but it was not easy to use database or other file format.
    
- PHP example can't select language and can't read "More", yet.

---

Other:

- [tripadvisor.com - using Scrapy](../tripadvisor.com%20-%20scrapy)
- [examples for other pages](..)
