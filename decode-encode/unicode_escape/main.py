a = 'ą'
print(len(a), a, type(a))
b = a.encode('utf-8')
print(len(b), b, type(b))
c = b.decode('unicode_escape') # to send bytes in JSON
print(len(c), c, type(c))
d = c.encode('raw_unicode_escape') # to receive bytes from JSON 
print(len(d), d, type(d))
e = d.decode('utf-8')
print(len(e), e, type(e))
