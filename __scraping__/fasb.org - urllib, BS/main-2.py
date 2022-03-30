# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.29
# [python - Downloading pdf from URL with urllib (getting weird html output instead) - Stack Overflow](https://stackoverflow.com/questions/71657540/downloading-pdf-from-url-with-urllib-getting-weird-html-output-instead/)

import urllib.request
import urllib.parse

url = 'https://www.fasb.org/page/showpdf?path=0001-%201700-UFI%20AICPA%20ACSEC%20Hanson.pdf'

url = url.replace('https://www.fasb.org/page/showpdf?path=', 'https://d2x0djib3vzbzj.cloudfront.net/')

filename = urllib.parse.unquote(url)
filename = filename.rsplit('/', 1)[-1]

urllib.request.urlretrieve(url, filename)

