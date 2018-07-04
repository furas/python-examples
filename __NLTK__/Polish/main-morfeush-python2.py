#!/usr/bin/env python2

from __future__ import print_function
import morfeusz2

m = morfeusz2.Morfeusz()

result = m.analyse('samochodu samochodem samochodowy samochodami')
for x in result:
    print(x[2][1], '<-', x[2][0])
    print('---')

result = m.generate('samochód')
for x in result:
    print(x)
    
