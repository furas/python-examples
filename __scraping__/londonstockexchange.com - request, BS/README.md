
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)

# date: 2020.09.08

# https://stackoverflow.com/questions/63785398/web-scraping-using-python-scrapy-or-beautiful-soup-fails-to-extract-data-from-ls


This page uses JavaScript to display data but it doesn't use AJAX to read them.
It has all data in `HTML` as `JSON` in `<script type="application/json">` 

After converting adn digging in JSON you can get all information without scraping.

Parsers `lxml` and `html.parser` had problem to parse it but it works with `html5lib`.
