

StackOverflow: [https://stackoverflow.com/a/23497912/1832058](https://stackoverflow.com/a/23497912/1832058)

StackOverflow: [https://stackoverflow.com/a/47745322/1832058](https://stackoverflow.com/a/47745322/1832058)

---

EDIT: it worked before but it seems they change something and it doesn't work any more.

---

`requests` automatically escapes parameters before it adds them to url.

You have to manually create string with url and all parameters.

create strings `key=value`

    args = ['{}={}'.format(k, v) for k,v in payload_10_vo_params.items()]

create one string `key1=value1&key2=value2`

    args_in_one_string = "&".join(args)

create url with parameters

    url = url + "?" + args_in_one_string

---

There is some [prepared-request](http://docs.python-requests.org/en/latest/user/advanced/#prepared-requests) 
and example in [request issues](https://github.com/requests/requests/issues/1839)


    import requests

    s = requests.Session()
    
    req = requests.Request('GET', url)
    prepped = s.prepare_request(req)
    
    prepped.url = prepped.url.replace('.', '%2E')
    resp = s.send(prepped)

but I don't know if it can help.

Maybe you will have to use urllib
