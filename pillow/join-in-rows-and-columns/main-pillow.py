#!/usr/bin/env python3 
#!/usr/bin/env python3 

# date: 2019.11.26
# 

from PIL import Image

img1 = Image.open('square-1.png')
img2 = Image.open('square-2.png')
img3 = Image.open('square-3.png')
img4 = Image.open('square-4.png')

w1, h1 = img1.size
w2, h2 = img1.size
w3, h3 = img1.size
w4, h4 = img1.size

w = max(w1, w2, w3, w4)
h = max(h1, h2, h3, h4)

# create big empty image with place for images
new_image = Image.new('RGB', (w*2, h*2))

# put images on new_image
new_image.paste(img1, (0, 0))
new_image.paste(img2, (w, 0))
new_image.paste(img3, (0, h))
new_image.paste(img4, (w, h))

new_image.save('new.png')
