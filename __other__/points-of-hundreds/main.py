def convert(text):
    parts = []
    while text:
        parts.insert(0, text[-3:])
        text = text[:-3]
    return '.'.join(parts)

print(convert(str(123)))
print(convert(str(1234)))
print(convert(str(12345)))
print(convert(str(123456)))
print(convert(str(1234567)))


'''
123
1.234
12.345
123.456
1.234.567
'''
