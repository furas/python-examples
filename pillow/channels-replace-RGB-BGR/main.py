from PIL import Image 

image = Image.open('image.jpg')

#print('mode:', image.mode)

r,g,b = image.split()
image = Image.merge('RGB', (b, g, r))
#image = Image.merge('RGBA', (b, g, r, r)) #TODO: create new channel `alpha`

#print('mode:', image.mode)

image.show() 
