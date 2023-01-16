import cv2

cap = cv2.VideoCapture(0)
bg_subt = cv2.createBackgroundSubtractorMOG2()

while True:
	ret,frame = cap.read()
	out = bg_subt.apply(frame)

	cv2.imshow("out",out)
	cv2.imshow("frame",frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()

