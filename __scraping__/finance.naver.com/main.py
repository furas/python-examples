from bs4 import  BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/sise/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

rows = soup.select("#contentarea_right #trend_tab_1 tr")
for row in rows:
    cols = row.select('td')
    print("-", cols[0].text, '|', cols[1].text)

