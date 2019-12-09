#!/usr/bin/env python3 

# date: 2019.12.09
# https://stackoverflow.com/questions/59242102/stanfordnlp-python-sentence-split-and-other-simple-functionality?noredirect=1#comment104695431_59242102

# convert tokens in sentence to one string with sentence. But it adds spaces before ,.!? etc.

import stanfordnlp

text = """this is ... sample input. I want
to split this text into a list of sentences. Can you? Please help"""

nlp = stanfordnlp.Pipeline(processors='tokenize,pos', lang='en')
nlp = stanfordnlp.Pipeline(processors='tokenize', lang='en')
doc = nlp(text)

for i, sentence in enumerate(doc.sentences):
    sent = ' '.join(word.text for word in sentence.tokens)
    print(sent)

#    for word in sentence.words:
#        print(word.pos)

