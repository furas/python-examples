
I use `while True` to run endless loop and `break` to exit when there is no data

    data = soup.select('.result-info')
    if not data:
        print('END: no data:')
        break

I use module `csv` to save data so I don't have to use `replace(","," ")`.
It will put text in " " if there is , in text.

`s={}` can be in any place after `?` so I put it at the end to make code more readable.

Portal gives first page even if you use `s=0` so I don't have to check `offset == 0` to use url without `s=0`

# https://stackoverflow.com/a/47720827/1832058
# https://stackoverflow.com/a/47720827/1832058
