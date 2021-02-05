It needs `Scrapy 2.4+` because `file_path` uses `item=`.

---

# Run without project

```
$ cd standalone
$ python main.py 2018 2020
```

---

# Run with project (if you put `spider` and `pipeline` in correct files)

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

It seems the same code in project works faster then without project - maybe project uses threads.
