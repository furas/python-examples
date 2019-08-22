#!/urs/bin/env python3

import pyscreenshot 

img = pyscreenshot.grab(bbox=(0,0,100,100), backend='scrot')
img.save('output.png')
img.show()

#from PIL import Image
#img = Image.open('output.png')
#img.show()
