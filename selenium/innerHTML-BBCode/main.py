#!/usr/bin/env python3 

# date: 2019.11.07
# https://stackoverflow.com/questions/58748338/fill-textarea-with-the-bb-code-in-selenium-python/58748608

import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get('https://stackoverflow.com/questions/58748338/fill-textarea-with-the-bb-code-in-selenium-python/58748608')

messageBox = driver.find_element_by_id('wmd-input')

# needs `\` at the end of lines to create one line in JavaScript`
bb_code = '''[B][FONT=Trebuchet MS][SIZE=7]Meteor[/SIZE][/FONT][/B]\
[COLOR=#000000][FONT=Verdana][I][B][SIZE=4]n: [/B][/I][/FONT]\
[S][B][FONT=Verdana]ki[/SIZE][/FONT][/B][/S][/COLOR]\
[URL='https:///coral-lps-6/']\
[FONT=Impact][SIZE=7][COLOR=#F41600][U]CLICK HERE TO BUY![/U][/COLOR][/SIZE][/FONT][/URL]'''

js = 'arguments[0].innerHTML = "{}"'.format(bb_code) # needs `" "` because `[URL]` already use `' '`

print(js)

driver.execute_script(js, messageBox)
