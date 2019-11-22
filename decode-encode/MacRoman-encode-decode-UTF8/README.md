
Date: 2019.11.14
Stackoverflow: [How can I convert encoding of special characters in python?](https://stackoverflow.com/questions/58863905/how-can-i-convert-encoding-of-special-characters-in-python)

# Problem with √§ √• √Ñ

Text has strange √§ √• √Ñ . Probably it was MacOS system. 

    Is there an outdoor grill/bbq place? P√§r

    Hej Hur l√•ngt aa√§r de till Stallarna? MVH LAILA

    √Ñr d√§r sandstrand och hur l√•ngt
    
It used `MAcRoman` instead of `UTF-8` to decode it.

So it need to be encoded to bytes with `MAcRoman` and decoded back to string with `utf-8`

    print( text.encode('MacRoman').decode('utf-8') )
    
---

Links: [How to decode these characters? √° √© √≠](https://stackoverflow.com/questions/15283189/how-to-decode-these-characters-%E2%88%9A-%E2%88%9A-%E2%88%9A%E2%89%A0)
    
