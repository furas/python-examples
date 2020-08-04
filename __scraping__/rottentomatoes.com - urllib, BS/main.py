
# author: https://blog.furas.pl
# date: 2020.07.28
# link: https://stackoverflow.com/questions/63125987/how-do-i-continue-printing-all-top-100-movies-from-rotten-tomatoes

import urllib.request 
from bs4 import BeautifulSoup as BS

my_url = 'https://www.rottentomatoes.com/top/bestofrt/'

# grabbing connection
req = urllib.request.urlopen(my_url)
html = req.read()
req.close()

# html parser
soup = BS(html, "html.parser")

# gather movies
all_tables = soup.find_all("table", {"class":"table"})

for table in all_tables:
    for row in table.find_all('tr')[1:]:
        movie_rank = row.find("td", {"class":"bold"})
        movie_rank = movie_rank.text

        movie_name = row.find("a", {"class":"unstyled articleLink"})
        movie_name = movie_name.text.strip()

        movie_rating = row.find("td", {"class":"right hidden-xs"})
        movie_rating = movie_rating.text

        print("Rank:", movie_rank)
        print("Name:", movie_name)
        print("Rating:", movie_rating)
