
# date: 2019.09.24
# https://stackoverflow.com/questions/58085910/python-convert-u0048-style-unicode-to-normal-string/58086131#58086131

print('#U0048#U0045#U004C#U004C#U004F'.replace('#U', '\\u').encode().decode('raw_unicode_escape'))
