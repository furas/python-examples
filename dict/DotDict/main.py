#!/usr/bin/env python3

class DotDict(dict):
    
    def __getitem__(self, key):
        keys = key.split('.')
        val = dict.__getitem__(self, keys[0])
        for key in keys[1:]:
            val = val.__getitem__(key)
        return val

a = DotDict({'a':1, 'b':{'x':{'y':2}}})

print(a['a'])
print(a['b.x.y'])
print(a['b.x'])
