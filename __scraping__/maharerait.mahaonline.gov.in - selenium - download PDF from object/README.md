After clicking it adds <object data="application/pdf;base64,..."> which has all PDF as text encoded bas64 in data=

driver.execute_script("arguments[0].click();",btn)

time.sleep(5)

# get tag <object>
obj = driver.find_element_by_tag_name('object')

# get `data=`
data = obj.get_attribute('data')

# get text after `base64,`
text = data.split(',')[1]

# encode text to PDF's content (as bytes)
import base64
bytes = base64.b64decode(text)

# save bytes in file
with open('output.pdf', 'wb') as fp:
    fp.write(bytes)

And now you have all in output.pdf
