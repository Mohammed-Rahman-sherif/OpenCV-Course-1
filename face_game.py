import cv2
import numpy as np 
import imutils

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(1):
    _, frame = cap.read()

    frame1 = cv2.flip(frame,1)

    cv2.line(frame1,(214,0),(214,480),(0,255,0),1)
    cv2.line(frame1,(428,0),(428,480),(0,255,0),1)
    #cv2.line(frame1,(240,240),(400,240),(0,255,0),1)
    cv2.rectangle(frame1,(240,170),(400,330),(255,0,0),1)

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

    faces = face_cascade.detectMultiScale(hsv, 1.3, 5)
    print(faces)
    
    for (x,y,w,h) in faces:
    	cv2.rectangle(frame1, (x,y), (x+w, y+h), (255,0,0), 2)

    	if w < 214 and x < 214:
            fnt = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame1,("LEFT:"),(0,40),fnt,1,(0,0,255),2)
        elif w > 428 and x > 428:
            fnt = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame1, ("RIGHT: "), (428,40), fnt, 1, (0,0,255), 2)
        elif h < 170 and y < 170:
            fnt = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame1,("UP:"),(215,40),fnt,1,(0,0,255),2)
        elif h > 330 and y > 330:
            fnt = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame1,("DOWN:"),(215,40),fnt,1,(0,0,255),2)
    	#print(x)
    cv2.imshow('game_screen', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

cap.release()
cv2.destroyAllWindows()
