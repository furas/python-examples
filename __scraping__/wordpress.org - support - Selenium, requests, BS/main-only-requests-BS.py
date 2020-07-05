import requests
from bs4 import BeautifulSoup
 
s = requests.Session()
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0' # it needs full user-agent
})

# --- get page with login form ---

r = s.get("https://login.wordpress.org/?locale=en_US")
soup = BeautifulSoup(r.text, 'html.parser')

# get all fields in form

payload = {}

for field in soup.find_all('input'):
    name = field['name']
    value = field['value']
    payload[name] = value
    print(name, '=', value)

# --- login ---

payload['log'] = 'my_login'
payload['pwd'] = 'my_password'

r = s.post('https://login.wordpress.org/wp-login.php', data=payload)
print('redirected to:', r.url)

# --- check if logged in ---

# check if logged in - check if redirected to different page
if r.url.startswith('https://login.wordpress.org/wp-login.php'):
    print('Problem to login')
    exit()

# check if logged in - check displayed name
url = 'https://wordpress.org/support/plugin/advanced-gutenberg/page/1/'
r = s.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
name = soup.find('span', {'class': 'display-name'})
if not name:
    print('Problem to login')
    exit()
else:    
    print('name:', name.text)
    
# --- pages ---

url = 'https://wordpress.org/support/plugin/advanced-gutenberg/page/{}/'
 
for page in range(1, 3):
    print('\n--- PAGE:', page, '---\n')
 
    # read page with list of posts
    r = s.get(url.format(page))
    soup = BeautifulSoup(r.text, 'html.parser') # 'lxml'
 
    all_uls = soup.find('li', class_="bbp-body").find_all('ul')
 
    for number, ul in enumerate(all_uls, 1):
 
        print('\n--- post:', number, '---\n')
 
        a = ul.find('a')
        if a:
            post_url = a['href']
            post_title = a.text
 
            print('text:', post_url)
            print('href:', post_title)
            print('---------')
 
            # read page with post content
            r = s.get(post_url)
            sub_soup = BeautifulSoup(r.text, 'html.parser')
 
            post_content = sub_soup.find(class_='bbp-topic-content').get_text(strip=True, separator='\n')
            print(post_content)
