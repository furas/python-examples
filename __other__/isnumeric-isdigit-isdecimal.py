#!/usr/bin/env python3

# https://docs.python.org/3/library/stdtypes.html#str.isdecimal

# isnumeric: Numeric_Type = Digit, Decimal or Numeric e.g. U+2155, VULGAR FRACTION ONE FIFTH.
#   isdigit: Numeric_Type = Digit or Decimal e.g. Kharosthi numbers.
# isdecimal: Unicode General Category “Nd” e.g. U+0660, ARABIC-INDIC DIGIT ZERO

# http://unicodefractions.com/
# "Nd" - http://www.fileformat.info/info/unicode/category/index.htm
#        http://www.fileformat.info/info/unicode/category/Nd/list.htm

# http://www.fileformat.info/info/unicode/category/Nd/list.htm
# http://www.fileformat.info/info/unicode/category/Nl/list.htm
# http://www.fileformat.info/info/unicode/category/No/list.htm

examples = [
    '\u00bd\u2153\u2155', # VULGAR FRACTION 1/2, 1/3, 1/5
    '\u0660', # ARABIC-INDIC DIGIT ZERO
    '\u2169\u2162', # Roman X III, 
    '\u00B2', # SUPERSCRIPT TWO
    '\u0F2A', # TIBETAN DIGIT HALF ONE
    '\u3007', # IDEOGRAPHIC NUMBER ZERO
]

for txt in examples:
    print('---', txt, '---')
    print('Numeric:', str.isnumeric(txt))
    print('  Digit:', str.isdigit(txt))
    print('Decimal:', str.isdecimal(txt))
