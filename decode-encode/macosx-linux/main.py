#
# date: 2019.04.18
# author: Bartlomiej 'furas' Burek (https://blog.furas.pl)
#
# https://stackoverflow.com/questions/16467479/normalizing-unicode
# https://www.pythonsheets.com/notes/python-unicode.html
#

import unicodedata
from unidecode import unidecode
import ftfy

# --- functions ---

def test(data):
    text, expected = data

    text2 = text.encode('cp437').decode('utf-8')

    text3 = unidecode(text2)
    text4 = unicodedata.normalize('NFC', text2)

    text5 = unidecode(text4)

    print('                                text:', text, '| len:', len(text))
    print('                            expected:', expected, '  | len:', len(expected))
    print('                    text == expected:', text == expected)
    print('-------------------------------------')
    print('text.encode("cp437").decode("utf-8"):', text2, '  | len:', len(text2), '| expected:', text2 == expected)
    print('                      unicode(text2):', text3, '  | len:', len(text3), '| expected:', text3 == expected)
    print('-------------------------------------')
    print(' unicodedata.normalize("NFC", text2):', text4, '  | len:', len(text4), '| expected:', text4 == expected)
    print('                      unicode(text4):', text5, '  | len:', len(text5), '| expected:', text5 == expected)
    print('-------------------------------------')
    print('                 ftfy.fix_text(text):', ftfy.fix_text(text))
    print('-------------------------------------')


# --- main ---

a1 = 'a╠¿'

a2 = a1.encode('cp437').decode('utf-8')
a4 = unidecode(a2)
a3 = unicodedata.normalize('NFC', a2)

a5 = unidecode(a3)
print(a1, a2, len(a2), a3, len(a3), a4, a5)

examples = [
    ('a╠¿', 'ą'),
    ('e╠¿', 'ę'),
    ('z╠ü', 'ż'),
    ('┼é',  'ł'),
    ('â€“', 'X'),
#    'z╠üle'
]

for data in examples:
    test(data)
    print('----------------------------------------------------------------')


