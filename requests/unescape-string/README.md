StackOverflow: [https://stackoverflow.com/a/47748952/1832058](https://stackoverflow.com/a/47748952/1832058)

---

In error message I see it tries to guess encoding used in file when you read it and finally it uses encoding cp1250 to read it (probably because Windows use cp1250 as default in system) but it is incorrect encoding becuse you saved it as 'utf-8'.

So you have to use open( ..., encoding='utf-8') and it will not have to guess encoding.

     # replacing '&gt'  with '>' and  '&lt' with '<'
     f = open('Table.html','r', encoding='utf-8')
     s = f.read()
     f.close()

     s = s.replace("&gt;",">")
     s = s.replace("&lt;","<")

     # writting content to html file
     f = open('Table.html','w', encoding='utf-8')
     f.write(s)
     f.close()

But you could change it before you save it. And then you don't have to open it again.

    table = json2html.convert(json=variable)


    table = table.replace("&gt;",">").replace("&lt;","<")


    f = open('Table.html', 'w', encoding='utf-8')
    f.write(table)
    f.close()

    #  output
    webbrowser.open("Table.html")

    BTW: python has function [html.unescape(text)](https://docs.python.org/3/library/html.html) to replace all "chars" like &gt; (so called [entity](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references))

    import html

    table = json2html.convert(json=variable)


    table = html.unescape(table)


    f = open('Table.html', 'w', encoding='utf-8')
    f.write(table)
    f.close()

    #  output
    webbrowser.open("Table.html")

