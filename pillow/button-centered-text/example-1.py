#!/usr/bin/env python3

'''
create button with centered text and put on image
'''

from PIL import Image, ImageFont, ImageDraw

text = "Very Loooooooooooooooooong Text"

# load font
font = ImageFont.truetype("arial", size=20)

# get text size in loaded font
text_size = font.getsize(text)

# set button size + 20px margins
button_size = (text_size[0]+40, text_size[1]+40)

# create image with correct size and black background
button_img = Image.new('RGBA', button_size, "grey")

# put text on image with 20px margin
button_draw = ImageDraw.Draw(button_img)
button_draw.text((20, 20), text, font=font)
button_draw.rectangle(((0,0), (button_size[0]-1,button_size[1]-1)), outline='red')

line = ( (1, button_size[1]-1), (1,0), (button_size[0]-2,0) )
button_draw.line(line, fill='white', width=2)
line = ( (button_size[0]-2,0), (button_size[0]-2, button_size[1]-1), (0, button_size[1]-1) )
button_draw.line(line, fill='black', width=2)

# save button in file
button_img.save("button.png", "PNG")

# ---------------------------------------------------------------------

# load image with some background
source_img = Image.open("input.jpg").convert("RGBA")

# put button on source image in position (50, 50)
source_img.paste(button_img, (50, 50))

# save in new file
source_img.save("output.png", "PNG")
