#!/usr/bin/env python

'''
date: 2019.10.28
link: https://stackoverflow.com/questions/58600150/what-does-handle-data-return
'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    text = []
    
    def handle_data(self, data):
        self.text.append(data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')
print(parser.text)

