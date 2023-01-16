import cv2

cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()
	laplasian = cv2.Laplacian(frame,cv2.CV_64F)
	slopeX = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize = 5)
	slopeY = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize = 5)

	cv2.imshow('laplasian',laplasian)
	cv2.imshow('slopeX',slopeX)
	cv2.imshow('slopeY',slopeY)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()