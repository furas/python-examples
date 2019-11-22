#!/usr/bin/env python3 

# date: 2019.11.15
# https://stackoverflow.com/questions/58863905/how-can-i-convert-encoding-of-special-characters-in-python


text = '''Is there an outdoor grill/bbq place? P√§r

Hej Hur l√•ngt aa√§r de till Stallarna? MVH LAILA

√Ñr d√§r sandstrand och hur l√•ngt'''

print(text.encode('MacRoman').decode('utf-8'))
