from bs4 import BeautifulSoup as BS

text = '''
    <link rel="image_src" />
    <link rel="image_src" href="image1.jpg" />
    <link rel="sound_src" href="hello.mp3" />
    <link rel="image_src" href="image2.jpg" />
'''
soup = BS(text, 'html.parser')

for item in soup.find_all('link', {'href': True, 'rel': "image_src"}):
    print(item['href'])

