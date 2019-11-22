import cv2
import imageio

img = imageio.imread('https://i.stack.imgur.com/erk2H.jpg')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = ~img

threshold = 185
img[ (img <  threshold) ] = 0
img[ (img >= threshold) ] = 255

cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
