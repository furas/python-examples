Use `BeautifulSoup`, `lxml` or similar module instead of `regex`.

---

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/):

    from bs4 import BeautifulSoup
    
    text = '<div class="ds"><div title="Today" class="dh">...<div title="Pazartesi" class="dh">26 Agu Pzt'
    
    soup = BeautifulSoup(text, 'html.parser')
    
    for item in soup.select('.ds div[title]'):
        print(item['title'])

    # or as list comprehensions 

    titles = [item['title'] for item in soup.select('.ds div[title]')]
    print(titles)

---

[lxml](https://lxml.de/):

    import lxml.html
    
    text = '<div class="ds"><div title="Today" class="dh">...<div title="Pazartesi" class="dh">26 Agu Pzt'
    
    soup = lxml.html.fromstring(text)
    
    for item in soup.cssselect('.ds div[title]'):
        print(item.attrib['title'])
            
    # or as list comprehensions 

    titles = [item.attrib['title'] for item in soup.cssselect('.ds div[title]')]
    print(titles)

---

[PyQuery](https://docs.scrapy.org/en/latest/topics/selectors.html):

    import pyquery
    
    text = '<div class="ds"><div title="Today" class="dh">...<div title="Pazartesi" class="dh">26 Agu Pzt'
    
    soup = pyquery.PyQuery(text)
    
    for item in soup('.ds div[title]'):
        print(item.attrib['title'])
    
    # or as list comprehensions 
    
    titles = [item.attrib['title'] for item in soup('.ds div[title]')]
    print(titles)

---

[parsel](https://parsel.readthedocs.io/en/latest/): (used by [Scrapy's Selectors](https://docs.scrapy.org/en/latest/topics/selectors.html))

    import parsel
    
    sel = parsel.Selector(text)
    
    for item in sel.css('.ds div[title]'):
        print(item.attrib['title'])
            
    # or as list comprehensions 

    titles = [item.attrib['title'] for item in sel.css('.ds div[title]')]
    print(titles)


