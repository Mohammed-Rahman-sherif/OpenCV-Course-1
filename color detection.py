import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	#lower_blue = np.array([150,50,50])
	#upper_blue = np.array([180,255,255])
	#lower_green = np.array([50,50,50])
	#upper_green = np.array([60,255,255])
	
	lower_blue = np.array([110,50,50])       # -----------BLUE
	upper_blue = np.array([130,255,255])      # ----------BLUE

	lower_green = np.array([70,50,50])       # ----------GREEN
	upper_green = np.array([130,255,255])     # ----------GREEN
	
	lower_pink = np.array([150,50,50])       # ----------PINK
	upper_pink = np.array([200,255,255])      # ----------PINK

   	#lower7 = np.array([130,50,50])
	#upper7 = np.array([140,255,255])
	#lower8 = np.array([150,50,50])
	#upper8 = np.array([160,255,255])
	#lower9 = np.array([170,50,50])
	#upper9 = np.array([180,255,255])
	#lower10 = np.array([190,50,50])
	#upper10 = np.array([200,255,255])
	
	#mask_blue = cv2.inRange(frame,lower_blue,upper_blue)
	#mask_green = cv2.inRange(frame,lower_green,upper_green)
	#mask7 = cv2.inRange(frame,lower7,upper7)
	#mask8 = cv2.inRange(frame,lower8,upper8)
	#mask9 = cv2.inRange(frame,lower9,upper9)
	#mask10 = cv2.inRange(frame,lower10,upper10)
	mask_green = cv2.inRange(frame,lower_green,upper_green)
	mask_pink = cv2.inRange(frame,lower_pink,upper_pink)
	
	res_green = cv2.bitwise_and(frame,frame,mask = mask_green)
	res_pink = cv2.bitwise_and(frame,frame,mask = mask_pink)
	#res7 = cv2.bitwise_and(frame,frame,mask = mask7)
	#res8 = cv2.bitwise_and(frame,frame,mask = mask8)
	#res9 = cv2.bitwise_and(frame,frame,mask = mask9)
	#res10 = cv2.bitwise_and(frame,frame,mask = mask10)

	cv2.imshow("res_green",res_green)
	cv2.imshow("res_pink",res_pink)
	#cv2.imshow("res7",res7)
	#cv2.imshow("res8",res8)
	#cv2.imshow("res9",res9)
	#cv2.imshow("res10",res10)
	#cv2.imshow("res_green",res_green)
	#cv2.imshow("mask_blue",mask_blue)
	#cv2.imshow("mask_green",mask_green)
	#cv2.imshow("hsv",hsv)
	#cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()