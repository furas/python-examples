
StackOverflow: [https://stackoverflow.com/a/48035123/1832058](https://stackoverflow.com/a/48035123/1832058)

---

Page checks `User-Agent` and if it incorrect then sends


    <HTML><HEAD>\n<TITLE>Access Denied</TITLE>\n</HEAD>...
    
In shell

    scrapy shell

    fetch("https://www.snapdeal.com", headers={'User-Agent': "Mozilla/5.0"})

    response.text    

Script gives

    url: https://www.snapdeal.com/
    All Offers
    Mobile & Tablets
    Electronics
    Computers & Gaming
    Home & Kitchen
    Men's Fashion
    Women's Fashion
    Kids' Toys & Fashion
    Beauty, Health & Daily Needs
    Sports, Fitness & Outdoor
    Motors & Accessories
    Refurbished Products
    Books, Media & Music

