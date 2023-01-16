import cv2
import numpy as np
import serial
import time

Myserial = serial.Serial('COM11',9600)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
count = 10

while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for(ex, ey, ew, eh) in eyes:
      cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
      count +=1
  cv2.imshow('img', img)

'''  if (len(faces)) == 0:
    Myserial.write('o'.encode())
    print ("No face is detected")
  elif (len(faces)) == 1:
    Myserial.write('n'.encode())
    print ("Face is detected")'''

'''  k = cv2.waitKey(100) & 0xff
  if k == 27:
    break'''
'''  elif count >= 30:
      break'''
    
cap.release()
cv2.destroyAllWindows()
