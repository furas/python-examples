#!/usr/bin/env python3 
#!/usr/bin/env python3 

# date: 2019.11.26
# 

from wand.image import Image

img1 = Image(filename='square-1.png')
img2 = Image(filename='square-2.png')
img3 = Image(filename='square-3.png')
img4 = Image(filename='square-4.png')

w1, h1 = img1.size
w2, h2 = img2.size
w3, h3 = img3.size
w4, h4 = img4.size

w = max(w1, w2, w3, w4)
h = max(h1, h2, h3, h4)

# create big empty image with place for images
new_image = Image(width=w*2, height=h*2)

# put images on new_image
new_image.composite(image=img1, left=0, top=0)
new_image.composite(image=img2, left=w, top=0)
new_image.composite(image=img3, left=0, top=h)
new_image.composite(image=img4, left=w, top=h)

new_image.save(filename='new-wand.png')

