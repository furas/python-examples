
# date: 2019.09.16
# https://stackoverflow.com/questions/57962172/understanding-how-to-deploy-python-code-to-pop-up-balloons

import numpy as np

import cv2

cap = cv2.VideoCapture(0)
    
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:

    ret, frame = cap.read()
    
    if frame is None:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(gray)
    
    #changes = sum(sum(fgmask>200))
    changes = (fgmask>200).sum() #
    is_moving = (changes > 10000)
    print(changes, is_moving)
    

    items = []

    contours, hier = cv2.findContours(fgmask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 200 < area:
            (x,y,w,h) = cv2.boundingRect(cnt)
            cv2.rectangle(fgmask, (x,y),(x+w,y+h),255, 2)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0), 2)
            items.append( (area, x, y, w, h) )

    if items:
        main_item = max(items)
        area, x, y, w, h = main_item
        if w > h:
            r = w//2
        else:
            r = h//2
        cv2.circle(frame, (x+w//2, y+h//2), r, (0,0,255), 2)
            
    cv2.imshow('fgmask', fgmask)
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()

