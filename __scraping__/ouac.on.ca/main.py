#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47874829/1832058
# 

import requests
import bs4
import webbrowser

def display(content):
    # to see this HTML in web browser
    with open('temp.html', 'wb') as f:
        f.write(content)
        webbrowser.open('temp.html')

with requests.session() as r:

    LOGIN = ""
    PASSWORD = ""

    login_url = "https://www.ouac.on.ca/apply/nonsecondary/intl/en_CA/user/login"
    profile_url="https://www.ouac.on.ca/apply/nonsecondary/intl/en_CA/profile/"

    # session need it only once and it will remember it
    r.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
    })

    # load page with form - to get cookies and `csrf` from HTML
    response = r.get(login_url)

    #display(response.content)

    # get `csrf` from HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'}).attrs['value']

    print('csrf:', csrf)

    # cookies are not part of form so you don't use in form_data,
    # session will use cookies from previous request so you don't have to copy them
    form_data = {
        'login': LOGIN,
        'password': PASSWORD,
        'submitButton': "Log In",
        'csrf': csrf,
    }

    # send form data to server
    response = r.post(login_url, data=form_data)

    print('status_code:', response.status_code)
    print('history:', response.history)
    print('url:', response.url)

    #display(response.content)

    response = r.get(profile_url)

    display(response.content)
