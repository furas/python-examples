It seems minimal working code.

It needs header `'X-Requested-With'` because it is AXAJ/XHR request.

It needs `permasession` but first `GET` doesn't send it so probably it is generated on page with JavaScript. But it works for me with the same `permasession` all the time.

Maybe later it will need new/fresh `permasession`

There are spaces in `" site2 "`

```python
import requests

headers={
    'X-Requested-With': 'XMLHttpRequest', # need it
}

data = {
    'action': 'shorten',
    'url': 'https://onet.pl',
    'url2': ' site2 ', # need spaces
    'url_hash': None,
    'url_stats_is_private': 0,
    'permasession': '1555801674|ole2ky65f9', # need it
}

r = requests.post('http://bit\.do/mod_perl/url-shortener.pl', headers=headers, data=data)

print(r.status_code)
print(r.json())
```

It didn't need `requests.Session()` nor `User-Agent` nor `GET` request at start.

---

**EDIT:** value `1555801674` in `'permasession': '1555801674|ole2ky65f9'` is timestamp with current date and time.

```python
import datetime

datetime.datetime.fromtimestamp(1555801674)

datetime.datetime(2019, 4, 21, 1, 7, 54)
```

Maybe `ole2ky65f9` is also timestampe but as shortened value.

