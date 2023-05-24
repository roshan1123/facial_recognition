import numpy as np
import cv2
import face_recognition 

myfile1 = "haarcascade_frontalface_default.xml"
myfile2 = "haarcascade_eye.xml"
faceCascade = cv2.CascadeClassifier(myfile1)
eye_cascade = cv2.CascadeClassifier(myfile2)
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    roi_gray = gray[y:y+h, x:x+w] 
    eyes = eye_cascade.detectMultiScale(roi_gray)   

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       
      for (ex,ey,ew,eh) in eyes:
        roi_color = gray[y:y+h,x:x+w]
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
  
    cv2.imshow('video',img,img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
