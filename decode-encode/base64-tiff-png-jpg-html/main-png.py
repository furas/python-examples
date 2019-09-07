
#------------------------------------------------------------------------------
# decode from base64 to png
#------------------------------------------------------------------------------

import base64

html = '<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAAAAACoWZBhAAAAMklEQVR4nEXNwQkAMBACwfFI/y2bxwXia8FFUwF1pCCNJTIIwaD04ctsKRyaldI/9i8u1iwOE6FA880AAAAASUVORK5CYII=">'

data_base64 = html.split('base64,')[1] # remove text before encoded data
data_base64 = data_base64[:-2]         # remove text after encoded data

#data_base64 = 'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAAAAACoWZBhAAAAMklEQVR4nEXNwQkAMBACwfFI/y2bxwXia8FFUwF1pCCNJTIIwaD04ctsKRyaldI/9i8u1iwOE6FA880AAAAASUVORK5CYII='

data_base64 = data_base64.encode()   # convert string to bytes
data = base64.b64decode(data_base64) # decode from base64 (bytes)
open('output-image.png', 'wb').write(data)  # write bytes to file



#------------------------------------------------------------------------------
# encode png to base64 and embed in html
#------------------------------------------------------------------------------

import base64

data = open('image.png', 'rb').read() # read bytes from file
data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
data_base64 = data_base64.decode()    # convert bytes to string

print(data_base64)

html = '<img src="data:image/png;base64,' + data_base64 + '">' # embed in html
open('output-png.html', 'w').write(html)

