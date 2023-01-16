import cv2
import numpy as np 
import imutils
from collections import deque


cap = cv2.VideoCapture(0)
pts = deque(maxlen=72)

while(1):
    _, frame = cap.read()

    frame1 = cv2.flip(frame,1)
    cv2.line(frame1,(214,0),(214,480),(0,255,0),1)
    cv2.line(frame1,(428,0),(428,480),(0,255,0),1)
 #   frame1 = np.hstack([frame,flip]) 

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([150,50,50])
    upper_blue = np.array([170,255,255])
    

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    mask = cv2.erode(mask,None,iterations = 2)
    mask = cv2.dilate(mask,None,iterations = 2)
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    res = cv2.bitwise_and(frame1,frame1, mask = mask)
    center = None
    if len(cnts)>0:
        c = max(cnts,key=cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))

        if center <= (214,480):
        #	print("left")
        	fnt = cv2.FONT_HERSHEY_SIMPLEX
        	cv2.putText(frame1,("LEFT:"),(0,40),fnt,1,(0,0,255),2)
        elif center <= (428,480):
        #	print("center")
        	fnt = cv2.FONT_HERSHEY_SIMPLEX
        	cv2.putText(frame1,("CENTER:"),(215,40),fnt,1,(0,0,255),2)
        else:
        #	print('right')
        	fnt = cv2.FONT_HERSHEY_SIMPLEX
        	cv2.putText(frame1,("RIGHT:"),(428,40),fnt,1,(0,0,255),2)

        print(center)
        if(radius > 10):
            cv2.circle(frame1,(int(x),int(y)),int(radius),(0,255,0),2)
            cv2.circle(frame1,center,5,(255,0,0),-1)
    pts.appendleft(center)
    for i in range(1, len(pts))       :
        if pts[i-1] is None or pts[i] is None:
            continue
        thickness = int(np.sqrt(72/float(i+1))*2.5)
        cv2.line(frame1,pts[i-1],pts[i],(100,100,0),thickness)

    cv2.imshow('frame',frame1)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()