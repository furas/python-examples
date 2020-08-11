
# author: https://blog.furas.pl
# date: 2020.08.05
# link: https://stackoverflow.com/questions/63256300/how-do-i-get-usb-webcam-property-ids-for-opencv/

import cv2

properties = []

for name in dir(cv2):
    if name.startswith('CAP_PROP'):
        value = getattr(cv2, name)
        properties.append((value, name))
        
# it will sort by values
# originaly it is sorted by names
#properties = sorted(properties)

for value, name in properties:
    print(f' {value:5} | cv2.{name}')

