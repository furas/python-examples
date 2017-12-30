
# Removing all tags from HTML and keeping only text

## Using `w3lib` which is installed with `scrapy`

    import w3lib

    html = '<a>A</a><div><span>B</span></div>'

    text = w3lib.html.remove_tags(html)
     
    print(text)


## Using `BeautifulSoup`

Found in [NLTK Book: 3. Processing Raw Text - Dealing with HTML](http://www.nltk.org/book/ch03.html)

    from bs4 import BeautifulSoup

    html = '<a>A</a><div><span>B</span></div>'

    text = BeautifulSoup(html, 'html.parser').get_text()
     
    print(text)
