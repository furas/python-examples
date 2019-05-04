
# date: 2019.05.05
# author: Bartłomiej 'furas' Burek

import robobrowser

br = robobrowser.RoboBrowser(user_agent='Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0')
br.parser = 'lxml'

br.open("https://www.just-eat.fr")
print(br.get_forms())

iframe_src = br.select('iframe')[0]['src']
print(iframe_src)

br.open("https://www.just-eat.fr"+iframe_src)
print(br.parsed)

br.open("https://www.just-eat.fr")
print(br.get_forms())
