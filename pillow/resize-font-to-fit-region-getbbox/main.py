
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.05.30
#
# title: How to add text in a “textbox” to an image?
# url: https://stackoverflow.com/questions/67760340/how-to-add-text-in-a-textbox-to-an-image/67762111#67762111

import PIL
print('PIL version:', PIL.__version__) 

from PIL import Image, ImageDraw, ImageFont

# create empty image
img = Image.new(size=(400, 300), mode='RGB')
draw = ImageDraw.Draw(img)

# draw white rectangle 200x100 with center in 200,150
draw.rectangle((200-100, 150-50, 200+100, 150+50), fill='white')
draw.line(((0, 150), (400, 150)), 'gray')
draw.line(((200, 0), (200, 300)), 'gray')

# find font size for text `"Hello World"` to fit in rectangle 200x100
selected_size = 1
for size in range(1, 150):
    arial = ImageFont.FreeTypeFont('/home/furas/.wine/drive_c/windows/Fonts/arial.ttf', size=size)
    w, h = arial.getsize("Hello World")  # older versions
    left, top, right, bottom = arial.getbbox("Hello World")  # needs PIL 8.0.0
    #w = right - left
    #h = bottom - top
    print(w, h)
    
    if w > 200 or h > 100:
        break
        
    selected_size = size

    print(arial.size)
    
# draw text in center of rectangle 200x100        
arial = ImageFont.FreeTypeFont('/home/furas/.wine/drive_c/windows/Fonts/arial.ttf', size=selected_size)

draw.text((200-w//2, 150-h//2), "Hello World", fill='black', font=arial)  # older versions
img.save('center-older-getsize.png')

#draw.text((200, 150), "Hello World", fill='black', anchor='mm', font=arial)
#img.save('center-newer.png')

img.show()


