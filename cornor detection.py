import cv2
import numpy as np 

img = cv2.imread('shapes.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

cornors = cv2.goodFeaturesToTrack(gray,100,0.01,10)
#gray = frame, 100 = maximum cornors to be detcted, 0.01 = quality/accuracy, 10 = eculidian distance(value can be varried)
cornors = np.int0(cornors)

for cornor in cornors:
	x,y = cornor.ravel()
	cv2.circle(img,(x,y),3,(255,0,0),5)
cv2.imshow('detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

