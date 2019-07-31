
# base64 to tiff

import base64

data_base64 = 'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAAAAACoWZBhAAAAMklEQVR4nEXNwQkAMBACwfFI/y2bxwXia8FFUwF1pCCNJTIIwaD04ctsKRyaldI/9i8u1iwOE6FA880AAAAASUVORK5CYII='

data_base64 = data_base64.encode()
data = base64.b64decode(data_base64)
open('image.png', 'wb').write(data)

# tiff to base64 and html

import base64

data = open('image.png', 'rb').read()
data_base64 = base64.b64encode(data)
data_base64 = data_base64.decode()

print(data_base64)

html = '<img src="data:image/png;base64,' + data_base64 + '">'
open('output-png.html', 'w').write(html)


