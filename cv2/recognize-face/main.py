
import cv2
import time
import os

fullpath = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')

face_cascade = cv2.CascadeClassifier(fullpath)
 
cap = cv2.VideoCapture(0)
 
while (True):
    #Reading frame from the live video feed
    ret, frame = cap.read()
    
    if not ret:
        print("No frame")
        break
    
    #Converting frame into grayscale for better efficiency
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Using Haar Cascade for detecting faces in an image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    #Creating the rectangle around face
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (120, 250, 0), 2)
        
    #Displaying the captured frame in a window
    cv2.imshow('gray', frame)
 
    #Applied 0.1 seconds delay such that a new frame will only be read every 0.1 seconds (10 frames per second)
    #This decreases load on machine, because in general webcam captures 15 to 25 frames per second
    time.sleep(0.1)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
