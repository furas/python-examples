import imageio

# date: 2019.08.10
# https://stackoverflow.com/questions/57440861/resizing-a-48bit-png-retaining-its-48bits-without-dropping-it-to-a-24bit-file
# https://github.com/imageio/imageio/issues/329
# http://freeimage.sourceforge.net/
# https://github.com/imageio/imageio/blob/master/imageio/plugins/freeimage.py

#img = imageio.imread('input.png', format='PNG-FI')
img = imageio.imread('input_48bit.png', format='PNG-FI')
print('shape:', img.shape)
print('max R:', img[:,:,0].max())
print('max G:', img[:,:,1].max())
print('max B:', img[:,:,2].max())
print('---')

img = img.copy()
img = img[370:375,1020:1025,:]
img = img.copy()
img.resize((256,256,3))

print('shape:', img.shape)
print('max R:', img[:,:,0].max())
print('max G:', img[:,:,1].max())
print('max B:', img[:,:,2].max())
print('---')
print('max X:', img[:,:,0].max(axis=0).argmax())
print('max Y:', img[:,:,0].max(axis=1).argmax())
print(' flat:', img[:,:,0].argmax())
print('---')

max_r = img[:,:,0].max()

for y, row in enumerate(img[:,:,0]):
    for x, it in enumerate(row):
        if it == max_r:
            print('value/x/y:', max_r, x, y)

imageio.imwrite('output_48bit.png', img, format='PNG-FI')
