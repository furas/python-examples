Stackoverflow: [https://stackoverflow.com/a/47742578/1832058](https://stackoverflow.com/a/47742578/1832058)

---

Using `lxml` or `html.parser` instead of `xml` I can get

    title > CONSOLIDATED BALANCE SHEETS
    row > Total assets
    column 0 > Total assets
    column 1 > 
    column 2 > $
    column 3 > 290,479
    column 4 > 
    column 5 > 
    column 6 > $
    column 7 > 231,839
    column 8 > 

---

Stackoverflow: [https://stackoverflow.com/a/47614478/1832058](https://stackoverflow.com/a/47614478/1832058)


Page uses entity &nbsp; (Not Breaking SPace) (with char code 160)
instead of normal space (code 32) in text ITEM 7(A)

You can replace all chars with code 160 (chr(160)) with normal space (" ").
In Python 2 (after encoding) you have to replace two chars - 194 and 160

    text = text.replace(chr(160), " ") # Python 3
    text = text.replace(char(194)+chr(160), " ") # Python 2


