import cv2

cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read(0)

	cv2.imshow("frame",frame)
	blur = cv2.blur(frame,(15,15))
	cv2.imshow('blur',blur)
	GaussianBlur = cv2.GaussianBlur(frame,(15,15),0)
	cv2.imshow('GaussianBlur',GaussianBlur)
	medianblur = cv2.medianBlur(frame,15)
	cv2.imshow('MedianBlur',medianblur)
	bilateral = cv2.bilateralFilter(frame,9,75,75)
	cv2.imshow('bilateral',bilateral)


	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()