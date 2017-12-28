Convert string `1000000` to `1.000.000` without `

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

Result 

    123
    1.234
    12.345
    123.456
    1.234.567

Using `locale` needs special files in system

    import locale

    # Set to users preferred locale:
    locale.setlocale(locale.LC_ALL, '')
    print('{:n}'.format(1000000))
    
    #   1000000

    # Or a specific locale:
    locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
    print('{:n}'.format(1000000))
    
    #   1,000,000   
    
    locale.setlocale(locale.LC_ALL, "de_DE.utf-8")
    print('{:n}'.format(1000000))
    
    #   error because I don't have `de_DE` in system
    
