It needs `Scrapy 2.4+` because `file_path` uses `item=`.

---

# Run without project (standalone)

```
$ cd standalone
$ python main.py 2018 2020
```

---

# Run with project

```
$ cd project
$ scrapy crawl myspider -a start=2018 -a end=2020
```

---

# Run in code 

```
c.crawl(MySpider, start=2018, end=2020)
```

or 

```
run(2018, 2020)
```

---

It seems `project` runs faster then `standalone`. Maybe `standalone` doesn't use `threads`.
